# Generated from Hello.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete generic visitor for a parse tree produced by HelloParser.

class HelloVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HelloParser#program.
    def visitProgram(self, ctx:HelloParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#class.
    def visitClass(self, ctx:HelloParser.ClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#feature.
    def visitFeature(self, ctx:HelloParser.FeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#formal.
    def visitFormal(self, ctx:HelloParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#expr.
    def visitExpr(self, ctx:HelloParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#r.
    def visitR(self, ctx:HelloParser.RContext):
        return self.visitChildren(ctx)



del HelloParser