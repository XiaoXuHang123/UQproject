# Generated from cspParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cspParserParser import cspParserParser
else:
    from cspParserParser import cspParserParser

# This class defines a complete generic visitor for a parse tree produced by cspParserParser.

class cspParserVisitor(ParseTreeVisitor):

    def defaultResult(self):
        return ""

    def aggregateResult(self, aggregate, nextResult):
        return aggregate+nextResult

    # Visit a parse tree produced by cspParserParser#specification.
    def visitSpecification(self, ctx:cspParserParser.SpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#specBody.
    def visitSpecBody(self, ctx:cspParserParser.SpecBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#library.
    def visitLibrary(self, ctx:cspParserParser.LibraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#channel.
    def visitChannel(self, ctx:cspParserParser.ChannelContext):
        return "free "+ctx.children[1].getText()+":channel\n"


    # Visit a parse tree produced by cspParserParser#assertion.
    def visitAssertion(self, ctx:cspParserParser.AssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#withClause.
    def visitWithClause(self, ctx:cspParserParser.WithClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#definitionRef.
    def visitDefinitionRef(self, ctx:cspParserParser.DefinitionRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#alphabet.
    def visitAlphabet(self, ctx:cspParserParser.AlphabetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#define.
    def visitDefine(self, ctx:cspParserParser.DefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#dparameter.
    def visitDparameter(self, ctx:cspParserParser.DparameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#dstatement.
    def visitDstatement(self, ctx:cspParserParser.DstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#block.
    def visitBlock(self, ctx:cspParserParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#statement.
    def visitStatement(self, ctx:cspParserParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx:cspParserParser.LocalVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#expression.
    def visitExpression(self, ctx:cspParserParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#conditionalOrExpression.
    def visitConditionalOrExpression(self, ctx:cspParserParser.ConditionalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#conditionalAndExpression.
    def visitConditionalAndExpression(self, ctx:cspParserParser.ConditionalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#conditionalXorExpression.
    def visitConditionalXorExpression(self, ctx:cspParserParser.ConditionalXorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#indexedExpression.
    def visitIndexedExpression(self, ctx:cspParserParser.IndexedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#bitwiseLogicExpression.
    def visitBitwiseLogicExpression(self, ctx:cspParserParser.BitwiseLogicExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#equalityExpression.
    def visitEqualityExpression(self, ctx:cspParserParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#relationalExpression.
    def visitRelationalExpression(self, ctx:cspParserParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:cspParserParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:cspParserParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#unaryExpression.
    def visitUnaryExpression(self, ctx:cspParserParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#arrayExpression.
    def visitArrayExpression(self, ctx:cspParserParser.ArrayExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#unaryExpressionNotPlusMinus.
    def visitUnaryExpressionNotPlusMinus(self, ctx:cspParserParser.UnaryExpressionNotPlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#methods_fields_call.
    def visitMethods_fields_call(self, ctx:cspParserParser.Methods_fields_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#letDefintion.
    def visitLetDefintion(self, ctx:cspParserParser.LetDefintionContext):

        if '<'in ctx.getText() and '>' in ctx.getText():
            ret = "type "
            type=ctx.getText().split('<')[1].split('>')[0].strip()
            ret+=type
            ret+='.\n'
            return ret

        return ''


    # Visit a parse tree produced by cspParserParser#variableRange.
    def visitVariableRange(self, ctx:cspParserParser.VariableRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#argumentExpression.
    def visitArgumentExpression(self, ctx:cspParserParser.ArgumentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#ifExpression.
    def visitIfExpression(self, ctx:cspParserParser.IfExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#whileExpression.
    def visitWhileExpression(self, ctx:cspParserParser.WhileExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#recordExpression.
    def visitRecordExpression(self, ctx:cspParserParser.RecordExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#recordElement.
    def visitRecordElement(self, ctx:cspParserParser.RecordElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#definition.
    def visitDefinition(self, ctx:cspParserParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#parameter.
    def visitParameter(self, ctx:cspParserParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#interleaveExpr.
    def visitInterleaveExpr(self, ctx:cspParserParser.InterleaveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#parallelExpr.
    def visitParallelExpr(self, ctx:cspParserParser.ParallelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#paralDef.
    def visitParalDef(self, ctx:cspParserParser.ParalDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#paralDef2.
    def visitParalDef2(self, ctx:cspParserParser.ParalDef2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#generalChoiceExpr.
    def visitGeneralChoiceExpr(self, ctx:cspParserParser.GeneralChoiceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#internalChoiceExpr.
    def visitInternalChoiceExpr(self, ctx:cspParserParser.InternalChoiceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#externalChoiceExpr.
    def visitExternalChoiceExpr(self, ctx:cspParserParser.ExternalChoiceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#interruptExpr.
    def visitInterruptExpr(self, ctx:cspParserParser.InterruptExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#hidingExpr.
    def visitHidingExpr(self, ctx:cspParserParser.HidingExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#sequentialExpr.
    def visitSequentialExpr(self, ctx:cspParserParser.SequentialExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#guardExpr.
    def visitGuardExpr(self, ctx:cspParserParser.GuardExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#channelExpr.
    def visitChannelExpr(self, ctx:cspParserParser.ChannelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#eventExpr.
    def visitEventExpr(self, ctx:cspParserParser.EventExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#caseExpr.
    def visitCaseExpr(self, ctx:cspParserParser.CaseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#caseCondition.
    def visitCaseCondition(self, ctx:cspParserParser.CaseConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#ifExpr.
    def visitIfExpr(self, ctx:cspParserParser.IfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#ifExprs.
    def visitIfExprs(self, ctx:cspParserParser.IfExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#ifBlock.
    def visitIfBlock(self, ctx:cspParserParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#atomicExpr.
    def visitAtomicExpr(self, ctx:cspParserParser.AtomicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#atom.
    def visitAtom(self, ctx:cspParserParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#eventM.
    def visitEventM(self, ctx:cspParserParser.EventMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#eventList.
    def visitEventList(self, ctx:cspParserParser.EventListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cspParserParser#eventName.
    def visitEventName(self, ctx:cspParserParser.EventNameContext):
        return self.visitChildren(ctx)



del cspParserParser