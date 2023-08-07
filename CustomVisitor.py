from yapl.grammar.HelloVisitor import HelloVisitor
from yapl.utils.Node import *

class CustomVisitor(HelloVisitor):
    def __init__(self):
        self.errores = []
    
    def visitInteger(self, ctx:HelloVisitor.IntegerContext):
        return IntNode(ctx.INT_VAR().getText())
    
    def visitBoolean(self, ctx:HelloVisitor.BooleanContext):
        return BooleanNode(ctx.BOOLEAN_VAR().getText())
    
    def visitSum(self, ctx:HelloVisitor.SumContext):
        return
    
    def visitMinus(self, ctx:HelloVisitor.MinusContext):
        return
    
    def visitMultiply(self, ctx:HelloVisitor.MultiplyContext):
        return
    
    def visitDivide(self, ctx:HelloVisitor.DivideContext):
        return
    
    def visitGreaterThan(self, ctx:HelloVisitor.GreaterThanContext):
        return
    
    def visitGreaterThanOrEqual(self, ctx:HelloVisitor.GreaterThanOrEqualContext):
        return
    
    def visitLessThan(self, ctx:HelloVisitor.LessThanContext):
        return
    
    def visitLessThanOrEqual(self, ctx:HelloVisitor.LessThanOrEqualContext):
        return
    
    def visitEqual(self, ctx:HelloVisitor.EqualContext):
        return
    
    def visitNot(self, ctx:HelloVisitor.NotContext):
        return
    
