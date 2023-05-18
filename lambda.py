from __future__ import annotations
from antlr4 import *
from lambdaLexer import lambdaLexer
from lambdaParser import lambdaParser
from dataclasses import dataclass
from lambdaVisitor import lambdaVisitor


@dataclass
class Var:
    val: str

@dataclass
class Apl:
    esq: Terme
    dre: Terme

@dataclass
class Abs:
    val: str
    expr: Terme

Terme = Var | Apl | Abs


class TreeVisitor(lambdaVisitor):
    def __init__(self):
        self.nivell = 0
    def visitParentesi(self, ctx):
        [p1, expressio, p2] = list(ctx.getChildren())
        print('  ' *  self.nivell + '(')
        self.nivell += 1
        self.visit(expressio) # visita recursiva
        print('  ' *  self.nivell + ')')
        self.nivell -= 1
    def visitAbstraccio(self, ctx):
        [sym, expr1 , point , expr2] = list(ctx.getChildren())
        print('  ' *  self.nivell + 'λ' )
        self.visit(expr1)
        self.nivell += 1
        self.visit(expr2) # visita recursiva
        print('  ' *  self.nivell + ')')
        self.nivell -= 1
    def visitAplicacio(self, ctx):
        [expressio1, expressio2] = list(ctx.getChildren())
        self.nivell += 1
        self.visit(expressio1) # visita recursiva
        self.visit(expressio2) # visita recursiva
        self.nivell -= 1
    def visitLletra(self, ctx):
        [lletra] = list(ctx.getChildren())
        print("  " * self.nivell + lletra.getText()) # posa tants espais com nivells i despres la lletra
















input_stream = InputStream(input('? '))
lexer = lambdaLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = lambdaParser(token_stream)
tree = parser.root()
# print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
print(tree.toStringTree(recog=parser))

