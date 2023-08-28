# Generated from Grammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#r.
    def visitR(self, ctx:GrammarParser.RContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#program.
    def visitProgram(self, ctx:GrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#CLASS_DEFINITION.
    def visitCLASS_DEFINITION(self, ctx:GrammarParser.CLASS_DEFINITIONContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#DEFINITION_METHOD_PARAMS.
    def visitDEFINITION_METHOD_PARAMS(self, ctx:GrammarParser.DEFINITION_METHOD_PARAMSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#DEFINITION_PARAMS.
    def visitDEFINITION_PARAMS(self, ctx:GrammarParser.DEFINITION_PARAMSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#formal.
    def visitFormal(self, ctx:GrammarParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#formalAssign.
    def visitFormalAssign(self, ctx:GrammarParser.FormalAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#CALL.
    def visitCALL(self, ctx:GrammarParser.CALLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#EXPR_PARAMS.
    def visitEXPR_PARAMS(self, ctx:GrammarParser.EXPR_PARAMSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#TIMES.
    def visitTIMES(self, ctx:GrammarParser.TIMESContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#EQUALS.
    def visitEQUALS(self, ctx:GrammarParser.EQUALSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#VOID_EXPR.
    def visitVOID_EXPR(self, ctx:GrammarParser.VOID_EXPRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#DISPATCH.
    def visitDISPATCH(self, ctx:GrammarParser.DISPATCHContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#BLOCK.
    def visitBLOCK(self, ctx:GrammarParser.BLOCKContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#TRUE.
    def visitTRUE(self, ctx:GrammarParser.TRUEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#WHILE_CLAUSE.
    def visitWHILE_CLAUSE(self, ctx:GrammarParser.WHILE_CLAUSEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#SUM.
    def visitSUM(self, ctx:GrammarParser.SUMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#LET_PASS.
    def visitLET_PASS(self, ctx:GrammarParser.LET_PASSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ASSIGN_VAL.
    def visitASSIGN_VAL(self, ctx:GrammarParser.ASSIGN_VALContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#MINUS.
    def visitMINUS(self, ctx:GrammarParser.MINUSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#DIVIDE.
    def visitDIVIDE(self, ctx:GrammarParser.DIVIDEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#BIGGER.
    def visitBIGGER(self, ctx:GrammarParser.BIGGERContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#NOT.
    def visitNOT(self, ctx:GrammarParser.NOTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#NEWOBJ.
    def visitNEWOBJ(self, ctx:GrammarParser.NEWOBJContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#IF_CLAUSE.
    def visitIF_CLAUSE(self, ctx:GrammarParser.IF_CLAUSEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#STRING.
    def visitSTRING(self, ctx:GrammarParser.STRINGContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#TILDE.
    def visitTILDE(self, ctx:GrammarParser.TILDEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#FALSE.
    def visitFALSE(self, ctx:GrammarParser.FALSEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ID.
    def visitID(self, ctx:GrammarParser.IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#BIGGEREQUALS.
    def visitBIGGEREQUALS(self, ctx:GrammarParser.BIGGEREQUALSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#INTEGER.
    def visitINTEGER(self, ctx:GrammarParser.INTEGERContext):
        return self.visitChildren(ctx)



del GrammarParser