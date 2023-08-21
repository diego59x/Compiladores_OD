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
        4,1,43,203,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,1,1,1,1,1,4,1,20,8,1,11,1,12,1,21,1,2,1,2,1,2,1,2,3,
        2,28,8,2,1,2,1,2,1,2,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,5,3,46,8,3,10,3,12,3,49,9,3,3,3,51,8,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,65,8,3,3,3,67,8,3,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,78,8,5,1,6,1,6,1,6,1,6,1,6,1,
        6,5,6,86,8,6,10,6,12,6,89,9,6,3,6,91,8,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,4,6,112,8,6,
        11,6,12,6,113,1,6,1,6,1,6,1,6,1,6,1,6,5,6,122,8,6,10,6,12,6,125,
        9,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,153,8,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,3,6,179,8,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,
        187,8,6,10,6,12,6,190,9,6,5,6,192,8,6,10,6,12,6,195,9,6,1,6,5,6,
        198,8,6,10,6,12,6,201,9,6,1,6,0,1,12,7,0,2,4,6,8,10,12,0,0,233,0,
        14,1,0,0,0,2,19,1,0,0,0,4,23,1,0,0,0,6,66,1,0,0,0,8,68,1,0,0,0,10,
        72,1,0,0,0,12,152,1,0,0,0,14,15,3,2,1,0,15,1,1,0,0,0,16,17,3,4,2,
        0,17,18,5,28,0,0,18,20,1,0,0,0,19,16,1,0,0,0,20,21,1,0,0,0,21,19,
        1,0,0,0,21,22,1,0,0,0,22,3,1,0,0,0,23,24,5,1,0,0,24,27,5,38,0,0,
        25,26,5,2,0,0,26,28,5,38,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,29,1,
        0,0,0,29,35,5,26,0,0,30,31,3,6,3,0,31,32,5,28,0,0,32,34,1,0,0,0,
        33,30,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,
        0,0,0,37,35,1,0,0,0,38,39,5,27,0,0,39,5,1,0,0,0,40,41,5,37,0,0,41,
        50,5,24,0,0,42,47,3,8,4,0,43,44,5,34,0,0,44,46,3,8,4,0,45,43,1,0,
        0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,51,1,0,0,0,49,47,
        1,0,0,0,50,42,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,53,5,25,0,0,
        53,54,5,33,0,0,54,55,5,38,0,0,55,56,5,26,0,0,56,57,3,12,6,0,57,58,
        5,27,0,0,58,67,1,0,0,0,59,60,5,37,0,0,60,61,5,33,0,0,61,64,5,38,
        0,0,62,63,5,31,0,0,63,65,3,12,6,0,64,62,1,0,0,0,64,65,1,0,0,0,65,
        67,1,0,0,0,66,40,1,0,0,0,66,59,1,0,0,0,67,7,1,0,0,0,68,69,5,37,0,
        0,69,70,5,33,0,0,70,71,5,38,0,0,71,9,1,0,0,0,72,73,5,37,0,0,73,74,
        5,33,0,0,74,77,5,38,0,0,75,76,5,31,0,0,76,78,3,12,6,0,77,75,1,0,
        0,0,77,78,1,0,0,0,78,11,1,0,0,0,79,80,6,6,-1,0,80,81,5,37,0,0,81,
        90,5,24,0,0,82,87,3,12,6,0,83,84,5,34,0,0,84,86,3,12,6,0,85,83,1,
        0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,91,1,0,0,0,89,
        87,1,0,0,0,90,82,1,0,0,0,90,91,1,0,0,0,91,92,1,0,0,0,92,153,5,25,
        0,0,93,94,5,5,0,0,94,95,3,12,6,0,95,96,5,13,0,0,96,97,3,12,6,0,97,
        98,5,7,0,0,98,99,3,12,6,0,99,100,5,6,0,0,100,153,1,0,0,0,101,102,
        5,8,0,0,102,103,3,12,6,0,103,104,5,9,0,0,104,105,3,12,6,0,105,106,
        5,10,0,0,106,153,1,0,0,0,107,111,5,26,0,0,108,109,3,12,6,0,109,110,
        5,28,0,0,110,112,1,0,0,0,111,108,1,0,0,0,112,113,1,0,0,0,113,111,
        1,0,0,0,113,114,1,0,0,0,114,115,1,0,0,0,115,116,5,27,0,0,116,153,
        1,0,0,0,117,118,5,11,0,0,118,123,3,10,5,0,119,120,5,34,0,0,120,122,
        3,10,5,0,121,119,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,
        1,0,0,0,124,126,1,0,0,0,125,123,1,0,0,0,126,127,5,12,0,0,127,128,
        3,12,6,19,128,153,1,0,0,0,129,130,5,14,0,0,130,153,5,38,0,0,131,
        132,5,15,0,0,132,153,3,12,6,17,133,134,5,32,0,0,134,153,3,12,6,12,
        135,136,5,16,0,0,136,137,5,24,0,0,137,138,3,12,6,0,138,139,5,25,
        0,0,139,153,1,0,0,0,140,141,5,24,0,0,141,142,3,12,6,0,142,143,5,
        25,0,0,143,153,1,0,0,0,144,153,5,37,0,0,145,153,5,4,0,0,146,153,
        5,3,0,0,147,153,5,22,0,0,148,153,5,23,0,0,149,150,5,37,0,0,150,151,
        5,31,0,0,151,153,3,12,6,1,152,79,1,0,0,0,152,93,1,0,0,0,152,101,
        1,0,0,0,152,107,1,0,0,0,152,117,1,0,0,0,152,129,1,0,0,0,152,131,
        1,0,0,0,152,133,1,0,0,0,152,135,1,0,0,0,152,140,1,0,0,0,152,144,
        1,0,0,0,152,145,1,0,0,0,152,146,1,0,0,0,152,147,1,0,0,0,152,148,
        1,0,0,0,152,149,1,0,0,0,153,199,1,0,0,0,154,155,10,16,0,0,155,156,
        5,29,0,0,156,198,3,12,6,17,157,158,10,15,0,0,158,159,5,30,0,0,159,
        198,3,12,6,16,160,161,10,14,0,0,161,162,5,21,0,0,162,198,3,12,6,
        15,163,164,10,13,0,0,164,165,5,20,0,0,165,198,3,12,6,14,166,167,
        10,11,0,0,167,168,5,18,0,0,168,198,3,12,6,12,169,170,10,10,0,0,170,
        171,5,19,0,0,171,198,3,12,6,11,172,173,10,9,0,0,173,174,5,17,0,0,
        174,198,3,12,6,10,175,178,10,24,0,0,176,177,5,36,0,0,177,179,5,38,
        0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,180,1,0,0,0,180,181,5,35,
        0,0,181,182,5,37,0,0,182,193,5,24,0,0,183,188,3,12,6,0,184,185,5,
        34,0,0,185,187,3,12,6,0,186,184,1,0,0,0,187,190,1,0,0,0,188,186,
        1,0,0,0,188,189,1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,191,183,
        1,0,0,0,192,195,1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,196,
        1,0,0,0,195,193,1,0,0,0,196,198,5,25,0,0,197,154,1,0,0,0,197,157,
        1,0,0,0,197,160,1,0,0,0,197,163,1,0,0,0,197,166,1,0,0,0,197,169,
        1,0,0,0,197,172,1,0,0,0,197,175,1,0,0,0,198,201,1,0,0,0,199,197,
        1,0,0,0,199,200,1,0,0,0,200,13,1,0,0,0,201,199,1,0,0,0,18,21,27,
        35,47,50,64,66,77,87,90,113,123,152,178,188,193,197,199
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
                     "'-'", "'<-'", "'~'", "':'", "','", "'.'", "'@'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'(*'", "'*)'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "INHERITS", "STRING", "INTEGER", 
                      "IF", "FI", "ELSE", "WHILE", "LOOP", "POOL", "LET", 
                      "IN", "THEN", "NEW", "ISVOID", "NOT", "EQUALS", "BIGGER", 
                      "BIGGEREQUALS", "DIVIDE", "TIMES", "TRUE", "FALSE", 
                      "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "SEMICOLON", 
                      "PLUS", "MINUS", "ASSIGN", "TILDE", "COLON", "COMMA", 
                      "DOT", "AT", "ID", "TYPE", "WS", "LINE_COMMENT", "INIT_COMMENT", 
                      "FINISH_COMMENT", "COMMENT" ]

    RULE_r = 0
    RULE_program = 1
    RULE_class = 2
    RULE_feature = 3
    RULE_formal = 4
    RULE_formalAssign = 5
    RULE_expr = 6

    ruleNames =  [ "r", "program", "class", "feature", "formal", "formalAssign", 
                   "expr" ]

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
    LINE_COMMENT=40
    INIT_COMMENT=41
    FINISH_COMMENT=42
    COMMENT=43

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
            self.state = 14
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
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.class_()
                self.state = 17
                self.match(HelloParser.SEMICOLON)
                self.state = 21 
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
            self.state = 23
            self.match(HelloParser.CLASS)
            self.state = 24
            self.match(HelloParser.TYPE)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 25
                self.match(HelloParser.INHERITS)
                self.state = 26
                self.match(HelloParser.TYPE)


            self.state = 29
            self.match(HelloParser.LBRACKET)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 30
                self.feature()
                self.state = 31
                self.match(HelloParser.SEMICOLON)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
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
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = HelloParser.DEFINITION_METHOD_PARAMSContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(HelloParser.ID)
                self.state = 41
                self.match(HelloParser.LPAREN)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 42
                    self.formal()
                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==34:
                        self.state = 43
                        self.match(HelloParser.COMMA)
                        self.state = 44
                        self.formal()
                        self.state = 49
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 52
                self.match(HelloParser.RPAREN)
                self.state = 53
                self.match(HelloParser.COLON)
                self.state = 54
                self.match(HelloParser.TYPE)
                self.state = 55
                self.match(HelloParser.LBRACKET)
                self.state = 56
                self.expr(0)
                self.state = 57
                self.match(HelloParser.RBRACKET)
                pass

            elif la_ == 2:
                localctx = HelloParser.DEFINITION_PARAMSContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(HelloParser.ID)
                self.state = 60
                self.match(HelloParser.COLON)
                self.state = 61
                self.match(HelloParser.TYPE)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 62
                    self.match(HelloParser.ASSIGN)
                    self.state = 63
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
            self.state = 68
            self.match(HelloParser.ID)
            self.state = 69
            self.match(HelloParser.COLON)
            self.state = 70
            self.match(HelloParser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalAssignContext(ParserRuleContext):
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

        def ASSIGN(self):
            return self.getToken(HelloParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_formalAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalAssign" ):
                listener.enterFormalAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalAssign" ):
                listener.exitFormalAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalAssign" ):
                return visitor.visitFormalAssign(self)
            else:
                return visitor.visitChildren(self)




    def formalAssign(self):

        localctx = HelloParser.FormalAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_formalAssign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(HelloParser.ID)
            self.state = 73
            self.match(HelloParser.COLON)
            self.state = 74
            self.match(HelloParser.TYPE)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 75
                self.match(HelloParser.ASSIGN)
                self.state = 76
                self.expr(0)


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
        def LPAREN(self):
            return self.getToken(HelloParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(HelloParser.RPAREN, 0)
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
        def formalAssign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.FormalAssignContext)
            else:
                return self.getTypedRuleContext(HelloParser.FormalAssignContext,i)

        def IN(self):
            return self.getToken(HelloParser.IN, 0)
        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)

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

        def NEW(self):
            return self.getToken(HelloParser.NEW, 0)
        def TYPE(self):
            return self.getToken(HelloParser.TYPE, 0)

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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = HelloParser.CALLContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 80
                self.match(HelloParser.ID)
                self.state = 81
                self.match(HelloParser.LPAREN)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 141830506808) != 0):
                    self.state = 82
                    self.expr(0)
                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==34:
                        self.state = 83
                        self.match(HelloParser.COMMA)
                        self.state = 84
                        self.expr(0)
                        self.state = 89
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 92
                self.match(HelloParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = HelloParser.IF_CLAUSEContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 93
                self.match(HelloParser.IF)
                self.state = 94
                self.expr(0)
                self.state = 95
                self.match(HelloParser.THEN)
                self.state = 96
                self.expr(0)
                self.state = 97
                self.match(HelloParser.ELSE)
                self.state = 98
                self.expr(0)
                self.state = 99
                self.match(HelloParser.FI)
                pass

            elif la_ == 3:
                localctx = HelloParser.WHILE_CLAUSEContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 101
                self.match(HelloParser.WHILE)
                self.state = 102
                self.expr(0)
                self.state = 103
                self.match(HelloParser.LOOP)
                self.state = 104
                self.expr(0)
                self.state = 105
                self.match(HelloParser.POOL)
                pass

            elif la_ == 4:
                localctx = HelloParser.BLOCKContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(HelloParser.LBRACKET)
                self.state = 111 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 108
                    self.expr(0)
                    self.state = 109
                    self.match(HelloParser.SEMICOLON)
                    self.state = 113 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141830506808) != 0)):
                        break

                self.state = 115
                self.match(HelloParser.RBRACKET)
                pass

            elif la_ == 5:
                localctx = HelloParser.LET_PASSContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 117
                self.match(HelloParser.LET)
                self.state = 118
                self.formalAssign()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 119
                    self.match(HelloParser.COMMA)
                    self.state = 120
                    self.formalAssign()
                    self.state = 125
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 126
                self.match(HelloParser.IN)
                self.state = 127
                self.expr(19)
                pass

            elif la_ == 6:
                localctx = HelloParser.NEWOBJContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 129
                self.match(HelloParser.NEW)
                self.state = 130
                self.match(HelloParser.TYPE)
                pass

            elif la_ == 7:
                localctx = HelloParser.VOID_EXPRContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 131
                self.match(HelloParser.ISVOID)
                self.state = 132
                self.expr(17)
                pass

            elif la_ == 8:
                localctx = HelloParser.TILDEContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133
                self.match(HelloParser.TILDE)
                self.state = 134
                self.expr(12)
                pass

            elif la_ == 9:
                localctx = HelloParser.NOTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.match(HelloParser.NOT)
                self.state = 136
                self.match(HelloParser.LPAREN)
                self.state = 137
                self.expr(0)
                self.state = 138
                self.match(HelloParser.RPAREN)
                pass

            elif la_ == 10:
                localctx = HelloParser.EXPR_PARAMSContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 140
                self.match(HelloParser.LPAREN)
                self.state = 141
                self.expr(0)
                self.state = 142
                self.match(HelloParser.RPAREN)
                pass

            elif la_ == 11:
                localctx = HelloParser.IDContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.match(HelloParser.ID)
                pass

            elif la_ == 12:
                localctx = HelloParser.INTEGERContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 145
                self.match(HelloParser.INTEGER)
                pass

            elif la_ == 13:
                localctx = HelloParser.STRINGContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(HelloParser.STRING)
                pass

            elif la_ == 14:
                localctx = HelloParser.TRUEContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 147
                self.match(HelloParser.TRUE)
                pass

            elif la_ == 15:
                localctx = HelloParser.FALSEContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(HelloParser.FALSE)
                pass

            elif la_ == 16:
                localctx = HelloParser.ASSIGN_VALContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 149
                self.match(HelloParser.ID)
                self.state = 150
                self.match(HelloParser.ASSIGN)
                self.state = 151
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 197
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = HelloParser.SUMContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 154
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 155
                        self.match(HelloParser.PLUS)
                        self.state = 156
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = HelloParser.MINUSContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 157
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 158
                        self.match(HelloParser.MINUS)
                        self.state = 159
                        self.expr(16)
                        pass

                    elif la_ == 3:
                        localctx = HelloParser.TIMESContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 160
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 161
                        self.match(HelloParser.TIMES)
                        self.state = 162
                        self.expr(15)
                        pass

                    elif la_ == 4:
                        localctx = HelloParser.DIVIDEContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 163
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 164
                        self.match(HelloParser.DIVIDE)
                        self.state = 165
                        self.expr(14)
                        pass

                    elif la_ == 5:
                        localctx = HelloParser.BIGGERContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 166
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 167
                        self.match(HelloParser.BIGGER)
                        self.state = 168
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = HelloParser.BIGGEREQUALSContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 169
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 170
                        self.match(HelloParser.BIGGEREQUALS)
                        self.state = 171
                        self.expr(11)
                        pass

                    elif la_ == 7:
                        localctx = HelloParser.EQUALSContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 172
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 173
                        self.match(HelloParser.EQUALS)
                        self.state = 174
                        self.expr(10)
                        pass

                    elif la_ == 8:
                        localctx = HelloParser.DISPATCHContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 175
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 178
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==36:
                            self.state = 176
                            self.match(HelloParser.AT)
                            self.state = 177
                            self.match(HelloParser.TYPE)


                        self.state = 180
                        self.match(HelloParser.DOT)
                        self.state = 181
                        self.match(HelloParser.ID)
                        self.state = 182
                        self.match(HelloParser.LPAREN)
                        self.state = 193
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & 141830506808) != 0):
                            self.state = 183
                            self.expr(0)
                            self.state = 188
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==34:
                                self.state = 184
                                self.match(HelloParser.COMMA)
                                self.state = 185
                                self.expr(0)
                                self.state = 190
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)

                            self.state = 195
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 196
                        self.match(HelloParser.RPAREN)
                        pass

             
                self.state = 201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self._predicates[6] = self.expr_sempred
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
         




