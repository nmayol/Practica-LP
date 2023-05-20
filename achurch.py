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


def beta(cap,cos,t2):
    match cos:
        case Var(x):
            if x == cap:
                return t2
            else:
                return Var(x)
        case Apl(x, y):
            return Apl(beta(cap,x,t2),beta(cap,y,t2))
        case Abs(x, y):
            if x == cap:
                return Abs(t2,beta(cap,y,t2))
            else:
                return Abs(x,beta(cap,y,t2))
        case Par(x):
            return Par(beta(cap,x,t2))



def avaluacio(t):
    match t:
        case Var(x):
            return Var(x)
        case Apl(x, y):
            match x:
                case Par(z):
                    match z:
                        case Abs(a,b):   # cas de la beta reduccio
                            print('β-reducció:')
                            return beta(a,b,y)
                        case _:
                            return Apl(avaluacio(x),avaluacio(y))
                case Abs(a,b):   # cas de la beta reduccio
                    print('β-reducció:')
                    return beta(a,b,y)
                case _:
                    return Apl(avaluacio(x),avaluacio(y))
        case Abs(x, y):
            return Abs(x,avaluacio(y))
        case Par(x):
            return Par(avaluacio(x))

        

input_stream = InputStream(input('? '))
lexer = lcLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = lcParser(token_stream)
tree = parser.root()
if parser.getNumberOfSyntaxErrors() == 0:
    visitor = TreeVisitor()
    t = visitor.visit(tree)
    print('Arbre:')
    print(printTree(t))
    step = 0
    while step < 6:
        t1 = avaluacio(t)
        if t1 != t:
            print(printTree(t) + ' → ' + printTree(t1))
        t = t1
        step += 1
    print('Resultat:')
    print(printTree(t))

else:
    print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
    print(tree.toStringTree(recog=parser))
