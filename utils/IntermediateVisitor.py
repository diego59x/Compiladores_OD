from generated.GrammarVisitor import GrammarVisitor
from generated.GrammarParser import GrammarParser

from utils.Node import *
from utils.Tag import Tag
from utils.Temporales import *
from utils.MIPS import *

class IntermediateVisitor(GrammarVisitor):
    def __init__(self, symbols_table, offset):
        self.currentClass = None
        self.currentMethod = None
        self.intermediateCode = ''
        self.temps = 0
        self.temporals = Temporales()
        self.labelTemps = 0
        self.tags = []
        self.symbols_table = symbols_table.getTable()
        self.current_offset = offset
        self.newClass = ''
        self.strings = []
        self.ints = []
    
    def getIntermediateCode(self):
        self.intermediateCode = insertStrings(self.strings, self.ints, self.intermediateCode)
        
        self.intermediateCode = inheritClasses([self.symbols_table["Main"]["superclass"]], self.intermediateCode)
        return self.intermediateCode
    
    def getCurrentClass(self):
        return self.currentClass
    
    def getFinalSymbolsTable(self):
        return self.symbols_table

    def addTempToSymbols(self):
        if self.currentMethod and self.currentClass:
            if not "variables" in self.symbols_table[self.currentClass]["methods"][self.currentMethod]:
                self.symbols_table[self.currentClass]["methods"][self.currentMethod]["variables"] = {}
            self.symbols_table[self.currentClass]["methods"][self.currentMethod]["variables"][f"t{self.temps}"] = {"type": "Int", "offset": self.current_offset}
        else:
            self.symbols_table[self.currentClass]["variables"][f"t{self.temps}"] = {"type": "Int", "offset": self.current_offset}
        self.current_offset += 4

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
        # print("visitCLASS_DEFINITION", name)
        self.currentClass = name
        # if self.currentClass is not None:
        #     self.intermediateCode += f'end_class_{self.currentClass}\n'
        #     self.currentClass = name
        #     self.intermediateCode += f'class_{name}:\n'
        # else:
        #     self.currentClass = name
        #     self.intermediateCode += f'class_{name}:\n' 
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
        params = []
        for param in range(len(ctx.formal())):
            formal = ctx.formal(param)
            visitedFormal = self.visit(formal)
            params.append(visitedFormal)
        typE = ctx.TYPE().getText()

        self.currentMethod = name
        self.intermediateCode += f'class_{name}_{self.currentClass}:\n'
    
        expr = self.visit(ctx.expr())
        # self.intermediateCode += f'end_class_{self.currentMethod}_{self.currentClass}\n'

        if (f'{self.currentMethod}_{self.currentClass}'== "main_Main"):
            # End system call
            self.intermediateCode += f'   li $v0, 10 \n   syscall \n'

        node = MethodNode(name, typE, params, expr)
        self.currentMethod = None
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
        self.ints.append([id, expr.token])
        contains_operator = any(op in str(expr) for op in operations)
        if not contains_operator:
            self.temps = self.temporals.get_correct_id(self.currentClass)
            res = self.temporals.set_temporal(self.currentClass, f't{str(self.temps)}', f'{id}')
            self.intermediateCode += f'    lw ${res}'
            # self.intermediateCode += f'    GP[{self.symbols_table[self.currentClass]["variables"][id]["offset"]}]={expr}\n'
        else:
            exp = str(ctx.expr().getText())
            result = generate_intermediate_code(exp, id)
            self.intermediateCode += f'    {result}\n'
        return node
    
    def visitFormal(self, ctx:GrammarParser.FormalContext):
        id = ctx.ID().getText()
        typE = ctx.TYPE().getText()
        node = FormalNode(id, typE)
        parent = ctx.parentCtx.ID().getText()
        gp = self.symbols_table[self.currentClass]["methods"][parent]["params"][id]["offset"]
        self.intermediateCode += f'    PARAM GP[{gp}]\n'
        return node
    
    def visitFormalAssign(self, ctx:GrammarParser.FormalAssignContext):
        typE = ctx.TYPE().getText()
        id = ctx.ID().getText()
        if ctx.expr() is None:
            node = FormalAssignNode(id, typE, None)
            return node
        expr = self.visit(ctx.expr())
        self.intermediateCode += f'    {id}={expr}\n'
        node = FormalAssignNode(id, typE, expr)
        # print("visitFormalAssign ", id, typE)
        return node
    
    def visitCALL(self, ctx:GrammarParser.CALLContext):
        name = ctx.ID().getText()
        expressions = []
        intermediate_call = ''

        for param in range(len(ctx.expr())):
            expr = ctx.expr(param)
            visitedExp = self.visit(expr)

            if (isinstance(visitedExp, str) and "string" in visitedExp):
                # Load string
                intermediate_call += f'   la $a{param}, {visitedExp}\n'
            else:        
                # Load temporal
                intermediate_call += f'   move $t{self.temps}, $a{param}\n'
            expressions.append(visitedExp)

        # self.temps += 1
        node = CallNode(name, expressions, "t"+str(self.temps))
        self.intermediateCode += f'{intermediate_call}'
        self.intermediateCode += f'   jal {name}\n'
        
        return node
    
    def visitEXPR_PARAMS(self, ctx:GrammarParser.EXPR_PARAMSContext):
        #print("visitEXPR_PARAMS")
        return self.visit(ctx.expr())
  
    def visitTIMES(self, ctx:GrammarParser.TIMESContext):
        #print("visitTIMES")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        self.temps = self.temporals.get_correct_id(self.currentClass)
        node = TimesNode(leftOperand, rightOperand, "t" + str(self.temps) )

        res = self.temporals.set_double_temporal(self.currentClass, f'$t{str(self.temps)}', f'${leftOperand}', f'${rightOperand}')
        self.intermediateCode += "    mul" + res

        return node
    
    def visitEQUALS(self, ctx:GrammarParser.EQUALSContext):
        #print("visitEQUALS")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = EqualsNode(leftOperand, rightOperand)
        self.intermediateCode += f'    {leftOperand}={rightOperand}\n'

        return node
    #TODO: ASK FOR THIS
    def visitVOID_EXPR(self, ctx:GrammarParser.VOID_EXPRContext):
        #print("visitVOID_EXPR")
        expr = self.visit(ctx.expr())
        node = VoidNode(expr)
        return node
    
    def visitDISPATCH(self, ctx:GrammarParser.DISPATCHContext):
        #print("visitDISPATCH")
        exprInitial = self.visit(ctx.expr(0))
        method = ctx.ID().getText()
        exprArguments = []

        for i in range(1, len(ctx.expr())):
            arg = self.visit(ctx.expr(i))
            exprArguments.append(arg)

        tokens = [obj.token for obj in exprArguments]
        arguments = ", ".join(tokens)

        self.intermediateCode += f'    new {exprInitial.token} goto {method} ({arguments})  \n'
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
        self.labelTemps+=1
        

        self.intermediateCode += f'    label{str(self.labelTemps)}_init\n'
        condition = self.visit(ctx.expr(0))
        if (hasattr(condition, "temp")):
            self.intermediateCode += f'    if {condition.temp} else goto label{self.labelTemps}_finish\n'
        else:
            self.intermediateCode += f'    if {condition} else goto label{self.labelTemps}_finish\n'
        expr = self.visit(ctx.expr(1))
        
        if (hasattr(condition, "left")):
            self.intermediateCode += f'    goto label{str(self.labelTemps)}_init\n'
        else:
            self.intermediateCode += f'    goto label{str(self.labelTemps)}_init\n'
            

        setattr(expr, "lastTemp", "t"+str(self.temps))
        self.intermediateCode += f'    label{str(self.labelTemps)}_finish\n'
            
        node = WhileNode(condition, expr)
        return node

    def visitSUM(self, ctx:GrammarParser.SUMContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        self.temps = self.temporals.get_correct_id(self.currentClass)

        # Add the temp to the symbols table
        used_offset = self.current_offset
        self.addTempToSymbols()

        if (leftOperand.type == "call" and rightOperand.type == "call"):
            self.intermediateCode += f'GP[{self.current_offset}]={leftOperand.temp}+{rightOperand.temp}\n'
        elif (leftOperand.type == "call" and rightOperand.type != "call"):
            self.intermediateCode += f'GP[{self.current_offset}]={leftOperand.temp}+{rightOperand}\n'
        elif (leftOperand.type != "call" and rightOperand.type == "call"):
            self.intermediateCode += f'GP[{self.current_offset}]={leftOperand}+{rightOperand.temp}\n'
        else:
            if self.currentMethod and self.currentClass:
                if leftOperand.type == 'id':
                    if leftOperand.token in self.symbols_table[self.currentClass]["methods"][self.currentMethod]["params"]:
                        final_left = f'GP[{self.symbols_table[self.currentClass]["methods"][self.currentMethod]["params"][leftOperand.token]["offset"]}]'
                    elif leftOperand.token in self.symbols_table[self.currentClass]["variables"]:
                        final_left = f'GP[{self.symbols_table[self.currentClass]["variables"][leftOperand.token]["offset"]}]'
                    else:
                        final_left = leftOperand.token
                else:
                    final_left = leftOperand
                if rightOperand.type == 'id':
                    if rightOperand.token in self.symbols_table[self.currentClass]["methods"][self.currentMethod]["params"]:
                        final_right = f'GP[{self.symbols_table[self.currentClass]["methods"][self.currentMethod]["params"][rightOperand.token]["offset"]}]'
                    elif rightOperand.token in self.symbols_table[self.currentClass]["variables"]:
                        final_right = f'GP[{self.symbols_table[self.currentClass]["variables"][rightOperand.token]["offset"]}]'
                    else:
                        final_right = rightOperand.token
                else:
                    final_right = rightOperand

                res = self.temporals.set_double_temporal(self.currentClass, f'$t{str(self.temps)}', f'${leftOperand.token}', f'${rightOperand.token}')
                self.intermediateCode += "    add" + res

                # self.intermediateCode += f'    GP[{used_offset}]={final_left}+{final_right}\n'
            else:
                self.intermediateCode += f'    GP[{used_offset}]={leftOperand}+{rightOperand}\n'
        
        node = SumNode(leftOperand, rightOperand, "t"+str(+self.temps))
        return node
    
    def visitLET_PASS(self, ctx:GrammarParser.LET_PASSContext):
        formalAssign = [self.visit(ctx.formalAssign(0))]
        for i in range(1, len(ctx.formalAssign())):
            formalAssignVisited = self.visit(ctx.formalAssign(i))
            formalAssign.append(formalAssignVisited)
        expr = self.visit(ctx.expr())

        node = LetPassNode(formalAssign, expr)
        return node
    
    def visitASSIGN_VAL(self, ctx:GrammarParser.ASSIGN_VALContext):
        id = ctx.ID().getText()
        exp = self.visit(ctx.expr())
        node = AssignNode(id, exp)
        if (hasattr(exp, "temp")):
            self.intermediateCode += f'    sw $t{str(self.temps)}, {id}\n'
            self.temporals.free_temporal(self.currentClass, self.temps)
        else:
            if self.currentClass and self.currentMethod:
                parent = ctx.parentCtx.getText()
                if id in self.symbols_table[self.currentClass]["methods"][self.currentMethod]["params"]:
                    gp = self.symbols_table[self.currentClass]["methods"][self.currentMethod]["params"][id]["offset"]
                elif "variables" in self.symbols_table[self.currentClass] and id in self.symbols_table[self.currentClass]["variables"]:
                    # get_class = validate_new_class("new", ctx.expr().getText())
                    gp = self.symbols_table[self.currentClass]["variables"][id]["offset"]
                    if (gp == -1 and self.newClass != ''):
                        gp = self.symbols_table[self.newClass]["offset"]
                        self.newClass = ''
                else:
                    # REVISAMOS LET
                    let_id = f'let-{id}'
                    if let_id in self.symbols_table[self.currentClass]["methods"][self.currentMethod]["params"]:
                        gp = self.symbols_table[self.currentClass]["methods"][self.currentMethod]["params"][let_id]["offset"]
                    
                    if (gp == None):
                        # Revisamos metodo heredado
                        superclass = self.symbols_table[self.currentClass]["superclass"]
                        print(id, self.currentMethod, superclass)

                        if (superclass != None):
                            if id in self.symbols_table[superclass]["methods"][self.currentMethod]["params"]:
                                gp = self.symbols_table[superclass]["methods"][self.currentMethod]["params"][id]["offset"]
                            elif "variables" in self.symbols_table[superclass] and id in self.symbols_table[superclass]["variables"]:
                                # get_class = validate_new_class("new", ctx.expr().getText())
                                gp = self.symbols_table[superclass]["variables"][id]["offset"]
                                if (gp == -1 and self.newClass != ''):
                                    gp = self.symbols_table[self.newClass]["offset"]
                                    self.newClass = ''

                self.intermediateCode += f'    GP[{gp}]={ctx.expr().getText()}\n'
            else:

                self.intermediateCode += f'    {id}={ctx.expr().getText()}\n'
        return node

    def visitMINUS(self, ctx:GrammarParser.MINUSContext):
        #print("visitMINUS")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        self.temps = self.temporals.get_correct_id(self.currentClass)
        node = MinusNode(leftOperand, rightOperand, "t" + str(self.temps))

        res = self.temporals.set_double_temporal(self.currentClass, f'$t{str(self.temps)}', f'${leftOperand}', f'${rightOperand}')
        self.intermediateCode += "    sub" + res

        return node

    def visitDIVIDE(self, ctx:GrammarParser.DIVIDEContext):
        #print("visitDIVIDE")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        self.temps = self.temporals.get_correct_id(self.currentClass)
        node = DivNode(leftOperand, rightOperand, "t" + str(self.temps))

        res = self.temporals.set_double_temporal(self.currentClass, f'$t{str(self.temps)}', f'${leftOperand}', f'${rightOperand}')
        self.intermediateCode += "    div" + res

        return node
    
    def visitBIGGER(self, ctx:GrammarParser.BIGGERContext):
        #print("visitBIGGER")
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        self.temps = self.temporals.get_correct_id(self.currentClass)
        node = BiggerNode(leftOperand, rightOperand, "t" + str(self.temps))

        res = self.temporals.set_temporal(self.currentClass, f't{str(self.temps)}', f'{leftOperand}>{rightOperand}')
        self.intermediateCode += res

        return node

    def visitNOT(self, ctx:GrammarParser.NOTContext):
        #print("visitNOT")
        expr = self.visit(ctx.expr())
        node = NotNode(expr)
        self.intermediateCode += f'    not {expr}\n'
        return node

    def visitNEWOBJ(self, ctx:GrammarParser.NEWOBJContext):
        self.newClass = ctx.TYPE().getText()
        return ObjNode(ctx.TYPE().getText())

    def visitIF_CLAUSE(self, ctx:GrammarParser.IF_CLAUSEContext):
        #print("visitIF_CLAUSE")
        condition = self.visit(ctx.expr(0))
        # self.temps = self.temporals.get_correct_id(self.currentClass)
        self.labelTemps += 1

        firstlabel = "label" + str(self.labelTemps)
        self.labelTemps += 1
        secondlabel = "label" + str(self.labelTemps)

        # self.intermediateCode += f'    t{str(self.temps)}={condition}\n'
        self.intermediateCode += f'    if t{str(self.temps)} goto {firstlabel}\n'
        self.intermediateCode += f'    else goto {secondlabel} endif\n'


        self.intermediateCode += f'    {firstlabel}_init\n'
        doIf = self.visit(ctx.expr(1))
        self.intermediateCode += f'    {firstlabel}_finish\n'
        self.intermediateCode += f'    {secondlabel}_init\n'
        doElse = self.visit(ctx.expr(2))
        self.intermediateCode += f'    {secondlabel}_finish\n'
        node = IfNode(condition, doIf, doElse)
        return node
    
    def visitSTRING(self, ctx:GrammarParser.STRINGContext):
        self.strings.append(ctx.STRING().getText())
        return f'string{len(self.strings) - 1}'

    def visitTILDE(self, ctx:GrammarParser.TILDEContext):
        #print("visitTILDE")
        expr = self.visit(ctx.expr())
        self.intermediateCode += f'    ~ {expr}\n'
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
        self.temps = self.temporals.get_correct_id(self.currentClass)
        node = BiggerEqualsNode(leftOperand, rightOperand,  "t" + str(self.temps))
        self.intermediateCode += f'    t{str(self.temps)}={leftOperand}>={rightOperand}\n'
        return node
    
    def visitINTEGER(self, ctx:GrammarParser.INTEGERContext):
        #print("visitINTEGER")
        return IntNode(ctx.INTEGER().getText())
    