from __future__ import annotations
from dataclasses import dataclass
from lambdaVisitor import lambdaVisitor


@dataclass
class Lletra:
    val: str

@dataclass
class Aplicacio:
    esq: Terme
    dre: Terme

@dataclass
class Abstraccio:
    val: Lletra
    expr: Terme

Terme = Lletra | Aplicacio | Abstraccio


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

