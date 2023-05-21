# Generated from lc.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser

# This class defines a complete generic visitor for a parse tree produced by lcParser.

class lcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lcParser#root.
    def visitRoot(self, ctx:lcParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#macro.
    def visitMacro(self, ctx:lcParser.MacroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#lletra.
    def visitLletra(self, ctx:lcParser.LletraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#parentesi.
    def visitParentesi(self, ctx:lcParser.ParentesiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#abstraccio.
    def visitAbstraccio(self, ctx:lcParser.AbstraccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#aplicacio.
    def visitAplicacio(self, ctx:lcParser.AplicacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#cap.
    def visitCap(self, ctx:lcParser.CapContext):
        return self.visitChildren(ctx)



del lcParser