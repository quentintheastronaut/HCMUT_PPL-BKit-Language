

from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from functools import reduce
from AST import *

def matchTuple(_exp, _stmt):
    (var,stmt) = _stmt
    return (_exp,var,stmt)

class ASTGeneration(BKITVisitor):

    
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        var_decl = reduce(lambda x,y: x + self.visitVar_decl(y), ctx.var_decl(), [])
        func_decl = list(map(lambda x: self.visitFunc_decl(x), ctx.func_decl()))
        return Program(var_decl + func_decl)
    
    def visitVar_decl(self, ctx: BKITParser.Var_declContext):
        return [self.visitDeclaration(x) for x in ctx.declaration()]

    def visitDeclaration(self, ctx: BKITParser.DeclarationContext):
        if ctx.value_decl(): return self.visit(ctx.value_decl())
        if ctx.array_decl(): return self.visit(ctx.array_decl())

    
    def visitValue_decl(self, ctx: BKITParser.Var_declContext):
        return VarDecl(Id(ctx.ID().getText()), [], self.visit(ctx.expr()) if ctx.expr() else None)

    def visitExpr(self, ctx: BKITParser.ExprContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr_cond())
        left = self.visit(ctx.expr())
        right = self.visit(ctx.expr_cond())
        op = ctx.getChild(1).getText()
        return BinaryOp(op,left,right)

    def visitExpr1(self, ctx: BKITParser.Expr1Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr2())
        left = self.visit(ctx.expr1())
        right = self.visit(ctx.expr2())
        op = ctx.getChild(1).getText()
        return BinaryOp(op,left,right)

    def visitExpr2(self, ctx: BKITParser.Expr2Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr3())
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        op = ctx.getChild(1).getText()
        return BinaryOp(op,left,right)

    def visitExpr3(self, ctx: BKITParser.Expr3Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr4())
        body = self.visit(ctx.expr4())
        op = ctx.getChild(0).getText()
        return UnaryOp(op,body)

    def visitExpr4(self, ctx: BKITParser.Expr4Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.operand())
        body = self.visit(ctx.operand())
        op = ctx.getChild(0).getText()
        return UnaryOp(op,body)

    def visitOperand(self, ctx: BKITParser.OperandContext):
        if ctx.ID():
            if ctx.expr():
                return ArrayCell(Id(ctx.ID().getText()),[self.visitExpr(x) for x in ctx.expr()] if ctx.expr() else [])
            else :
                return Id(ctx.ID().getText())
        if ctx.literals(): return self.visit(ctx.literals())
        if ctx.func_call(): return self.visit(ctx.func_call())
        if ctx.LP(): 
            return self.visit(ctx.expr(0))
        

    def visitLiterals(self, ctx: BKITParser.LiteralsContext):
        if ctx.intlit(): return self.visit(ctx.intlit())
        elif ctx.REAL(): return FloatLiteral(float(ctx.REAL().getText()))
        elif ctx.STRINGLIT(): return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.array_lit(): return ArrayLiteral(self.visit(ctx.array_lit()))
        elif ctx.bool_lit(): return self.visitChildren(ctx)

    def visitIntlit(self, ctx: BKITParser.IntlitContext):
        if ctx.DECIMAL(): return IntLiteral(int(ctx.DECIMAL().getText()))
        if ctx.HEXADECIMAL(): return IntLiteral(int(ctx.HEXADECIMAL().getText(),16))
        if ctx.OCTAL(): return IntLiteral(int(ctx.OCTAL().getText(),8))

    def visitArray_lit(self, ctx: BKITParser.Array_litContext):
        if ctx.array1dlit(): return self.visit(ctx.array1dlit())
        if ctx.arrayndlit(): return self.visit(ctx.arrayndlit())

    def visitArray1dlit(self, ctx: BKITParser.Array1dlitContext):
        return [self.visitLiterals(x) for x in ctx.literals()]

    def visitArrayndlit(self, ctx: BKITParser.ArrayndlitContext):
        return [self.visitLiterals(x) for x in ctx.literals()]

    def visitBool_lit(self, ctx: BKITParser.Bool_litContext):
        if ctx.TRUE(): return BooleanLiteral(ctx.TRUE().getText())
        else: return BooleanLiteral(ctx.FALSE().getText())

    # array_decl
    def visitArray_decl(self, ctx: BKITParser.Array_declContext):
        return self.visitChildren(ctx)

    def visitArray_1d_decl(self, ctx: BKITParser.Array_1d_declContext):
        dimen = [self.visitIndex(ctx.index())] if ctx.index() else []
        return VarDecl(Id(str(ctx.ID().getText())), dimen, self.visit(ctx.array_assignment()) )

    def visitArray_assignment(self, ctx: BKITParser.Array_assignmentContext):
        if ctx.array_lit(): return ArrayLiteral(self.visit(ctx.array_lit()))

    def visitArray_nd_decl(self, ctx: BKITParser.Array_nd_declContext):
        dimen = [self.visitIndex(x) for x in ctx.index()] if ctx.index() else []
        return VarDecl(Id(str(ctx.ID().getText())), dimen, self.visit(ctx.array_assignment()) )

    def visitIndex(self, ctx: BKITParser.IndexContext):
        if ctx.intlit():
            return self.visit(ctx.intlit())
        else :
            return self.visit(ctx.expr())

    def visitFunc_decl(self, ctx: BKITParser.Func_declContext):
        id = Id(ctx.ID().getText())
        param = self.visit(ctx.param()) if ctx.param() else []
        var_decl = reduce(lambda x,y: x + self.visitVar_decl(y), ctx.var_decl(), [])
        array_decl= reduce(lambda x,y: x + self.visitArray_decl(y), ctx.array_decl(), [])
        stmt = [self.visitStatement(x) for x in ctx.statement()]
        returnStmt = self.visit(ctx.return_statement()) if ctx.return_statement() else []
        return FuncDecl(id,param,(var_decl+array_decl,stmt+returnStmt))

    def visitParam(self, ctx: BKITParser.ParamContext):
        paramlist = []
        for i in ctx.ID():
            paramlist.append(VarDecl(Id(str(i.getText())), [],None))
        return paramlist

    def visitBody(self, ctx: BKITParser.BodyContext):
        return self.visitChildren(ctx)

    def visitAssignment_statement(self, ctx: BKITParser.Assignment_statementContext):
        if ctx.index(): 
            id = Id(ctx.ID().getText())
            dimen = [self.visitIndex(x) for x in ctx.index()] if ctx.index() else []
            return Assign(ArrayCell(id,dimen),self.visit(ctx.expr()))
        else :
            return Assign(Id(ctx.ID().getText()) , self.visit(ctx.expr()))

    def visitExpr_cond(self, ctx: BKITParser.Expr_condContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr1())
        left = self.visit(ctx.expr_cond())
        right = self.visit(ctx.expr1())
        op = ctx.getChild(1).getText()
        return BinaryOp(op,left,right)


    def visitIf_statement(self, ctx: BKITParser.If_statementContext):
        ifStmt = self.visit(ctx.if_stmt())
        elseifStmt = reduce(lambda x,y: x + self.visitElseif_stmt(y), ctx.elseif_stmt(), [])
        elseStmt = self.visit(ctx.else_stmt()) if ctx.else_stmt() else ()
        return If(ifStmt + elseifStmt  ,elseStmt)


    def visitIf_stmt(self, ctx: BKITParser.If_stmtContext):
        expr = self.visit(ctx.expr())
        var_decl = reduce(lambda x,y: x + self.visitVar_decl(y), ctx.var_decl(), [])
        
        stmt = [self.visit(x) for x in ctx.statement()]
        returnStmt = self.visit(ctx.return_statement()) if ctx.return_statement() else []
        return [( expr, var_decl, stmt + returnStmt)]
        

    def visitElseif_stmt(self, ctx: BKITParser.If_stmtContext):
        expr = self.visit(ctx.expr())
        var_decl = reduce(lambda x,y: x + self.visitVar_decl(y), ctx.var_decl(), [])
        
        stmt = [self.visit(x) for x in ctx.statement()]
        returnStmt = self.visit(ctx.return_statement()) if ctx.return_statement() else []
        return [( expr, var_decl, stmt + returnStmt)]

    def visitElse_stmt(self, ctx: BKITParser.If_stmtContext):
        var_decl = reduce(lambda x,y: x + self.visitVar_decl(y), ctx.var_decl(), [])
        array_decl= reduce(lambda x,y: x + [self.visitArray_decl(y)], ctx.array_decl(), [])
        stmt = [self.visit(x) for x in ctx.statement()]
       
        returnStmt = self.visit(ctx.return_statement()) if ctx.return_statement() else []
        return (var_decl , stmt + returnStmt )

    def visitReturn_statement(self, ctx: BKITParser.Return_statementContext):
        if ctx.expr(): return [Return(self.visit(ctx.expr()))]
        
    def visitStatement(self, ctx: BKITParser.StatementContext):
        if ctx.assignment_statement(): return self.visit(ctx.assignment_statement())
        elif ctx.func_call(): return self.visit(ctx.func_call())
        else:
            return self.visitChildren(ctx)

    def visitContinue_statement(self, ctx: BKITParser.Continue_statementContext):
        return Continue()

    def visitBreak_statement(self, ctx: BKITParser.Break_statementContext):
        return Break()

    def visitFunc_call(self, ctx: BKITParser.Func_callContext):
        iden = Id(ctx.ID().getText())
        expr = [self.visit(x) for x in ctx.arguement()]   
        return CallStmt(iden,expr)

    def visitArguement(self, ctx: BKITParser.ArguementContext):
        if ctx.ID(): return Id(ctx.ID().getText())
        if ctx.expr(): return self.visit(ctx.expr()) if ctx.expr() else None
        if ctx.literals(): return self.visit(ctx.literals()) if ctx.literals() else None

    def visitFor_statement(self, ctx: BKITParser.For_statementContext):
        idx1 = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr_cond())
        expr3 = self.visit(ctx.expr(1))
        var_decl = reduce(lambda x,y: x + self.visitVar_decl(y), ctx.var_decl(), [])
        stmt = [self.visit(x) for x in ctx.statement()]        
        returnStmt = self.visit(ctx.return_statement()) if ctx.return_statement() else []
        return For(idx1,expr1,expr2,expr3,(var_decl,stmt+returnStmt))


    def visitWhile_statement(self, ctx: BKITParser.While_statementContext):
        expr = self.visit(ctx.expr())
        var_decl = reduce(lambda x,y: x + self.visitVar_decl(y), ctx.var_decl(), [])
        stmt = [self.visit(x) for x in ctx.statement()]        
        returnStmt = self.visit(ctx.return_statement()) if ctx.return_statement() else []
        return While(expr,(var_decl,stmt+returnStmt))

    def visitDo_while_statement(self, ctx: BKITParser.While_statementContext):
        expr = self.visit(ctx.expr())
        var_decl = reduce(lambda x,y: x + self.visitVar_decl(y), ctx.var_decl(), [])
        stmt = [self.visit(x) for x in ctx.statement()]        
        returnStmt = self.visit(ctx.return_statement()) if ctx.return_statement() else []
        return Dowhile((var_decl,stmt+returnStmt),expr)


    def visitWhile_statement(self, ctx: BKITParser.While_statementContext):
        expr = self.visit(ctx.expr())
        var_decl = reduce(lambda x,y: x + self.visitVar_decl(y), ctx.var_decl(), [])
        stmt = [self.visit(x) for x in ctx.statement()]        
        returnStmt = self.visit(ctx.return_statement()) if ctx.return_statement() else []
        return While(expr,(var_decl,stmt+returnStmt))

    











    

