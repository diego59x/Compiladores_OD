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
        print("visitR")
        return self.visit(ctx.program())

    def visitProgram(self, ctx:HelloParser.ProgramContext):
        classS = []
        for c in ctx.class_():
            visitedClass = self.visit(c)
            classS.append(visitedClass)
        node = ProgramNode(classS)
        print("visitProgram")
        return node
    
    def visitClass(self, ctx:HelloParser.ClassContext):
        name = ctx.TYPE(0).getText()
        inherits = None
        features = []
        for f in ctx.feature():
            featureVisited = self.visit(f)
            features.append(featureVisited)
        if len(ctx.TYPE()) > 1:
            inherits = ctx.TYPE(1).getText()
        node = ClassNode(name, inherits, features)
        print("visitClass")
        self.symbol_table.add_method(name, '', 'void')
        return node

    def visitDEFINITION_METHOD_PARAMS(self, ctx:HelloParser.DEFINITION_METHOD_PARAMSContext):
        name = ctx.ID().getText()
        params = []
        for param in range(len(ctx.formal())):
            formal = ctx.formal(param)
            visitedFormal = self.visit(formal)
            params.append(visitedFormal)
        expr = self.visit(ctx.expr())
        typE = ctx.TYPE().getText()
        node = MethodNode(name, typE, params, expr)
        self.symbol_table.add_method(name, params, typE)
        print("visitDEFINITION_METHOD_PARAMS")
        return node
    
    def visitDEFINITION_PARAMS(self, ctx:HelloParser.DEFINITION_PARAMSContext):
        typE = ctx.TYPE().getText()
        id = ctx.ID().getText()
        if ctx.expr() is None:
            node = DefParamsNode(id, typE, None)
            return node
        expr = self.visit(ctx.expr())
        node = DefParamsNode(id, typE, expr)
        definition_value = expr.token
        self.symbol_table.add_attribute(id, definition_value, typE)
        print("visitDEFINITION_PARAMS", expr.token)
        return node
    
    def visitFormal(self, ctx:HelloParser.FormalContext):
        id = ctx.ID().getText()
        typE = ctx.TYPE().getText()
        node = FormalNode(id, typE)
        print("visitFormal")
        return node

    def visitFormalAssign(self, ctx:HelloParser.FormalAssignContext):
        typE = ctx.TYPE().getText()
        id = ctx.ID().getText()
        if ctx.expr() is None:
            node = FormalAssignNode(id, typE, None)
            return node
        expr = self.visit(ctx.expr())
        node = FormalAssignNode(id, typE, expr)
        print("visitFormalAssign")
        return node
    
    def visitCALL(self, ctx:HelloParser.CALLContext):
        name = ctx.ID().getText()
        expressions = []
        for param in range(len(ctx.expr())):
            expr = ctx.expr(param)
            visitedExp = self.visit(expr)
            expressions.append(visitedExp)
        node = CallNode(name, expressions)
        self.symbol_table.add_method(name, '', 'void')
        print("visitCALL")
        return node
    
    def visitEXPR_PARAMS(self, ctx:HelloParser.EXPR_PARAMSContext):
        print("visitEXPR_PARAMS")
        return self.visitChildren(ctx.expr())
  
    def visitTIMES(self, ctx:HelloParser.TIMESContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = TimesNode(leftOperand, rightOperand)
        print("visitTIMES")
        return node
    
    def visitEQUALS(self, ctx:HelloParser.EQUALSContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = EqualsNode(leftOperand, rightOperand)
        print("visitEQUALS")
        return node

    def visitVOID_EXPR(self, ctx:HelloParser.VOID_EXPRContext):
        expr = self.visit(ctx.expr())
        node = VoidNode(expr)
        print("visitVOID_EXPR")
        return node

    def visitDISPATCH(self, ctx:HelloParser.DISPATCHContext):
        exprInitial = self.visit(ctx.expr(0))
        method = ctx.ID().getText()
        exprArguments = []

        for i in range(1, len(ctx.expr())):
            arg = self.visit(ctx.expr(i))
            exprArguments.append(arg)
        node = DispatchNode(exprInitial, method, exprArguments)
        print("visitDISPATCH")
        return node
    
    def visitBLOCK(self, ctx:HelloParser.BLOCKContext):
        expr = []
        for e in ctx.expr():
            expr.append(self.visit(e))
        node = BlockNode(expr)
        print("visitBLOCK")
        return node
    
    def visitTRUE(self, ctx:HelloParser.TRUEContext):
        print("visitTRUE")
        return BooleanNode(ctx.TRUE().getText())

    def visitWHILE_CLAUSE(self, ctx:HelloParser.WHILE_CLAUSEContext):
        condition = self.visit(ctx.expr(0))
        expr = self.visit(ctx.expr(1))
        node = WhileNode(condition, expr)
        print("visitWHILE_CLAUSE")
        return node

    def visitSUM(self, ctx:HelloParser.SUMContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = SumNode(leftOperand, rightOperand)
        print("visitSUM")
        return node
    
    def visitLET_PASS(self, ctx:HelloParser.LET_PASSContext):
        #print("visitLET_PASS")
        formalAssign = [self.visit(ctx.formalAssign(0))]
        for i in range(1, len(ctx.formalAssign())):
            formalAssignVisited = self.visit(ctx.formalAssign(i))
            formalAssign.append(formalAssignVisited)
        expr = self.visit(ctx.expr())
        node = LetPassNode(formalAssign, expr)
        print("visitLET_PASS")
        return node
    
    def visitASSIGN_VAL(self, ctx:HelloParser.ASSIGN_VALContext):
        id = ctx.ID().getText()
        exp = self.visit(ctx.expr())
        node = AssignNode(id, exp)
        if (id not in self.symbol_table.attributes.keys()):
            self.symbol_table.add_local_variable(
                name=id, 
                value=exp, 
                scope='local', 
                type=type(exp)
            )
        print("visitASSIGN_VAL")
        return node

    def visitMINUS(self, ctx:HelloParser.MINUSContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = MinusNode(leftOperand, rightOperand)
        print("visitMINUS")
        return node

    def visitDIVIDE(self, ctx:HelloParser.DIVIDEContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = DivNode(leftOperand, rightOperand)
        print("visitDIVIDE")
        return node
    
    def visitBIGGER(self, ctx:HelloParser.BIGGERContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = BiggerNode(leftOperand, rightOperand)
        print("visitBIGGER")
        return node
    
    def visitNOT(self, ctx:HelloParser.NOTContext):
        expr = self.visit(ctx.expr())
        node = NotNode(expr)
        print("visitNOT")
        return node

    def visitNEWOBJ(self, ctx:HelloParser.NEWOBJContext):
        print("visitNEWOBJ")
        return ObjNode(ctx.TYPE().getText())

    def visitIF_CLAUSE(self, ctx:HelloParser.IF_CLAUSEContext):
        condition = self.visit(ctx.expr(0))
        doIf = self.visit(ctx.expr(1))
        doElse = self.visit(ctx.expr(2))
        node = IfNode(condition, doIf, doElse)
        print("visitIF_CLAUSE")
        return node
    
    def visitSTRING(self, ctx:HelloParser.STRINGContext):
        print("visitSTRING", ctx.STRING().getText())
        return StringNode(ctx.STRING().getText())

    def visitTILDE(self, ctx:HelloParser.TILDEContext):
        expr = self.visit(ctx.expr())
        print("visitTILDE")
        return TildeNode(expr)

    def visitFALSE(self, ctx:HelloParser.FALSEContext):
        print("visitFALSE")
        return BooleanNode(ctx.FALSE().getText())

    def visitID(self, ctx:HelloParser.IDContext):
        print("visitID")
        return IdNode(ctx.ID().getText())

    def visitBIGGEREQUALS(self, ctx:HelloParser.BIGGEREQUALSContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = BiggerEqualsNode(leftOperand, rightOperand)
        print("visitBIGGEREQUALS")
        return node
    
    def visitINTEGER(self, ctx:HelloParser.INTEGERContext):
        print("visitINTEGER")
        return IntNode(ctx.INTEGER().getText())
    
