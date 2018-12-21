import sys
from antlr4 import *
from CLexer import CLexer
from CParser import CParser
from CVisitor import CVisitor


def addIndex(a, num=2):
    return '\n'.join([' ' * num + i for i in a.split('\n')])


class ToJSVisitor(CVisitor):
    def visitCompilationUnit(self, ctx):
        return '\n'.join([self.visit(i) for i in ctx.children[:-1]])

    def visitFunctionDefinition(self, ctx):
        functionname = self.visit(ctx.declarator())
        if functionname == 'main':
            return self.visitCompoundStatementInMain(ctx.compoundStatement())
        ans = 'function'
        ans += ' ' + self.visit(ctx.declarator())
        ans += ' ' + self.visit(ctx.compoundStatement())
        return ans

    def visitTypeSpecifier(self, ctx):
        if ctx.CONST():
            return 'const'
        return 'let'

    def visitDeclarator(self, ctx):
        return ctx.Identifier().getText()

    def visitDeclaration(self, ctx):
        return self.visit(ctx.typeSpecifier()) + ' ' + self.visit(ctx.initDeclaratorList()) + ';'

    def visitCompoundStatement(self, ctx):
        return '{\n' + addIndex('\n'.join([self.visit(i) for i in ctx.children[1:-1]])) + '\n}'

    def visitCompoundStatementInMain(self, ctx):
        return '\n'.join([self.visit(i) for i in ctx.children[1:-1]])

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

    def visitStatement(self, ctx):
        return "visitStatement"

    def visitInitializer(self, ctx):
        return "visitInitializer"


def main(argv):
    input = FileStream('test.c' if len(argv) <= 1 else argv[1])
    lexer = CLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.compilationUnit()
    ans = ToJSVisitor().visit(tree)
    print(ans)


if __name__ == '__main__':
    main(sys.argv)