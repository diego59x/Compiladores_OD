class Node():
    def __init__(self, token):
        self.token = token
        self.type = "none"
    def __str__(self):
        return self.token

class IntNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = "integer"

class BooleanNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = "boolean"

class DispatchNode(Node):
    def __init__(self, exprInitial, method, exprArguments):
        self.exprInitial = exprInitial
        self.method = method
        self.exprArguments = exprArguments
        self.type = "dispatch"

class DefParamsNode(Node):
    def __init__(self, token, type, expr):
        self.token = token
        self.type = type
        self.expr = expr    
class StringNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = "string"
class BlockNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = "block"

class ClassNode(Node):
    def __init__(self, token, inherits, features):
        self.token = token
        self.inherits = inherits
        self.features = features
        self.type = "class"

class FormalNode(Node):
    def __init__(self, token, type):
        self.token = token
        self.type = type
        self.type = "formal"

class SumNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.type = "sum"
        self.token = left.token + "+" + right.token

class MinusNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.type = "minus"
        self.token = left.token + "-" + right.token

class DivNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.type = "divide"
        self.token = "/"
        self.token = left.token + "/" + right.token

class TimesNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.type = "times"
        self.token = left.token + "*" + right.token

class EqualsNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.type = "equals"
        self.token = left.token + "=" + right.token

class BiggerNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.token = left.token + ">" + right.token
        self.type = "bigger"

class BiggerEqualsNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.token = left.token + ">=" + right.token
        self.type = "biggerEquals"

class IfNode(Node):
    def __init__(self, condition, doIf, doElse):
        self.condition = condition
        self.doIf = doIf
        self.doElse = doElse
        self.type = "if"

class WhileNode(Node):
    def __init__(self, condition, expr):
        self.condition = condition
        self.expr = expr
        self.type = "while"
class VoidNode(Node):
    def __init__(self, expr):
        self.expr = expr
        self.type = "void"

class TildeNode(Node):
    def __init__(self, expr):
        self.expr = expr
        self.type = "intNegation"

class NotNode(Node):
    def __init__(self, expr):
        self.expr = expr
        self.type = "not"

class AssignNode(Node):
    def __init__(self, token, expr):
        self.token = token
        self.expr = expr
        self.type = "assign"

class MethodNode(Node):
    def __init__(self, name, typE, params, expr):
        self.token = name
        self.typE = typE
        self.params = params
        self.expr = expr
        self.type = "method"

class CallNode(Node):
    def __init__(self, token, expr):
        self.token = token
        self.expr = expr
        self.type = "call"

class ObjNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = "object"

class ProgramNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = "program"

class FormalAssignNode(Node):
    def __init__(self, token, type, expr):
        self.token = token
        self.type = type
        self.expr = expr
        self.type = "formalAssign"    

class LetPassNode(Node):
    def __init__(self, formalAssign, expr):
        self.formalAssign = formalAssign
        self.expr = expr
        self.type = "letPass"

class IdNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = "id"

class ErrorNode(Node):
    def __init__(self, token):
        self.token = token
        self.error_list = []

class ArithmeticNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.type = "arithmetic"

class LogicalNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.type = "logical"