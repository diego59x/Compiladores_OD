# Generated from Hello.g4 by ANTLR 4.13.0
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
        4,1,39,207,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,3,1,24,8,1,1,1,1,1,
        1,1,1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        5,2,42,8,2,10,2,12,2,45,9,2,3,2,47,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,61,8,2,3,2,63,8,2,1,3,1,3,1,3,1,3,1,4,
        1,4,1,4,1,4,4,4,73,8,4,11,4,12,4,74,1,4,1,4,1,4,1,4,1,4,5,4,82,8,
        4,10,4,12,4,85,9,4,3,4,87,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,108,8,4,11,4,12,4,
        109,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,120,8,4,1,4,1,4,1,4,1,4,
        1,4,1,4,3,4,128,8,4,5,4,130,8,4,10,4,12,4,133,9,4,1,4,1,4,1,4,1,
        4,4,4,139,8,4,11,4,12,4,140,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,161,8,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,193,8,4,10,4,12,4,196,
        9,4,3,4,198,8,4,5,4,200,8,4,10,4,12,4,203,9,4,1,5,1,5,1,5,0,1,8,
        6,0,2,4,6,8,10,0,0,240,0,15,1,0,0,0,2,19,1,0,0,0,4,62,1,0,0,0,6,
        64,1,0,0,0,8,160,1,0,0,0,10,204,1,0,0,0,12,13,3,2,1,0,13,14,5,1,
        0,0,14,16,1,0,0,0,15,12,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,
        1,0,0,0,18,1,1,0,0,0,19,20,5,14,0,0,20,23,5,38,0,0,21,22,5,15,0,
        0,22,24,5,38,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,31,
        5,2,0,0,26,27,3,4,2,0,27,28,5,1,0,0,28,30,1,0,0,0,29,26,1,0,0,0,
        30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,
        0,0,0,34,35,5,3,0,0,35,3,1,0,0,0,36,37,5,37,0,0,37,46,5,4,0,0,38,
        43,3,6,3,0,39,40,5,5,0,0,40,42,3,6,3,0,41,39,1,0,0,0,42,45,1,0,0,
        0,43,41,1,0,0,0,43,44,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,46,38,
        1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,49,5,6,0,0,49,50,5,7,0,0,
        50,51,5,38,0,0,51,52,5,2,0,0,52,53,3,8,4,0,53,54,5,3,0,0,54,63,1,
        0,0,0,55,56,5,37,0,0,56,57,5,7,0,0,57,60,5,38,0,0,58,59,5,8,0,0,
        59,61,3,8,4,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,36,1,
        0,0,0,62,55,1,0,0,0,63,5,1,0,0,0,64,65,5,37,0,0,65,66,5,7,0,0,66,
        67,5,38,0,0,67,7,1,0,0,0,68,72,6,4,-1,0,69,70,5,37,0,0,70,71,5,8,
        0,0,71,73,3,8,4,0,72,69,1,0,0,0,73,74,1,0,0,0,74,72,1,0,0,0,74,75,
        1,0,0,0,75,161,1,0,0,0,76,77,5,37,0,0,77,86,5,4,0,0,78,83,3,8,4,
        0,79,80,5,5,0,0,80,82,3,8,4,0,81,79,1,0,0,0,82,85,1,0,0,0,83,81,
        1,0,0,0,83,84,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,86,78,1,0,0,0,
        86,87,1,0,0,0,87,88,1,0,0,0,88,161,5,6,0,0,89,90,5,18,0,0,90,91,
        3,8,4,0,91,92,5,26,0,0,92,93,3,8,4,0,93,94,5,20,0,0,94,95,3,8,4,
        0,95,96,5,19,0,0,96,161,1,0,0,0,97,98,5,21,0,0,98,99,3,8,4,0,99,
        100,5,22,0,0,100,101,3,8,4,0,101,102,5,23,0,0,102,161,1,0,0,0,103,
        107,5,2,0,0,104,105,3,8,4,0,105,106,5,1,0,0,106,108,1,0,0,0,107,
        104,1,0,0,0,108,109,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,
        111,1,0,0,0,111,112,5,3,0,0,112,161,1,0,0,0,113,114,5,24,0,0,114,
        115,5,37,0,0,115,116,5,7,0,0,116,119,5,38,0,0,117,118,5,8,0,0,118,
        120,3,8,4,0,119,117,1,0,0,0,119,120,1,0,0,0,120,131,1,0,0,0,121,
        122,5,5,0,0,122,123,5,37,0,0,123,124,5,7,0,0,124,127,5,38,0,0,125,
        126,5,8,0,0,126,128,3,8,4,0,127,125,1,0,0,0,127,128,1,0,0,0,128,
        130,1,0,0,0,129,121,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,
        132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,135,5,25,0,0,135,
        161,3,8,4,18,136,137,5,27,0,0,137,139,5,38,0,0,138,136,1,0,0,0,139,
        140,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,161,1,0,0,0,142,
        143,5,28,0,0,143,161,3,8,4,16,144,145,5,13,0,0,145,161,3,8,4,11,
        146,147,5,29,0,0,147,148,5,4,0,0,148,149,3,8,4,0,149,150,5,6,0,0,
        150,161,1,0,0,0,151,152,5,4,0,0,152,153,3,8,4,0,153,154,5,6,0,0,
        154,161,1,0,0,0,155,161,5,37,0,0,156,161,5,17,0,0,157,161,5,16,0,
        0,158,161,5,35,0,0,159,161,5,36,0,0,160,68,1,0,0,0,160,76,1,0,0,
        0,160,89,1,0,0,0,160,97,1,0,0,0,160,103,1,0,0,0,160,113,1,0,0,0,
        160,138,1,0,0,0,160,142,1,0,0,0,160,144,1,0,0,0,160,146,1,0,0,0,
        160,151,1,0,0,0,160,155,1,0,0,0,160,156,1,0,0,0,160,157,1,0,0,0,
        160,158,1,0,0,0,160,159,1,0,0,0,161,201,1,0,0,0,162,163,10,15,0,
        0,163,164,5,11,0,0,164,200,3,8,4,16,165,166,10,14,0,0,166,167,5,
        12,0,0,167,200,3,8,4,15,168,169,10,13,0,0,169,170,5,34,0,0,170,200,
        3,8,4,14,171,172,10,12,0,0,172,173,5,33,0,0,173,200,3,8,4,13,174,
        175,10,10,0,0,175,176,5,31,0,0,176,200,3,8,4,11,177,178,10,9,0,0,
        178,179,5,32,0,0,179,200,3,8,4,10,180,181,10,8,0,0,181,182,5,30,
        0,0,182,200,3,8,4,9,183,184,10,23,0,0,184,185,5,9,0,0,185,186,5,
        38,0,0,186,187,1,0,0,0,187,188,5,10,0,0,188,197,5,37,0,0,189,194,
        3,8,4,0,190,191,5,5,0,0,191,193,3,8,4,0,192,190,1,0,0,0,193,196,
        1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,198,1,0,0,0,196,194,
        1,0,0,0,197,189,1,0,0,0,197,198,1,0,0,0,198,200,1,0,0,0,199,162,
        1,0,0,0,199,165,1,0,0,0,199,168,1,0,0,0,199,171,1,0,0,0,199,174,
        1,0,0,0,199,177,1,0,0,0,199,180,1,0,0,0,199,183,1,0,0,0,200,203,
        1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,9,1,0,0,0,203,201,1,
        0,0,0,204,205,3,0,0,0,205,11,1,0,0,0,20,17,23,31,43,46,60,62,74,
        83,86,109,119,127,131,140,160,194,197,199,201
    ]

class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'{'", "'}'", "'('", "','", "')'", 
                     "':'", "'<-'", "'@'", "'.'", "'+'", "'-'", "'~'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'='", "'<'", 
                     "'<='", "'/'", "'*'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "CLASS", "INHERITS", "STRING", 
                      "INTEGER", "IF", "FI", "ELSE", "WHILE", "LOOP", "POOL", 
                      "LET", "IN", "THEN", "NEW", "ISVOID", "NOT", "EQUALS", 
                      "BIGGER", "BIGGEREQUALS", "DEVIDE", "TIMES", "TRUE", 
                      "FALSE", "ID", "TYPE", "WS" ]

    RULE_program = 0
    RULE_class = 1
    RULE_feature = 2
    RULE_formal = 3
    RULE_expr = 4
    RULE_r = 5

    ruleNames =  [ "program", "class", "feature", "formal", "expr", "r" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    CLASS=14
    INHERITS=15
    STRING=16
    INTEGER=17
    IF=18
    FI=19
    ELSE=20
    WHILE=21
    LOOP=22
    POOL=23
    LET=24
    IN=25
    THEN=26
    NEW=27
    ISVOID=28
    NOT=29
    EQUALS=30
    BIGGER=31
    BIGGEREQUALS=32
    DEVIDE=33
    TIMES=34
    TRUE=35
    FALSE=36
    ID=37
    TYPE=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




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
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.class_()
                self.state = 13
                self.match(HelloParser.T__0)
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
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

        def INHERITS(self):
            return self.getToken(HelloParser.INHERITS, 0)

        def feature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.FeatureContext)
            else:
                return self.getTypedRuleContext(HelloParser.FeatureContext,i)


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
        self.enterRule(localctx, 2, self.RULE_class)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(HelloParser.CLASS)
            self.state = 20
            self.match(HelloParser.TYPE)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 21
                self.match(HelloParser.INHERITS)
                self.state = 22
                self.match(HelloParser.TYPE)


            self.state = 25
            self.match(HelloParser.T__1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 26
                self.feature()
                self.state = 27
                self.match(HelloParser.T__0)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(HelloParser.T__2)
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

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def TYPE(self):
            return self.getToken(HelloParser.TYPE, 0)

        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)


        def formal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.FormalContext)
            else:
                return self.getTypedRuleContext(HelloParser.FormalContext,i)


        def getRuleIndex(self):
            return HelloParser.RULE_feature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeature" ):
                listener.enterFeature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeature" ):
                listener.exitFeature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeature" ):
                return visitor.visitFeature(self)
            else:
                return visitor.visitChildren(self)




    def feature(self):

        localctx = HelloParser.FeatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_feature)
        self._la = 0 # Token type
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(HelloParser.ID)
                self.state = 37
                self.match(HelloParser.T__3)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 38
                    self.formal()
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 39
                        self.match(HelloParser.T__4)
                        self.state = 40
                        self.formal()
                        self.state = 45
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 48
                self.match(HelloParser.T__5)
                self.state = 49
                self.match(HelloParser.T__6)
                self.state = 50
                self.match(HelloParser.TYPE)
                self.state = 51
                self.match(HelloParser.T__1)
                self.state = 52
                self.expr(0)
                self.state = 53
                self.match(HelloParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(HelloParser.ID)
                self.state = 56
                self.match(HelloParser.T__6)
                self.state = 57
                self.match(HelloParser.TYPE)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 58
                    self.match(HelloParser.T__7)
                    self.state = 59
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
        self.enterRule(localctx, 6, self.RULE_formal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(HelloParser.ID)
            self.state = 65
            self.match(HelloParser.T__6)
            self.state = 66
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.ID)
            else:
                return self.getToken(HelloParser.ID, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)


        def IF(self):
            return self.getToken(HelloParser.IF, 0)

        def THEN(self):
            return self.getToken(HelloParser.THEN, 0)

        def ELSE(self):
            return self.getToken(HelloParser.ELSE, 0)

        def FI(self):
            return self.getToken(HelloParser.FI, 0)

        def WHILE(self):
            return self.getToken(HelloParser.WHILE, 0)

        def LOOP(self):
            return self.getToken(HelloParser.LOOP, 0)

        def POOL(self):
            return self.getToken(HelloParser.POOL, 0)

        def LET(self):
            return self.getToken(HelloParser.LET, 0)

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.TYPE)
            else:
                return self.getToken(HelloParser.TYPE, i)

        def IN(self):
            return self.getToken(HelloParser.IN, 0)

        def NEW(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.NEW)
            else:
                return self.getToken(HelloParser.NEW, i)

        def ISVOID(self):
            return self.getToken(HelloParser.ISVOID, 0)

        def NOT(self):
            return self.getToken(HelloParser.NOT, 0)

        def INTEGER(self):
            return self.getToken(HelloParser.INTEGER, 0)

        def STRING(self):
            return self.getToken(HelloParser.STRING, 0)

        def TRUE(self):
            return self.getToken(HelloParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(HelloParser.FALSE, 0)

        def TIMES(self):
            return self.getToken(HelloParser.TIMES, 0)

        def DEVIDE(self):
            return self.getToken(HelloParser.DEVIDE, 0)

        def BIGGER(self):
            return self.getToken(HelloParser.BIGGER, 0)

        def BIGGEREQUALS(self):
            return self.getToken(HelloParser.BIGGEREQUALS, 0)

        def EQUALS(self):
            return self.getToken(HelloParser.EQUALS, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HelloParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 72 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 69
                        self.match(HelloParser.ID)
                        self.state = 70
                        self.match(HelloParser.T__7)
                        self.state = 71
                        self.expr(0)

                    else:
                        raise NoViableAltException(self)
                    self.state = 74 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass

            elif la_ == 2:
                self.state = 76
                self.match(HelloParser.ID)
                self.state = 77
                self.match(HelloParser.T__3)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 241477034004) != 0):
                    self.state = 78
                    self.expr(0)
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 79
                        self.match(HelloParser.T__4)
                        self.state = 80
                        self.expr(0)
                        self.state = 85
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 88
                self.match(HelloParser.T__5)
                pass

            elif la_ == 3:
                self.state = 89
                self.match(HelloParser.IF)
                self.state = 90
                self.expr(0)
                self.state = 91
                self.match(HelloParser.THEN)
                self.state = 92
                self.expr(0)
                self.state = 93
                self.match(HelloParser.ELSE)
                self.state = 94
                self.expr(0)
                self.state = 95
                self.match(HelloParser.FI)
                pass

            elif la_ == 4:
                self.state = 97
                self.match(HelloParser.WHILE)
                self.state = 98
                self.expr(0)
                self.state = 99
                self.match(HelloParser.LOOP)
                self.state = 100
                self.expr(0)
                self.state = 101
                self.match(HelloParser.POOL)
                pass

            elif la_ == 5:
                self.state = 103
                self.match(HelloParser.T__1)
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 104
                    self.expr(0)
                    self.state = 105
                    self.match(HelloParser.T__0)
                    self.state = 109 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 241477034004) != 0)):
                        break

                self.state = 111
                self.match(HelloParser.T__2)
                pass

            elif la_ == 6:
                self.state = 113
                self.match(HelloParser.LET)
                self.state = 114
                self.match(HelloParser.ID)
                self.state = 115
                self.match(HelloParser.T__6)
                self.state = 116
                self.match(HelloParser.TYPE)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 117
                    self.match(HelloParser.T__7)
                    self.state = 118
                    self.expr(0)


                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 121
                    self.match(HelloParser.T__4)
                    self.state = 122
                    self.match(HelloParser.ID)
                    self.state = 123
                    self.match(HelloParser.T__6)
                    self.state = 124
                    self.match(HelloParser.TYPE)
                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==8:
                        self.state = 125
                        self.match(HelloParser.T__7)
                        self.state = 126
                        self.expr(0)


                    self.state = 133
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 134
                self.match(HelloParser.IN)
                self.state = 135
                self.expr(18)
                pass

            elif la_ == 7:
                self.state = 138 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 136
                        self.match(HelloParser.NEW)
                        self.state = 137
                        self.match(HelloParser.TYPE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 140 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                pass

            elif la_ == 8:
                self.state = 142
                self.match(HelloParser.ISVOID)
                self.state = 143
                self.expr(16)
                pass

            elif la_ == 9:
                self.state = 144
                self.match(HelloParser.T__12)
                self.state = 145
                self.expr(11)
                pass

            elif la_ == 10:
                self.state = 146
                self.match(HelloParser.NOT)
                self.state = 147
                self.match(HelloParser.T__3)
                self.state = 148
                self.expr(0)
                self.state = 149
                self.match(HelloParser.T__5)
                pass

            elif la_ == 11:
                self.state = 151
                self.match(HelloParser.T__3)
                self.state = 152
                self.expr(0)
                self.state = 153
                self.match(HelloParser.T__5)
                pass

            elif la_ == 12:
                self.state = 155
                self.match(HelloParser.ID)
                pass

            elif la_ == 13:
                self.state = 156
                self.match(HelloParser.INTEGER)
                pass

            elif la_ == 14:
                self.state = 157
                self.match(HelloParser.STRING)
                pass

            elif la_ == 15:
                self.state = 158
                self.match(HelloParser.TRUE)
                pass

            elif la_ == 16:
                self.state = 159
                self.match(HelloParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 199
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = HelloParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 162
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 163
                        self.match(HelloParser.T__10)
                        self.state = 164
                        self.expr(16)
                        pass

                    elif la_ == 2:
                        localctx = HelloParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 165
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 166
                        self.match(HelloParser.T__11)
                        self.state = 167
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = HelloParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 168
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 169
                        self.match(HelloParser.TIMES)
                        self.state = 170
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = HelloParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 171
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 172
                        self.match(HelloParser.DEVIDE)
                        self.state = 173
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = HelloParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 174
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 175
                        self.match(HelloParser.BIGGER)
                        self.state = 176
                        self.expr(11)
                        pass

                    elif la_ == 6:
                        localctx = HelloParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 177
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 178
                        self.match(HelloParser.BIGGEREQUALS)
                        self.state = 179
                        self.expr(10)
                        pass

                    elif la_ == 7:
                        localctx = HelloParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 180
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 181
                        self.match(HelloParser.EQUALS)
                        self.state = 182
                        self.expr(9)
                        pass

                    elif la_ == 8:
                        localctx = HelloParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 183
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")

                        self.state = 184
                        self.match(HelloParser.T__8)
                        self.state = 185
                        self.match(HelloParser.TYPE)
                        self.state = 187
                        self.match(HelloParser.T__9)
                        self.state = 188
                        self.match(HelloParser.ID)
                        self.state = 197
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                        if la_ == 1:
                            self.state = 189
                            self.expr(0)
                            self.state = 194
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
                            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                                if _alt==1:
                                    self.state = 190
                                    self.match(HelloParser.T__4)
                                    self.state = 191
                                    self.expr(0) 
                                self.state = 196
                                self._errHandler.sync(self)
                                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)



                        pass

             
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


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
        self.enterRule(localctx, 10, self.RULE_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.program()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 23)
         




