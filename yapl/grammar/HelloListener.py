# Generated from ./Hello.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete listener for a parse tree produced by HelloParser.
class HelloListener(ParseTreeListener):

    # Enter a parse tree produced by HelloParser#r.
    def enterR(self, ctx:HelloParser.RContext):
        pass

    # Exit a parse tree produced by HelloParser#r.
    def exitR(self, ctx:HelloParser.RContext):
        pass


    # Enter a parse tree produced by HelloParser#program.
    def enterProgram(self, ctx:HelloParser.ProgramContext):
        pass

    # Exit a parse tree produced by HelloParser#program.
    def exitProgram(self, ctx:HelloParser.ProgramContext):
        pass


    # Enter a parse tree produced by HelloParser#class.
    def enterClass(self, ctx:HelloParser.ClassContext):
        pass

    # Exit a parse tree produced by HelloParser#class.
    def exitClass(self, ctx:HelloParser.ClassContext):
        pass


    # Enter a parse tree produced by HelloParser#DEFINITION_METHOD_PARAMS.
    def enterDEFINITION_METHOD_PARAMS(self, ctx:HelloParser.DEFINITION_METHOD_PARAMSContext):
        pass

    # Exit a parse tree produced by HelloParser#DEFINITION_METHOD_PARAMS.
    def exitDEFINITION_METHOD_PARAMS(self, ctx:HelloParser.DEFINITION_METHOD_PARAMSContext):
        pass


    # Enter a parse tree produced by HelloParser#DEFINITION_PARAMS.
    def enterDEFINITION_PARAMS(self, ctx:HelloParser.DEFINITION_PARAMSContext):
        pass

    # Exit a parse tree produced by HelloParser#DEFINITION_PARAMS.
    def exitDEFINITION_PARAMS(self, ctx:HelloParser.DEFINITION_PARAMSContext):
        pass


    # Enter a parse tree produced by HelloParser#formal.
    def enterFormal(self, ctx:HelloParser.FormalContext):
        pass

    # Exit a parse tree produced by HelloParser#formal.
    def exitFormal(self, ctx:HelloParser.FormalContext):
        pass


    # Enter a parse tree produced by HelloParser#formalAssign.
    def enterFormalAssign(self, ctx:HelloParser.FormalAssignContext):
        pass

    # Exit a parse tree produced by HelloParser#formalAssign.
    def exitFormalAssign(self, ctx:HelloParser.FormalAssignContext):
        pass


    # Enter a parse tree produced by HelloParser#CALL.
    def enterCALL(self, ctx:HelloParser.CALLContext):
        pass

    # Exit a parse tree produced by HelloParser#CALL.
    def exitCALL(self, ctx:HelloParser.CALLContext):
        pass


    # Enter a parse tree produced by HelloParser#EXPR_PARAMS.
    def enterEXPR_PARAMS(self, ctx:HelloParser.EXPR_PARAMSContext):
        pass

    # Exit a parse tree produced by HelloParser#EXPR_PARAMS.
    def exitEXPR_PARAMS(self, ctx:HelloParser.EXPR_PARAMSContext):
        pass


    # Enter a parse tree produced by HelloParser#TIMES.
    def enterTIMES(self, ctx:HelloParser.TIMESContext):
        pass

    # Exit a parse tree produced by HelloParser#TIMES.
    def exitTIMES(self, ctx:HelloParser.TIMESContext):
        pass


    # Enter a parse tree produced by HelloParser#EQUALS.
    def enterEQUALS(self, ctx:HelloParser.EQUALSContext):
        pass

    # Exit a parse tree produced by HelloParser#EQUALS.
    def exitEQUALS(self, ctx:HelloParser.EQUALSContext):
        pass


    # Enter a parse tree produced by HelloParser#VOID_EXPR.
    def enterVOID_EXPR(self, ctx:HelloParser.VOID_EXPRContext):
        pass

    # Exit a parse tree produced by HelloParser#VOID_EXPR.
    def exitVOID_EXPR(self, ctx:HelloParser.VOID_EXPRContext):
        pass


    # Enter a parse tree produced by HelloParser#DISPATCH.
    def enterDISPATCH(self, ctx:HelloParser.DISPATCHContext):
        pass

    # Exit a parse tree produced by HelloParser#DISPATCH.
    def exitDISPATCH(self, ctx:HelloParser.DISPATCHContext):
        pass


    # Enter a parse tree produced by HelloParser#BLOCK.
    def enterBLOCK(self, ctx:HelloParser.BLOCKContext):
        pass

    # Exit a parse tree produced by HelloParser#BLOCK.
    def exitBLOCK(self, ctx:HelloParser.BLOCKContext):
        pass


    # Enter a parse tree produced by HelloParser#TRUE.
    def enterTRUE(self, ctx:HelloParser.TRUEContext):
        pass

    # Exit a parse tree produced by HelloParser#TRUE.
    def exitTRUE(self, ctx:HelloParser.TRUEContext):
        pass


    # Enter a parse tree produced by HelloParser#WHILE_CLAUSE.
    def enterWHILE_CLAUSE(self, ctx:HelloParser.WHILE_CLAUSEContext):
        pass

    # Exit a parse tree produced by HelloParser#WHILE_CLAUSE.
    def exitWHILE_CLAUSE(self, ctx:HelloParser.WHILE_CLAUSEContext):
        pass


    # Enter a parse tree produced by HelloParser#SUM.
    def enterSUM(self, ctx:HelloParser.SUMContext):
        pass

    # Exit a parse tree produced by HelloParser#SUM.
    def exitSUM(self, ctx:HelloParser.SUMContext):
        pass


    # Enter a parse tree produced by HelloParser#LET_PASS.
    def enterLET_PASS(self, ctx:HelloParser.LET_PASSContext):
        pass

    # Exit a parse tree produced by HelloParser#LET_PASS.
    def exitLET_PASS(self, ctx:HelloParser.LET_PASSContext):
        pass


    # Enter a parse tree produced by HelloParser#ASSIGN_VAL.
    def enterASSIGN_VAL(self, ctx:HelloParser.ASSIGN_VALContext):
        pass

    # Exit a parse tree produced by HelloParser#ASSIGN_VAL.
    def exitASSIGN_VAL(self, ctx:HelloParser.ASSIGN_VALContext):
        pass


    # Enter a parse tree produced by HelloParser#MINUS.
    def enterMINUS(self, ctx:HelloParser.MINUSContext):
        pass

    # Exit a parse tree produced by HelloParser#MINUS.
    def exitMINUS(self, ctx:HelloParser.MINUSContext):
        pass


    # Enter a parse tree produced by HelloParser#DIVIDE.
    def enterDIVIDE(self, ctx:HelloParser.DIVIDEContext):
        pass

    # Exit a parse tree produced by HelloParser#DIVIDE.
    def exitDIVIDE(self, ctx:HelloParser.DIVIDEContext):
        pass


    # Enter a parse tree produced by HelloParser#BIGGER.
    def enterBIGGER(self, ctx:HelloParser.BIGGERContext):
        pass

    # Exit a parse tree produced by HelloParser#BIGGER.
    def exitBIGGER(self, ctx:HelloParser.BIGGERContext):
        pass


    # Enter a parse tree produced by HelloParser#NOT.
    def enterNOT(self, ctx:HelloParser.NOTContext):
        pass

    # Exit a parse tree produced by HelloParser#NOT.
    def exitNOT(self, ctx:HelloParser.NOTContext):
        pass


    # Enter a parse tree produced by HelloParser#NEWOBJ.
    def enterNEWOBJ(self, ctx:HelloParser.NEWOBJContext):
        pass

    # Exit a parse tree produced by HelloParser#NEWOBJ.
    def exitNEWOBJ(self, ctx:HelloParser.NEWOBJContext):
        pass


    # Enter a parse tree produced by HelloParser#IF_CLAUSE.
    def enterIF_CLAUSE(self, ctx:HelloParser.IF_CLAUSEContext):
        pass

    # Exit a parse tree produced by HelloParser#IF_CLAUSE.
    def exitIF_CLAUSE(self, ctx:HelloParser.IF_CLAUSEContext):
        pass


    # Enter a parse tree produced by HelloParser#STRING.
    def enterSTRING(self, ctx:HelloParser.STRINGContext):
        pass

    # Exit a parse tree produced by HelloParser#STRING.
    def exitSTRING(self, ctx:HelloParser.STRINGContext):
        pass


    # Enter a parse tree produced by HelloParser#TILDE.
    def enterTILDE(self, ctx:HelloParser.TILDEContext):
        pass

    # Exit a parse tree produced by HelloParser#TILDE.
    def exitTILDE(self, ctx:HelloParser.TILDEContext):
        pass


    # Enter a parse tree produced by HelloParser#FALSE.
    def enterFALSE(self, ctx:HelloParser.FALSEContext):
        pass

    # Exit a parse tree produced by HelloParser#FALSE.
    def exitFALSE(self, ctx:HelloParser.FALSEContext):
        pass


    # Enter a parse tree produced by HelloParser#ID.
    def enterID(self, ctx:HelloParser.IDContext):
        pass

    # Exit a parse tree produced by HelloParser#ID.
    def exitID(self, ctx:HelloParser.IDContext):
        pass


    # Enter a parse tree produced by HelloParser#BIGGEREQUALS.
    def enterBIGGEREQUALS(self, ctx:HelloParser.BIGGEREQUALSContext):
        pass

    # Exit a parse tree produced by HelloParser#BIGGEREQUALS.
    def exitBIGGEREQUALS(self, ctx:HelloParser.BIGGEREQUALSContext):
        pass


    # Enter a parse tree produced by HelloParser#INTEGER.
    def enterINTEGER(self, ctx:HelloParser.INTEGERContext):
        pass

    # Exit a parse tree produced by HelloParser#INTEGER.
    def exitINTEGER(self, ctx:HelloParser.INTEGERContext):
        pass



del HelloParser