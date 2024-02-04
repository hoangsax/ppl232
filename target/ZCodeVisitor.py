# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#other.
    def visitOther(self, ctx:ZCodeParser.OtherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl.
    def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#mainfunc.
    def visitMainfunc(self, ctx:ZCodeParser.MainfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcdecl.
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcproto.
    def visitFuncproto(self, ctx:ZCodeParser.FuncprotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcblock.
    def visitFuncblock(self, ctx:ZCodeParser.FuncblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#restmt.
    def visitRestmt(self, ctx:ZCodeParser.RestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_00.
    def visitStmt_00(self, ctx:ZCodeParser.Stmt_00Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtlist.
    def visitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignstmt.
    def visitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifstmt.
    def visitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifblock.
    def visitIfblock(self, ctx:ZCodeParser.IfblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elseblk.
    def visitElseblk(self, ctx:ZCodeParser.ElseblkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifblk.
    def visitElifblk(self, ctx:ZCodeParser.ElifblkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifblk_0.
    def visitElifblk_0(self, ctx:ZCodeParser.Elifblk_0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forstmt.
    def visitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#loopblock.
    def visitLoopblock(self, ctx:ZCodeParser.LoopblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#loopkey.
    def visitLoopkey(self, ctx:ZCodeParser.LoopkeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcall.
    def visitFuncall(self, ctx:ZCodeParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramcall.
    def visitParamcall(self, ctx:ZCodeParser.ParamcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramlist.
    def visitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#params.
    def visitParams(self, ctx:ZCodeParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#allexp.
    def visitAllexp(self, ctx:ZCodeParser.AllexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp.
    def visitExp(self, ctx:ZCodeParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp_01.
    def visitExp_01(self, ctx:ZCodeParser.Exp_01Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp_00.
    def visitExp_00(self, ctx:ZCodeParser.Exp_00Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expall.
    def visitExpall(self, ctx:ZCodeParser.ExpallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array.
    def visitArray(self, ctx:ZCodeParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#explist.
    def visitExplist(self, ctx:ZCodeParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#explist_1.
    def visitExplist_1(self, ctx:ZCodeParser.Explist_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#explist_2.
    def visitExplist_2(self, ctx:ZCodeParser.Explist_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#explist_3.
    def visitExplist_3(self, ctx:ZCodeParser.Explist_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexp.
    def visitIndexp(self, ctx:ZCodeParser.IndexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indop.
    def visitIndop(self, ctx:ZCodeParser.IndopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indop_0.
    def visitIndop_0(self, ctx:ZCodeParser.Indop_0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indop_1.
    def visitIndop_1(self, ctx:ZCodeParser.Indop_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ariexp.
    def visitAriexp(self, ctx:ZCodeParser.AriexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ariexp_00.
    def visitAriexp_00(self, ctx:ZCodeParser.Ariexp_00Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relatexp.
    def visitRelatexp(self, ctx:ZCodeParser.RelatexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relatexp_00.
    def visitRelatexp_00(self, ctx:ZCodeParser.Relatexp_00Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relatexp_01.
    def visitRelatexp_01(self, ctx:ZCodeParser.Relatexp_01Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logicexp.
    def visitLogicexp(self, ctx:ZCodeParser.LogicexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logicexp_00.
    def visitLogicexp_00(self, ctx:ZCodeParser.Logicexp_00Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stringexp.
    def visitStringexp(self, ctx:ZCodeParser.StringexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stringexp_00.
    def visitStringexp_00(self, ctx:ZCodeParser.Stringexp_00Context):
        return self.visitChildren(ctx)



del ZCodeParser