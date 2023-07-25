# Generated from Hello.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete listener for a parse tree produced by HelloParser.
class HelloListener(ParseTreeListener):

    # Enter a parse tree produced by HelloParser#program.
    def enterProgram(self, ctx:HelloParser.ProgramContext):
        pass

    # Exit a parse tree produced by HelloParser#program.
    def exitProgram(self, ctx:HelloParser.ProgramContext):
        pass


    # Enter a parse tree produced by HelloParser#class.
    def enterClass(self, ctx:HelloParser.ClassContext):
        pass

    # Exit a parse tree produced by HelloParser#class.
    def exitClass(self, ctx:HelloParser.ClassContext):
        pass


    # Enter a parse tree produced by HelloParser#feature.
    def enterFeature(self, ctx:HelloParser.FeatureContext):
        pass

    # Exit a parse tree produced by HelloParser#feature.
    def exitFeature(self, ctx:HelloParser.FeatureContext):
        pass


    # Enter a parse tree produced by HelloParser#formal.
    def enterFormal(self, ctx:HelloParser.FormalContext):
        pass

    # Exit a parse tree produced by HelloParser#formal.
    def exitFormal(self, ctx:HelloParser.FormalContext):
        pass


    # Enter a parse tree produced by HelloParser#expr.
    def enterExpr(self, ctx:HelloParser.ExprContext):
        pass

    # Exit a parse tree produced by HelloParser#expr.
    def exitExpr(self, ctx:HelloParser.ExprContext):
        pass


    # Enter a parse tree produced by HelloParser#r.
    def enterR(self, ctx:HelloParser.RContext):
        pass

    # Exit a parse tree produced by HelloParser#r.
    def exitR(self, ctx:HelloParser.RContext):
        pass



del HelloParser