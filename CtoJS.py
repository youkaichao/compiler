import sys
from antlr4 import *
from CLexer import CLexer
from CParser import CParser
from CVisitor import CVisitor


def addIndentation(a, num=2):
    return '\n'.join([' ' * num + i for i in a.split('\n')])


class ToJSVisitor(CVisitor):
    def visitCompilationUnit(self, ctx):
        ans = [self.visit(i) for i in ctx.children[:-1]]
        ans = [x for x in ans if x]
        return '\n'.join(ans) + '\nmain()\n'

    def visitFunctionDefinition(self, ctx):
        ans = 'function'
        ans += ' ' + self.visit(ctx.declarator())
        ans += ' ' + self.visit(ctx.compoundStatement())
        return ans

    def visitTypeSpecifier(self, ctx):
        if ctx.CONST():
            return 'const'
        return 'let'

    def visitPureIdentifier(self, ctx:CParser.PureIdentifierContext):
        return ctx.Identifier().getText()

    def visitArrayIdentifier(self, ctx:CParser.ArrayIdentifierContext):
        if ctx.assignmentExpression():
            # array definition
            length = self.visit(ctx.assignmentExpression())
            return f'{ctx.Identifier().getText()} = new Array({length})'
        else:
            # string definition
            return f'{ctx.Identifier().getText()}'

    def visitFunctionDefinitionOrDeclaration(self, ctx:CParser.FunctionDefinitionOrDeclarationContext):
        if ctx.parameterTypeList():
            return f'{ctx.Identifier().getText()}({self.visit(ctx.parameterTypeList())})'
        return f'{ctx.Identifier().getText()}()'

    def visitDeclaration(self, ctx):
        if isinstance(ctx.initDeclaratorList().initDeclarator(0).declarator(), CParser.FunctionDefinitionOrDeclarationContext):
            # there is no function declaration in JS
            return
        return self.visit(ctx.typeSpecifier()) + ' ' + self.visit(ctx.initDeclaratorList()) + ';'

    def visitAssignmentExpression(self, ctx:CParser.AssignmentExpressionContext):
        if ctx.logicalAndExpression():
            return self.visit(ctx.logicalAndExpression())
        else:
            return self.visit(ctx.unaryExpression()) + ' = ' + self.visit(ctx.assignmentExpression())

    def visitLogicalAndExpression(self, ctx:CParser.LogicalAndExpressionContext):
        if ctx.logicalAndExpression():
            return self.visit(ctx.logicalAndExpression()) + ' && ' + self.visit(ctx.equalityExpression())
        else:
            return self.visit(ctx.equalityExpression())

    def visitEqualityExpression(self, ctx:CParser.EqualityExpressionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.relationalExpression())
        else:
            op = ctx.children[1].getText()
            if op == '==':
                op = '==='
            if op == '!=':
                op = '!=='
            return self.visit(ctx.equalityExpression()) + f' {op} ' + \
                   self.visit(ctx.relationalExpression())

    def visitRelationalExpression(self, ctx:CParser.RelationalExpressionContext):
        if len(ctx.children) > 1:
            return self.visit(ctx.castExpression(0)) + ' < ' + self.visit(ctx.castExpression(1))
        else:
            return self.visit(ctx.castExpression(0))

    def visitCastExpression(self, ctx:CParser.CastExpressionContext):
        if ctx.unaryExpression():
            return self.visit(ctx.unaryExpression())
        else:
            return ' '.join([self.visit(x) for x in ctx.children])

    def visitUnaryExpression(self, ctx:CParser.UnaryExpressionContext):
        if len(ctx.children) > 1:
            return ctx.children[0].getText() + ' ' + self.visit(ctx.postfixExpression())
        else:
            return self.visit(ctx.postfixExpression())

    def visitPostfixExpression(self, ctx:CParser.PostfixExpressionContext):
        if ctx.primaryExpression():
            return self.visit(ctx.primaryExpression())
        if ctx.children[1].getText() == '[':
            return f'{self.visit(ctx.postfixExpression())}[{self.visit(ctx.expression())}]'
        # function call
        functionName = ctx.postfixExpression().getText()
        if functionName == 'strlen':
            return f'{self.visit(ctx.expression())}.length'
        if functionName == 'printf':
            # printf doesn't append a newline but console
            args = ctx.expression().assignmentExpression()
            args = [self.visit(x) for x in args]
            if args[0].endswith('\\n\"'):
                args[0] = args[0][:-3] + '"'
            return f'console.log({", ".join(args)})'
        if ctx.expression():
            return f'{ctx.postfixExpression().getText()}({self.visit(ctx.expression())})'
        return f'{ctx.postfixExpression().getText()}()'

    def visitPrimaryExpression(self, ctx:CParser.PrimaryExpressionContext):
        return ctx.children[0].getText()

    def visitExpression(self, ctx:CParser.ExpressionContext):
        return ', '.join([self.visit(x) for x in ctx.assignmentExpression()])

    def visitCompoundStatement(self, ctx):
        return '\n{\n' + addIndentation('\n'.join([self.visit(i) for i in ctx.children[1:-1]])) + '\n}'

    def visitBlockItem(self, ctx):
        if ctx.statement():
            return self.visit(ctx.statement())
        return self.visit(ctx.declaration())

    def visitInitDeclaratorList(self, ctx):
        return ', '.join([self.visit(i) for i in ctx.initDeclarator()])

    def visitInitDeclarator(self, ctx):
        if ctx.initializer():
            return self.visit(ctx.declarator()) + ' = ' + self.visit(ctx.initializer())
        return self.visit(ctx.declarator())

    def visitInitializer(self, ctx):
        if ctx.assignmentExpression():
            return self.visit(ctx.assignmentExpression())
        if ctx.initializerList():
            return '[' + self.visit(ctx.initializerList()) + ']'
        return '[]'

    def visitStatement(self, ctx):
        if ctx.compoundStatement():
            return self.visit(ctx.compoundStatement())
        if isinstance(ctx.children[0], CParser.ExpressionContext):
            return self.visit(ctx.children[0]) + ';'
        txt = ctx.children[0].getText()
        if txt == 'if':
            if_statements = f'if({self.visit(ctx.expression())})' + self.visit(ctx.statement(0))
            else_statement = ''
            if len(ctx.children) > 5:
                else_statement = 'else\n' + self.visit(ctx.statement(1))
            return if_statements + else_statement
        if txt == 'while':
            return f'while({self.visit(ctx.expression())})' + self.visit(ctx.statement(0))
        if txt == 'for':
            forDeclaration = ctx.forDeclaration()
            forDeclaration = '' if not forDeclaration else self.visit(forDeclaration)
            forExpression_0 = ctx.forExpression(0)
            forExpression_0 = '' if not forExpression_0 else self.visit(forExpression_0)
            forExpression_1 = ctx.forExpression(1)
            forExpression_1 = '' if not forExpression_1 else self.visit(forExpression_1)
            return f'for ({forDeclaration}; {forExpression_0}; {forExpression_1})' + self.visit(ctx.statement(0))
        if txt == 'return':
            expression = ''
            if ctx.expression():
                expression = self.visit(ctx.expression())
            return f'return {expression};'
        return ctx.getText()

    def visitForDeclaration(self, ctx:CParser.ForDeclarationContext):
        return self.visit(ctx.typeSpecifier()) + ' ' + self.visit(ctx.initDeclaratorList())

    def visitTerminal(self, node):
        return node.getText()

    def visitInitializerList(self, ctx: CParser.InitializerListContext):
        return ', '.join([self.visit(x) for x in ctx.initializer()])

    def visitParameterList(self, ctx: CParser.ParameterListContext):
        return ', '.join([self.visit(x) for x in ctx.parameterDeclaration()])

    def visitParameterDeclaration(self, ctx: CParser.ParameterDeclarationContext):
        return self.visit(ctx.typeSpecifier()) + ' ' + self.visit(ctx.declarator())

def main(argv):
    input = FileStream('test.c' if len(argv) <= 1 else argv[1])
    lexer = CLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.compilationUnit()
    ans = ToJSVisitor().visit(tree)
    outfile = open('test.js' if len(argv) <= 1 else argv[1].split('.')[0]+'.js', 'w')
    outfile.write(ans)
    outfile.close()
    print(ans)

if __name__ == '__main__':
    main(sys.argv)