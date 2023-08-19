# Generated from ./Hello.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,203,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,1,1,1,1,1,4,1,18,8,1,11,1,12,1,19,1,2,1,2,1,2,1,2,3,2,26,8,2,
        1,2,1,2,1,2,1,2,5,2,32,8,2,10,2,12,2,35,9,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,5,3,44,8,3,10,3,12,3,47,9,3,3,3,49,8,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,63,8,3,3,3,65,8,3,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,77,8,5,10,5,12,5,80,9,5,3,5,82,8,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,4,5,103,8,5,11,5,12,5,104,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,115,8,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,123,8,5,5,5,125,
        8,5,10,5,12,5,128,9,5,1,5,1,5,1,5,1,5,4,5,134,8,5,11,5,12,5,135,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,3,5,159,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,5,5,191,8,5,10,5,12,5,194,9,5,3,5,196,8,
        5,5,5,198,8,5,10,5,12,5,201,9,5,1,5,0,1,10,6,0,2,4,6,8,10,0,0,235,
        0,12,1,0,0,0,2,17,1,0,0,0,4,21,1,0,0,0,6,64,1,0,0,0,8,66,1,0,0,0,
        10,158,1,0,0,0,12,13,3,2,1,0,13,1,1,0,0,0,14,15,3,4,2,0,15,16,5,
        28,0,0,16,18,1,0,0,0,17,14,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,
        20,1,0,0,0,20,3,1,0,0,0,21,22,5,1,0,0,22,25,5,38,0,0,23,24,5,2,0,
        0,24,26,5,38,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,33,
        5,26,0,0,28,29,3,6,3,0,29,30,5,28,0,0,30,32,1,0,0,0,31,28,1,0,0,
        0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,36,1,0,0,0,35,33,
        1,0,0,0,36,37,5,27,0,0,37,5,1,0,0,0,38,39,5,37,0,0,39,48,5,24,0,
        0,40,45,3,8,4,0,41,42,5,34,0,0,42,44,3,8,4,0,43,41,1,0,0,0,44,47,
        1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,
        48,40,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,50,51,5,25,0,0,51,52,5,
        33,0,0,52,53,5,38,0,0,53,54,5,26,0,0,54,55,3,10,5,0,55,56,5,27,0,
        0,56,65,1,0,0,0,57,58,5,37,0,0,58,59,5,33,0,0,59,62,5,38,0,0,60,
        61,5,31,0,0,61,63,3,10,5,0,62,60,1,0,0,0,62,63,1,0,0,0,63,65,1,0,
        0,0,64,38,1,0,0,0,64,57,1,0,0,0,65,7,1,0,0,0,66,67,5,37,0,0,67,68,
        5,33,0,0,68,69,5,38,0,0,69,9,1,0,0,0,70,71,6,5,-1,0,71,72,5,37,0,
        0,72,81,5,24,0,0,73,78,3,10,5,0,74,75,5,34,0,0,75,77,3,10,5,0,76,
        74,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,82,1,0,0,
        0,80,78,1,0,0,0,81,73,1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,159,
        5,25,0,0,84,85,5,5,0,0,85,86,3,10,5,0,86,87,5,13,0,0,87,88,3,10,
        5,0,88,89,5,7,0,0,89,90,3,10,5,0,90,91,5,6,0,0,91,159,1,0,0,0,92,
        93,5,8,0,0,93,94,3,10,5,0,94,95,5,9,0,0,95,96,3,10,5,0,96,97,5,10,
        0,0,97,159,1,0,0,0,98,102,5,26,0,0,99,100,3,10,5,0,100,101,5,28,
        0,0,101,103,1,0,0,0,102,99,1,0,0,0,103,104,1,0,0,0,104,102,1,0,0,
        0,104,105,1,0,0,0,105,106,1,0,0,0,106,107,5,27,0,0,107,159,1,0,0,
        0,108,109,5,11,0,0,109,110,5,37,0,0,110,111,5,33,0,0,111,114,5,38,
        0,0,112,113,5,31,0,0,113,115,3,10,5,0,114,112,1,0,0,0,114,115,1,
        0,0,0,115,126,1,0,0,0,116,117,5,34,0,0,117,118,5,37,0,0,118,119,
        5,33,0,0,119,122,5,38,0,0,120,121,5,31,0,0,121,123,3,10,5,0,122,
        120,1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,116,1,0,0,0,125,
        128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,129,1,0,0,0,128,
        126,1,0,0,0,129,130,5,12,0,0,130,159,3,10,5,19,131,132,5,14,0,0,
        132,134,5,38,0,0,133,131,1,0,0,0,134,135,1,0,0,0,135,133,1,0,0,0,
        135,136,1,0,0,0,136,159,1,0,0,0,137,138,5,15,0,0,138,159,3,10,5,
        17,139,140,5,32,0,0,140,159,3,10,5,12,141,142,5,16,0,0,142,143,5,
        24,0,0,143,144,3,10,5,0,144,145,5,25,0,0,145,159,1,0,0,0,146,147,
        5,24,0,0,147,148,3,10,5,0,148,149,5,25,0,0,149,159,1,0,0,0,150,159,
        5,37,0,0,151,159,5,4,0,0,152,159,5,3,0,0,153,159,5,22,0,0,154,159,
        5,23,0,0,155,156,5,37,0,0,156,157,5,31,0,0,157,159,3,10,5,1,158,
        70,1,0,0,0,158,84,1,0,0,0,158,92,1,0,0,0,158,98,1,0,0,0,158,108,
        1,0,0,0,158,133,1,0,0,0,158,137,1,0,0,0,158,139,1,0,0,0,158,141,
        1,0,0,0,158,146,1,0,0,0,158,150,1,0,0,0,158,151,1,0,0,0,158,152,
        1,0,0,0,158,153,1,0,0,0,158,154,1,0,0,0,158,155,1,0,0,0,159,199,
        1,0,0,0,160,161,10,16,0,0,161,162,5,29,0,0,162,198,3,10,5,17,163,
        164,10,15,0,0,164,165,5,30,0,0,165,198,3,10,5,16,166,167,10,14,0,
        0,167,168,5,21,0,0,168,198,3,10,5,15,169,170,10,13,0,0,170,171,5,
        20,0,0,171,198,3,10,5,14,172,173,10,11,0,0,173,174,5,18,0,0,174,
        198,3,10,5,12,175,176,10,10,0,0,176,177,5,19,0,0,177,198,3,10,5,
        11,178,179,10,9,0,0,179,180,5,17,0,0,180,198,3,10,5,10,181,182,10,
        24,0,0,182,183,5,36,0,0,183,184,5,38,0,0,184,185,1,0,0,0,185,186,
        5,35,0,0,186,195,5,37,0,0,187,192,3,10,5,0,188,189,5,34,0,0,189,
        191,3,10,5,0,190,188,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,
        193,1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,0,195,187,1,0,0,0,195,
        196,1,0,0,0,196,198,1,0,0,0,197,160,1,0,0,0,197,163,1,0,0,0,197,
        166,1,0,0,0,197,169,1,0,0,0,197,172,1,0,0,0,197,175,1,0,0,0,197,
        178,1,0,0,0,197,181,1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,
        200,1,0,0,0,200,11,1,0,0,0,201,199,1,0,0,0,19,19,25,33,45,48,62,
        64,78,81,104,114,122,126,135,158,192,195,197,199
    ]

class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "'<'", "'<='", "'/'", "'*'", "'true'", 
                     "'false'", "'('", "')'", "'{'", "'}'", "';'", "'+'", 
                     "'-'", "'<-'", "'~'", "':'", "','", "'.'", "'@'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "INHERITS", "STRING", "INTEGER", 
                      "IF", "FI", "ELSE", "WHILE", "LOOP", "POOL", "LET", 
                      "IN", "THEN", "NEW", "ISVOID", "NOT", "EQUALS", "BIGGER", 
                      "BIGGEREQUALS", "DIVIDE", "TIMES", "TRUE", "FALSE", 
                      "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "SEMICOLON", 
                      "PLUS", "MINUS", "ASSIGN", "TILDE", "COLON", "COMMA", 
                      "DOT", "AT", "ID", "TYPE", "WS" ]

    RULE_r = 0
    RULE_program = 1
    RULE_class = 2
    RULE_feature = 3
    RULE_formal = 4
    RULE_expr = 5

    ruleNames =  [ "r", "program", "class", "feature", "formal", "expr" ]

    EOF = Token.EOF
    CLASS=1
    INHERITS=2
    STRING=3
    INTEGER=4
    IF=5
    FI=6
    ELSE=7
    WHILE=8
    LOOP=9
    POOL=10
    LET=11
    IN=12
    THEN=13
    NEW=14
    ISVOID=15
    NOT=16
    EQUALS=17
    BIGGER=18
    BIGGEREQUALS=19
    DIVIDE=20
    TIMES=21
    TRUE=22
    FALSE=23
    LPAREN=24
    RPAREN=25
    LBRACKET=26
    RBRACKET=27
    SEMICOLON=28
    PLUS=29
    MINUS=30
    ASSIGN=31
    TILDE=32
    COLON=33
    COMMA=34
    DOT=35
    AT=36
    ID=37
    TYPE=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(HelloParser.ProgramContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR" ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR" ):
                listener.exitR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR" ):
                return visitor.visitR(self)
            else:
                return visitor.visitChildren(self)




    def r(self):

        localctx = HelloParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.program()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ClassContext)
            else:
                return self.getTypedRuleContext(HelloParser.ClassContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.SEMICOLON)
            else:
                return self.getToken(HelloParser.SEMICOLON, i)

        def getRuleIndex(self):
            return HelloParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = HelloParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.class_()
                self.state = 15
                self.match(HelloParser.SEMICOLON)
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(HelloParser.CLASS, 0)

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.TYPE)
            else:
                return self.getToken(HelloParser.TYPE, i)

        def LBRACKET(self):
            return self.getToken(HelloParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(HelloParser.RBRACKET, 0)

        def INHERITS(self):
            return self.getToken(HelloParser.INHERITS, 0)

        def feature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.FeatureContext)
            else:
                return self.getTypedRuleContext(HelloParser.FeatureContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.SEMICOLON)
            else:
                return self.getToken(HelloParser.SEMICOLON, i)

        def getRuleIndex(self):
            return HelloParser.RULE_class

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass" ):
                listener.enterClass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass" ):
                listener.exitClass(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass" ):
                return visitor.visitClass(self)
            else:
                return visitor.visitChildren(self)




    def class_(self):

        localctx = HelloParser.ClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(HelloParser.CLASS)
            self.state = 22
            self.match(HelloParser.TYPE)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 23
                self.match(HelloParser.INHERITS)
                self.state = 24
                self.match(HelloParser.TYPE)


            self.state = 27
            self.match(HelloParser.LBRACKET)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 28
                self.feature()
                self.state = 29
                self.match(HelloParser.SEMICOLON)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(HelloParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HelloParser.RULE_feature

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DEFINITION_METHOD_PARAMSContext(FeatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.FeatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(HelloParser.ID, 0)
        def LPAREN(self):
            return self.getToken(HelloParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(HelloParser.RPAREN, 0)
        def COLON(self):
            return self.getToken(HelloParser.COLON, 0)
        def TYPE(self):
            return self.getToken(HelloParser.TYPE, 0)
        def LBRACKET(self):
            return self.getToken(HelloParser.LBRACKET, 0)
        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)

        def RBRACKET(self):
            return self.getToken(HelloParser.RBRACKET, 0)
        def formal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.FormalContext)
            else:
                return self.getTypedRuleContext(HelloParser.FormalContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.COMMA)
            else:
                return self.getToken(HelloParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDEFINITION_METHOD_PARAMS" ):
                listener.enterDEFINITION_METHOD_PARAMS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDEFINITION_METHOD_PARAMS" ):
                listener.exitDEFINITION_METHOD_PARAMS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDEFINITION_METHOD_PARAMS" ):
                return visitor.visitDEFINITION_METHOD_PARAMS(self)
            else:
                return visitor.visitChildren(self)


    class DEFINITION_PARAMSContext(FeatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.FeatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(HelloParser.ID, 0)
        def COLON(self):
            return self.getToken(HelloParser.COLON, 0)
        def TYPE(self):
            return self.getToken(HelloParser.TYPE, 0)
        def ASSIGN(self):
            return self.getToken(HelloParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDEFINITION_PARAMS" ):
                listener.enterDEFINITION_PARAMS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDEFINITION_PARAMS" ):
                listener.exitDEFINITION_PARAMS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDEFINITION_PARAMS" ):
                return visitor.visitDEFINITION_PARAMS(self)
            else:
                return visitor.visitChildren(self)



    def feature(self):

        localctx = HelloParser.FeatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_feature)
        self._la = 0 # Token type
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = HelloParser.DEFINITION_METHOD_PARAMSContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(HelloParser.ID)
                self.state = 39
                self.match(HelloParser.LPAREN)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 40
                    self.formal()
                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==34:
                        self.state = 41
                        self.match(HelloParser.COMMA)
                        self.state = 42
                        self.formal()
                        self.state = 47
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 50
                self.match(HelloParser.RPAREN)
                self.state = 51
                self.match(HelloParser.COLON)
                self.state = 52
                self.match(HelloParser.TYPE)
                self.state = 53
                self.match(HelloParser.LBRACKET)
                self.state = 54
                self.expr(0)
                self.state = 55
                self.match(HelloParser.RBRACKET)
                pass

            elif la_ == 2:
                localctx = HelloParser.DEFINITION_PARAMSContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.match(HelloParser.ID)
                self.state = 58
                self.match(HelloParser.COLON)
                self.state = 59
                self.match(HelloParser.TYPE)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 60
                    self.match(HelloParser.ASSIGN)
                    self.state = 61
                    self.expr(0)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def COLON(self):
            return self.getToken(HelloParser.COLON, 0)

        def TYPE(self):
            return self.getToken(HelloParser.TYPE, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_formal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal" ):
                listener.enterFormal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal" ):
                listener.exitFormal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormal" ):
                return visitor.visitFormal(self)
            else:
                return visitor.visitChildren(self)




    def formal(self):

        localctx = HelloParser.FormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_formal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(HelloParser.ID)
            self.state = 67
            self.match(HelloParser.COLON)
            self.state = 68
            self.match(HelloParser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HelloParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CALLContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(HelloParser.ID, 0)
        def LPAREN(self):
            return self.getToken(HelloParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(HelloParser.RPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.COMMA)
            else:
                return self.getToken(HelloParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCALL" ):
                listener.enterCALL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCALL" ):
                listener.exitCALL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCALL" ):
                return visitor.visitCALL(self)
            else:
                return visitor.visitChildren(self)


    class EXPR_PARAMSContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(HelloParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(HelloParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEXPR_PARAMS" ):
                listener.enterEXPR_PARAMS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEXPR_PARAMS" ):
                listener.exitEXPR_PARAMS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEXPR_PARAMS" ):
                return visitor.visitEXPR_PARAMS(self)
            else:
                return visitor.visitChildren(self)


    class TIMESContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def TIMES(self):
            return self.getToken(HelloParser.TIMES, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTIMES" ):
                listener.enterTIMES(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTIMES" ):
                listener.exitTIMES(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTIMES" ):
                return visitor.visitTIMES(self)
            else:
                return visitor.visitChildren(self)


    class EQUALSContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def EQUALS(self):
            return self.getToken(HelloParser.EQUALS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEQUALS" ):
                listener.enterEQUALS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEQUALS" ):
                listener.exitEQUALS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEQUALS" ):
                return visitor.visitEQUALS(self)
            else:
                return visitor.visitChildren(self)


    class VOID_EXPRContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ISVOID(self):
            return self.getToken(HelloParser.ISVOID, 0)
        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVOID_EXPR" ):
                listener.enterVOID_EXPR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVOID_EXPR" ):
                listener.exitVOID_EXPR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVOID_EXPR" ):
                return visitor.visitVOID_EXPR(self)
            else:
                return visitor.visitChildren(self)


    class DISPATCHContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def DOT(self):
            return self.getToken(HelloParser.DOT, 0)
        def ID(self):
            return self.getToken(HelloParser.ID, 0)
        def AT(self):
            return self.getToken(HelloParser.AT, 0)
        def TYPE(self):
            return self.getToken(HelloParser.TYPE, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.COMMA)
            else:
                return self.getToken(HelloParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDISPATCH" ):
                listener.enterDISPATCH(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDISPATCH" ):
                listener.exitDISPATCH(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDISPATCH" ):
                return visitor.visitDISPATCH(self)
            else:
                return visitor.visitChildren(self)


    class BLOCKContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACKET(self):
            return self.getToken(HelloParser.LBRACKET, 0)
        def RBRACKET(self):
            return self.getToken(HelloParser.RBRACKET, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.SEMICOLON)
            else:
                return self.getToken(HelloParser.SEMICOLON, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBLOCK" ):
                listener.enterBLOCK(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBLOCK" ):
                listener.exitBLOCK(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBLOCK" ):
                return visitor.visitBLOCK(self)
            else:
                return visitor.visitChildren(self)


    class TRUEContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(HelloParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTRUE" ):
                listener.enterTRUE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTRUE" ):
                listener.exitTRUE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTRUE" ):
                return visitor.visitTRUE(self)
            else:
                return visitor.visitChildren(self)


    class WHILE_CLAUSEContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(HelloParser.WHILE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def LOOP(self):
            return self.getToken(HelloParser.LOOP, 0)
        def POOL(self):
            return self.getToken(HelloParser.POOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWHILE_CLAUSE" ):
                listener.enterWHILE_CLAUSE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWHILE_CLAUSE" ):
                listener.exitWHILE_CLAUSE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWHILE_CLAUSE" ):
                return visitor.visitWHILE_CLAUSE(self)
            else:
                return visitor.visitChildren(self)


    class SUMContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(HelloParser.PLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSUM" ):
                listener.enterSUM(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSUM" ):
                listener.exitSUM(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSUM" ):
                return visitor.visitSUM(self)
            else:
                return visitor.visitChildren(self)


    class LET_PASSContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(HelloParser.LET, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.ID)
            else:
                return self.getToken(HelloParser.ID, i)
        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.COLON)
            else:
                return self.getToken(HelloParser.COLON, i)
        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.TYPE)
            else:
                return self.getToken(HelloParser.TYPE, i)
        def IN(self):
            return self.getToken(HelloParser.IN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.ASSIGN)
            else:
                return self.getToken(HelloParser.ASSIGN, i)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.COMMA)
            else:
                return self.getToken(HelloParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLET_PASS" ):
                listener.enterLET_PASS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLET_PASS" ):
                listener.exitLET_PASS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLET_PASS" ):
                return visitor.visitLET_PASS(self)
            else:
                return visitor.visitChildren(self)


    class ASSIGN_VALContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(HelloParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(HelloParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterASSIGN_VAL" ):
                listener.enterASSIGN_VAL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitASSIGN_VAL" ):
                listener.exitASSIGN_VAL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitASSIGN_VAL" ):
                return visitor.visitASSIGN_VAL(self)
            else:
                return visitor.visitChildren(self)


    class MINUSContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def MINUS(self):
            return self.getToken(HelloParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMINUS" ):
                listener.enterMINUS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMINUS" ):
                listener.exitMINUS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMINUS" ):
                return visitor.visitMINUS(self)
            else:
                return visitor.visitChildren(self)


    class DIVIDEContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def DIVIDE(self):
            return self.getToken(HelloParser.DIVIDE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDIVIDE" ):
                listener.enterDIVIDE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDIVIDE" ):
                listener.exitDIVIDE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDIVIDE" ):
                return visitor.visitDIVIDE(self)
            else:
                return visitor.visitChildren(self)


    class BIGGERContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def BIGGER(self):
            return self.getToken(HelloParser.BIGGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBIGGER" ):
                listener.enterBIGGER(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBIGGER" ):
                listener.exitBIGGER(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBIGGER" ):
                return visitor.visitBIGGER(self)
            else:
                return visitor.visitChildren(self)


    class NOTContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(HelloParser.NOT, 0)
        def LPAREN(self):
            return self.getToken(HelloParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(HelloParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNOT" ):
                listener.enterNOT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNOT" ):
                listener.exitNOT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNOT" ):
                return visitor.visitNOT(self)
            else:
                return visitor.visitChildren(self)


    class NEWOBJContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.NEW)
            else:
                return self.getToken(HelloParser.NEW, i)
        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.TYPE)
            else:
                return self.getToken(HelloParser.TYPE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNEWOBJ" ):
                listener.enterNEWOBJ(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNEWOBJ" ):
                listener.exitNEWOBJ(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNEWOBJ" ):
                return visitor.visitNEWOBJ(self)
            else:
                return visitor.visitChildren(self)


    class IF_CLAUSEContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(HelloParser.IF, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def THEN(self):
            return self.getToken(HelloParser.THEN, 0)
        def ELSE(self):
            return self.getToken(HelloParser.ELSE, 0)
        def FI(self):
            return self.getToken(HelloParser.FI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIF_CLAUSE" ):
                listener.enterIF_CLAUSE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIF_CLAUSE" ):
                listener.exitIF_CLAUSE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIF_CLAUSE" ):
                return visitor.visitIF_CLAUSE(self)
            else:
                return visitor.visitChildren(self)


    class STRINGContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(HelloParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSTRING" ):
                listener.enterSTRING(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSTRING" ):
                listener.exitSTRING(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSTRING" ):
                return visitor.visitSTRING(self)
            else:
                return visitor.visitChildren(self)


    class TILDEContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TILDE(self):
            return self.getToken(HelloParser.TILDE, 0)
        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTILDE" ):
                listener.enterTILDE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTILDE" ):
                listener.exitTILDE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTILDE" ):
                return visitor.visitTILDE(self)
            else:
                return visitor.visitChildren(self)


    class FALSEContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(HelloParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFALSE" ):
                listener.enterFALSE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFALSE" ):
                listener.exitFALSE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFALSE" ):
                return visitor.visitFALSE(self)
            else:
                return visitor.visitChildren(self)


    class IDContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterID" ):
                listener.enterID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitID" ):
                listener.exitID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitID" ):
                return visitor.visitID(self)
            else:
                return visitor.visitChildren(self)


    class BIGGEREQUALSContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def BIGGEREQUALS(self):
            return self.getToken(HelloParser.BIGGEREQUALS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBIGGEREQUALS" ):
                listener.enterBIGGEREQUALS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBIGGEREQUALS" ):
                listener.exitBIGGEREQUALS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBIGGEREQUALS" ):
                return visitor.visitBIGGEREQUALS(self)
            else:
                return visitor.visitChildren(self)


    class INTEGERContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(HelloParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterINTEGER" ):
                listener.enterINTEGER(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitINTEGER" ):
                listener.exitINTEGER(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitINTEGER" ):
                return visitor.visitINTEGER(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HelloParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = HelloParser.CALLContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 71
                self.match(HelloParser.ID)
                self.state = 72
                self.match(HelloParser.LPAREN)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 141830506808) != 0):
                    self.state = 73
                    self.expr(0)
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==34:
                        self.state = 74
                        self.match(HelloParser.COMMA)
                        self.state = 75
                        self.expr(0)
                        self.state = 80
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 83
                self.match(HelloParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = HelloParser.IF_CLAUSEContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84
                self.match(HelloParser.IF)
                self.state = 85
                self.expr(0)
                self.state = 86
                self.match(HelloParser.THEN)
                self.state = 87
                self.expr(0)
                self.state = 88
                self.match(HelloParser.ELSE)
                self.state = 89
                self.expr(0)
                self.state = 90
                self.match(HelloParser.FI)
                pass

            elif la_ == 3:
                localctx = HelloParser.WHILE_CLAUSEContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 92
                self.match(HelloParser.WHILE)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.match(HelloParser.LOOP)
                self.state = 95
                self.expr(0)
                self.state = 96
                self.match(HelloParser.POOL)
                pass

            elif la_ == 4:
                localctx = HelloParser.BLOCKContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 98
                self.match(HelloParser.LBRACKET)
                self.state = 102 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 99
                    self.expr(0)
                    self.state = 100
                    self.match(HelloParser.SEMICOLON)
                    self.state = 104 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141830506808) != 0)):
                        break

                self.state = 106
                self.match(HelloParser.RBRACKET)
                pass

            elif la_ == 5:
                localctx = HelloParser.LET_PASSContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(HelloParser.LET)
                self.state = 109
                self.match(HelloParser.ID)
                self.state = 110
                self.match(HelloParser.COLON)
                self.state = 111
                self.match(HelloParser.TYPE)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 112
                    self.match(HelloParser.ASSIGN)
                    self.state = 113
                    self.expr(0)


                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 116
                    self.match(HelloParser.COMMA)
                    self.state = 117
                    self.match(HelloParser.ID)
                    self.state = 118
                    self.match(HelloParser.COLON)
                    self.state = 119
                    self.match(HelloParser.TYPE)
                    self.state = 122
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==31:
                        self.state = 120
                        self.match(HelloParser.ASSIGN)
                        self.state = 121
                        self.expr(0)


                    self.state = 128
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 129
                self.match(HelloParser.IN)
                self.state = 130
                self.expr(19)
                pass

            elif la_ == 6:
                localctx = HelloParser.NEWOBJContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 131
                        self.match(HelloParser.NEW)
                        self.state = 132
                        self.match(HelloParser.TYPE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 135 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass

            elif la_ == 7:
                localctx = HelloParser.VOID_EXPRContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.match(HelloParser.ISVOID)
                self.state = 138
                self.expr(17)
                pass

            elif la_ == 8:
                localctx = HelloParser.TILDEContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 139
                self.match(HelloParser.TILDE)
                self.state = 140
                self.expr(12)
                pass

            elif la_ == 9:
                localctx = HelloParser.NOTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 141
                self.match(HelloParser.NOT)
                self.state = 142
                self.match(HelloParser.LPAREN)
                self.state = 143
                self.expr(0)
                self.state = 144
                self.match(HelloParser.RPAREN)
                pass

            elif la_ == 10:
                localctx = HelloParser.EXPR_PARAMSContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(HelloParser.LPAREN)
                self.state = 147
                self.expr(0)
                self.state = 148
                self.match(HelloParser.RPAREN)
                pass

            elif la_ == 11:
                localctx = HelloParser.IDContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.match(HelloParser.ID)
                pass

            elif la_ == 12:
                localctx = HelloParser.INTEGERContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.match(HelloParser.INTEGER)
                pass

            elif la_ == 13:
                localctx = HelloParser.STRINGContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 152
                self.match(HelloParser.STRING)
                pass

            elif la_ == 14:
                localctx = HelloParser.TRUEContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self.match(HelloParser.TRUE)
                pass

            elif la_ == 15:
                localctx = HelloParser.FALSEContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 154
                self.match(HelloParser.FALSE)
                pass

            elif la_ == 16:
                localctx = HelloParser.ASSIGN_VALContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 155
                self.match(HelloParser.ID)
                self.state = 156
                self.match(HelloParser.ASSIGN)
                self.state = 157
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 197
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = HelloParser.SUMContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 160
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 161
                        self.match(HelloParser.PLUS)
                        self.state = 162
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = HelloParser.MINUSContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 163
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 164
                        self.match(HelloParser.MINUS)
                        self.state = 165
                        self.expr(16)
                        pass

                    elif la_ == 3:
                        localctx = HelloParser.TIMESContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 166
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 167
                        self.match(HelloParser.TIMES)
                        self.state = 168
                        self.expr(15)
                        pass

                    elif la_ == 4:
                        localctx = HelloParser.DIVIDEContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 169
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 170
                        self.match(HelloParser.DIVIDE)
                        self.state = 171
                        self.expr(14)
                        pass

                    elif la_ == 5:
                        localctx = HelloParser.BIGGERContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 172
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 173
                        self.match(HelloParser.BIGGER)
                        self.state = 174
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = HelloParser.BIGGEREQUALSContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 175
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 176
                        self.match(HelloParser.BIGGEREQUALS)
                        self.state = 177
                        self.expr(11)
                        pass

                    elif la_ == 7:
                        localctx = HelloParser.EQUALSContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 178
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 179
                        self.match(HelloParser.EQUALS)
                        self.state = 180
                        self.expr(10)
                        pass

                    elif la_ == 8:
                        localctx = HelloParser.DISPATCHContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 181
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")

                        self.state = 182
                        self.match(HelloParser.AT)
                        self.state = 183
                        self.match(HelloParser.TYPE)
                        self.state = 185
                        self.match(HelloParser.DOT)
                        self.state = 186
                        self.match(HelloParser.ID)
                        self.state = 195
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                        if la_ == 1:
                            self.state = 187
                            self.expr(0)
                            self.state = 192
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
                            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                                if _alt==1:
                                    self.state = 188
                                    self.match(HelloParser.COMMA)
                                    self.state = 189
                                    self.expr(0) 
                                self.state = 194
                                self._errHandler.sync(self)
                                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)



                        pass

             
                self.state = 201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 24)
         




