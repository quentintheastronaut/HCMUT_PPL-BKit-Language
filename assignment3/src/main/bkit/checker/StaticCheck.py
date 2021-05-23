
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, NewType, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *
from main.bkit.checker.StaticError import Variable

from main.bkit.utils.AST import ArrayCell, ArrayLiteral, BinaryOp, CallExpr, CallStmt, Dowhile, FuncDecl, Id, Program, VarDecl

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass


class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass


class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

    def __init__(self, name, typ=Unknown()):
        self.name = name
        self.mtype = typ

class StaticChecker(BaseVisitor):
    type_list = [
        MType,IntType,FloatType,VoidType,BoolType,StringType,Unknown,ArrayType
    ]
    func_check = False
    func = []
    globalID = []
    globalStmt = [
        "int_of_float",
        "float_of_int",
        "int_of_string",
        "string_of_int",
        "float_of_string",
        "string_of_float",
        "bool_of_string",
        "string_of_bool",
        "read"

    ]

    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
# callexpr
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_of_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),

#callstmt
Symbol("printLn",MType([],VoidType())),
Symbol("print"     ,MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]                           
   
    def check(self):
        return self.visit(self.ast,self.global_envi)
        

    def visitProgram(self, ctx: Program, o):
        self.globalID = []
        o = []
        self.func = []

        self.func_check = True
        for decl in ctx.decl:
          
            if type(decl) == FuncDecl:
                
                self.visit(decl, self.func)

   
        self.func_check = False

        for decl in ctx.decl:
            self.visit(decl, o)


        flag = False
        for check_main in self.globalID:
            if check_main.name == "main":
                flag = True
                break
        if flag == False:
            raise NoEntryPoint()

      

        
    
    def visitVarDecl(self, ctx: VarDecl, o):
        if len(list(filter(lambda x: x.name == ctx.variable.name, o))) > 0:
            raise Redeclared(Variable(),ctx.variable.name)

        if ctx.varInit != None:
            init = self.visit(ctx.varInit,o)
            init.dimen = ctx.varDimen

            if type(self.visit(ctx.varInit,o)) == ArrayType or len(ctx.varDimen) > 0:
                
                o.append(Symbol(ctx.variable.name,init))
                self.globalID.append(Symbol(ctx.variable.name,init))
            else :
                
                o.append(Symbol(ctx.variable.name,init))
                self.globalID.append(Symbol(ctx.variable.name,init))
             
        else :
            if len(ctx.varDimen) > 0:
                init = ArrayType([],Unknown)
                init.dimen = ctx.varDimen

                o.append(Symbol(ctx.variable.name,init))
                self.globalID.append(Symbol(ctx.variable.name,init))
            else :
                o.append(Symbol(ctx.variable.name))
                self.globalID.append(Symbol(ctx.variable.name))


            
        
    
    def visitFuncDecl(self, ctx: FuncDecl ,o):
        
        if self.func_check == False:
              

            if list(filter(lambda x: x.name == ctx.name.name,o)):
                raise Redeclared(Function(),ctx.name.name) 
            else:
                o.append(Symbol(ctx.name.name,MType([],None)))
                self.globalID.append(Symbol(ctx.name.name,MType([],None)))
                

                index_local = len(o)-1
                index_global = len(self.globalID)-1
                
                params = []
                
                for param in ctx.param:
                    arr = list(filter(lambda x: x.name == param.variable.name, params))
                    if len(arr) > 0:
                        raise Redeclared(Parameter(),param.variable.name) 
                    params.append(Symbol(param.variable.name))  
                    o[len(o)-1].mtype.intype.append(Unknown())
                    self.globalID[len(self.globalID)-1].mtype.intype.append(Unknown())
                    
                o[len(o)-1].mtype.restype = Unknown()
                self.globalID[len(self.globalID)-1].mtype.restype = Unknown()

                for name in ctx.body[0]:
                    self.visit(name,params)
                
                newParam = params + o
                
                for stmt in ctx.body[1]:
                    if type(stmt) is Return:
                        o[len(o)-1].mtype.restype = self.visit(stmt,newParam)
                        self.globalID[len(self.globalID)-1].mtype.restype = self.visit(stmt,newParam)
                    else:
                        self.visit(stmt,newParam)

                
                # ép kiểu cho param

                for i in range(0,len(ctx.param)):
                  
                    if type(o[len(o)-1].mtype.intype[i]) == Unknown:
                        o[index_local].mtype.intype[i] = type(newParam[i].mtype)
                        self.globalID[index_global].mtype.intype[i] = type(newParam[i].mtype)
            


                for name in params:
                    for id_name in self.globalID:
                        if name.name == id_name.name:
                            self.globalID.remove(id_name)

        else:
            if list(filter(lambda x: x.name == ctx.name.name,self.func)):
                raise Redeclared(Function(),ctx.name.name) 

            self.func.append(Symbol(ctx.name.name,MType([],None)))

            index_local = len(self.func)-1
            params = []
            for param in ctx.param:
                arr = list(filter(lambda x: x.name == param.variable.name, params))
                if len(arr) > 0:
                    raise Redeclared(Parameter(),param.variable.name) 
                params.append(Symbol(param.variable.name))  
                self.func[index_local].mtype.intype.append(Unknown())  

            self.func[index_local].mtype.restype = Unknown()
           

    def visitAssign(self, ctx: Assign, o):

    

        if type(ctx.rhs) == CallExpr:
            rhs_exp = self.visit(ctx.rhs,o)
            
            type_rhs = type(rhs_exp)
         
        
        elif type(ctx.rhs) == ArrayCell:
          
            rhs_exp = self.visit(ctx.rhs,o)
            type_rhs = rhs_exp if rhs_exp in self.type_list else type(rhs_exp.mtype)
        else:

            rhs_exp = ctx.rhs.accept(self,o)
            type_rhs = type(rhs_exp.mtype if type(rhs_exp) is Symbol else rhs_exp)


        lhs_id = self.visit(ctx.lhs,o)
        if type(lhs_id) == Symbol:
            
            type_lhs = type(lhs_id.mtype)

        elif type(ctx.rhs) == ArrayCell:
          
            lhs_exp = self.visit(ctx.lhs,o)
            type_lhs = lhs_exp if lhs_exp in self.type_list else type(lhs_exp.mtype)
        else:
            lhs_id = self.visit(ctx.lhs,o)
            type_lhs = lhs_id
            

        if type_lhs == ArrayType and type_rhs != type_lhs:
            raise TypeMismatchInStatement(ctx)
        elif type_lhs == ArrayType and type_rhs == type_lhs:
            dimen_lhs = lhs_id.mtype.dimen
            dimen_rhs = rhs_exp.mtype.dimen

         
      

            if len(dimen_rhs) != len(dimen_lhs):
                raise TypeCannotBeInferred(ctx)

            for i in dimen_rhs:
                if i not in dimen_lhs:
                    raise TypeMismatchInStatement(ctx)

            for i in dimen_lhs:
                if i not in dimen_rhs:
                    raise TypeMismatchInStatement(ctx)
            

        else :
          
            if (type_lhs == Unknown) and (type_rhs == Unknown):
              
                raise TypeCannotBeInferred(ctx)
            elif (type_lhs == Unknown) and (type_rhs != Unknown):
                lhs_id.mtype = rhs_exp.mtype if type(rhs_exp) is Symbol else rhs_exp
            elif (type_lhs != Unknown) and (type_rhs == Unknown):  
                rhs_exp.mtype = lhs_id.mtype 
            elif (type_lhs != Unknown) and (type_rhs != Unknown):
                if type_lhs != type_rhs:
                  
          
                    raise TypeMismatchInStatement(ctx)

    
    def visitArrayCell(self, ctx: ArrayCell, o):
        arr = self.visit(ctx.arr,o)

        if type(arr) == Symbol:
            
        
            if type(arr.mtype) != ArrayType:
            
                raise TypeMismatchInExpression(ctx)
            
            for idx in ctx.idx:
                expression = self.visit(idx,o)
                type_expr = type(expression.mtype if type(expression) is Symbol else expression)
                if type_expr != IntType:
               
                    raise TypeMismatchInExpression(ctx)

            
            return arr.mtype.eletype
            
        else:
            
            for idx in ctx.idx:
                expression = self.visit(idx,o)
                if type(expression) != IntType:
                  
                    raise TypeMismatchInExpression(ctx)
           
            return type(arr)


 
    def visitBinaryOp(self, ctx: BinaryOp, o):
        l_exp, r_exp = ctx.left.accept(self, o), ctx.right.accept(self, o)

        type_lexp = type(l_exp.mtype if type(l_exp) is Symbol else l_exp)
        type_rexp = type(r_exp.mtype if type(r_exp) is Symbol else r_exp)
        if ctx.op in ['+', '-', '*', '\\','%']:
            if type_lexp is Unknown:
                l_exp.mtype = IntType()
            if type_rexp is Unknown:
                r_exp.mtype = IntType()
            if BoolType in [type_lexp, type_rexp] or FloatType in [type_lexp, type_rexp]:
                raise TypeMismatchInExpression(ctx)
            return IntType()
            
        if ctx.op in ['+.', '-.', '*.', '\.']:
            if type_lexp is Unknown:
                l_exp.mtype = FloatType()
            if type_rexp is Unknown:
                r_exp.mtype = FloatType()
            if BoolType in [type_lexp, type_rexp] or IntType in [type_lexp, type_rexp]:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
            
        if ctx.op in ['>', '==','<','!=','>=','<=']:



            if type_lexp is Unknown:
                l_exp.mtype = IntType()
            if type_rexp is Unknown:
                r_exp.mtype = IntType()
            if BoolType in [type_lexp, type_rexp] or FloatType in [type_lexp, type_rexp]:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
            
        if ctx.op in ['>.', '=/=','<.','>=.','<=.']:
            if type_lexp is Unknown:
                l_exp.mtype = FloatType()
            if type_rexp is Unknown:
                r_exp.mtype = FloatType()
            if BoolType in [type_lexp, type_rexp] or IntType in [type_lexp, type_rexp]:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
            
        if ctx.op in ['&&','||']:
            if type_lexp is Unknown:
                l_exp.mtype = BoolType()
            if type_rexp is Unknown:
                r_exp.mtype = BoolType()
            if IntType in [type_lexp, type_rexp] or FloatType in [type_lexp, type_rexp]:
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitUnaryOp(self, ctx: UnaryOp, o):
        exp = ctx.body.accept(self, o)
        type_exp = type(exp.mtype if type(exp) is Symbol else exp)
        if ctx.op == '-':
            if type_exp is Unknown:
                exp.mtype = IntType()
            elif type_exp is not IntType:
                raise TypeMismatchInExpression(ctx)
            return IntType()
            
        if ctx.op == '-.':
            if type_exp is Unknown:
                exp.mtype = FloatType()
            elif type_exp is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
            
        if ctx.op == '!':
      
            
            if type_exp is Unknown:
                exp.mtype = BoolType()
            elif type_exp is not BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
            
        if ctx.op == 'i2f':
            if type_exp is Unknown:
                exp.mtype = IntType()
            elif type_exp is not IntType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
            
        if ctx.op == 'floor':
            if type_exp is Unknown:
                exp.mtype = FloatType()
            elif type_exp is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return IntType()


    def visitIntLiteral(self, ctx: IntType, o):
        return IntType()

    def visitStringLiteral(self, ctx: StringType, o):
        return StringType()

    def visitArrayLiteral(self, ctx: ArrayType, o):
        type_of_value = self.visit(ctx.value[0],o)
        return ArrayType([],type(type_of_value))

    def visitFloatLiteral(self, ctx: FloatType, o):
        return FloatType()

    def visitBooleanLiteral(self, ctx: BoolType, o):
        return BoolType()



    def visitId(self, ctx: Id, o):
        
        arr = list(filter(lambda x: x.name == ctx.name, o))
        if len(arr) == 0:
            arr = list(filter(lambda x: x.name == ctx.name, self.globalID))
            if len(arr) == 0:
                arr = list(filter(lambda x: x.name == ctx.name, self.func))
                if len(arr) == 0:
                    raise Undeclared(Identifier(),ctx.name)
        
        
        return arr[0]
        
    def visitCallStmt(self, ctx:CallStmt,o):
        method_id = ctx.method.name
        
        if method_id == "printStrLn" or  method_id == "print":
            if len(ctx.param) != len(self.global_envi[11].mtype.intype):
                
                
                raise TypeMismatchInStatement(ctx)

            this_param = self.visit(ctx.param[0],o)
            type_param = type(this_param.mtype if type(this_param) == Symbol else this_param)


            if type_param != type(self.global_envi[11].mtype.intype[0]):
                    
                    raise TypeMismatchInStatement(ctx)

        elif method_id == "printLn":
            if len(ctx.param) != len(self.global_envi[9].mtype.intype):
                raise TypeMismatchInStatement(ctx)
    
        
        else:
            arr = list(filter(lambda x: x.name == method_id, o))
            if len(arr) == 0:
                arr = list(filter(lambda x: x.name == method_id, self.globalID))
                if len(arr) == 0:
                    raise Undeclared(Function(),method_id)
                else :
                    
                    for i in range(0,len(self.globalID)):
                        if self.globalID[i].name == method_id:
                            index = i
                            break

                    if len(ctx.param) != len(self.globalID[index].mtype.intype):
                        raise TypeMismatchInStatement(ctx)

                
                    for i in range(0,len(ctx.param)):
                    
                        x = self.visit(ctx.param[i],self.globalID)      #type của param từ code
                        y = self.globalID[index].mtype.intype[i]                    #type chuẩn
                        
                        y_type = type(y)
                        x_type = type(x.mtype if type(x) == Symbol else x)

                        if x_type == Unknown and y_type == Unknown:
                            raise TypeCannotBeInferred(ctx)
                        elif y_type == Unknown and x_type != Unknown:
                            y_type = x.mtype if type(x) == Symbol else x
                        elif y_type != Unknown and x_type == Unknown:
                            x.mtype = y.mtype if type(y) == Symbol else y
                        elif y_type != x_type:
                            raise TypeMismatchInStatement(ctx)
                    
            else:
            
                for i in range(0,len(o)):
                    if o[i].name == method_id:
                        index = i
                        break

                if len(ctx.param) != len(o[index].mtype.intype):
                
                    raise TypeMismatchInStatement(ctx)

            
                for i in range(0,len(ctx.param)):
                    
                    x = self.visit(ctx.param[i],o)     #type của param từ code
                    y = o[index].mtype.intype[i]        #type chuẩn
                    
                    y_type = y if y in self.type_list else type(y)
                    
                    if type(x) == Symbol:
                        if x.mtype in self.type_list:
                            x_type = x.mtype
                        else :
                            x_type = type(x.mtype)

                    
                    elif x in self.type_list:
                        x_type = x
                    else :
                        x_type = type(x) 

                    if x_type == Unknown and y_type == Unknown:
        
                        raise TypeCannotBeInferred(ctx)
                    elif y_type == Unknown and x_type != Unknown:
                        
                        o[index].mtype.intype[i] = x.mtype if type(x) == Symbol else x
                    elif y_type != Unknown and x_type == Unknown:
                        
                        x.mtype = y.mtype if type(y) == Symbol else y
        

                    elif y_type != x_type:
                        
                        


                      
            
                        raise TypeMismatchInStatement(ctx)

    def visitReturn(self, ctx: Return,o):
       
        return_symbol = self.visit(ctx.expr,o)
        return_type = return_symbol.mtype if type(return_symbol) is Symbol else return_symbol
       
        return return_type



    def visitWhile(self, ctx: While, o):
        exp = self.visit(ctx.exp,o)
        exp_type = type(exp.mtype if type(exp) is Symbol else exp)

        if exp_type != BoolType:
            raise TypeMismatchInStatement(ctx)

        params = []

        for decl in ctx.sl[0]:
            self.visit(decl,params)
        
        for stmt in ctx.sl[1]:
            self.visit(stmt,params+o)

        for param in params:
            for id_name in self.globalID:
                if id_name.name == param.name:
                    self.globalID.remove(id_name)



    def visitDowhile( self, ctx: Dowhile, o):
        params = []
        

        for decl in ctx.sl[0]:
            self.visit(decl,params)
        
        for stmt in ctx.sl[1]:
            self.visit(stmt,params+o)

        for param in params:
            for id_name in self.globalID:
                if id_name.name == param.name:
                    self.globalID.remove(id_name)

        exp = self.visit(ctx.exp,o)
        exp_type = type(exp.mtype if type(exp) is Symbol else exp)
        
        if exp_type != BoolType:
            raise TypeMismatchInStatement(ctx)

        

    def visitContinue(self, ctx: Continue,o ):
        pass

    def visitBreak(self, ctx: Break,o ):
        pass

    def visitFor(self, ctx: For,o):
        
        idex = self.visit(ctx.idx1,o)
        expr1 = self.visit(ctx.expr1,o)
        expr2 = self.visit(ctx.expr2,o)
        expr3 = self.visit(ctx.expr3,o)

        idex_type = type(idex.mtype if type(idex) is Symbol else idex)
        expr1_type = type(expr1.mtype if type(expr1) is Symbol else expr1)
        expr2_type = type(expr2.mtype if type(expr2) is Symbol else expr2)
        expr3_type = type(expr3.mtype if type(expr3) is Symbol else expr3)

        if idex_type != IntType or expr1_type != IntType or expr3_type != IntType:
          
            raise TypeMismatchInStatement(ctx)
        elif expr2_type != BoolType:
          
            raise TypeMismatchInStatement(ctx)

        params = []

        for decl in ctx.loop[0]:
            self.visit(decl,params)
        
        for stmt in ctx.loop[1]:
            self.visit(stmt,params+o)

        for param in params:
            for id_name in self.globalID:
                if id_name.name == param.name:
                    self.globalID.remove(id_name)


    

    def visitIf(self, ctx: If,o):
        
        for ifstmt in ctx.ifthenStmt:
            
            cond_expr = self.visit(ifstmt[0],o)
            type_cond = type(cond_expr.mtype if type(cond_expr) is Symbol else cond_expr )
            if type_cond != BoolType:
                raise TypeMismatchInStatement(ctx)

            params = []
            for decl in ifstmt[1]:
                self.visit(decl,params)
            
            for stmt in ifstmt[2]:
                self.visit(stmt,params+o)

            for param in params:
                for id_name in self.globalID:
                    if id_name.name == param.name:
                        self.globalID.remove(id_name)

        

        params = []

        for decl in ctx.elseStmt[0]:
                self.visit(decl,params)

        for stmt in ctx.elseStmt[1]:
                self.visit(stmt,params+o)
        
        for param in params:
            for id_name in self.globalID:
                if id_name.name == param.name:
                    self.globalID.remove(id_name)
        
        

    def visitCallExpr(self, ctx: CallExpr,o):
        
        method_id = ctx.method.name
     

        if method_id =="read":
            if len(ctx.param) != len(self.global_envi[8].mtype.intype):
                raise TypeMismatchInExpression(ctx)

        elif method_id in self.globalStmt:
           
            for i in range(0,9):
                if method_id == self.global_envi[i].name:
                   
                    if len(ctx.param) != len(self.global_envi[i].mtype.intype):
                        raise TypeMismatchInExpression(ctx)
                    
                   
                    this_param = self.visit(ctx.param[0],o)
                    type_param = type(this_param.mtype if type(this_param) == Symbol else this_param)


                    if type_param != type(self.global_envi[i].mtype.intype[0]):
                       
                        raise TypeMismatchInExpression(ctx)
                    
                    else:
                      
                        return self.global_envi[i].mtype.restype

                
        else:

            arr = list(filter(lambda x: x.name == method_id, o))
            if len(arr) == 0:
                arr = list(filter(lambda x: x.name == method_id, self.globalID))
                if len(arr) == 0:
                    arr = list(filter(lambda x: x.name == method_id, self.func))
                    if len(arr) == 0:
                        raise Undeclared(Function(),method_id)
                    else:
                        for i in range(0,len(self.func)):
                            if self.func[i].name == method_id:
                                index = i
                                break
                        return self.func[index].mtype.restype

                else :
                    
                    for i in range(0,len(self.globalID)):
                        if self.globalID[i].name == method_id:
                            index = i
                            break

                    if len(ctx.param) != len(self.globalID[index].mtype.intype):
                        
                        raise TypeMismatchInExpression(ctx)

                
                    for i in range(0,len(ctx.param)):
                    
                        x = self.visit(ctx.param[i],self.globalID)      #type của param từ code
                        y = self.globalID[index].mtype.intype[i]                    #type chuẩn
                        


                        y_type = type(y)
                        x_type = type(x.mtype if type(x) == Symbol else x)

                      

                        if x_type == Unknown and y_type == Unknown:
                            raise TypeCannotBeInferred(ctx)
                        elif y_type == Unknown and x_type != Unknown:
                            y_type = x.mtype if type(x) == Symbol else x
                        elif y_type != Unknown and x_type == Unknown:
                            x.mtype = y.mtype if type(y) == Symbol else y
                        elif y_type != x_type:
                            
                            raise TypeMismatchInExpression(ctx)
                    
                    return self.globalID[index].mtype.restype
                    
            else:
            
                for i in range(0,len(o)):
                    if o[i].name == method_id:
                        index = i
                        break

                if len(ctx.param) != len(o[index].mtype.intype):
                    
                    raise TypeMismatchInExpression(ctx)

            
                for i in range(0,len(ctx.param)):
                    
                    x = self.visit(ctx.param[i],o)     #type của param từ code
                    y = o[index].mtype.intype[i]        #type chuẩn
                    
                    y_type = y if y in self.type_list else type(y) 
                    x_type = type(x.mtype if type(x) == Symbol else x)

            
                            #type chuẩn của func
                    if x_type == Unknown and y_type == Unknown:
        
                        raise TypeCannotBeInferred(ctx)
                    elif y_type == Unknown and x_type != Unknown:
                        
                        o[index].mtype.intype[i] = x.mtype if type(x) == Symbol else x
                    elif y_type != Unknown and x_type == Unknown:
                        
                        x.mtype = y
        

                    elif y_type != x_type:
                        
                        raise TypeMismatchInExpression(ctx)
                
                return o[index].mtype.restype 
        



