# Generated from Grammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#r.
    def enterR(self, ctx:GrammarParser.RContext):
        pass

    # Exit a parse tree produced by GrammarParser#r.
    def exitR(self, ctx:GrammarParser.RContext):
        pass


    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx:GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx:GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by GrammarParser#CLASS_DEFINITION.
    def enterCLASS_DEFINITION(self, ctx:GrammarParser.CLASS_DEFINITIONContext):
        pass

    # Exit a parse tree produced by GrammarParser#CLASS_DEFINITION.
    def exitCLASS_DEFINITION(self, ctx:GrammarParser.CLASS_DEFINITIONContext):
        pass


    # Enter a parse tree produced by GrammarParser#DEFINITION_METHOD_PARAMS.
    def enterDEFINITION_METHOD_PARAMS(self, ctx:GrammarParser.DEFINITION_METHOD_PARAMSContext):
        pass

    # Exit a parse tree produced by GrammarParser#DEFINITION_METHOD_PARAMS.
    def exitDEFINITION_METHOD_PARAMS(self, ctx:GrammarParser.DEFINITION_METHOD_PARAMSContext):
        pass


    # Enter a parse tree produced by GrammarParser#DEFINITION_PARAMS.
    def enterDEFINITION_PARAMS(self, ctx:GrammarParser.DEFINITION_PARAMSContext):
        pass

    # Exit a parse tree produced by GrammarParser#DEFINITION_PARAMS.
    def exitDEFINITION_PARAMS(self, ctx:GrammarParser.DEFINITION_PARAMSContext):
        pass


    # Enter a parse tree produced by GrammarParser#formal.
    def enterFormal(self, ctx:GrammarParser.FormalContext):
        pass

    # Exit a parse tree produced by GrammarParser#formal.
    def exitFormal(self, ctx:GrammarParser.FormalContext):
        pass


    # Enter a parse tree produced by GrammarParser#formalAssign.
    def enterFormalAssign(self, ctx:GrammarParser.FormalAssignContext):
        pass

    # Exit a parse tree produced by GrammarParser#formalAssign.
    def exitFormalAssign(self, ctx:GrammarParser.FormalAssignContext):
        pass


    # Enter a parse tree produced by GrammarParser#CALL.
    def enterCALL(self, ctx:GrammarParser.CALLContext):
        pass

    # Exit a parse tree produced by GrammarParser#CALL.
    def exitCALL(self, ctx:GrammarParser.CALLContext):
        pass


    # Enter a parse tree produced by GrammarParser#EXPR_PARAMS.
    def enterEXPR_PARAMS(self, ctx:GrammarParser.EXPR_PARAMSContext):
        pass

    # Exit a parse tree produced by GrammarParser#EXPR_PARAMS.
    def exitEXPR_PARAMS(self, ctx:GrammarParser.EXPR_PARAMSContext):
        pass


    # Enter a parse tree produced by GrammarParser#TIMES.
    def enterTIMES(self, ctx:GrammarParser.TIMESContext):
        pass

    # Exit a parse tree produced by GrammarParser#TIMES.
    def exitTIMES(self, ctx:GrammarParser.TIMESContext):
        pass


    # Enter a parse tree produced by GrammarParser#EQUALS.
    def enterEQUALS(self, ctx:GrammarParser.EQUALSContext):
        pass

    # Exit a parse tree produced by GrammarParser#EQUALS.
    def exitEQUALS(self, ctx:GrammarParser.EQUALSContext):
        pass


    # Enter a parse tree produced by GrammarParser#VOID_EXPR.
    def enterVOID_EXPR(self, ctx:GrammarParser.VOID_EXPRContext):
        pass

    # Exit a parse tree produced by GrammarParser#VOID_EXPR.
    def exitVOID_EXPR(self, ctx:GrammarParser.VOID_EXPRContext):
        pass


    # Enter a parse tree produced by GrammarParser#DISPATCH.
    def enterDISPATCH(self, ctx:GrammarParser.DISPATCHContext):
        pass

    # Exit a parse tree produced by GrammarParser#DISPATCH.
    def exitDISPATCH(self, ctx:GrammarParser.DISPATCHContext):
        pass


    # Enter a parse tree produced by GrammarParser#BLOCK.
    def enterBLOCK(self, ctx:GrammarParser.BLOCKContext):
        pass

    # Exit a parse tree produced by GrammarParser#BLOCK.
    def exitBLOCK(self, ctx:GrammarParser.BLOCKContext):
        pass


    # Enter a parse tree produced by GrammarParser#TRUE.
    def enterTRUE(self, ctx:GrammarParser.TRUEContext):
        pass

    # Exit a parse tree produced by GrammarParser#TRUE.
    def exitTRUE(self, ctx:GrammarParser.TRUEContext):
        pass


    # Enter a parse tree produced by GrammarParser#WHILE_CLAUSE.
    def enterWHILE_CLAUSE(self, ctx:GrammarParser.WHILE_CLAUSEContext):
        pass

    # Exit a parse tree produced by GrammarParser#WHILE_CLAUSE.
    def exitWHILE_CLAUSE(self, ctx:GrammarParser.WHILE_CLAUSEContext):
        pass


    # Enter a parse tree produced by GrammarParser#SUM.
    def enterSUM(self, ctx:GrammarParser.SUMContext):
        pass

    # Exit a parse tree produced by GrammarParser#SUM.
    def exitSUM(self, ctx:GrammarParser.SUMContext):
        pass


    # Enter a parse tree produced by GrammarParser#LET_PASS.
    def enterLET_PASS(self, ctx:GrammarParser.LET_PASSContext):
        pass

    # Exit a parse tree produced by GrammarParser#LET_PASS.
    def exitLET_PASS(self, ctx:GrammarParser.LET_PASSContext):
        pass


    # Enter a parse tree produced by GrammarParser#ASSIGN_VAL.
    def enterASSIGN_VAL(self, ctx:GrammarParser.ASSIGN_VALContext):
        pass

    # Exit a parse tree produced by GrammarParser#ASSIGN_VAL.
    def exitASSIGN_VAL(self, ctx:GrammarParser.ASSIGN_VALContext):
        pass


    # Enter a parse tree produced by GrammarParser#MINUS.
    def enterMINUS(self, ctx:GrammarParser.MINUSContext):
        pass

    # Exit a parse tree produced by GrammarParser#MINUS.
    def exitMINUS(self, ctx:GrammarParser.MINUSContext):
        pass


    # Enter a parse tree produced by GrammarParser#DIVIDE.
    def enterDIVIDE(self, ctx:GrammarParser.DIVIDEContext):
        pass

    # Exit a parse tree produced by GrammarParser#DIVIDE.
    def exitDIVIDE(self, ctx:GrammarParser.DIVIDEContext):
        pass


    # Enter a parse tree produced by GrammarParser#BIGGER.
    def enterBIGGER(self, ctx:GrammarParser.BIGGERContext):
        pass

    # Exit a parse tree produced by GrammarParser#BIGGER.
    def exitBIGGER(self, ctx:GrammarParser.BIGGERContext):
        pass


    # Enter a parse tree produced by GrammarParser#NOT.
    def enterNOT(self, ctx:GrammarParser.NOTContext):
        pass

    # Exit a parse tree produced by GrammarParser#NOT.
    def exitNOT(self, ctx:GrammarParser.NOTContext):
        pass


    # Enter a parse tree produced by GrammarParser#NEWOBJ.
    def enterNEWOBJ(self, ctx:GrammarParser.NEWOBJContext):
        pass

    # Exit a parse tree produced by GrammarParser#NEWOBJ.
    def exitNEWOBJ(self, ctx:GrammarParser.NEWOBJContext):
        pass


    # Enter a parse tree produced by GrammarParser#IF_CLAUSE.
    def enterIF_CLAUSE(self, ctx:GrammarParser.IF_CLAUSEContext):
        pass

    # Exit a parse tree produced by GrammarParser#IF_CLAUSE.
    def exitIF_CLAUSE(self, ctx:GrammarParser.IF_CLAUSEContext):
        pass


    # Enter a parse tree produced by GrammarParser#STRING.
    def enterSTRING(self, ctx:GrammarParser.STRINGContext):
        pass

    # Exit a parse tree produced by GrammarParser#STRING.
    def exitSTRING(self, ctx:GrammarParser.STRINGContext):
        pass


    # Enter a parse tree produced by GrammarParser#TILDE.
    def enterTILDE(self, ctx:GrammarParser.TILDEContext):
        pass

    # Exit a parse tree produced by GrammarParser#TILDE.
    def exitTILDE(self, ctx:GrammarParser.TILDEContext):
        pass


    # Enter a parse tree produced by GrammarParser#FALSE.
    def enterFALSE(self, ctx:GrammarParser.FALSEContext):
        pass

    # Exit a parse tree produced by GrammarParser#FALSE.
    def exitFALSE(self, ctx:GrammarParser.FALSEContext):
        pass


    # Enter a parse tree produced by GrammarParser#ID.
    def enterID(self, ctx:GrammarParser.IDContext):
        pass

    # Exit a parse tree produced by GrammarParser#ID.
    def exitID(self, ctx:GrammarParser.IDContext):
        pass


    # Enter a parse tree produced by GrammarParser#BIGGEREQUALS.
    def enterBIGGEREQUALS(self, ctx:GrammarParser.BIGGEREQUALSContext):
        pass

    # Exit a parse tree produced by GrammarParser#BIGGEREQUALS.
    def exitBIGGEREQUALS(self, ctx:GrammarParser.BIGGEREQUALSContext):
        pass


    # Enter a parse tree produced by GrammarParser#INTEGER.
    def enterINTEGER(self, ctx:GrammarParser.INTEGERContext):
        pass

    # Exit a parse tree produced by GrammarParser#INTEGER.
    def exitINTEGER(self, ctx:GrammarParser.INTEGERContext):
        pass



del GrammarParser