from yapl.grammar.HelloVisitor import HelloVisitor
from yapl.grammar.HelloParser import HelloParser
from yapl.utils.Node import *
from SymbolsTable import *

class TableVisitor(HelloVisitor):
    def __init__(self):
        self.hello = HelloVisitor()
        self.errores = []
        self.symbol_table = SymbolsTable()

    def visitR(self, ctx:HelloParser.RContext):
        #print("visitR")
        return self.visit(ctx.program())

    def visitProgram(self, ctx:HelloParser.ProgramContext):
        #print("visitProgram")
        classS = []
        for c in ctx.class_():
            visitedClass = self.visit(c)
            classS.append(visitedClass)
        node = ProgramNode(classS)
        return node
    
    def visitClass(self, ctx:HelloParser.ClassContext):
        #print("visitClass")
        name = ctx.TYPE(0).getText()
        inherits = None
        features = []
        for f in ctx.feature():
            featureVisited = self.visit(f)
            features.append(featureVisited)
        if len(ctx.TYPE()) > 1:
            inherits = ctx.TYPE(1).getText()
        node = ClassNode(name, inherits, features)
        return node

    def visitDEFINITION_METHOD_PARAMS(self, ctx:HelloParser.DEFINITION_METHOD_PARAMSContext):
        #print("visitDEFINITION_METHOD_PARAMS")
        name = ctx.ID().getText()
        params = []
        for param in range(len(ctx.formal())):
            formal = ctx.formal(param)
            visitedFormal = self.visit(formal)
            params.append(visitedFormal)
        expr = self.visit(ctx.expr())
        typE = ctx.TYPE().getText()
        node = MethodNode(name, typE, params, expr)
        return node
    
    def visitDEFINITION_PARAMS(self, ctx:HelloParser.DEFINITION_PARAMSContext):
        #print("visitDEFINITION_PARAMS")
        typE = ctx.TYPE().getText()
        id = ctx.ID().getText()
        if ctx.expr() is None:
            node = DefParamsNode(id, typE, None)
            return node
        expr = self.visit(ctx.expr())
        node = DefParamsNode(id, typE, expr)
        self.symbol_table.add_attribute(self, id, typE)
        return node
    
    def visitFormal(self, ctx:HelloParser.FormalContext):
        #print("visitFormal")
        id = ctx.ID().getText()
        typE = ctx.TYPE().getText()
        node = FormalNode(id, typE)
        return node

    def visitFormalAssign(self, ctx:HelloParser.FormalAssignContext):
        #print("visitFormalAssign")
        typE = ctx.TYPE().getText()
        id = ctx.ID().getText()
        if ctx.expr() is None:
            node = FormalAssignNode(id, typE, None)
            return node
        expr = self.visit(ctx.expr())
        node = FormalAssignNode(id, typE, expr)
        return node
    
    def visitCALL(self, ctx:HelloParser.CALLContext):
        #print("visitCALL")
        name = ctx.ID().getText()
        expressions = []
        for param in range(len(ctx.expr())):
            expr = ctx.expr(param)
            visitedExp = self.visit(expr)
            expressions.append(visitedExp)
        node = CallNode(name, expressions)
        return node
    
    def visitEXPR_PARAMS(self, ctx:HelloParser.EXPR_PARAMSContext):
        #print("visitEXPR_PARAMS")
        return self.visitChildren(ctx.expr())
  
    def visitTIMES(self, ctx:HelloParser.TIMESContext):
        #print("visitTIMES")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = TimesNode(leftOperand, rightOperand)
        return node
    
    def visitEQUALS(self, ctx:HelloParser.EQUALSContext):
        #print("visitEQUALS")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = EqualsNode(leftOperand, rightOperand)
        return node

    def visitVOID_EXPR(self, ctx:HelloParser.VOID_EXPRContext):
        #print("visitVOID_EXPR")
        expr = self.visit(ctx.expr())
        node = VoidNode(expr)
        return node

    def visitDISPATCH(self, ctx:HelloParser.DISPATCHContext):
        #print("visitDISPATCH")
        exprInitial = self.visit(ctx.expr(0))
        method = ctx.ID().getText()
        exprArguments = []

        for i in range(1, len(ctx.expr())):
            arg = self.visit(ctx.expr(i))
            exprArguments.append(arg)
        node = DispatchNode(exprInitial, method, exprArguments)
        return node
    
    def visitBLOCK(self, ctx:HelloParser.BLOCKContext):
        #print("visitBLOCK")
        expr = []
        for e in ctx.expr():
            expr.append(self.visit(e))
        node = BlockNode(expr)
        return node
    
    def visitTRUE(self, ctx:HelloParser.TRUEContext):
        #print("visitTRUE")
        return BooleanNode(ctx.TRUE().getText())

    def visitWHILE_CLAUSE(self, ctx:HelloParser.WHILE_CLAUSEContext):
        #print("visitWHILE_CLAUSE")
        condition = self.visit(ctx.expr(0))
        expr = self.visit(ctx.expr(1))
        node = WhileNode(condition, expr)
        return node

    def visitSUM(self, ctx:HelloParser.SUMContext):
        #print("visitSUM")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = SumNode(leftOperand, rightOperand)
        return node
    
    def visitLET_PASS(self, ctx:HelloParser.LET_PASSContext):
        #print("visitLET_PASS")
        formalAssign = [self.visit(ctx.formalAssign(0))]
        for i in range(1, len(ctx.formalAssign())):
            formalAssignVisited = self.visit(ctx.formalAssign(i))
            formalAssign.append(formalAssignVisited)
        expr = self.visit(ctx.expr())
        node = LetPassNode(formalAssign, expr)
        return node
    
    def visitASSIGN_VAL(self, ctx:HelloParser.ASSIGN_VALContext):
        #print("visitASSIGN_VAL")
        id = ctx.ID().getText()
        exp = self.visit(ctx.expr())
        node = AssignNode(id, exp)
        return node

    def visitMINUS(self, ctx:HelloParser.MINUSContext):
        #print("visitMINUS")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = MinusNode(leftOperand, rightOperand)
        return node

    def visitDIVIDE(self, ctx:HelloParser.DIVIDEContext):
        #print("visitDIVIDE")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = DivNode(leftOperand, rightOperand)
        return node
    
    def visitBIGGER(self, ctx:HelloParser.BIGGERContext):
        #print("visitBIGGER")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = BiggerNode(leftOperand, rightOperand)
        return node
    
    def visitNOT(self, ctx:HelloParser.NOTContext):
        #print("visitNOT")
        expr = self.visit(ctx.expr())
        node = NotNode(expr)
        return node

    def visitNEWOBJ(self, ctx:HelloParser.NEWOBJContext):
        #print("visitNEWOBJ")
        return ObjNode(ctx.TYPE().getText())

    def visitIF_CLAUSE(self, ctx:HelloParser.IF_CLAUSEContext):
        #print("visitIF_CLAUSE")
        condition = self.visit(ctx.expr(0))
        doIf = self.visit(ctx.expr(1))
        doElse = self.visit(ctx.expr(2))
        node = IfNode(condition, doIf, doElse)
        return node
    
    def visitSTRING(self, ctx:HelloParser.STRINGContext):
        #print("visitSTRING")
        return StringNode(ctx.STRING().getText())

    def visitTILDE(self, ctx:HelloParser.TILDEContext):
        #print("visitTILDE")
        expr = self.visit(ctx.expr())
        return TildeNode(expr)

    def visitFALSE(self, ctx:HelloParser.FALSEContext):
        #print("visitFALSE")
        return BooleanNode(ctx.FALSE().getText())

    def visitID(self, ctx:HelloParser.IDContext):
        #print("visitID")
        return IdNode(ctx.ID().getText())

    def visitBIGGEREQUALS(self, ctx:HelloParser.BIGGEREQUALSContext):
        #print("visitBIGGEREQUALS")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = BiggerEqualsNode(leftOperand, rightOperand)
        return node
    
    def visitINTEGER(self, ctx:HelloParser.INTEGERContext):
        #print("visitINTEGER")
        return IntNode(ctx.INTEGER().getText())
    
