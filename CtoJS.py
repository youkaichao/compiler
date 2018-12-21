import sys
from antlr4 import *
from CLexer import CLexer
from CParser import CParser
from CVisitor import CVisitor


def addIndex(a, num=2):
    '\n'.join([' ' * num + i for i in a.split('\n')])


class ToJSVisitor(CVisitor):
    def visitCompilationUnit(self, ctx):
        return self.visit(ctx.translationUnit())

    def visitTranslationUnit(self, ctx):
        if ctx.translationUnit():
            return self.visit(ctx.translationUnit()) + '\n' + self.visit(ctx.externalDeclaration())
        return self.visit(ctx.externalDeclaration())

    def visitExternalDeclaration(self, ctx):
        if ctx.functionDefinition():
            return self.visit(ctx.functionDefinition())
        elif ctx.declaration():
            return self.visit(ctx.declaration())
        return ctx.getText()

    def visitFunctionDefinition(self, ctx):
        # ans = ""
        # if ctx.declarationSpecifiers():
        #     ans += self.visit(ctx.declarationSpecifiers())
        ans = 'function'
        ans += ' ' + self.visit(ctx.declarator())
        if ctx.declarationList():
            ans += ' ' + self.visit(ctx.declarationList())
        ans += ' ' + self.visit(ctx.compoundStatement())
        return ans

    def visitDeclaration(self, ctx):
        if ctx.initDeclaratorList():
            return self.visit(ctx.declarationSpecifiers()) + ' ' + self.visit(ctx.initDeclaratorList()) + ';'
        return self.visit(ctx.declarationSpecifiers()) + ';'

    def visitDeclarationSpecifiers(self, ctx):
        datas = ctx.declarationSpecifier()
        ans = ''
        started = False
        for data in datas:
            if started:
                ans += ' ' + self.visit(data)
            else:
                started = True
                ans += self.visit(data)
        return ans

    def visitDeclarationSpecifiers2(self, ctx):
        datas = ctx.declarationSpecifier()
        ans = ''
        started = False
        for data in datas:
            if started:
                ans += ' ' + self.visit(data)
            else:
                started = True
                ans += self.visit(data)
        return ans

    def visitDeclarationSpecifier(self, ctx):
        if ctx.typeSpecifier():
            return self.visit(ctx.typeSpecifier())
        return self.visit(ctx.typeQualifier())

    def visitTypeSpecifier(self, ctx):
        # if ctx.typedefName():
        #     return self.visit(ctx.typedefName())
        # if ctx.typeSpecifier():
        #     return self.visit(ctx.typeSpecifier()) + ' ' + self.visit(ctx.pointer())
        # return ctx.getText()
        return 'let'

    def visitTypeQualifier(self, ctx):
        return ctx.getText()

    def visitTypedefName(self, ctx):
        return ctx.Identifier().getText()
    
    def visitPointer(self, ctx):
        ans = '*'
        if ctx.typeQualifierList():
            ans += ' ' + self.visit(ctx.typeQualifierList())
        if ctx.pointer():
            ans += ' ' + self.visit(ctx.pointer())
        return ans

    def visitTypeQualifierList(self, ctx):
        return "visitTypeQualifierList"

    def visitDeclarator(self, ctx):
        return "visitdeclarator"
    
    def visitDeclarationList(self, ctx):
        if ctx.declarationList():
            return self.visit(ctx.declarationList()) + ' ' + self.visit(ctx.declaration())
        return self.visit(ctx.declaration())

    def visitCompoundStatement(self, ctx):
        return "visitCompoundStatement"

    def visitInitDeclaratorList(self, ctx):
        return "VISITinitDeclaratorList"


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