from yapl.grammar.HelloVisitor import HelloVisitor
from yapl.utils.Node import *

class CustomVisitor(HelloVisitor):
    def __init__(self):
        self.errores = []

    def visitProgram(self, ctx:HelloVisitor.ProgramContext):
        #Creacion nodo
        #variable o una clase tabla de simbolos
        #verifico reglas
        return 
    
    def visitClass(self, ctx:HelloVisitor.ClassContext):
        return 

    def visitDEFINITION_METHOD_PARAMS(self, ctx:HelloVisitor.DEFINITION_METHOD_PARAMSContext):
        return 

    def visitDEFINITION_PARAMS(self, ctx:HelloVisitor.DEFINITION_PARAMSContext):
        return 

    def visitFormal(self, ctx:HelloVisitor.FormalContext):
        return 
    
    def visitEXPR_PARAMS(self, ctx:HelloVisitor.EXPR_PARAMSContext):
        return 
  
    def visitTIMES(self, ctx:HelloVisitor.TIMESContext):
        return
    
    def visitEQUALS(self, ctx:HelloVisitor.EQUALSContext):
        return

    def visitVOID_EXPR(self, ctx:HelloVisitor.VOID_EXPRContext):
        return 

    def visitDECLARE_TYPE(self, ctx:HelloVisitor.DECLARE_TYPEContext):
        return 
    
    def visitTRUE(self, ctx:HelloVisitor.TRUEContext):
        return BooleanNode(ctx.BOOLEAN_VAR().getText())

    def visitWHILE_CLAUSE(self, ctx:HelloVisitor.WHILE_CLAUSEContext):
        return 

    def visitSUM(self, ctx:HelloVisitor.SUMContext):
        return
    
    def visitASSIGN_VAL(self, ctx:HelloVisitor.ASSIGN_VALContext):
        return 

    def visitMINUS(self, ctx:HelloVisitor.MINUSContext):
        return 

    def visitDIVIDE(self, ctx:HelloVisitor.DIVIDEContext):
        return
    
    def visitEXPR_NOT_KNOWN2(self, ctx:HelloVisitor.EXPR_NOT_KNOWN2Context):
        return 
    
    def visitDEFINITION_ASSIGN(self, ctx:HelloVisitor.DEFINITION_ASSIGNContext):
        return 

    def visitBIGGER(self, ctx:HelloVisitor.BIGGERContext):
        return 
    
    def visitEXPR_NOT_KNOWN1(self, ctx:HelloVisitor.EXPR_NOT_KNOWN1Context):
        return 

    def visitNOT(self, ctx:HelloVisitor.NOTContext):
        return 

    def visitOBJ_DEF(self, ctx:HelloVisitor.OBJ_DEFContext):
        return 

    def visitIF_CLAUSE(self, ctx:HelloVisitor.IF_CLAUSEContext):
        return 
    
    def visitSTRING(self, ctx:HelloVisitor.STRINGContext):
        return 

    def visitTILDE(self, ctx:HelloVisitor.TILDEContext):
        return 

    def visitFALSE(self, ctx:HelloVisitor.FALSEContext):
        return BooleanNode(ctx.BOOLEAN_VAR().getText())

    def visitID(self, ctx:HelloVisitor.IDContext):
        return 

    def visitBIGGEREQUALS(self, ctx:HelloVisitor.BIGGEREQUALSContext):
        return
    
    def visitINTEGER(self, ctx:HelloVisitor.INTEGERContext):
        return IntNode(ctx.INT_VAR().getText())
    
    def visitR(self, ctx:HelloVisitor.RContext):
        return 
