
from generated.GrammarVisitor import GrammarVisitor
from generated.GrammarParser import GrammarParser
from generated.GrammarVisitor import GrammarVisitor

from utils.Node import *
from utils.SymbolsTable import SymbolsTable
from utils.ErrorTable import ErrorTable
from utils.Validations import *

TYPES = {
    'Int': int,
    'String': str,
    'Bool': bool,
}

class SemanticVisitor(GrammarVisitor):
    def __init__(self):
        self.grammar = GrammarVisitor()
        self.errors = []
        self.symbols_table = SymbolsTable()
        self.errors_table = ErrorTable()
        self.formal_params = {}
        self.bool_list = ['true', 'false']
        self.current_scope = None
    def getSymbolsTable(self):
        return self.symbols_table.getTable()
    def getErrorsTable(self):
        return self.errors_table.getErrors()

    def visitR(self, ctx:GrammarParser.RContext):
        return self.visit(ctx.program())

    def visitProgram(self, ctx:GrammarParser.ProgramContext):
        classS = []
        for c in ctx.classDef():
            visitedClass = self.visit(c)
            classS.append(visitedClass)
        node = ProgramNode(classS)
        return node
    
    def visitCLASS_DEFINITION(self, ctx:GrammarParser.CLASS_DEFINITIONContext):
        name = ctx.TYPE(0).getText()
        inherits = None
        features = []
        for f in ctx.feature():
            featureVisited = self.visit(f)
            features.append(featureVisited)
        if len(ctx.TYPE()) > 1:
            inherits = ctx.TYPE(1).getText()
        node = ClassNode(name, inherits, features)
        self.symbols_table.addInherits(name, inherits)
        if name == 'Main' and inherits != 'IO':
            self.errors_table.addMainShouldInheritIOError(f'{ctx.start.line}:{ctx.start.column}')
        return node

    def visitDEFINITION_METHOD_PARAMS(self, ctx:GrammarParser.DEFINITION_METHOD_PARAMSContext):
        name = ctx.ID().getText()
        params = []
        for param in range(len(ctx.formal())):
            formal = ctx.formal(param)
            visitedFormal = self.visit(formal)
            params.append(visitedFormal)
        expr = self.visit(ctx.expr())
        typE = ctx.TYPE().getText()
        node = MethodNode(name, typE, params, expr)

        # Add method to table
        parent = ctx.parentCtx.TYPE(0).getText()
        self.current_scope = parent
        self.symbols_table.addMethod(parent, name, typE, self.formal_params)
        self.formal_params = {}
        table = self.symbols_table.getTable()
        return node
    
    def visitDEFINITION_PARAMS(self, ctx:GrammarParser.DEFINITION_PARAMSContext):
        # Add scope to table
        parent = ctx.parentCtx.TYPE(0).getText()
        self.current_scope = parent
        self.symbols_table.addScope(parent)

        typE = ctx.TYPE().getText()
        id = ctx.ID().getText()
        expr = ctx.expr()


        if expr is None:
            node = DefParamsNode(id, typE, None)
            self.symbols_table.addVariable(parent, id, typE, None)
            return node
        expr = self.visit(ctx.expr())
        node = DefParamsNode(id, typE, expr)
        exp_value = ctx.expr().getText()

        if typE not in TYPES:
            self.errors_table.addVariableTypeError(f'{ctx.start.line}:{ctx.start.column}', typE)
        else:
            realType = TYPES[typE].__name__
            if realType == 'str':
                if not exp_value.startswith('"') or not exp_value.endswith('"'):
                    if exp_value.count('"') != 2 and exp_value.count('"') != 0:
                        self.errors_table.addStringQuotesError(f'{ctx.start.line}:{ctx.start.column}')
                    else:
                        if exp_value.lower() not in self.bool_list:
                            try:
                                int(exp_value)
                                self.errors_table.addVariableDeclarationTypeError(f'{ctx.start.line}:{ctx.start.column}', id, typE, 'Int')
                            except:
                                self.errors_table.addVariableDeclarationTypeError(f'{ctx.start.line}:{ctx.start.column}', id, typE, 'Unknown')
                        else:
                            self.errors_table.addVariableDeclarationTypeError(f'{ctx.start.line}:{ctx.start.column}', id, typE, 'Bool')
            elif realType == 'int':
                try:
                    int(exp_value)
                except:
                    if exp_value in self.bool_list:
                        self.errors_table.addVariableDeclarationTypeError(f'{ctx.start.line}:{ctx.start.column}', id, typE, 'Bool')
                    elif exp_value.startswith('"') and exp_value.endswith('"'):
                        self.errors_table.addVariableDeclarationTypeError(f'{ctx.start.line}:{ctx.start.column}', id, typE, 'String')
                    else:
                        self.errors_table.addVariableDeclarationTypeError(f'{ctx.start.line}:{ctx.start.column}', id, typE, 'Unknown')

        # Add variable to table
        if 'variables' in self.symbols_table.getTable()[self.current_scope] and id in self.symbols_table.getTable()[self.current_scope]['variables']:
            self.errors_table.addVarAlreadyExistsError(f'{ctx.start.line}:{ctx.start.column}', id)
        else:
            self.symbols_table.addVariable(parent, id, typE, exp_value)
        return node
    
    def visitFormal(self, ctx:GrammarParser.FormalContext):
        id = ctx.ID().getText()
        typE = ctx.TYPE().getText()
        node = FormalNode(id, typE)

        # Add variable to formals
        self.formal_params[id] = typE
        return node

    def visitFormalAssign(self, ctx:GrammarParser.FormalAssignContext):
        typE = ctx.TYPE().getText()
        id = ctx.ID().getText()
        if ctx.expr() is None:
            node = FormalAssignNode(id, typE, None)
            return node
        expr = self.visit(ctx.expr())
        node = FormalAssignNode(id, typE, expr)
        return node
    
    def visitCALL(self, ctx:GrammarParser.CALLContext):
        name = ctx.ID().getText()
        expressions = []
        for param in range(len(ctx.expr())):
            expr = ctx.expr(param)
            visitedExp = self.visit(expr)
            expressions.append(visitedExp)
        node = CallNode(name, expressions)
        return node
    
    def visitEXPR_PARAMS(self, ctx:GrammarParser.EXPR_PARAMSContext):
        return self.visitChildren(ctx.expr())
  
    def visitTIMES(self, ctx:GrammarParser.TIMESContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = TimesNode(leftOperand, rightOperand)
        return node
    
    def visitEQUALS(self, ctx:GrammarParser.EQUALSContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = EqualsNode(leftOperand, rightOperand)
        return node

    def visitVOID_EXPR(self, ctx:GrammarParser.VOID_EXPRContext):
        expr = self.visit(ctx.expr())
        node = VoidNode(expr)
        return node

    def visitDISPATCH(self, ctx:GrammarParser.DISPATCHContext):
        exprInitial = self.visit(ctx.expr(0))
        method = ctx.ID().getText()
        exprArguments = []

        for i in range(1, len(ctx.expr())):
            arg = self.visit(ctx.expr(i))
            exprArguments.append(arg)
        node = DispatchNode(exprInitial, method, exprArguments)
        return node
    
    def visitBLOCK(self, ctx:GrammarParser.BLOCKContext):
        expr = []
        for e in ctx.expr():
            expr.append(self.visit(e))
        node = BlockNode(expr)
        return node
    
    def visitTRUE(self, ctx:GrammarParser.TRUEContext):
        return BooleanNode(ctx.TRUE().getText())

    def visitWHILE_CLAUSE(self, ctx:GrammarParser.WHILE_CLAUSEContext):
        condition = self.visit(ctx.expr(0))
        expr = self.visit(ctx.expr(1))
        node = WhileNode(condition, expr)
        return node

    def visitSUM(self, ctx:GrammarParser.SUMContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))

        leftOperantToken = leftOperand.token
        rightOperantToken = rightOperand.token
        valid, message = validateSum(leftOperantToken, rightOperantToken, self.symbols_table.getTable(), self.current_scope, self.formal_params)
        if not valid:
            self.errors_table.addCustomError(f'{ctx.start.line}:{ctx.start.column}', message)

        node = SumNode(leftOperand, rightOperand)
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
        if hasattr(exp, 'type'):
            if exp.type in ['sum', 'minus', 'times']:
                pass
            else:
                if hasattr(exp, 'token'):
                    exp_value = exp.token if exp is not None else ''
                    valid, message = validateAssignVal(self.current_scope, self.formal_params, self.symbols_table.getTable(), id, exp_value)
                    if not valid:
                        self.errors_table.addCustomError(f'{ctx.start.line}:{ctx.start.column}', message)
        return node

    def visitMINUS(self, ctx:GrammarParser.MINUSContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = MinusNode(leftOperand, rightOperand)
        return node

    def visitDIVIDE(self, ctx:GrammarParser.DIVIDEContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = DivNode(leftOperand, rightOperand)
        return node
    
    def visitBIGGER(self, ctx:GrammarParser.BIGGERContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = BiggerNode(leftOperand, rightOperand)
        return node
    
    def visitNOT(self, ctx:GrammarParser.NOTContext):
        expr = self.visit(ctx.expr())
        node = NotNode(expr)
        return node

    def visitNEWOBJ(self, ctx:GrammarParser.NEWOBJContext):
        return ObjNode(ctx.TYPE().getText())

    def visitIF_CLAUSE(self, ctx:GrammarParser.IF_CLAUSEContext):
        condition = self.visit(ctx.expr(0))
        doIf = self.visit(ctx.expr(1))
        doElse = self.visit(ctx.expr(2))
        node = IfNode(condition, doIf, doElse)
        if condition.type == 'id':
            token = condition.token
            valid, message = validateIfClause(self.current_scope, self.formal_params, self.symbols_table.getTable(), token, recursion_depth=0)
            if not valid:
                self.errors_table.addCustomError(f'{ctx.start.line}:{ctx.start.column}', message)
        else:
            if hasattr(condition, 'token'):
                valid, result = validateValueType(condition.token)
                if not valid:
                    self.errors_table.addCustomError(f'{ctx.start.line}:{ctx.start.column}', result)
                else:
                    if result != 'Bool':
                        if result == 'Int':
                            if int(condition.token) == 0 or int(condition.token) == 1:
                                pass
                            else:
                                self.errors_table.addCustomError(f'{ctx.start.line}:{ctx.start.column}', f'If clause condition must be of type Bool, got { result } instead.')
                        else:
                            self.errors_table.addCustomError(f'{ctx.start.line}:{ctx.start.column}', f'If clause condition must be of type Bool, got { result } instead.')
        return node
    
    def visitSTRING(self, ctx:GrammarParser.STRINGContext):
        return StringNode(ctx.STRING().getText())

    def visitTILDE(self, ctx:GrammarParser.TILDEContext):
        expr = self.visit(ctx.expr())
        return TildeNode(expr)

    def visitFALSE(self, ctx:GrammarParser.FALSEContext):
        return BooleanNode(ctx.FALSE().getText())

    def visitID(self, ctx:GrammarParser.IDContext):
        return IdNode(ctx.ID().getText())

    def visitBIGGEREQUALS(self, ctx:GrammarParser.BIGGEREQUALSContext):
        leftOperand = self.visit(ctx.expr(0))
        rightOperand = self.visit(ctx.expr(1))
        node = BiggerEqualsNode(leftOperand, rightOperand)
        return node
    
    def visitINTEGER(self, ctx:GrammarParser.INTEGERContext):
        return IntNode(ctx.INTEGER().getText())
    
