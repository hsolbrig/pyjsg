# Generated from /Users/mrf7578/Development/git/hsolbrig/pyjsg/grammar/jsgParser.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jsgParser import jsgParser
else:
    from jsgParser import jsgParser

# This class defines a complete generic visitor for a parse tree produced by jsgParser.

class jsgParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by jsgParser#doc.
    def visitDoc(self, ctx:jsgParser.DocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#typeDirective.
    def visitTypeDirective(self, ctx:jsgParser.TypeDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#ignoreDirective.
    def visitIgnoreDirective(self, ctx:jsgParser.IgnoreDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#typeExceptions.
    def visitTypeExceptions(self, ctx:jsgParser.TypeExceptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#grammarElt.
    def visitGrammarElt(self, ctx:jsgParser.GrammarEltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#objectDef.
    def visitObjectDef(self, ctx:jsgParser.ObjectDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#objectExprObj.
    def visitObjectExprObj(self, ctx:jsgParser.ObjectExprObjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#objectExprMap.
    def visitObjectExprMap(self, ctx:jsgParser.ObjectExprMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#objectExprDef.
    def visitObjectExprDef(self, ctx:jsgParser.ObjectExprDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#particleOpt.
    def visitParticleOpt(self, ctx:jsgParser.ParticleOptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#arrayDef.
    def visitArrayDef(self, ctx:jsgParser.ArrayDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#arrayExpr.
    def visitArrayExpr(self, ctx:jsgParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#particle.
    def visitParticle(self, ctx:jsgParser.ParticleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#propertyOrGroupSimple.
    def visitPropertyOrGroupSimple(self, ctx:jsgParser.PropertyOrGroupSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#propertyOrGroupShorthand.
    def visitPropertyOrGroupShorthand(self, ctx:jsgParser.PropertyOrGroupShorthandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#propertyOrGroupChoice.
    def visitPropertyOrGroupChoice(self, ctx:jsgParser.PropertyOrGroupChoiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#propertyOrGroupList.
    def visitPropertyOrGroupList(self, ctx:jsgParser.PropertyOrGroupListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#propertyTypeID.
    def visitPropertyTypeID(self, ctx:jsgParser.PropertyTypeIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#propertyTypeSTRING.
    def visitPropertyTypeSTRING(self, ctx:jsgParser.PropertyTypeSTRINGContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#propertyTypeObjectExpr.
    def visitPropertyTypeObjectExpr(self, ctx:jsgParser.PropertyTypeObjectExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#propertyTypeArrayExpr.
    def visitPropertyTypeArrayExpr(self, ctx:jsgParser.PropertyTypeArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#propertyTypeChoice.
    def visitPropertyTypeChoice(self, ctx:jsgParser.PropertyTypeChoiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#propertyTypeAny.
    def visitPropertyTypeAny(self, ctx:jsgParser.PropertyTypeAnyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#typeAlternatives.
    def visitTypeAlternatives(self, ctx:jsgParser.TypeAlternativesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#nonObject.
    def visitNonObject(self, ctx:jsgParser.NonObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#ebnfSuffix.
    def visitEbnfSuffix(self, ctx:jsgParser.EbnfSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#lexerRuleSpec.
    def visitLexerRuleSpec(self, ctx:jsgParser.LexerRuleSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#lexerebnf.
    def visitLexerebnf(self, ctx:jsgParser.LexerebnfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#lexerRuleBlock.
    def visitLexerRuleBlock(self, ctx:jsgParser.LexerRuleBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#lexerAltList.
    def visitLexerAltList(self, ctx:jsgParser.LexerAltListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#lexerAlt.
    def visitLexerAlt(self, ctx:jsgParser.LexerAltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#lexerElements.
    def visitLexerElements(self, ctx:jsgParser.LexerElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#lexerElement.
    def visitLexerElement(self, ctx:jsgParser.LexerElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#lexerBlock.
    def visitLexerBlock(self, ctx:jsgParser.LexerBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#lexerAtomTerminal.
    def visitLexerAtomTerminal(self, ctx:jsgParser.LexerAtomTerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#lexerAtomCharSet.
    def visitLexerAtomCharSet(self, ctx:jsgParser.LexerAtomCharSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#lexerAtomDot.
    def visitLexerAtomDot(self, ctx:jsgParser.LexerAtomDotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#lexerTerminalID.
    def visitLexerTerminalID(self, ctx:jsgParser.LexerTerminalIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsgParser#lexerTerminalString.
    def visitLexerTerminalString(self, ctx:jsgParser.LexerTerminalStringContext):
        return self.visitChildren(ctx)



del jsgParser