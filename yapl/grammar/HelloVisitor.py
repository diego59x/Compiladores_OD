# Generated from ./Hello.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete generic visitor for a parse tree produced by HelloParser.

class HelloVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HelloParser#program.
    def visitProgram(self, ctx:HelloParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#class.
    def visitClass(self, ctx:HelloParser.ClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#DEFINITION_METHOD_PARAMS.
    def visitDEFINITION_METHOD_PARAMS(self, ctx:HelloParser.DEFINITION_METHOD_PARAMSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#DEFINITION_PARAMS.
    def visitDEFINITION_PARAMS(self, ctx:HelloParser.DEFINITION_PARAMSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#formal.
    def visitFormal(self, ctx:HelloParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#EXPR_PARAMS.
    def visitEXPR_PARAMS(self, ctx:HelloParser.EXPR_PARAMSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#TIMES.
    def visitTIMES(self, ctx:HelloParser.TIMESContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#EQUALS.
    def visitEQUALS(self, ctx:HelloParser.EQUALSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#VOID_EXPR.
    def visitVOID_EXPR(self, ctx:HelloParser.VOID_EXPRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#DECLARE_TYPE.
    def visitDECLARE_TYPE(self, ctx:HelloParser.DECLARE_TYPEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#TRUE.
    def visitTRUE(self, ctx:HelloParser.TRUEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#WHILE_CLAUSE.
    def visitWHILE_CLAUSE(self, ctx:HelloParser.WHILE_CLAUSEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#SUM.
    def visitSUM(self, ctx:HelloParser.SUMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#ASSIGN_VAL.
    def visitASSIGN_VAL(self, ctx:HelloParser.ASSIGN_VALContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#MINUS.
    def visitMINUS(self, ctx:HelloParser.MINUSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#DIVIDE.
    def visitDIVIDE(self, ctx:HelloParser.DIVIDEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#EXPR_NOT_KNOWN2.
    def visitEXPR_NOT_KNOWN2(self, ctx:HelloParser.EXPR_NOT_KNOWN2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#DEFINITION_ASSIGN.
    def visitDEFINITION_ASSIGN(self, ctx:HelloParser.DEFINITION_ASSIGNContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#BIGGER.
    def visitBIGGER(self, ctx:HelloParser.BIGGERContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#EXPR_NOT_KNOWN1.
    def visitEXPR_NOT_KNOWN1(self, ctx:HelloParser.EXPR_NOT_KNOWN1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#NOT.
    def visitNOT(self, ctx:HelloParser.NOTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#OBJ_DEF.
    def visitOBJ_DEF(self, ctx:HelloParser.OBJ_DEFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#IF_CLAUSE.
    def visitIF_CLAUSE(self, ctx:HelloParser.IF_CLAUSEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#STRING.
    def visitSTRING(self, ctx:HelloParser.STRINGContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#TILDE.
    def visitTILDE(self, ctx:HelloParser.TILDEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#FALSE.
    def visitFALSE(self, ctx:HelloParser.FALSEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#ID.
    def visitID(self, ctx:HelloParser.IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#BIGGEREQUALS.
    def visitBIGGEREQUALS(self, ctx:HelloParser.BIGGEREQUALSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#INTEGER.
    def visitINTEGER(self, ctx:HelloParser.INTEGERContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#r.
    def visitR(self, ctx:HelloParser.RContext):
        return self.visitChildren(ctx)



del HelloParser