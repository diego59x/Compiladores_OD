from yapl.grammar.HelloVisitor import HelloVisitor
from yapl.grammar.HelloParser import HelloParser
from yapl.utils.Node import *

class CustomVisitor(HelloVisitor):
    def __init__(self):
        self.hello = HelloVisitor()
        self.errores = []

    def visitProgram(self, ctx:HelloParser.ProgramContext):
        #Creacion nodo
        #variable o una clase tabla de simbolos
        #verifico reglas
        return self.visitChildren(ctx)
    
    def visitClass(self, ctx:HelloParser.ClassContext):
        return self.visitChildren(ctx)

    def visitDEFINITION_METHOD_PARAMS(self, ctx:HelloParser.DEFINITION_METHOD_PARAMSContext):
        return self.visitChildren(ctx)
    
    def visitDEFINITION_PARAMS(self, ctx:HelloParser.DEFINITION_PARAMSContext):
        return self.visitChildren(ctx)
    
    def visitFormal(self, ctx:HelloParser.FormalContext):
        return self.visitChildren(ctx)
    
    def visitEXPR_PARAMS(self, ctx:HelloParser.EXPR_PARAMSContext):
        return self.visitChildren(ctx)
  
    def visitTIMES(self, ctx:HelloParser.TIMESContext):
        return self.visitChildren(ctx)
    
    def visitEQUALS(self, ctx:HelloParser.EQUALSContext):
        return self.visitChildren(ctx)

    def visitVOID_EXPR(self, ctx:HelloParser.VOID_EXPRContext):
        return self.visitChildren(ctx)

    def visitDECLARE_TYPE(self, ctx:HelloParser.DECLARE_TYPEContext):
        return self.visitChildren(ctx)
    
    def visitTRUE(self, ctx:HelloParser.TRUEContext):
        # BooleanNode(ctx.BOOLEAN_VAR().getText())
        return self.visitChildren(ctx)

    def visitWHILE_CLAUSE(self, ctx:HelloParser.WHILE_CLAUSEContext):
        return self.visitChildren(ctx)

    def visitSUM(self, ctx:HelloParser.SUMContext):
        return self.visitChildren(ctx)
    
    def visitASSIGN_VAL(self, ctx:HelloParser.ASSIGN_VALContext):
        return self.visitChildren(ctx)

    def visitMINUS(self, ctx:HelloParser.MINUSContext):
        return self.visitChildren(ctx)

    def visitDIVIDE(self, ctx:HelloParser.DIVIDEContext):
        return self.visitChildren(ctx)
    
    def visitEXPR_NOT_KNOWN2(self, ctx:HelloParser.EXPR_NOT_KNOWN2Context):
        return self.visitChildren(ctx)
    
    def visitDEFINITION_ASSIGN(self, ctx:HelloParser.DEFINITION_ASSIGNContext):
        return self.visitChildren(ctx)

    def visitBIGGER(self, ctx:HelloParser.BIGGERContext):
        return self.visitChildren(ctx)
    
    def visitEXPR_NOT_KNOWN1(self, ctx:HelloParser.EXPR_NOT_KNOWN1Context):
        return self.visitChildren(ctx)

    def visitNOT(self, ctx:HelloParser.NOTContext):
        return self.visitChildren(ctx)

    def visitOBJ_DEF(self, ctx:HelloParser.OBJ_DEFContext):
        return self.visitChildren(ctx)

    def visitIF_CLAUSE(self, ctx:HelloParser.IF_CLAUSEContext):
        return self.visitChildren(ctx)
    
    def visitSTRING(self, ctx:HelloParser.STRINGContext):
        return self.visitChildren(ctx)

    def visitTILDE(self, ctx:HelloParser.TILDEContext):
        return self.visitChildren(ctx)

    def visitFALSE(self, ctx:HelloParser.FALSEContext):
        # BooleanNode(ctx.BOOLEAN_VAR().getText())
        return self.visitChildren(ctx)

    def visitID(self, ctx:HelloParser.IDContext):
        return self.visitChildren(ctx)

    def visitBIGGEREQUALS(self, ctx:HelloParser.BIGGEREQUALSContext):
        return self.visitChildren(ctx)
    
    def visitINTEGER(self, ctx:HelloParser.INTEGERContext):
        return IntNode(ctx.INTEGER().getText())
    
    def visitR(self, ctx:HelloParser.RContext):
        return self.visitChildren(ctx)
