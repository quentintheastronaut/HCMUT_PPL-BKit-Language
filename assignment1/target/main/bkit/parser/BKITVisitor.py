# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_decl.
    def visitVar_decl(self, ctx:BKITParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#declaration.
    def visitDeclaration(self, ctx:BKITParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#value_decl.
    def visitValue_decl(self, ctx:BKITParser.Value_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#postfix_array_exp_for_decl.
    def visitPostfix_array_exp_for_decl(self, ctx:BKITParser.Postfix_array_exp_for_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#postfix_array_exp_for_call.
    def visitPostfix_array_exp_for_call(self, ctx:BKITParser.Postfix_array_exp_for_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_assignment.
    def visitArray_assignment(self, ctx:BKITParser.Array_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_decl.
    def visitArray_decl(self, ctx:BKITParser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_nd_decl.
    def visitArray_nd_decl(self, ctx:BKITParser.Array_nd_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_1d_decl.
    def visitArray_1d_decl(self, ctx:BKITParser.Array_1d_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_decl.
    def visitFunc_decl(self, ctx:BKITParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param.
    def visitParam(self, ctx:BKITParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body.
    def visitBody(self, ctx:BKITParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_call.
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arguement.
    def visitArguement(self, ctx:BKITParser.ArguementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_of_float.
    def visitInt_of_float(self, ctx:BKITParser.Int_of_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_of_int.
    def visitFloat_of_int(self, ctx:BKITParser.Float_of_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_of_string.
    def visitInt_of_string(self, ctx:BKITParser.Int_of_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#string_of_int.
    def visitString_of_int(self, ctx:BKITParser.String_of_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_of_string.
    def visitFloat_of_string(self, ctx:BKITParser.Float_of_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#string_of_float.
    def visitString_of_float(self, ctx:BKITParser.String_of_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_of_string.
    def visitBool_of_string(self, ctx:BKITParser.Bool_of_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#string_of_bool.
    def visitString_of_bool(self, ctx:BKITParser.String_of_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement_list.
    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignment_statement.
    def visitAssignment_statement(self, ctx:BKITParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arithmetic.
    def visitArithmetic(self, ctx:BKITParser.ArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr.
    def visitExpr(self, ctx:BKITParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr1.
    def visitExpr1(self, ctx:BKITParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr2.
    def visitExpr2(self, ctx:BKITParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr3.
    def visitExpr3(self, ctx:BKITParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr4.
    def visitExpr4(self, ctx:BKITParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr_cond.
    def visitExpr_cond(self, ctx:BKITParser.Expr_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_statement.
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elseif_stmt.
    def visitElseif_stmt(self, ctx:BKITParser.Elseif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_stmt.
    def visitElse_stmt(self, ctx:BKITParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_statement.
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_statement.
    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_statement.
    def visitDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_statement.
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_statement.
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_statement.
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#println.
    def visitPrintln(self, ctx:BKITParser.PrintlnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#printstr.
    def visitPrintstr(self, ctx:BKITParser.PrintstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#printstrln.
    def visitPrintstrln(self, ctx:BKITParser.PrintstrlnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#read.
    def visitRead(self, ctx:BKITParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literals.
    def visitLiterals(self, ctx:BKITParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_lit.
    def visitBool_lit(self, ctx:BKITParser.Bool_litContext):
        return self.visitChildren(ctx)



del BKITParser