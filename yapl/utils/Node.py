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

class TypeNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = "type"

class StringNode(Node):
    def __init__(self, token):
        self.token = token
        self.type = "string"

class SumNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.type = "sum"

class AssignNode(Node):
    def __init__(self, token, expr):
        self.token = token
        self.expr = expr
        self.type = "assign"

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