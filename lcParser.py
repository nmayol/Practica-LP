# Generated from lc.g4 by ANTLR 4.13.0
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
        4,1,10,44,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,27,8,1,1,1,
        1,1,1,1,1,1,1,1,5,1,34,8,1,10,1,12,1,37,9,1,1,2,4,2,40,8,2,11,2,
        12,2,41,1,2,0,1,2,3,0,2,4,0,1,1,0,3,4,48,0,6,1,0,0,0,2,26,1,0,0,
        0,4,39,1,0,0,0,6,7,3,2,1,0,7,1,1,0,0,0,8,9,6,1,-1,0,9,10,5,1,0,0,
        10,11,3,2,1,0,11,12,5,2,0,0,12,27,1,0,0,0,13,14,7,0,0,0,14,15,3,
        4,2,0,15,16,5,5,0,0,16,17,3,2,1,6,17,27,1,0,0,0,18,27,5,7,0,0,19,
        20,5,8,0,0,20,21,5,6,0,0,21,27,3,2,1,4,22,23,5,9,0,0,23,24,5,6,0,
        0,24,27,3,2,1,3,25,27,5,8,0,0,26,8,1,0,0,0,26,13,1,0,0,0,26,18,1,
        0,0,0,26,19,1,0,0,0,26,22,1,0,0,0,26,25,1,0,0,0,27,35,1,0,0,0,28,
        29,10,7,0,0,29,34,3,2,1,8,30,31,10,1,0,0,31,32,5,9,0,0,32,34,3,2,
        1,2,33,28,1,0,0,0,33,30,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,
        1,0,0,0,36,3,1,0,0,0,37,35,1,0,0,0,38,40,5,7,0,0,39,38,1,0,0,0,40,
        41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,5,1,0,0,0,4,26,33,35,41
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'\\u03BB'", "'\\'", "'.'", 
                     "'\\u2261'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LLETRA", "MACRO", 
                      "MACROINFIXA", "WS" ]

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
    T__5=6
    LLETRA=7
    MACRO=8
    MACROINFIXA=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
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


    class MacroContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MACRO(self):
            return self.getToken(lcParser.MACRO, 0)
        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro" ):
                return visitor.visitMacro(self)
            else:
                return visitor.visitChildren(self)


    class MacroIFormulaContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.TermeContext)
            else:
                return self.getTypedRuleContext(lcParser.TermeContext,i)

        def MACROINFIXA(self):
            return self.getToken(lcParser.MACROINFIXA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacroIFormula" ):
                return visitor.visitMacroIFormula(self)
            else:
                return visitor.visitChildren(self)


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


    class MacroIContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MACROINFIXA(self):
            return self.getToken(lcParser.MACROINFIXA, 0)
        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacroI" ):
                return visitor.visitMacroI(self)
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


    class MacroFormulaContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MACRO(self):
            return self.getToken(lcParser.MACRO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacroFormula" ):
                return visitor.visitMacroFormula(self)
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
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
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

            elif la_ == 2:
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
                self.terme(6)
                pass

            elif la_ == 3:
                localctx = lcParser.LletraContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(lcParser.LLETRA)
                pass

            elif la_ == 4:
                localctx = lcParser.MacroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                self.match(lcParser.MACRO)
                self.state = 20
                self.match(lcParser.T__5)
                self.state = 21
                self.terme(4)
                pass

            elif la_ == 5:
                localctx = lcParser.MacroIContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(lcParser.MACROINFIXA)
                self.state = 23
                self.match(lcParser.T__5)
                self.state = 24
                self.terme(3)
                pass

            elif la_ == 6:
                localctx = lcParser.MacroFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(lcParser.MACRO)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 33
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = lcParser.AplicacioContext(self, lcParser.TermeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                        self.state = 28
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 29
                        self.terme(8)
                        pass

                    elif la_ == 2:
                        localctx = lcParser.MacroIFormulaContext(self, lcParser.TermeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                        self.state = 30
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 31
                        self.match(lcParser.MACROINFIXA)
                        self.state = 32
                        self.terme(2)
                        pass

             
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.match(lcParser.LLETRA)
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
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
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




