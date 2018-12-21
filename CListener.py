# Generated from D:/Courses/network2/compiler/hw/compiler\C.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete listener for a parse tree produced by CParser.
class CListener(ParseTreeListener):

    # Enter a parse tree produced by CParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:CParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by CParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:CParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by CParser#postfixExpression.
    def enterPostfixExpression(self, ctx:CParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by CParser#postfixExpression.
    def exitPostfixExpression(self, ctx:CParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by CParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:CParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by CParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:CParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by CParser#unaryExpression.
    def enterUnaryExpression(self, ctx:CParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by CParser#unaryExpression.
    def exitUnaryExpression(self, ctx:CParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by CParser#unaryOperator.
    def enterUnaryOperator(self, ctx:CParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by CParser#unaryOperator.
    def exitUnaryOperator(self, ctx:CParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by CParser#castExpression.
    def enterCastExpression(self, ctx:CParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by CParser#castExpression.
    def exitCastExpression(self, ctx:CParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by CParser#relationalExpression.
    def enterRelationalExpression(self, ctx:CParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by CParser#relationalExpression.
    def exitRelationalExpression(self, ctx:CParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by CParser#equalityExpression.
    def enterEqualityExpression(self, ctx:CParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by CParser#equalityExpression.
    def exitEqualityExpression(self, ctx:CParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by CParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:CParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by CParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:CParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by CParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:CParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by CParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:CParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by CParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:CParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by CParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:CParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by CParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:CParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by CParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:CParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by CParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:CParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by CParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:CParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by CParser#expression.
    def enterExpression(self, ctx:CParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CParser#expression.
    def exitExpression(self, ctx:CParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CParser#constantExpression.
    def enterConstantExpression(self, ctx:CParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by CParser#constantExpression.
    def exitConstantExpression(self, ctx:CParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by CParser#declaration.
    def enterDeclaration(self, ctx:CParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CParser#declaration.
    def exitDeclaration(self, ctx:CParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CParser#declarationSpecifiers.
    def enterDeclarationSpecifiers(self, ctx:CParser.DeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by CParser#declarationSpecifiers.
    def exitDeclarationSpecifiers(self, ctx:CParser.DeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by CParser#declarationSpecifiers2.
    def enterDeclarationSpecifiers2(self, ctx:CParser.DeclarationSpecifiers2Context):
        pass

    # Exit a parse tree produced by CParser#declarationSpecifiers2.
    def exitDeclarationSpecifiers2(self, ctx:CParser.DeclarationSpecifiers2Context):
        pass


    # Enter a parse tree produced by CParser#declarationSpecifier.
    def enterDeclarationSpecifier(self, ctx:CParser.DeclarationSpecifierContext):
        pass

    # Exit a parse tree produced by CParser#declarationSpecifier.
    def exitDeclarationSpecifier(self, ctx:CParser.DeclarationSpecifierContext):
        pass


    # Enter a parse tree produced by CParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:CParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by CParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:CParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by CParser#initDeclarator.
    def enterInitDeclarator(self, ctx:CParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by CParser#initDeclarator.
    def exitInitDeclarator(self, ctx:CParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by CParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CParser#specifierQualifierList.
    def enterSpecifierQualifierList(self, ctx:CParser.SpecifierQualifierListContext):
        pass

    # Exit a parse tree produced by CParser#specifierQualifierList.
    def exitSpecifierQualifierList(self, ctx:CParser.SpecifierQualifierListContext):
        pass


    # Enter a parse tree produced by CParser#typeQualifier.
    def enterTypeQualifier(self, ctx:CParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by CParser#typeQualifier.
    def exitTypeQualifier(self, ctx:CParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by CParser#declarator.
    def enterDeclarator(self, ctx:CParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CParser#declarator.
    def exitDeclarator(self, ctx:CParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by CParser#directDeclarator.
    def enterDirectDeclarator(self, ctx:CParser.DirectDeclaratorContext):
        pass

    # Exit a parse tree produced by CParser#directDeclarator.
    def exitDirectDeclarator(self, ctx:CParser.DirectDeclaratorContext):
        pass


    # Enter a parse tree produced by CParser#nestedParenthesesBlock.
    def enterNestedParenthesesBlock(self, ctx:CParser.NestedParenthesesBlockContext):
        pass

    # Exit a parse tree produced by CParser#nestedParenthesesBlock.
    def exitNestedParenthesesBlock(self, ctx:CParser.NestedParenthesesBlockContext):
        pass


    # Enter a parse tree produced by CParser#pointer.
    def enterPointer(self, ctx:CParser.PointerContext):
        pass

    # Exit a parse tree produced by CParser#pointer.
    def exitPointer(self, ctx:CParser.PointerContext):
        pass


    # Enter a parse tree produced by CParser#typeQualifierList.
    def enterTypeQualifierList(self, ctx:CParser.TypeQualifierListContext):
        pass

    # Exit a parse tree produced by CParser#typeQualifierList.
    def exitTypeQualifierList(self, ctx:CParser.TypeQualifierListContext):
        pass


    # Enter a parse tree produced by CParser#parameterTypeList.
    def enterParameterTypeList(self, ctx:CParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by CParser#parameterTypeList.
    def exitParameterTypeList(self, ctx:CParser.ParameterTypeListContext):
        pass


    # Enter a parse tree produced by CParser#parameterList.
    def enterParameterList(self, ctx:CParser.ParameterListContext):
        pass

    # Exit a parse tree produced by CParser#parameterList.
    def exitParameterList(self, ctx:CParser.ParameterListContext):
        pass


    # Enter a parse tree produced by CParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:CParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:CParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by CParser#identifierList.
    def enterIdentifierList(self, ctx:CParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by CParser#identifierList.
    def exitIdentifierList(self, ctx:CParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by CParser#typeName.
    def enterTypeName(self, ctx:CParser.TypeNameContext):
        pass

    # Exit a parse tree produced by CParser#typeName.
    def exitTypeName(self, ctx:CParser.TypeNameContext):
        pass


    # Enter a parse tree produced by CParser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:CParser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by CParser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:CParser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by CParser#directAbstractDeclarator.
    def enterDirectAbstractDeclarator(self, ctx:CParser.DirectAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by CParser#directAbstractDeclarator.
    def exitDirectAbstractDeclarator(self, ctx:CParser.DirectAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by CParser#typedefName.
    def enterTypedefName(self, ctx:CParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by CParser#typedefName.
    def exitTypedefName(self, ctx:CParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by CParser#initializer.
    def enterInitializer(self, ctx:CParser.InitializerContext):
        pass

    # Exit a parse tree produced by CParser#initializer.
    def exitInitializer(self, ctx:CParser.InitializerContext):
        pass


    # Enter a parse tree produced by CParser#initializerList.
    def enterInitializerList(self, ctx:CParser.InitializerListContext):
        pass

    # Exit a parse tree produced by CParser#initializerList.
    def exitInitializerList(self, ctx:CParser.InitializerListContext):
        pass


    # Enter a parse tree produced by CParser#designation.
    def enterDesignation(self, ctx:CParser.DesignationContext):
        pass

    # Exit a parse tree produced by CParser#designation.
    def exitDesignation(self, ctx:CParser.DesignationContext):
        pass


    # Enter a parse tree produced by CParser#designatorList.
    def enterDesignatorList(self, ctx:CParser.DesignatorListContext):
        pass

    # Exit a parse tree produced by CParser#designatorList.
    def exitDesignatorList(self, ctx:CParser.DesignatorListContext):
        pass


    # Enter a parse tree produced by CParser#designator.
    def enterDesignator(self, ctx:CParser.DesignatorContext):
        pass

    # Exit a parse tree produced by CParser#designator.
    def exitDesignator(self, ctx:CParser.DesignatorContext):
        pass


    # Enter a parse tree produced by CParser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx:CParser.StaticAssertDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx:CParser.StaticAssertDeclarationContext):
        pass


    # Enter a parse tree produced by CParser#statement.
    def enterStatement(self, ctx:CParser.StatementContext):
        pass

    # Exit a parse tree produced by CParser#statement.
    def exitStatement(self, ctx:CParser.StatementContext):
        pass


    # Enter a parse tree produced by CParser#compoundStatement.
    def enterCompoundStatement(self, ctx:CParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by CParser#compoundStatement.
    def exitCompoundStatement(self, ctx:CParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by CParser#blockItemList.
    def enterBlockItemList(self, ctx:CParser.BlockItemListContext):
        pass

    # Exit a parse tree produced by CParser#blockItemList.
    def exitBlockItemList(self, ctx:CParser.BlockItemListContext):
        pass


    # Enter a parse tree produced by CParser#blockItem.
    def enterBlockItem(self, ctx:CParser.BlockItemContext):
        pass

    # Exit a parse tree produced by CParser#blockItem.
    def exitBlockItem(self, ctx:CParser.BlockItemContext):
        pass


    # Enter a parse tree produced by CParser#expressionStatement.
    def enterExpressionStatement(self, ctx:CParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by CParser#expressionStatement.
    def exitExpressionStatement(self, ctx:CParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by CParser#selectionStatement.
    def enterSelectionStatement(self, ctx:CParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by CParser#selectionStatement.
    def exitSelectionStatement(self, ctx:CParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by CParser#iterationStatement.
    def enterIterationStatement(self, ctx:CParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by CParser#iterationStatement.
    def exitIterationStatement(self, ctx:CParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by CParser#forCondition.
    def enterForCondition(self, ctx:CParser.ForConditionContext):
        pass

    # Exit a parse tree produced by CParser#forCondition.
    def exitForCondition(self, ctx:CParser.ForConditionContext):
        pass


    # Enter a parse tree produced by CParser#forDeclaration.
    def enterForDeclaration(self, ctx:CParser.ForDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#forDeclaration.
    def exitForDeclaration(self, ctx:CParser.ForDeclarationContext):
        pass


    # Enter a parse tree produced by CParser#forExpression.
    def enterForExpression(self, ctx:CParser.ForExpressionContext):
        pass

    # Exit a parse tree produced by CParser#forExpression.
    def exitForExpression(self, ctx:CParser.ForExpressionContext):
        pass


    # Enter a parse tree produced by CParser#jumpStatement.
    def enterJumpStatement(self, ctx:CParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by CParser#jumpStatement.
    def exitJumpStatement(self, ctx:CParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by CParser#compilationUnit.
    def enterCompilationUnit(self, ctx:CParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by CParser#compilationUnit.
    def exitCompilationUnit(self, ctx:CParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by CParser#translationUnit.
    def enterTranslationUnit(self, ctx:CParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by CParser#translationUnit.
    def exitTranslationUnit(self, ctx:CParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by CParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:CParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:CParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by CParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CParser#declarationList.
    def enterDeclarationList(self, ctx:CParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by CParser#declarationList.
    def exitDeclarationList(self, ctx:CParser.DeclarationListContext):
        pass


