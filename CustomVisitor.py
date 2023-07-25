from yapl.grammar.HelloVisitor import HelloVisitor
from yapl.utils.Node import *

class CustomVisitor(HelloVisitor):
    def __init__(self):
        self.errores = []
    def visitInteger(self, ctx:HelloVisitor.IntegerContext):
        return IntNode(ctx.INT_VAR().getText())
