from yapl.grammar.HelloVisitor import HelloVisitor
from yapl.grammar.HelloParser import HelloParser
from yapl.utils.Node import *

class CustomVisitor(HelloVisitor):
    def __init__(self):
        self.hello = HelloVisitor()
        self.errores = []

    def visitR(self, ctx:HelloParser.RContext):
        return self.visitChildren(ctx)

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
        print("DEFINITION_PARAMS")
        return self.visitChildren(ctx)
    
    def visitFormal(self, ctx:HelloParser.FormalContext):
        return self.visitChildren(ctx)
    
    def visitCALL(self, ctx:HelloParser.CALLContext):
        return self.visitChildren(ctx)
    
    def visitEXPR_PARAMS(self, ctx:HelloParser.EXPR_PARAMSContext):
        return self.visitChildren(ctx)
  
    def visitTIMES(self, ctx:HelloParser.TIMESContext):
        return self.visitChildren(ctx)
    
    def visitEQUALS(self, ctx:HelloParser.EQUALSContext):
        return self.visitChildren(ctx)

    def visitVOID_EXPR(self, ctx:HelloParser.VOID_EXPRContext):
        return self.visitChildren(ctx)

    def visitDISPATCH(self, ctx:HelloParser.DISPATCHContext):
        TypeNode(ctx.TYPE().getText())
        return self.visitChildren(ctx)
    
    def visitBLOCK(self, ctx:HelloParser.BLOCKContext):
        return self.visitChildren(ctx)
    
    def visitTRUE(self, ctx:HelloParser.TRUEContext):
        return BooleanNode(ctx.TRUE().getText())

    def visitWHILE_CLAUSE(self, ctx:HelloParser.WHILE_CLAUSEContext):
        return self.visitChildren(ctx)

    def visitSUM(self, ctx:HelloParser.SUMContext):
        left_operand = ctx.expr(0)
        right_operand = ctx.expr(1)

        # Check if both operands are integers
        if (self.is_integer(left_operand) and self.is_integer(right_operand)):
            # Both operands are integers, sum is possible
            return int(left_operand.getText()) + int(right_operand.getText())
        else:
            # At least one operand is not an integer, sum is not possible
            self.errores.append("Error: Both operands of '+' must be integers.")

        return self.visitChildren(ctx)
    
    def visitLET_PASS(self, ctx:HelloParser.LET_PASSContext):
        return self.visitChildren(ctx)
    
    def visitASSIGN_VAL(self, ctx:HelloParser.ASSIGN_VALContext):
        print("asign", ctx.ID())
        id = ctx.ID().getText()
        exp = self.visit(ctx.expr())
        node = AssignNode(id, exp)
        print( ".-..-...- ", id, exp)
        return node

    def visitMINUS(self, ctx:HelloParser.MINUSContext):
        return self.visitChildren(ctx)

    def visitDIVIDE(self, ctx:HelloParser.DIVIDEContext):
        return self.visitChildren(ctx)
    
    def visitBIGGER(self, ctx:HelloParser.BIGGERContext):
        return self.visitChildren(ctx)
    
    def visitNOT(self, ctx:HelloParser.NOTContext):
        return self.visitChildren(ctx)

    def visitNEWOBJ(self, ctx:HelloParser.OBJ_DEFContext):
        return self.visitChildren(ctx)

    def visitIF_CLAUSE(self, ctx:HelloParser.IF_CLAUSEContext):
        return self.visitChildren(ctx)
    
    def visitSTRING(self, ctx:HelloParser.STRINGContext):
        return StringNode(ctx.STRING().getText())

    def visitTILDE(self, ctx:HelloParser.TILDEContext):
        return self.visitChildren(ctx)

    def visitFALSE(self, ctx:HelloParser.FALSEContext):
        return BooleanNode(ctx.FALSE().getText())

    def visitID(self, ctx:HelloParser.IDContext):
        return IdNode(ctx.ID().getText())

    def visitBIGGEREQUALS(self, ctx:HelloParser.BIGGEREQUALSContext):
        return self.visitChildren(ctx)
    
    def visitINTEGER(self, ctx:HelloParser.INTEGERContext):
        return IntNode(ctx.INTEGER().getText())
    
