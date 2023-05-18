# Generated from lambda.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lambdaParser import lambdaParser
else:
    from lambdaParser import lambdaParser

# This class defines a complete generic visitor for a parse tree produced by lambdaParser.

class lambdaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lambdaParser#root.
    def visitRoot(self, ctx:lambdaParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#lletra.
    def visitLletra(self, ctx:lambdaParser.LletraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#parentesi.
    def visitParentesi(self, ctx:lambdaParser.ParentesiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#abstraccio.
    def visitAbstraccio(self, ctx:lambdaParser.AbstraccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#aplicacio.
    def visitAplicacio(self, ctx:lambdaParser.AplicacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#cap.
    def visitCap(self, ctx:lambdaParser.CapContext):
        return self.visitChildren(ctx)



del lambdaParser