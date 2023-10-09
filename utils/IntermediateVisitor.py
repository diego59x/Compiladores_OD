from generated.GrammarVisitor import GrammarVisitor
from generated.GrammarParser import GrammarParser

from utils.Node import *
from utils.Tag import Tag
from utils.Temporales import *

class IntermediateVisitor(GrammarVisitor):
    def __init__(self):
        self.currentClass = None
        self.currentMethod = None
        self.intermediateCode = ''
        self.temps = 0
        self.labelTemps = 0
        self.tags = []
    
    def getIntermediateCode(self):
        return self.intermediateCode

    def getCurrentClass(self):
        return self.currentClass

    def visitR(self, ctx:GrammarParser.RContext):
        #print("visitR")
        return self.visit(ctx.program())

    def visitProgram(self, ctx:GrammarParser.ProgramContext):
        #print("visitProgram")
        classS = []
        for c in ctx.classDef():
            visitedClass = self.visit(c)
            classS.append(visitedClass)
        node = ProgramNode(classS)
        return node
    
    def visitCLASS_DEFINITION(self, ctx:GrammarParser.CLASS_DEFINITIONContext):
        name = ctx.TYPE(0).getText()
        # print("visitCLASS_DEFINITION")
        if self.currentClass is not None:
            self.intermediateCode += f'end_class_{self.currentClass}\n'
            self.currentClass = name
            self.intermediateCode += f'class_{name}:\n'
        else:
            self.currentClass = name
            self.intermediateCode += f'class_{name}:\n' 
        inherits = None
        features = []
        for f in ctx.feature():
            featureVisited = self.visit(f)
            features.append(featureVisited)
        if len(ctx.TYPE()) > 1:
            inherits = ctx.TYPE(1).getText()
        node = ClassNode(name, inherits, features)
        return node

    def visitDEFINITION_METHOD_PARAMS(self, ctx:GrammarParser.DEFINITION_METHOD_PARAMSContext):
        name = ctx.ID().getText()
        # print("visitDEFINITION_METHOD_PARAMS ", name, ctx.TYPE().getText())
        params = []
        for param in range(len(ctx.formal())):
            formal = ctx.formal(param)
            visitedFormal = self.visit(formal)
            params.append(visitedFormal)
        typE = ctx.TYPE().getText()
        if self.currentMethod is not None:
            self.currentMethod = name
            if typE:
                self.intermediateCode += f'class_{name}_{self.currentClass}[{typE}]:\n'
            else:
                self.intermediateCode += f'class_{name}_{self.currentClass}:\n'
        else:
            self.currentMethod = name
            if typE:
                self.intermediateCode += f'class_{name}_{self.currentClass}[{typE}]:\n'
            else:
                self.intermediateCode += f'class_{name}_{self.currentClass}:\n'
        expr = self.visit(ctx.expr())
        self.intermediateCode += f'end_class_{self.currentMethod}_{self.currentClass}\n'
        node = MethodNode(name, typE, params, expr)
        return node
    
    def visitDEFINITION_PARAMS(self, ctx:GrammarParser.DEFINITION_PARAMSContext):
        operations = ['+', '-', '*', '/', '<', '<=', '=', '~']
        typE = ctx.TYPE().getText()
        id = ctx.ID().getText()
        if ctx.expr() is None:
            node = DefParamsNode(id, typE, None)
            return node
        expr = self.visit(ctx.expr())
        node = DefParamsNode(id, typE, expr)
        contains_operator = any(op in str(expr) for op in operations)
        if not contains_operator:
            self.intermediateCode += f'{id}={expr}\n'
        else:
            exp = str(ctx.expr().getText())
            result = generate_intermediate_code(exp, id)
            self.intermediateCode += f'{result}\n'
        print("visitDEFINITION_PARAMS ", id, typE)
        return node
    #JUST ADD OFFSET
    def visitFormal(self, ctx:GrammarParser.FormalContext):
        id = ctx.ID().getText()
        typE = ctx.TYPE().getText()
        node = FormalNode(id, typE)
        self.intermediateCode += f'PARAM {id}\n'
        # print("visitFormal ", id, typE)
        return node
    #TODO: Verify Case
    def visitFormalAssign(self, ctx:GrammarParser.FormalAssignContext):
        typE = ctx.TYPE().getText()
        id = ctx.ID().getText()
        if ctx.expr() is None:
            node = FormalAssignNode(id, typE, None)
            return node
        expr = self.visit(ctx.expr())
        node = FormalAssignNode(id, typE, expr)
        # print("visitFormalAssign ", id, typE)
        return node
    
    def visitCALL(self, ctx:GrammarParser.CALLContext):
        # print("visitCALL")
        name = ctx.ID().getText()
        expressions = []
        intermediate_call = '' + name + '('
        for param in range(len(ctx.expr())):
            expr = ctx.expr(param)
            if param < len(ctx.expr()) - 1:
                intermediate_call += ','
            visitedExp = self.visit(expr)
            intermediate_call += f't{self.temps}'
            expressions.append(visitedExp)
        intermediate_call += ')'
        self.temps += 1
        node = CallNode(name, expressions, "t"+str(self.temps))
        self.intermediateCode += f't{self.temps}= CALL {intermediate_call}\n'
        return node
    #TODO: ASK FOR THIS
    def visitEXPR_PARAMS(self, ctx:GrammarParser.EXPR_PARAMSContext):
        #print("visitEXPR_PARAMS")
        return self.visitChildren(ctx.expr())
  
    def visitTIMES(self, ctx:GrammarParser.TIMESContext):
        #print("visitTIMES")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = TimesNode(leftOperand, rightOperand)
        self.temps += 1
        self.intermediateCode += f't{str(self.temps)}={leftOperand}*{rightOperand}\n'
        return node
    
    def visitEQUALS(self, ctx:GrammarParser.EQUALSContext):
        #print("visitEQUALS")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = EqualsNode(leftOperand, rightOperand)
        self.intermediateCode += f'{leftOperand}={rightOperand}\n'
        return node
    #TODO: ASK FOR THIS
    def visitVOID_EXPR(self, ctx:GrammarParser.VOID_EXPRContext):
        #print("visitVOID_EXPR")
        expr = self.visit(ctx.expr())
        node = VoidNode(expr)
        return node
    #TODO: ASK FOR THIS
    def visitDISPATCH(self, ctx:GrammarParser.DISPATCHContext):
        #print("visitDISPATCH")
        exprInitial = self.visit(ctx.expr(0))
        method = ctx.ID().getText()
        exprArguments = []

        for i in range(1, len(ctx.expr())):
            arg = self.visit(ctx.expr(i))
            exprArguments.append(arg)
        node = DispatchNode(exprInitial, method, exprArguments)
        return node

    def visitBLOCK(self, ctx:GrammarParser.BLOCKContext):
        #print("visitBLOCK")
        expr = []
        for e in ctx.expr():
            expr.append(self.visit(e))
        node = BlockNode(expr)
        return node
    
    def visitTRUE(self, ctx:GrammarParser.TRUEContext):
        #print("visitTRUE")
        return BooleanNode(ctx.TRUE().getText())

    def visitWHILE_CLAUSE(self, ctx:GrammarParser.WHILE_CLAUSEContext):
        #print("visitWHILE_CLAUSE")
        condition = self.visit(ctx.expr(0))
        expr = self.visit(ctx.expr(1))
        node = WhileNode(condition, expr)
        return node

    def visitSUM(self, ctx:GrammarParser.SUMContext):
        #print("visitSUM")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        self.temps += 1

        if (leftOperand.type == "call" and rightOperand.type == "call"):
            self.intermediateCode += f't{str(self.temps)}={leftOperand.temp}+{rightOperand.temp}\n'
        elif (leftOperand.type == "call" and rightOperand.type != "call"):
            self.intermediateCode += f't{str(self.temps)}={leftOperand.temp}+{rightOperand}\n'
        elif (leftOperand.type != "call" and rightOperand.type == "call"):
            self.intermediateCode += f't{str(self.temps)}={leftOperand}+{rightOperand.temp}\n'
        else:
            self.intermediateCode += f't{str(self.temps)}={leftOperand}+{rightOperand}\n'
        node = SumNode(leftOperand, rightOperand, "t"+str(+self.temps))
        return node
    # TODO: NEED REVIEW
    def visitLET_PASS(self, ctx:GrammarParser.LET_PASSContext):
        #print("visitLET_PASS")
        formalAssign = [self.visit(ctx.formalAssign(0))]
        for i in range(1, len(ctx.formalAssign())):
            formalAssignVisited = self.visit(ctx.formalAssign(i))
            formalAssign.append(formalAssignVisited)
        expr = self.visit(ctx.expr())
        # self.intermediateCode += f'class_{name}_{self.currentClass}:\n'

        node = LetPassNode(formalAssign, expr)
        return node
    
    def visitASSIGN_VAL(self, ctx:GrammarParser.ASSIGN_VALContext):
        id = ctx.ID().getText()
        exp = self.visit(ctx.expr())
        node = AssignNode(id, exp)
        # print("visitASSIGN_VAL ")
        if (hasattr(exp, "temp")):
            self.intermediateCode += f'{id}={exp.temp}\n'
        else:
            self.intermediateCode += f'{id}={ctx.expr().getText()}\n'
        return node

    def visitMINUS(self, ctx:GrammarParser.MINUSContext):
        #print("visitMINUS")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = MinusNode(leftOperand, rightOperand)
        self.temps += 1
        self.intermediateCode += f't{str(self.temps)}={leftOperand}-{rightOperand}\n'
        return node

    def visitDIVIDE(self, ctx:GrammarParser.DIVIDEContext):
        #print("visitDIVIDE")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = DivNode(leftOperand, rightOperand)
        self.temps += 1
        self.intermediateCode += f't{str(self.temps)}={leftOperand}/{rightOperand}\n'
        return node
    
    def visitBIGGER(self, ctx:GrammarParser.BIGGERContext):
        #print("visitBIGGER")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = BiggerNode(leftOperand, rightOperand)
        self.temps += 1
        self.intermediateCode += f't{str(self.temps)}={leftOperand}>{rightOperand}\n'
        return node

    def visitNOT(self, ctx:GrammarParser.NOTContext):
        #print("visitNOT")
        expr = self.visit(ctx.expr())
        node = NotNode(expr)
        self.intermediateCode += f'not {expr}\n'
        return node

    def visitNEWOBJ(self, ctx:GrammarParser.NEWOBJContext):
        #print("visitNEWOBJ")
        return ObjNode(ctx.TYPE().getText())

    def visitIF_CLAUSE(self, ctx:GrammarParser.IF_CLAUSEContext):
        #print("visitIF_CLAUSE")
        condition = self.visit(ctx.expr(0))
        self.temps += 1
        self.labelTemps += 1

        firstlabel = "label" + str(self.labelTemps)
        self.labelTemps += 1
        secondlabel = "label" + str(self.labelTemps)

        self.intermediateCode += f't{str(self.temps)}={condition}\n'
        self.intermediateCode += f'if t{str(self.temps)} goto {firstlabel}\n'
        self.intermediateCode += f'else goto {secondlabel} endif\n'


        self.intermediateCode += f'{firstlabel}_init\n'
        doIf = self.visit(ctx.expr(1))
        self.intermediateCode += f'{firstlabel}_finish\n'
        self.intermediateCode += f'{secondlabel}_init\n'
        doElse = self.visit(ctx.expr(2))
        self.intermediateCode += f'{secondlabel}_finish\n'
        node = IfNode(condition, doIf, doElse)
        return node
    
    def visitSTRING(self, ctx:GrammarParser.STRINGContext):
        #print("visitSTRING")
        return StringNode(ctx.STRING().getText())

    def visitTILDE(self, ctx:GrammarParser.TILDEContext):
        #print("visitTILDE")
        expr = self.visit(ctx.expr())
        self.intermediateCode += f'~ {expr}\n'
        return TildeNode(expr)

    def visitFALSE(self, ctx:GrammarParser.FALSEContext):
        #print("visitFALSE")
        return BooleanNode(ctx.FALSE().getText())

    def visitID(self, ctx:GrammarParser.IDContext):
        #print("visitID")
        return IdNode(ctx.ID().getText())

    def visitBIGGEREQUALS(self, ctx:GrammarParser.BIGGEREQUALSContext):
        #print("visitBIGGEREQUALS")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = BiggerEqualsNode(leftOperand, rightOperand)
        self.temps += 1
        self.intermediateCode += f't{str(self.temps)}={leftOperand}>={rightOperand}\n'
        return node
    
    def visitINTEGER(self, ctx:GrammarParser.INTEGERContext):
        #print("visitINTEGER")
        return IntNode(ctx.INTEGER().getText())
    