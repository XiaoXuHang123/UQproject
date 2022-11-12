# Generated from cspParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cspParserParser import cspParserParser
else:
    from cspParserParser import cspParserParser

# This class defines a complete listener for a parse tree produced by cspParserParser.
class cspParserListener(ParseTreeListener):

    # Enter a parse tree produced by cspParserParser#specification.
    def enterSpecification(self, ctx:cspParserParser.SpecificationContext):
        pass

    # Exit a parse tree produced by cspParserParser#specification.
    def exitSpecification(self, ctx:cspParserParser.SpecificationContext):
        pass


    # Enter a parse tree produced by cspParserParser#specBody.
    def enterSpecBody(self, ctx:cspParserParser.SpecBodyContext):
        pass

    # Exit a parse tree produced by cspParserParser#specBody.
    def exitSpecBody(self, ctx:cspParserParser.SpecBodyContext):
        pass


    # Enter a parse tree produced by cspParserParser#library.
    def enterLibrary(self, ctx:cspParserParser.LibraryContext):
        pass

    # Exit a parse tree produced by cspParserParser#library.
    def exitLibrary(self, ctx:cspParserParser.LibraryContext):
        pass


    # Enter a parse tree produced by cspParserParser#channel.
    def enterChannel(self, ctx:cspParserParser.ChannelContext):
        pass

    # Exit a parse tree produced by cspParserParser#channel.
    def exitChannel(self, ctx:cspParserParser.ChannelContext):
        pass


    # Enter a parse tree produced by cspParserParser#assertion.
    def enterAssertion(self, ctx:cspParserParser.AssertionContext):
        pass

    # Exit a parse tree produced by cspParserParser#assertion.
    def exitAssertion(self, ctx:cspParserParser.AssertionContext):
        pass


    # Enter a parse tree produced by cspParserParser#withClause.
    def enterWithClause(self, ctx:cspParserParser.WithClauseContext):
        pass

    # Exit a parse tree produced by cspParserParser#withClause.
    def exitWithClause(self, ctx:cspParserParser.WithClauseContext):
        pass


    # Enter a parse tree produced by cspParserParser#definitionRef.
    def enterDefinitionRef(self, ctx:cspParserParser.DefinitionRefContext):
        pass

    # Exit a parse tree produced by cspParserParser#definitionRef.
    def exitDefinitionRef(self, ctx:cspParserParser.DefinitionRefContext):
        pass


    # Enter a parse tree produced by cspParserParser#alphabet.
    def enterAlphabet(self, ctx:cspParserParser.AlphabetContext):
        pass

    # Exit a parse tree produced by cspParserParser#alphabet.
    def exitAlphabet(self, ctx:cspParserParser.AlphabetContext):
        pass


    # Enter a parse tree produced by cspParserParser#define.
    def enterDefine(self, ctx:cspParserParser.DefineContext):
        pass

    # Exit a parse tree produced by cspParserParser#define.
    def exitDefine(self, ctx:cspParserParser.DefineContext):
        pass


    # Enter a parse tree produced by cspParserParser#dparameter.
    def enterDparameter(self, ctx:cspParserParser.DparameterContext):
        pass

    # Exit a parse tree produced by cspParserParser#dparameter.
    def exitDparameter(self, ctx:cspParserParser.DparameterContext):
        pass


    # Enter a parse tree produced by cspParserParser#dstatement.
    def enterDstatement(self, ctx:cspParserParser.DstatementContext):
        pass

    # Exit a parse tree produced by cspParserParser#dstatement.
    def exitDstatement(self, ctx:cspParserParser.DstatementContext):
        pass


    # Enter a parse tree produced by cspParserParser#block.
    def enterBlock(self, ctx:cspParserParser.BlockContext):
        pass

    # Exit a parse tree produced by cspParserParser#block.
    def exitBlock(self, ctx:cspParserParser.BlockContext):
        pass


    # Enter a parse tree produced by cspParserParser#statement.
    def enterStatement(self, ctx:cspParserParser.StatementContext):
        pass

    # Exit a parse tree produced by cspParserParser#statement.
    def exitStatement(self, ctx:cspParserParser.StatementContext):
        pass


    # Enter a parse tree produced by cspParserParser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:cspParserParser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by cspParserParser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:cspParserParser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by cspParserParser#expression.
    def enterExpression(self, ctx:cspParserParser.ExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#expression.
    def exitExpression(self, ctx:cspParserParser.ExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#conditionalOrExpression.
    def enterConditionalOrExpression(self, ctx:cspParserParser.ConditionalOrExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#conditionalOrExpression.
    def exitConditionalOrExpression(self, ctx:cspParserParser.ConditionalOrExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#conditionalAndExpression.
    def enterConditionalAndExpression(self, ctx:cspParserParser.ConditionalAndExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#conditionalAndExpression.
    def exitConditionalAndExpression(self, ctx:cspParserParser.ConditionalAndExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#conditionalXorExpression.
    def enterConditionalXorExpression(self, ctx:cspParserParser.ConditionalXorExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#conditionalXorExpression.
    def exitConditionalXorExpression(self, ctx:cspParserParser.ConditionalXorExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#indexedExpression.
    def enterIndexedExpression(self, ctx:cspParserParser.IndexedExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#indexedExpression.
    def exitIndexedExpression(self, ctx:cspParserParser.IndexedExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#bitwiseLogicExpression.
    def enterBitwiseLogicExpression(self, ctx:cspParserParser.BitwiseLogicExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#bitwiseLogicExpression.
    def exitBitwiseLogicExpression(self, ctx:cspParserParser.BitwiseLogicExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#equalityExpression.
    def enterEqualityExpression(self, ctx:cspParserParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#equalityExpression.
    def exitEqualityExpression(self, ctx:cspParserParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#relationalExpression.
    def enterRelationalExpression(self, ctx:cspParserParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#relationalExpression.
    def exitRelationalExpression(self, ctx:cspParserParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:cspParserParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:cspParserParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:cspParserParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:cspParserParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#unaryExpression.
    def enterUnaryExpression(self, ctx:cspParserParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#unaryExpression.
    def exitUnaryExpression(self, ctx:cspParserParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#arrayExpression.
    def enterArrayExpression(self, ctx:cspParserParser.ArrayExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#arrayExpression.
    def exitArrayExpression(self, ctx:cspParserParser.ArrayExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#unaryExpressionNotPlusMinus.
    def enterUnaryExpressionNotPlusMinus(self, ctx:cspParserParser.UnaryExpressionNotPlusMinusContext):
        pass

    # Exit a parse tree produced by cspParserParser#unaryExpressionNotPlusMinus.
    def exitUnaryExpressionNotPlusMinus(self, ctx:cspParserParser.UnaryExpressionNotPlusMinusContext):
        pass


    # Enter a parse tree produced by cspParserParser#methods_fields_call.
    def enterMethods_fields_call(self, ctx:cspParserParser.Methods_fields_callContext):
        pass

    # Exit a parse tree produced by cspParserParser#methods_fields_call.
    def exitMethods_fields_call(self, ctx:cspParserParser.Methods_fields_callContext):
        pass


    # Enter a parse tree produced by cspParserParser#letDefintion.
    def enterLetDefintion(self, ctx:cspParserParser.LetDefintionContext):
        pass

    # Exit a parse tree produced by cspParserParser#letDefintion.
    def exitLetDefintion(self, ctx:cspParserParser.LetDefintionContext):
        pass


    # Enter a parse tree produced by cspParserParser#variableRange.
    def enterVariableRange(self, ctx:cspParserParser.VariableRangeContext):
        pass

    # Exit a parse tree produced by cspParserParser#variableRange.
    def exitVariableRange(self, ctx:cspParserParser.VariableRangeContext):
        pass


    # Enter a parse tree produced by cspParserParser#argumentExpression.
    def enterArgumentExpression(self, ctx:cspParserParser.ArgumentExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#argumentExpression.
    def exitArgumentExpression(self, ctx:cspParserParser.ArgumentExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#ifExpression.
    def enterIfExpression(self, ctx:cspParserParser.IfExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#ifExpression.
    def exitIfExpression(self, ctx:cspParserParser.IfExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#whileExpression.
    def enterWhileExpression(self, ctx:cspParserParser.WhileExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#whileExpression.
    def exitWhileExpression(self, ctx:cspParserParser.WhileExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#recordExpression.
    def enterRecordExpression(self, ctx:cspParserParser.RecordExpressionContext):
        pass

    # Exit a parse tree produced by cspParserParser#recordExpression.
    def exitRecordExpression(self, ctx:cspParserParser.RecordExpressionContext):
        pass


    # Enter a parse tree produced by cspParserParser#recordElement.
    def enterRecordElement(self, ctx:cspParserParser.RecordElementContext):
        pass

    # Exit a parse tree produced by cspParserParser#recordElement.
    def exitRecordElement(self, ctx:cspParserParser.RecordElementContext):
        pass


    # Enter a parse tree produced by cspParserParser#definition.
    def enterDefinition(self, ctx:cspParserParser.DefinitionContext):
        pass

    # Exit a parse tree produced by cspParserParser#definition.
    def exitDefinition(self, ctx:cspParserParser.DefinitionContext):
        pass


    # Enter a parse tree produced by cspParserParser#parameter.
    def enterParameter(self, ctx:cspParserParser.ParameterContext):
        pass

    # Exit a parse tree produced by cspParserParser#parameter.
    def exitParameter(self, ctx:cspParserParser.ParameterContext):
        pass


    # Enter a parse tree produced by cspParserParser#interleaveExpr.
    def enterInterleaveExpr(self, ctx:cspParserParser.InterleaveExprContext):
        pass

    # Exit a parse tree produced by cspParserParser#interleaveExpr.
    def exitInterleaveExpr(self, ctx:cspParserParser.InterleaveExprContext):
        pass


    # Enter a parse tree produced by cspParserParser#parallelExpr.
    def enterParallelExpr(self, ctx:cspParserParser.ParallelExprContext):
        pass

    # Exit a parse tree produced by cspParserParser#parallelExpr.
    def exitParallelExpr(self, ctx:cspParserParser.ParallelExprContext):
        pass


    # Enter a parse tree produced by cspParserParser#paralDef.
    def enterParalDef(self, ctx:cspParserParser.ParalDefContext):
        pass

    # Exit a parse tree produced by cspParserParser#paralDef.
    def exitParalDef(self, ctx:cspParserParser.ParalDefContext):
        pass


    # Enter a parse tree produced by cspParserParser#paralDef2.
    def enterParalDef2(self, ctx:cspParserParser.ParalDef2Context):
        pass

    # Exit a parse tree produced by cspParserParser#paralDef2.
    def exitParalDef2(self, ctx:cspParserParser.ParalDef2Context):
        pass


    # Enter a parse tree produced by cspParserParser#generalChoiceExpr.
    def enterGeneralChoiceExpr(self, ctx:cspParserParser.GeneralChoiceExprContext):
        pass

    # Exit a parse tree produced by cspParserParser#generalChoiceExpr.
    def exitGeneralChoiceExpr(self, ctx:cspParserParser.GeneralChoiceExprContext):
        pass


    # Enter a parse tree produced by cspParserParser#internalChoiceExpr.
    def enterInternalChoiceExpr(self, ctx:cspParserParser.InternalChoiceExprContext):
        pass

    # Exit a parse tree produced by cspParserParser#internalChoiceExpr.
    def exitInternalChoiceExpr(self, ctx:cspParserParser.InternalChoiceExprContext):
        pass


    # Enter a parse tree produced by cspParserParser#externalChoiceExpr.
    def enterExternalChoiceExpr(self, ctx:cspParserParser.ExternalChoiceExprContext):
        pass

    # Exit a parse tree produced by cspParserParser#externalChoiceExpr.
    def exitExternalChoiceExpr(self, ctx:cspParserParser.ExternalChoiceExprContext):
        pass


    # Enter a parse tree produced by cspParserParser#interruptExpr.
    def enterInterruptExpr(self, ctx:cspParserParser.InterruptExprContext):
        pass

    # Exit a parse tree produced by cspParserParser#interruptExpr.
    def exitInterruptExpr(self, ctx:cspParserParser.InterruptExprContext):
        pass


    # Enter a parse tree produced by cspParserParser#hidingExpr.
    def enterHidingExpr(self, ctx:cspParserParser.HidingExprContext):
        pass

    # Exit a parse tree produced by cspParserParser#hidingExpr.
    def exitHidingExpr(self, ctx:cspParserParser.HidingExprContext):
        pass


    # Enter a parse tree produced by cspParserParser#sequentialExpr.
    def enterSequentialExpr(self, ctx:cspParserParser.SequentialExprContext):
        pass

    # Exit a parse tree produced by cspParserParser#sequentialExpr.
    def exitSequentialExpr(self, ctx:cspParserParser.SequentialExprContext):
        pass


    # Enter a parse tree produced by cspParserParser#guardExpr.
    def enterGuardExpr(self, ctx:cspParserParser.GuardExprContext):
        pass

    # Exit a parse tree produced by cspParserParser#guardExpr.
    def exitGuardExpr(self, ctx:cspParserParser.GuardExprContext):
        pass


    # Enter a parse tree produced by cspParserParser#channelExpr.
    def enterChannelExpr(self, ctx:cspParserParser.ChannelExprContext):
        pass

    # Exit a parse tree produced by cspParserParser#channelExpr.
    def exitChannelExpr(self, ctx:cspParserParser.ChannelExprContext):
        pass


    # Enter a parse tree produced by cspParserParser#eventExpr.
    def enterEventExpr(self, ctx:cspParserParser.EventExprContext):
        pass

    # Exit a parse tree produced by cspParserParser#eventExpr.
    def exitEventExpr(self, ctx:cspParserParser.EventExprContext):
        pass


    # Enter a parse tree produced by cspParserParser#caseExpr.
    def enterCaseExpr(self, ctx:cspParserParser.CaseExprContext):
        pass

    # Exit a parse tree produced by cspParserParser#caseExpr.
    def exitCaseExpr(self, ctx:cspParserParser.CaseExprContext):
        pass


    # Enter a parse tree produced by cspParserParser#caseCondition.
    def enterCaseCondition(self, ctx:cspParserParser.CaseConditionContext):
        pass

    # Exit a parse tree produced by cspParserParser#caseCondition.
    def exitCaseCondition(self, ctx:cspParserParser.CaseConditionContext):
        pass


    # Enter a parse tree produced by cspParserParser#ifExpr.
    def enterIfExpr(self, ctx:cspParserParser.IfExprContext):
        pass

    # Exit a parse tree produced by cspParserParser#ifExpr.
    def exitIfExpr(self, ctx:cspParserParser.IfExprContext):
        pass


    # Enter a parse tree produced by cspParserParser#ifExprs.
    def enterIfExprs(self, ctx:cspParserParser.IfExprsContext):
        pass

    # Exit a parse tree produced by cspParserParser#ifExprs.
    def exitIfExprs(self, ctx:cspParserParser.IfExprsContext):
        pass


    # Enter a parse tree produced by cspParserParser#ifBlock.
    def enterIfBlock(self, ctx:cspParserParser.IfBlockContext):
        pass

    # Exit a parse tree produced by cspParserParser#ifBlock.
    def exitIfBlock(self, ctx:cspParserParser.IfBlockContext):
        pass


    # Enter a parse tree produced by cspParserParser#atomicExpr.
    def enterAtomicExpr(self, ctx:cspParserParser.AtomicExprContext):
        pass

    # Exit a parse tree produced by cspParserParser#atomicExpr.
    def exitAtomicExpr(self, ctx:cspParserParser.AtomicExprContext):
        pass


    # Enter a parse tree produced by cspParserParser#atom.
    def enterAtom(self, ctx:cspParserParser.AtomContext):
        pass

    # Exit a parse tree produced by cspParserParser#atom.
    def exitAtom(self, ctx:cspParserParser.AtomContext):
        pass


    # Enter a parse tree produced by cspParserParser#eventM.
    def enterEventM(self, ctx:cspParserParser.EventMContext):
        pass

    # Exit a parse tree produced by cspParserParser#eventM.
    def exitEventM(self, ctx:cspParserParser.EventMContext):
        pass


    # Enter a parse tree produced by cspParserParser#eventList.
    def enterEventList(self, ctx:cspParserParser.EventListContext):
        pass

    # Exit a parse tree produced by cspParserParser#eventList.
    def exitEventList(self, ctx:cspParserParser.EventListContext):
        pass


    # Enter a parse tree produced by cspParserParser#eventName.
    def enterEventName(self, ctx:cspParserParser.EventNameContext):
        pass

    # Exit a parse tree produced by cspParserParser#eventName.
    def exitEventName(self, ctx:cspParserParser.EventNameContext):
        pass



del cspParserParser