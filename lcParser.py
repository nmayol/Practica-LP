# Generated from lc.g4 by ANTLR 4.12.0
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
        4,1,7,34,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,20,8,1,1,1,1,1,5,1,24,8,1,10,1,12,1,27,9,
        1,1,2,4,2,30,8,2,11,2,12,2,31,1,2,0,1,2,3,0,2,4,0,1,1,0,3,4,34,0,
        6,1,0,0,0,2,19,1,0,0,0,4,29,1,0,0,0,6,7,3,2,1,0,7,1,1,0,0,0,8,9,
        6,1,-1,0,9,10,5,1,0,0,10,11,3,2,1,0,11,12,5,2,0,0,12,20,1,0,0,0,
        13,14,7,0,0,0,14,15,3,4,2,0,15,16,5,5,0,0,16,17,3,2,1,2,17,20,1,
        0,0,0,18,20,5,6,0,0,19,8,1,0,0,0,19,13,1,0,0,0,19,18,1,0,0,0,20,
        25,1,0,0,0,21,22,10,3,0,0,22,24,3,2,1,4,23,21,1,0,0,0,24,27,1,0,
        0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,3,1,0,0,0,27,25,1,0,0,0,28,30,
        5,6,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,
        32,5,1,0,0,0,3,19,25,31
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'\\u03BB'", "'\\'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "LLETRA", "WS" ]

    RULE_root = 0
    RULE_terme = 1
    RULE_cap = 2

    ruleNames =  [ "root", "terme", "cap" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    LLETRA=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def getRuleIndex(self):
            return lcParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = lcParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.terme(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lcParser.RULE_terme

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LletraContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LLETRA(self):
            return self.getToken(lcParser.LLETRA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLletra" ):
                return visitor.visitLletra(self)
            else:
                return visitor.visitChildren(self)


    class ParentesiContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesi" ):
                return visitor.visitParentesi(self)
            else:
                return visitor.visitChildren(self)


    class AbstraccioContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cap(self):
            return self.getTypedRuleContext(lcParser.CapContext,0)

        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraccio" ):
                return visitor.visitAbstraccio(self)
            else:
                return visitor.visitChildren(self)


    class AplicacioContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.TermeContext)
            else:
                return self.getTypedRuleContext(lcParser.TermeContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAplicacio" ):
                return visitor.visitAplicacio(self)
            else:
                return visitor.visitChildren(self)



    def terme(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = lcParser.TermeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_terme, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = lcParser.ParentesiContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 9
                self.match(lcParser.T__0)
                self.state = 10
                self.terme(0)
                self.state = 11
                self.match(lcParser.T__1)
                pass
            elif token in [3, 4]:
                localctx = lcParser.AbstraccioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 14
                self.cap()
                self.state = 15
                self.match(lcParser.T__4)
                self.state = 16
                self.terme(2)
                pass
            elif token in [6]:
                localctx = lcParser.LletraContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(lcParser.LLETRA)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = lcParser.AplicacioContext(self, lcParser.TermeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                    self.state = 21
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 22
                    self.terme(4) 
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CapContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLETRA(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.LLETRA)
            else:
                return self.getToken(lcParser.LLETRA, i)

        def getRuleIndex(self):
            return lcParser.RULE_cap

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCap" ):
                return visitor.visitCap(self)
            else:
                return visitor.visitChildren(self)




    def cap(self):

        localctx = lcParser.CapContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_cap)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.match(lcParser.LLETRA)
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6):
                    break

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
        self._predicates[1] = self.terme_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def terme_sempred(self, localctx:TermeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




