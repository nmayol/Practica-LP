from __future__ import annotations
from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from dataclasses import dataclass
from lcVisitor import lcVisitor


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

@dataclass
class Par:
    expr: Terme


Terme = Par | Var | Apl | Abs


class TreeVisitor(lcVisitor):

    def visitRoot(self, ctx):
        [expr] = list(ctx.getChildren())
        x = self.visit(expr)
        return x
    
    def visitParentesi(self, ctx):
        [p1, expr, p2] = list(ctx.getChildren())
        return Par(self.visit(expr))
    
    def visitAbstraccio(self, ctx):
        [sym, expr1, point, expr2] = list(ctx.getChildren())
        return Abs(expr1.getText(),self.visit(expr2))
    
    def visitAplicacio(self, ctx):
        [expr1, expr2] = list(ctx.getChildren())
        return Apl(self.visit(expr1), self.visit(expr2))
    
    def visitLletra(self, ctx):
        [lletra] = list(ctx.getChildren())
        return Var(lletra.getText())


def printTree(t):
    # print(t)      # descomentar per fer proves
    match t:
        case Var(x):
            return x
        case Apl(x, y):
            return ("(" + printTree(x) + printTree(y) + ")")  
        case Abs(x, y):
            return "(λ" + x + "." + printTree(y) + ")" 
        case Par(x):
            return ( printTree(x))
        

input_stream = InputStream(input('? '))
lexer = lcLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = lcParser(token_stream)
tree = parser.root()
if parser.getNumberOfSyntaxErrors() == 0:
    visitor = TreeVisitor()
    print('Arbre:')
    print(printTree(visitor.visitRoot(tree))) 
else:
    print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
    print(tree.toStringTree(recog=parser))
