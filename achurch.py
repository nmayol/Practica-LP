from __future__ import annotations
import random
import string
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
class Abs: # type: ignore
    val: str
    expr: Terme

@dataclass
class Abs:
    val: str
    expr: Terme

@dataclass
class Macro:
    nom: str
    expr: Terme



Terme = Var | Apl | Abs 


class TreeVisitor(lcVisitor):

    def visitRoot(self, ctx):
        [expr] = list(ctx.getChildren())
        return self.visit(expr)
    
    def visitParentesi(self, ctx):
        [p1, expr, p2] = list(ctx.getChildren())
        return self.visit(expr)
    
    def visitAbstraccio(self, ctx):
        [sym, expr1, point, expr2] = list(ctx.getChildren())
        res2 = self.visit(expr2)
        res1 = expr1.getText()
        while len(res1) != 1:
            lastChar = expr1.getText()[-1]
            res2 = Abs(lastChar,res2)
            res1 = res1[:-1]
        return Abs(res1,res2)
    
    def visitAplicacio(self, ctx):
        [expr1, expr2] = list(ctx.getChildren())
        return Apl(self.visit(expr1), self.visit(expr2))
    
    def visitLletra(self, ctx):
        [lletra] = list(ctx.getChildren())
        return Var(lletra.getText())
    
    def visitMacro(self, ctx):
        [nom,inutil,expr] = list(ctx.getChildren())
        res = self.visit(expr)
        return Macro(nom.getText(),res)
    
    def visitMacroI(self, ctx):
        [nom,inutil,expr] = list(ctx.getChildren())
        res = self.visit(expr)
        return Macro(nom.getText(),res)

    def visitMacroFormula(self, ctx):
        [nom] = list(ctx.getChildren())
        [macro] = [obj for obj in MACROS if obj.nom == nom.getText()]
        return macro.expr
    
    def visitMacroIFormula(self, ctx):
        [expr1, op, expr2] = list(ctx.getChildren())
        [op] = [obj for obj in MACROS if obj.nom == op.getText()]
        return Apl(Apl(op.expr,self.visit(expr1)),self.visit(expr2))
    





def printTree(t):
    # print(t)      # descomentar per fer proves
    match t:
        case Var(x):
            return x
        case Apl(x, y):
            return ("(" + printTree(x) + printTree(y) + ")")  
        case Abs(x, y):
            return "(λ" + x + "." + printTree(y) + ")" 
        case Macro(x,y):
            return  x + ' ≡ ' + printTree(y)
        case _:
            return (printTree(t.expr))



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
                return Abs(x,y)
            else:
                return Abs(x,beta(cap,y,t2))
    

# retorna una llista  amb tots els valors lliures de la expressio
def freeValues(t):
    match t:
        case Var(x):
            return set([x])
        case Apl(x, y):
            return freeValues(x).union(freeValues(y))
        case Abs(x, y):
            return freeValues(y) - set([x])

def boundValues(t):
    match t:
        case Var(x):
            return set([])
        case Apl(x, y):
            return boundValues(x).union(boundValues(y))
        case Abs(x, y):
            return boundValues(y).union(set([x]))
        


def change(z,n2c,s):
    match z:
        case Var(x):
            if (x in n2c):
                return Var(s[n2c.index(x)])
            else:
                return Var(x)
        case Apl(x,y):
            return Apl(change(x,n2c,s),change(y,n2c,s))
        case Abs(x,y):
            if x in n2c:
                return Abs(s[n2c.index(x)],change(y,n2c,s))
            else:
                return Abs(x,change(y,n2c,s))
        



def alfa(z,t2):
    have2change = freeValues(t2) # lliures de la dreta
    zfrees = freeValues(z) # lliures de l'esquerra
    boundValuesFirst = boundValues(z) # lligades de l'esquerra
    need2change = list(set(have2change).intersection(boundValuesFirst)) # llista amb les lletres que es volen canviar

    
    substitution = set(''.join(random.choices(string.ascii_lowercase, k = len(need2change)))) # llista amb les lletres que substituiran les que es volen canviar
    # creen una nova llista amb les lletres que no es repeteixen i que no estan a la llista de lletres que es volen canviar ni a la llista de lletres que es volen substituir
    # per cert les condicions del while comproven que la llista de substitucio no te cap carcater que coincideixi amb un dels que ja hi ha a l'expressio o que coincideixi amb un dels que es volen substituir
    while (set(substitution).intersection(need2change) or set(substitution).intersection(zfrees)): # type: ignore
        substitution = list(''.join(random.choices(string.ascii_lowercase, k = len(need2change))))

    # print(need2change)
    for x in need2change:
        print('α-conversió: ' + x + ' → ' + list(substitution)[need2change.index(x)])

    z1 = change(z,need2change,list(substitution)) # type: ignore
    if (z != z1):
        print(printTree(z) + ' → ' + printTree(z1))
    return z1
    


def avaluacio(t):
    match t:
        case Var(x):
            return Var(x)
        case Apl(x, y):
            match x:                        
                case Abs(a,b):   # cas de la beta reduccio
                    # comprovem que no s'hagi de fer cap alfa conversio abans de la beta reduccio
                    x1 = alfa(x,y)
                    print('β-reducció: ')
                    return beta(x1.val,x1.expr,y)                    # type: ignore
                case _:
                    return Apl(avaluacio(x),avaluacio(y))
        case Abs(x, y):
            return Abs(x,avaluacio(y))
        

MACROS = []        
while True:
    input_stream = InputStream(input('? '))
    lexer = lcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lcParser(token_stream)
    tree = parser.root()
    

    if parser.getNumberOfSyntaxErrors() == 0:
        visitor = TreeVisitor()
        t = visitor.visit(tree)
        match t:
            case Macro(x,y):
                MACROS.append(t)
                for x in MACROS:
                    print(printTree(x))
            case _:
                print('Arbre:')
                print(printTree(t))
                step = 0
                while step < 20:
                    t1 = avaluacio(t)
                    if t1 != t:
                        print(printTree(t) + ' → ' + printTree(t1))
                    else:
                        break
                    t = t1
                    step += 1
                #### printem resultat
                print('Resultat:')
                if step == 20:
                    print('Nothing')
                else:
                    print(printTree(t))
        

    else:
        print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
        print(tree.toStringTree(recog=parser))
