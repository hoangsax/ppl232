# Generated from c:/Users/hoang/Desktop/New folder (2)/ppl232/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#main.
    def enterMain(self, ctx:ZCodeParser.MainContext):
        pass

    # Exit a parse tree produced by ZCodeParser#main.
    def exitMain(self, ctx:ZCodeParser.MainContext):
        pass


    # Enter a parse tree produced by ZCodeParser#other.
    def enterOther(self, ctx:ZCodeParser.OtherContext):
        pass

    # Exit a parse tree produced by ZCodeParser#other.
    def exitOther(self, ctx:ZCodeParser.OtherContext):
        pass


    # Enter a parse tree produced by ZCodeParser#mainblock.
    def enterMainblock(self, ctx:ZCodeParser.MainblockContext):
        pass

    # Exit a parse tree produced by ZCodeParser#mainblock.
    def exitMainblock(self, ctx:ZCodeParser.MainblockContext):
        pass


    # Enter a parse tree produced by ZCodeParser#valdecl.
    def enterValdecl(self, ctx:ZCodeParser.ValdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#valdecl.
    def exitValdecl(self, ctx:ZCodeParser.ValdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#mainfunc.
    def enterMainfunc(self, ctx:ZCodeParser.MainfuncContext):
        pass

    # Exit a parse tree produced by ZCodeParser#mainfunc.
    def exitMainfunc(self, ctx:ZCodeParser.MainfuncContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcdecl.
    def enterFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcdecl.
    def exitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcblock.
    def enterFuncblock(self, ctx:ZCodeParser.FuncblockContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcblock.
    def exitFuncblock(self, ctx:ZCodeParser.FuncblockContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmts.
    def enterStmts(self, ctx:ZCodeParser.StmtsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmts.
    def exitStmts(self, ctx:ZCodeParser.StmtsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt.
    def enterStmt(self, ctx:ZCodeParser.StmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt.
    def exitStmt(self, ctx:ZCodeParser.StmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmtblock.
    def enterStmtblock(self, ctx:ZCodeParser.StmtblockContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmtblock.
    def exitStmtblock(self, ctx:ZCodeParser.StmtblockContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignstmt.
    def enterAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignstmt.
    def exitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ifstmt.
    def enterIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ifstmt.
    def exitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ifblock.
    def enterIfblock(self, ctx:ZCodeParser.IfblockContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ifblock.
    def exitIfblock(self, ctx:ZCodeParser.IfblockContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elseblk.
    def enterElseblk(self, ctx:ZCodeParser.ElseblkContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elseblk.
    def exitElseblk(self, ctx:ZCodeParser.ElseblkContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elifblk.
    def enterElifblk(self, ctx:ZCodeParser.ElifblkContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elifblk.
    def exitElifblk(self, ctx:ZCodeParser.ElifblkContext):
        pass


    # Enter a parse tree produced by ZCodeParser#forstmt.
    def enterForstmt(self, ctx:ZCodeParser.ForstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#forstmt.
    def exitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#loopblock.
    def enterLoopblock(self, ctx:ZCodeParser.LoopblockContext):
        pass

    # Exit a parse tree produced by ZCodeParser#loopblock.
    def exitLoopblock(self, ctx:ZCodeParser.LoopblockContext):
        pass


    # Enter a parse tree produced by ZCodeParser#loopkey.
    def enterLoopkey(self, ctx:ZCodeParser.LoopkeyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#loopkey.
    def exitLoopkey(self, ctx:ZCodeParser.LoopkeyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array.
    def enterArray(self, ctx:ZCodeParser.ArrayContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array.
    def exitArray(self, ctx:ZCodeParser.ArrayContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcall.
    def enterFuncall(self, ctx:ZCodeParser.FuncallContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcall.
    def exitFuncall(self, ctx:ZCodeParser.FuncallContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramcall.
    def enterParamcall(self, ctx:ZCodeParser.ParamcallContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramcall.
    def exitParamcall(self, ctx:ZCodeParser.ParamcallContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramlist.
    def enterParamlist(self, ctx:ZCodeParser.ParamlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramlist.
    def exitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#params.
    def enterParams(self, ctx:ZCodeParser.ParamsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#params.
    def exitParams(self, ctx:ZCodeParser.ParamsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#exp.
    def enterExp(self, ctx:ZCodeParser.ExpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#exp.
    def exitExp(self, ctx:ZCodeParser.ExpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#exp_01.
    def enterExp_01(self, ctx:ZCodeParser.Exp_01Context):
        pass

    # Exit a parse tree produced by ZCodeParser#exp_01.
    def exitExp_01(self, ctx:ZCodeParser.Exp_01Context):
        pass


    # Enter a parse tree produced by ZCodeParser#exp_00.
    def enterExp_00(self, ctx:ZCodeParser.Exp_00Context):
        pass

    # Exit a parse tree produced by ZCodeParser#exp_00.
    def exitExp_00(self, ctx:ZCodeParser.Exp_00Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expall.
    def enterExpall(self, ctx:ZCodeParser.ExpallContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expall.
    def exitExpall(self, ctx:ZCodeParser.ExpallContext):
        pass


    # Enter a parse tree produced by ZCodeParser#indexp.
    def enterIndexp(self, ctx:ZCodeParser.IndexpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#indexp.
    def exitIndexp(self, ctx:ZCodeParser.IndexpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#indop.
    def enterIndop(self, ctx:ZCodeParser.IndopContext):
        pass

    # Exit a parse tree produced by ZCodeParser#indop.
    def exitIndop(self, ctx:ZCodeParser.IndopContext):
        pass


    # Enter a parse tree produced by ZCodeParser#indop_1.
    def enterIndop_1(self, ctx:ZCodeParser.Indop_1Context):
        pass

    # Exit a parse tree produced by ZCodeParser#indop_1.
    def exitIndop_1(self, ctx:ZCodeParser.Indop_1Context):
        pass


    # Enter a parse tree produced by ZCodeParser#ariexp.
    def enterAriexp(self, ctx:ZCodeParser.AriexpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ariexp.
    def exitAriexp(self, ctx:ZCodeParser.AriexpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ariexp_00.
    def enterAriexp_00(self, ctx:ZCodeParser.Ariexp_00Context):
        pass

    # Exit a parse tree produced by ZCodeParser#ariexp_00.
    def exitAriexp_00(self, ctx:ZCodeParser.Ariexp_00Context):
        pass


    # Enter a parse tree produced by ZCodeParser#logicexp.
    def enterLogicexp(self, ctx:ZCodeParser.LogicexpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#logicexp.
    def exitLogicexp(self, ctx:ZCodeParser.LogicexpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#logicexp_00.
    def enterLogicexp_00(self, ctx:ZCodeParser.Logicexp_00Context):
        pass

    # Exit a parse tree produced by ZCodeParser#logicexp_00.
    def exitLogicexp_00(self, ctx:ZCodeParser.Logicexp_00Context):
        pass


    # Enter a parse tree produced by ZCodeParser#relatexp.
    def enterRelatexp(self, ctx:ZCodeParser.RelatexpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#relatexp.
    def exitRelatexp(self, ctx:ZCodeParser.RelatexpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#relatexp_00.
    def enterRelatexp_00(self, ctx:ZCodeParser.Relatexp_00Context):
        pass

    # Exit a parse tree produced by ZCodeParser#relatexp_00.
    def exitRelatexp_00(self, ctx:ZCodeParser.Relatexp_00Context):
        pass


    # Enter a parse tree produced by ZCodeParser#relatexp_01.
    def enterRelatexp_01(self, ctx:ZCodeParser.Relatexp_01Context):
        pass

    # Exit a parse tree produced by ZCodeParser#relatexp_01.
    def exitRelatexp_01(self, ctx:ZCodeParser.Relatexp_01Context):
        pass



del ZCodeParser