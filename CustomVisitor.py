from yapl.grammar.HelloVisitor import HelloVisitor
from yapl.utils.Node import *

class CustomVisitor(HelloVisitor):
    def __init__(self):
        self.hello = HelloVisitor()
        self.errores = []

    def visitProgram(self, ctx):
        #Creacion nodo
        #variable o una clase tabla de simbolos
        #verifico reglas
        return self.hello.visitProgram(self)
    
    def visitClass(self):
        return HelloVisitor.visitClass(self, ctx=HelloVisitor)

    def visitDEFINITION_METHOD_PARAMS(self):
        return HelloVisitor.visitDEFINITION_METHOD_PARAMS(self, ctx=HelloVisitor)

    def visitDEFINITION_PARAMS(self):
        return HelloVisitor.visitDEFINITION_PARAMS(self, ctx=HelloVisitor)

    def visitFormal(self):
        return HelloVisitor.visitFormal(self, ctx=HelloVisitor)
    
    def visitEXPR_PARAMS(self):
        return HelloVisitor.visitEXPR_PARAMS(self, ctx=HelloVisitor)
  
    def visitTIMES(self):
        return HelloVisitor.visitTIMES(self, ctx=HelloVisitor)
    
    def visitEQUALS(self):
        return HelloVisitor.visitEQUALS(self, ctx=HelloVisitor)

    def visitVOID_EXPR(self):
        return HelloVisitor.visitVOID_EXPR(self, ctx=HelloVisitor)

    def visitDECLARE_TYPE(self):
        return HelloVisitor.visitDECLARE_TYPE(self, ctx=HelloVisitor)
    
    def visitTRUE(self):
        # BooleanNode(ctx.BOOLEAN_VAR().getText())
        return HelloVisitor.visitTRUE(self, ctx=HelloVisitor)

    def visitWHILE_CLAUSE(self):
        return HelloVisitor.visitWHILE_CLAUSE(self, ctx=HelloVisitor)

    def visitSUM(self):
        return HelloVisitor.visitSUM(self, ctx=HelloVisitor)
    def visitASSIGN_VAL(self):
        return HelloVisitor.visitASSIGN_VAL(self, ctx=HelloVisitor)

    def visitMINUS(self):
        return HelloVisitor.visitMINUS(self, ctx=HelloVisitor)

    def visitDIVIDE(self):
        return HelloVisitor.visitDIVIDE(self, ctx=HelloVisitor)
    
    def visitEXPR_NOT_KNOWN2(self):
        return HelloVisitor.visitEXPR_NOT_KNOWN2(self, ctx=HelloVisitor)
    
    def visitDEFINITION_ASSIGN(self):
        return HelloVisitor.visitDEFINITION_ASSIGN(self, ctx=HelloVisitor)

    def visitBIGGER(self):
        return HelloVisitor.visitBIGGER(self, ctx=HelloVisitor)
    
    def visitEXPR_NOT_KNOWN1(self):
        return HelloVisitor.visitEXPR_NOT_KNOWN1(self, ctx=HelloVisitor)

    def visitNOT(self):
        return HelloVisitor.visitNOT(self, ctx=HelloVisitor)

    def visitOBJ_DEF(self):
        return HelloVisitor.visitOBJ_DEF(self, ctx=HelloVisitor)

    def visitIF_CLAUSE(self):
        return HelloVisitor.visitIF_CLAUSE(self, ctx=HelloVisitor)
    
    def visitSTRING(self):
        return HelloVisitor.visitSTRING(self, ctx=HelloVisitor)

    def visitTILDE(self):
        return HelloVisitor.visitTILDE(self, ctx=HelloVisitor)

    def visitFALSE(self):
        # BooleanNode(ctx.BOOLEAN_VAR().getText())
        return HelloVisitor.visitFALSE(self, ctx=HelloVisitor)

    def visitID(self):
        return HelloVisitor.visitID(self, ctx=HelloVisitor)

    def visitBIGGEREQUALS(self):
        return HelloVisitor.visitBIGGEREQUALS(self, ctx=HelloVisitor)
    
    def visitINTEGER(self):
        # IntNode(ctx.INT_VAR().getText())
        return HelloVisitor.visitINTEGER(self, ctx=HelloVisitor)
    
    def visitR(self):
        return HelloVisitor.visitR(self, ctx=HelloVisitor)
