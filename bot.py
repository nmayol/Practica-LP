from __future__ import annotations
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

######### CODI INTERPRET #########

import random
import string
from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from dataclasses import dataclass
from lcVisitor import lcVisitor
import pydot


######### VARIABLES GLOBALS #########

MACROS = []         # llista de macros

# TASCA 7:
i = 0               # index de nodes del graf per fer la imatge
graf = """digraph arbre {
    bgcolor="white";
    """            # graf base que es passarà a Graphviz per fer la imatge


######### CODI DEL VISITOR #########
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
        print(MACROS)
        [op] = [obj for obj in MACROS if obj.nom == op.getText()]
        return Apl(Apl(op.expr,self.visit(expr1)),self.visit(expr2))
    

######### CODI PER IMPRIMIR L'ARBRE #########

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




######### CODI PER FER L'ALFA-CONVERSIÓ #########    

# retorna una llista  amb tots els valors lliures de la expressio
def freeValues(t):
    match t:
        case Var(x):
            return set([x])
        case Apl(x, y):
            return freeValues(x).union(freeValues(y))
        case Abs(x, y):
            return freeValues(y) - set([x])

# retorna una llista amb tots els valors lligats de la expressio
def boundValues(t):
    match t:
        case Var(x):
            return set([])
        case Apl(x, y):
            return boundValues(x).union(boundValues(y))
        case Abs(x, y):
            return boundValues(y).union(set([x]))
        

# fa tots els canvis necessaris per l'alfa-conversio
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
        

# funcio base per fer l'alfa-conversio: examina quines variables ha de canviar i crida una altra funció per fer els canvis
def alfa(z,t2):
    have2change = freeValues(t2)
    zfrees = freeValues(z)
    boundValuesFirst = boundValues(z)
    need2change = list(set(have2change).intersection(boundValuesFirst)) # llista amb les lletres que es volen canviar
    
    substitution = set(''.join(random.choices(string.ascii_lowercase, k = len(need2change)))) # llista amb les lletres que substituiran les que es volen canviar
    # creen una nova llista amb les lletres que no es repeteixen i que no estan a la llista de lletres que es volen canviar ni a la llista de lletres que es volen substituir
    # per cert les condicions del while comproven que la llista de substitucio no te cap carcater que coincideixi amb un dels que ja hi ha a l'expressio o que coincideixi amb un dels que es volen substituir
    while (set(substitution).intersection(need2change) or set(substitution).intersection(zfrees)): # type: ignore
        substitution = list(''.join(random.choices(string.ascii_lowercase, k = len(need2change))))

    for x in need2change:
        print('α-conversió: ' + x + ' → ' + list(substitution)[need2change.index(x)])

    z1 = change(z,need2change,list(substitution)) # type: ignore
    if (z != z1):
        print(printTree(z) + ' → ' + printTree(z1))
    return z1
    

######### CODI PER FER LA BETA-REDUCCIÓ #########
# Funcio que fa les beta-reduccions
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


######### CODI PER FER L'AVALUACIÓ (ALFA-REDUCCIONS I BETA-REDUCCIONS) #########
# Funcio base d'avaluacio, des d'aqui es criden les alfa conversio i les beta reduccions
def avaluacio(t):
    print(t)
    match t:
        case Var(x):
            return ['β',Var(x)]
        case Apl(x, y):
            match x:                        
                case Abs(a,b):   # cas de la beta reduccio
                    # comprovem que no s'hagi de fer cap alfa conversio abans de la beta reduccio
                    x1 = alfa(x,y)
                    if x != x1:
                        return ['α',Apl(x1,y)] # type: ignore
                    else:
                        return ['β',beta(x1.val,x1.expr,y)]                    # type: ignore
                case _:
                    [lletra,a] = avaluacio(x)
                    [lletra,b] = avaluacio(y) 
                    return [lletra, Apl(a,b)]
        case Abs(x, y):
            [lletra,a] = avaluacio(y)
            return [lletra, Abs(x,a)]
        


##################  TRACTAT DEL GRAF (TASCA 7) ###################

# afegeix un node al graf
def afegeixNode(text):
    global graf
    global i
    graf = graf + ('    ' + str(i) + ' [label="' + text + '", shape=none ];\n') # type: ignore

# afegeix una aresta al graf
def afegeixAresta(n1,n2):
    global graf
    global i
    graf = graf + ('    ' + str(n1) + ' -> ' + str(n2) + ';\n') # type: ignore

# afegeix una aresta discontinua al graf (variable lligada)
def afegeixArestaLligada(n1,n2):
    global graf
    global i
    graf = graf + ('    ' + str(n1) + ' -> ' + str(n2) + '[style = "dashed"];\n') # type: ignore

# funcio que agafa l'arbre i en rotarna un String interpretable per graphViz (per que sigui totalment interpretable cal afegir un '}' al final del String, cosa que es fa a la linia 300)
def graphString(t,l):
    global i
    match t:
        case Var(x):
            if x in l:
                afegeixArestaLligada(i,l[x])
            afegeixNode(x)
        case Apl(x, y):
            afegeixNode('@')
            afegeixAresta(i,i+1)
            j = i
            i += 1
            graphString(x,l)
            afegeixAresta(j,i+1)
            i += 1
            graphString(y,l)

        case Abs(x, y):
            j = -1
            if x in l:
                j = l[x]
            l[x] = i
            afegeixNode('&#955;'+x)
            afegeixAresta(i,i+1)
            i+=1
            graphString(y,l)
            if j != -1:
                l[x] = j
            else:
                del l[x]
   

# funcio que agafa l'arbre i crea la imatge del graf, la imatge es guarda a output.png
def montaGraf(t):
    global graf
    global i
    
    i = 0
    graf = """digraph arbre {
    bgcolor="white";
    
    """
    lligades = dict()
    graphString(t,lligades)
    print(graf)
    graphs = pydot.graph_from_dot_data(graf+ '}') # type: ignore
    graph = graphs[0]
    graph.write_png("output.png")
    
#######################################################################################################




########################################## TELEGRAM ########################################## 


# emoji d'una granota
granota = "🐸"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# funcio que s'executa quan es rep un missatge (que no sigui una comanda)
async def text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input_stream = InputStream(update.message.text)
    lexer = lcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lcParser(token_stream)
    tree = parser.root()
    visitor = TreeVisitor()
    t = visitor.visit(tree)

    match t:
        case Macro(x,y):
            MACROS.append(t)     
        case _:
            await context.bot.send_message(chat_id=update.effective_chat.id, text= 'Arbre:\n' + printTree(t))
            montaGraf(t)
            await context.bot.send_photo(chat_id=update.message.chat_id, photo=open('output.png', 'rb'))
            [lletra,t1] = avaluacio(t)
            while t != t1:
                await context.bot.send_message(chat_id=update.effective_chat.id, text= printTree(t) + ' → ' + lletra + ' → ' + printTree(t1))
                t = t1
                [lletra, t1] = avaluacio(t)
            await context.bot.send_message(chat_id=update.effective_chat.id, text= printTree(t))
            montaGraf(t)
            await context.bot.send_photo(chat_id=update.message.chat_id, photo=open('output.png', 'rb'))


# funcio que s'executa quan es rep la comanda /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "Salutacions, devots seguidors. Sóc Harold, la Granota del Lambda Càlcul " + granota + ", portador de la veritat absoluta. Seguiu-me en aquest camí celestial. /help revelarà el coneixement sagrat.\n"
    msg1 = update.message.from_user.first_name + ", que la llum de les lambda-regles us il·lumini."
    global MACROS
    MACROS = [] 
    await context.bot.send_message(chat_id=update.effective_chat.id, text= msg)
    await context.bot.send_message(chat_id=update.effective_chat.id, text= msg1)

# funcio que s'executa quan es rep la comanda /help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "/start\n/author\n/help\n/macros\nExpressió λ-càlcul"
    await context.bot.send_message(chat_id=update.effective_chat.id, text= msg)

# funcio que s'executa quan es rep la comanda /author
async def author(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "Salutacions, sóc Harold " + granota + ",  la Granota Suprema del Lambda Càlcul. La meva saviesa sublim il·luminarà les vostres ments opaques. Seguiu-me i abraceu la veritat absoluta del poder del càlcul diví.\n"
    msg1 = "Realment em dic Neus Mayol (Grup 12), però això no és important."
    await context.bot.send_message(chat_id=update.effective_chat.id, text= msg)
    await context.bot.send_photo(chat_id=update.message.chat_id, \
         photo='https://i.redd.it/' + \
         'q72plc416o851.jpg')
    await context.bot.send_message(chat_id=update.effective_chat.id, text= msg1)

# funcio que s'executa quan es rep la comanda /macros
async def macros(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = ''
    for x in MACROS:
        msg += (x.nom + ' ≡ ' + printTree(x.expr) + '\n')
    await context.bot.send_message(chat_id=update.effective_chat.id, text= msg)
    

# codi main del bot
if __name__ == '__main__':
    application = ApplicationBuilder().token(open("token.txt", "r").read()).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    author_handler = CommandHandler('author', author)
    application.add_handler(author_handler)
    
    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)

    macros_handler = CommandHandler('macros', macros)
    application.add_handler(macros_handler)

    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, text)
    application.add_handler(text_handler)
    
    application.run_polling()

#######################################################################################################