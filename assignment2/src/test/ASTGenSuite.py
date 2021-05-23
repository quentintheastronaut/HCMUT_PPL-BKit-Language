import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def testcase1(self):
        """Simple program: int main() {} """
        input = """Var: intNumber = 1 ;"""
        expect = Program([VarDecl(Id("intNumber"),[],IntLiteral("1"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def testcase2(self):
        """Simple program: int main() {} """
        input = """Var: floatNumber = 1.56 ;"""
        expect = Program([VarDecl(Id("floatNumber"),[],FloatLiteral("1.56"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def testcase3(self):
        """Simple program: int main() {} """
        input = """Var: flag = True ;"""
        expect = Program([VarDecl(Id("flag"),[],BooleanLiteral("true"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def testcase4(self):
        """Simple program: int main() {} """
        input = """Var: flag = False ;"""
        expect = Program([VarDecl(Id("flag"),[],BooleanLiteral("false"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def testcase5(self):
        """Simple program: int main() {} """
        input = """Var: x ;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def testcase6(self):
        """Simple program: int main() {} """
        input = """Var:x;Var:a;"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def testcase7(self):
        """Simple program: int main() {} """
        input = """Var:a,b,c;"""
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def testcase8(self):
        """Simple program: int main() {} """
        input = """Var:a = 0o12345607; """
        expect = Program([VarDecl(Id("a"),[],IntLiteral(2739079))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def testcase9(self):
        """Simple program: int main() {} """
        input = """Var:a = 0XABC; """
        expect = Program([VarDecl(Id("a"),[],IntLiteral(2748))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def testcase10(self):
        """Simple program: int main() {} """
        input = """Var:a = 1.e-4; """
        expect = Program([VarDecl(Id("a"),[],FloatLiteral(0.0001))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    
    def testcase11(self):
        """Simple program: int main() {} """
        input = """Var:a = 1.34567e-4; """
        expect = Program([VarDecl(Id("a"),[],FloatLiteral(0.000134567))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def testcase12(self):
        """Simple program: int main() {} """
        input = """Var:a = 13127351234567e-4876542342; """
        expect = Program([VarDecl(Id("a"),[],FloatLiteral(0.0))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def testcase13(self):
        """Simple program: int main() {} """
        input = """Var:a ={1,2,3}; """
        expect = """Program([VarDecl(Id(a),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def testcase14(self):
        """Simple program: int main() {} """
        input = """Var:a = {True,False}; """
        expect = """Program([VarDecl(Id(a),ArrayLiteral(BooleanLiteral(true),BooleanLiteral(false)))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def testcase15(self):
        """Simple program: int main() {} """
        input = """Var:a = "DangNhatQuan"; """
        expect = Program([VarDecl(Id("a"),[],StringLiteral("DangNhatQuan"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def testcase16(self):
        """Simple program: int main() {} """
        input = """Var:a = {"s","b","t","c"}; """
        expect = """Program([VarDecl(Id(a),ArrayLiteral(StringLiteral(s),StringLiteral(b),StringLiteral(t),StringLiteral(c)))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def testcase17(self):
        """Simple program: int main() {} """
        input = """Var:a = "DangNhatQuan"; """
        expect = Program([VarDecl(Id("a"),[],StringLiteral("DangNhatQuan"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def testcase18(self):
        """Simple program: int main() {} """
        input = """Var:a = {{1,2,3},{1,2,3}}; """
        expect = """Program([VarDecl(Id(a),ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3))))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def testcase19(self):
        """Simple program: int main() {} """
        input = """Var:a[2][3] = {{"a","b","c"},{"x","y","z"}}; """
        expect = """Program([VarDecl(Id(a),[IntLiteral(2),IntLiteral(3)],ArrayLiteral(ArrayLiteral(StringLiteral(a),StringLiteral(b),StringLiteral(c)),ArrayLiteral(StringLiteral(x),StringLiteral(y),StringLiteral(z))))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    
    def testcase20(self):
        """Simple program: int main() {} """
        input = """
        Function: main
        Parameter: a,b,c
            Body:
                Do
                    Do
                        fact(12);
                        If count == 80 Then
                            Return 1;
                        EndIf.
                    While count < 10 && flag != False
                    EndDo. 
                While count < 10 && flag != False 
                EndDo.
            EndBody. """
        expect = """Program([FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))],([][Dowhile([],[Dowhile([],[CallStmt(Id(fact),[IntLiteral(12)]),If(BinaryOp(==,Id(count),IntLiteral(80)),[],[Return(IntLiteral(1))])],BinaryOp(&&,BinaryOp(<,Id(count),IntLiteral(10)),BinaryOp(!=,Id(flag),BooleanLiteral(false))))],BinaryOp(&&,BinaryOp(<,Id(count),IntLiteral(10)),BinaryOp(!=,Id(flag),BooleanLiteral(false))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def testcase21(self):
        """Simple program: int main() {} """
        input = """Var: a[1][2];"""
        
        expect = """Program([VarDecl(Id(a),[IntLiteral(1),IntLiteral(2)])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def testcase22(self):
        """Simple program: int main() {} """
        input = """
        Function: main
        Parameter: a,b,c
            Body:
               Var: a = 2;
               a = a + 2;
            EndBody. """
        
        expect = """Program([FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))],([VarDecl(Id(a),IntLiteral(2))][Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(2)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    
    def testcase23(self):
        """Simple program: int main() {} """
        input = """
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    n[1] = n + 2;
                    Return n * fact(n-1);
                EndIf.
            EndBody. 

        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody.
        """
        
        expect = """Program([FuncDecl(Id(fact)[VarDecl(Id(n))],([][If(BinaryOp(==,Id(n),IntLiteral(0)),[],[Return(IntLiteral(1))])Else([],[Assign(ArrayCell(Id(n),[IntLiteral(1)]),BinaryOp(+,Id(n),IntLiteral(2))),Return(BinaryOp(*,Id(n),CallStmt(Id(fact),[BinaryOp(-,Id(n),IntLiteral(1))])))])])),FuncDecl(Id(main)[],([][Assign(Id(x),IntLiteral(10)),CallStmt(Id(fact),[Id(x)])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def testcase24(self):
        """Simple program: int main() {} """
        input ="""
            Var: a=5;
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            Var: c,d = 6,e,f;
            Var: m,n[10];
        """
        
        expect = """Program([VarDecl(Id(a),IntLiteral(5)),VarDecl(Id(b),[IntLiteral(2),IntLiteral(3)],ArrayLiteral(ArrayLiteral(IntLiteral(2),IntLiteral(3),IntLiteral(4)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6)))),VarDecl(Id(c)),VarDecl(Id(d),IntLiteral(6)),VarDecl(Id(e)),VarDecl(Id(f)),VarDecl(Id(m)),VarDecl(Id(n),[IntLiteral(10)])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def testcase25(self):
        """Simple program: int main() {} """
        input ="""
        Function: foo
        Parameter: a[5],b
        Body:
            Var: i =0;
            While i<5 Do
                Var: a[5] = {1,2,3};
                a[1] = 12;
                i = i + 1; 
            EndWhile.
        EndBody.
        """
        
        expect = """Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(i),IntLiteral(0))][While(BinaryOp(<,Id(i),IntLiteral(5)),[VarDecl(Id(a),[IntLiteral(5)],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)))],[Assign(ArrayCell(Id(a),[IntLiteral(1)]),IntLiteral(12)),Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def testcase26(self):
        """Simple program: int main() {} """
        input ="""
        Function: foo
        Body:
            Var: r = 10. , v;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody.
        """
        
        expect = """Program([FuncDecl(Id(foo)[],([VarDecl(Id(r),FloatLiteral(10.0)),VarDecl(Id(v))][Assign(Id(v),BinaryOp(*.,BinaryOp(*.,BinaryOp(*.,BinaryOp(*.,BinaryOp(\.,FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id(r)),Id(r)),Id(r)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def testcase27(self):
        """Simple program: int main() {} """
        input ="""
        Function: fib
            Parameter: n
            Body:
                If n <= 1 Then
                    Return n;
                EndIf.

                Return fib(n-1) + fib(n-2);
            EndBody.
        Function: main
            Body:
                Var: n = 9;
                Return 0;
            EndBody.
        """
        
        expect = """Program([FuncDecl(Id(fib)[VarDecl(Id(n))],([][If(BinaryOp(<=,Id(n),IntLiteral(1)),[],[Return(Id(n))]),Return(BinaryOp(+,CallStmt(Id(fib),[BinaryOp(-,Id(n),IntLiteral(1))]),CallStmt(Id(fib),[BinaryOp(-,Id(n),IntLiteral(2))])))])),FuncDecl(Id(main)[],([VarDecl(Id(n),IntLiteral(9))][Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def testcase28(self):
        """Simple program: int main() {} """
        input ="""
        Function: fib
            Parameter: n
            Body:
                Var: f[3],i;

                f[0] = 0;
                f[1] = 1;

                For( i = 2 , i <= n , i + 1 )Do 
                    Var: a = 11;
                    Return a;
                EndFor.

                Return f[5];
            EndBody.

        Function: main
            Body:
                Var: n = 9;
                Return 0;
            EndBody.
        """
        
        expect = """Program([FuncDecl(Id(fib)[VarDecl(Id(n))],([VarDecl(Id(f),[IntLiteral(3)]),VarDecl(Id(i))][Assign(ArrayCell(Id(f),[IntLiteral(0)]),IntLiteral(0)),Assign(ArrayCell(Id(f),[IntLiteral(1)]),IntLiteral(1)),For(Id(i),IntLiteral(2),BinaryOp(<=,Id(i),Id(n)),BinaryOp(+,Id(i),IntLiteral(1)),[VarDecl(Id(a),IntLiteral(11))],[Return(Id(a))]),Return(ArrayCell(Id(f),[IntLiteral(5)]))])),FuncDecl(Id(main)[],([VarDecl(Id(n),IntLiteral(9))][Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def testcase29(self):
        """Simple program: int main() {} """
        input ="""
        Function: add
            Parameter: a,b
            Body:
                Var: x = 0.0;
                x = a +. b;
                Return x;
            EndBody. 

        Function: sub
            Parameter: a,b
            Body:
                Var: x = 0.0;
                x = a -. b;
                Return x;
            EndBody.     

        Function: main
            Body:
                Var: a = 9.0, b = 2.0;
                Return 0;
            EndBody.
        """
        
        expect = """Program([FuncDecl(Id(add)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(x),FloatLiteral(0.0))][Assign(Id(x),BinaryOp(+.,Id(a),Id(b))),Return(Id(x))])),FuncDecl(Id(sub)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(x),FloatLiteral(0.0))][Assign(Id(x),BinaryOp(-.,Id(a),Id(b))),Return(Id(x))])),FuncDecl(Id(main)[],([VarDecl(Id(a),FloatLiteral(9.0)),VarDecl(Id(b),FloatLiteral(2.0))][Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def testcase30(self):
        """Simple program: int main() {} """
        input ="""
        Function: mul
            Parameter: a,b
            Body:
                Var: x = 0.0;
                x = a *. b;
                Return x;
            EndBody. 

        Function: div
            Parameter: a,b
            Body:
                Var: x = 0.0;
                x = a \. b;
                Return x;
            EndBody.     

        Function: main
            Body:
                Var: a = 9.0, b = 2.0;
                Return 0;
            EndBody.
        """
    
        expect = """Program([FuncDecl(Id(mul)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(x),FloatLiteral(0.0))][Assign(Id(x),BinaryOp(*.,Id(a),Id(b))),Return(Id(x))])),FuncDecl(Id(div)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(x),FloatLiteral(0.0))][Assign(Id(x),BinaryOp(\.,Id(a),Id(b))),Return(Id(x))])),FuncDecl(Id(main)[],([VarDecl(Id(a),FloatLiteral(9.0)),VarDecl(Id(b),FloatLiteral(2.0))][Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,330))


    def testcase31(self):
        """Simple program: int main() {} """
        input ="""
        ** This is comment **
        Function: mul
            Parameter: a,b
            Body:
                ** Quan dep trai **
                Var: x = 0.0;
                x = a *. b;
                Return x;
            EndBody. 

        Function: div
            Parameter: a,b
            Body:
                Var: x = 0.0;
                x = a \. b;
                Return x;
            EndBody.     

        Function: main
            Body:
                Var: a = 9.0, b = 2.0;
                Return 0;
            EndBody.
        """
    
        expect = """Program([FuncDecl(Id(mul)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(x),FloatLiteral(0.0))][Assign(Id(x),BinaryOp(*.,Id(a),Id(b))),Return(Id(x))])),FuncDecl(Id(div)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(x),FloatLiteral(0.0))][Assign(Id(x),BinaryOp(\.,Id(a),Id(b))),Return(Id(x))])),FuncDecl(Id(main)[],([VarDecl(Id(a),FloatLiteral(9.0)),VarDecl(Id(b),FloatLiteral(2.0))][Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,331))


    def testcase32(self):
        """Simple program: int main() {} """
        input ="""
        ** This is a
        * multi-line
        * comment.
        **
        Function: mul
            Parameter: a,b
            Body:
                ** Multilines comment testing 1..2..3 **
                Var: x = 0.0;
                x = a *. b;
                Return x;
            EndBody. 

        Function: div
            Parameter: a,b
            Body:
                Var: x = 0.0;
                x = a \. b;
                Return x;
            EndBody.     

        Function: main
            Body:
                Var: a = 9.0, b = 2.0;
                Return 0;
            EndBody.
        """
    
        expect = """Program([FuncDecl(Id(mul)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(x),FloatLiteral(0.0))][Assign(Id(x),BinaryOp(*.,Id(a),Id(b))),Return(Id(x))])),FuncDecl(Id(div)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(x),FloatLiteral(0.0))][Assign(Id(x),BinaryOp(\.,Id(a),Id(b))),Return(Id(x))])),FuncDecl(Id(main)[],([VarDecl(Id(a),FloatLiteral(9.0)),VarDecl(Id(b),FloatLiteral(2.0))][Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,332))


    def testcase33(self):
        """Simple program: int main() {} """
        input ="""
        Var: a = 5,b = 6, c = 9;
        Var: h = b;
        Var: pi = 3.14 , x = 1.2 ,y = 10. ,z = 8.9;
        Var: map[4] = {1,2,3,4};
        Var: flag = True;
        Var: str = "string";
        """
    
        expect = """Program([VarDecl(Id(a),IntLiteral(5)),VarDecl(Id(b),IntLiteral(6)),VarDecl(Id(c),IntLiteral(9)),VarDecl(Id(h),Id(b)),VarDecl(Id(pi),FloatLiteral(3.14)),VarDecl(Id(x),FloatLiteral(1.2)),VarDecl(Id(y),FloatLiteral(10.0)),VarDecl(Id(z),FloatLiteral(8.9)),VarDecl(Id(map),[IntLiteral(4)],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4))),VarDecl(Id(flag),BooleanLiteral(true)),VarDecl(Id(str),StringLiteral(string))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,333))  

    def testcase34(self):
        """Simple program: int main() {} """
        input ="""
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c[2] = {1,2,3};
        Var: m,n[10];
        """
    
        expect = """Program([VarDecl(Id(b),[IntLiteral(2),IntLiteral(3)],ArrayLiteral(ArrayLiteral(IntLiteral(2),IntLiteral(3),IntLiteral(4)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6)))),VarDecl(Id(c),[IntLiteral(2)],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3))),VarDecl(Id(m)),VarDecl(Id(n),[IntLiteral(10)])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,334))  

    def testcase35(self):
        """Simple program: int main() {} """
        input ="""
        Var: name = "Dang Nhat Quan";
        Var: studentID = "K1813694";
        Var: classID = "KH1040";
        """
    
        expect = """Program([VarDecl(Id(name),StringLiteral(Dang Nhat Quan)),VarDecl(Id(studentID),StringLiteral(K1813694)),VarDecl(Id(classID),StringLiteral(KH1040))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,335))  

    def testcase36(self):
        """Simple program: int main() {} """
        input ="""
        Function: fib
            Parameter: n
            Body:
                If n <= 1 Then
                    Return n;
                EndIf.

                Return fib(n-1)+fib(n-2);
            EndBody.
        """
    
        expect = """Program([FuncDecl(Id(fib)[VarDecl(Id(n))],([][If(BinaryOp(<=,Id(n),IntLiteral(1)),[],[Return(Id(n))]),Return(BinaryOp(+,CallStmt(Id(fib),[BinaryOp(-,Id(n),IntLiteral(1))]),CallStmt(Id(fib),[BinaryOp(-,Id(n),IntLiteral(2))])))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,336))  

    def testcase37(self):
        """Simple program: int main() {} """
        input ="""
        Function: fib
            Parameter: n
            Body:
                If n <= 1 Then
                    Return n;
                EndIf.

                Return fib(n-1)+fib(n-2);
            EndBody.

        Function: main
            Body:
                Var: n = 9;
                Var: list[2] = {0,0} ;
                list[ 1+2*3+9*12*12-6-7 ] = fib(12);
                Return 0;
            EndBody.
        """
    
        expect = """Program([FuncDecl(Id(fib)[VarDecl(Id(n))],([][If(BinaryOp(<=,Id(n),IntLiteral(1)),[],[Return(Id(n))]),Return(BinaryOp(+,CallStmt(Id(fib),[BinaryOp(-,Id(n),IntLiteral(1))]),CallStmt(Id(fib),[BinaryOp(-,Id(n),IntLiteral(2))])))])),FuncDecl(Id(main)[],([VarDecl(Id(n),IntLiteral(9)),VarDecl(Id(list),[IntLiteral(2)],ArrayLiteral(IntLiteral(0),IntLiteral(0)))][Assign(ArrayCell(Id(list),[BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,IntLiteral(1),BinaryOp(*,IntLiteral(2),IntLiteral(3))),BinaryOp(*,BinaryOp(*,IntLiteral(9),IntLiteral(12)),IntLiteral(12))),IntLiteral(6)),IntLiteral(7))]),CallStmt(Id(fib),[IntLiteral(12)])),Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,337))  

    def testcase38(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
            Body:
                Var: array[10];
                For (i = 0 , i < 10 ,2) Do
                    a[i] = i;
                EndFor.    
            EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(array),[IntLiteral(10)])][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[Assign(ArrayCell(Id(a),[Id(i)]),Id(i))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,338))  


    def testcase39(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
            Body:
                Var: a = 1.;
                If a >. 5. Then 
                    a = 4. + 1.;
                ElseIf a <. 5. Then
                    a = 4. -. 1.;
                Else 
                    a = 5.;
                EndIf.
            EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(a),FloatLiteral(1.0))][If(BinaryOp(>.,Id(a),FloatLiteral(5.0)),[],[Assign(Id(a),BinaryOp(+,FloatLiteral(4.0),FloatLiteral(1.0)))])ElseIf(BinaryOp(<.,Id(a),FloatLiteral(5.0)),[],[Assign(Id(a),BinaryOp(-.,FloatLiteral(4.0),FloatLiteral(1.0)))])Else([],[Assign(Id(a),FloatLiteral(5.0))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,339))  

    def testcase40(self):
        """Simple program: int main() {} """
        input ="""
        Var: a = {True,False};
        Var: b = {"String1","String2"};
        Var: c = {9.23,8.5};
        Var: d = {2,1,4};
        """
    
        expect = """Program([VarDecl(Id(a),ArrayLiteral(BooleanLiteral(true),BooleanLiteral(false))),VarDecl(Id(b),ArrayLiteral(StringLiteral(String1),StringLiteral(String2))),VarDecl(Id(c),ArrayLiteral(FloatLiteral(9.23),FloatLiteral(8.5))),VarDecl(Id(d),ArrayLiteral(IntLiteral(2),IntLiteral(1),IntLiteral(4)))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,340))  


    def testcase41(self):
        """Simple program: int main() {} """
        input = """Var: a[100];
        
        Function: main
        Body:
            a[foo(12)+3*5-6] = 123;
            a[foo(12)+3*5+6] = 432;
        EndBody."""
        expect = """Program([VarDecl(Id(a),[IntLiteral(100)]),FuncDecl(Id(main)[],([][Assign(ArrayCell(Id(a),[BinaryOp(-,BinaryOp(+,CallStmt(Id(foo),[IntLiteral(12)]),BinaryOp(*,IntLiteral(3),IntLiteral(5))),IntLiteral(6))]),IntLiteral(123)),Assign(ArrayCell(Id(a),[BinaryOp(+,BinaryOp(+,CallStmt(Id(foo),[IntLiteral(12)]),BinaryOp(*,IntLiteral(3),IntLiteral(5))),IntLiteral(6))]),IntLiteral(432))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def testcase42(self):
        """Simple program: int main() {} """
        input = """
        Var: a,b,c,d,e[2];
        
        Function: foo
        Parameter: a[5],b
        Body:
            Var: i = 0;
            While i<5 Do
                a[i] = b +. 10;
                i = i + 1;
            EndWhile.
        EndBody.
        
        Function: main
        Body:
            Var: x = 0;
            a = 1;
            b = 12.6;
            c = "string";
            d = True;
            e[x] = 0;
            e[a] = 1;
            Var: h[100];
            h[3 + foo(2)] = a[b[2][3]] + 4;
        EndBody."""
        expect = """Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(d)),VarDecl(Id(e),[IntLiteral(2)]),FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(i),IntLiteral(0))][While(BinaryOp(<,Id(i),IntLiteral(5)),[],[Assign(ArrayCell(Id(a),[Id(i)]),BinaryOp(+.,Id(b),IntLiteral(10))),Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1)))])])),FuncDecl(Id(main)[],([VarDecl(Id(x),IntLiteral(0)),VarDecl(Id(h),[IntLiteral(100)])][Assign(Id(a),IntLiteral(1)),Assign(Id(b),FloatLiteral(12.6)),Assign(Id(c),StringLiteral(string)),Assign(Id(d),BooleanLiteral(true)),Assign(ArrayCell(Id(e),[Id(x)]),IntLiteral(0)),Assign(ArrayCell(Id(e),[Id(a)]),IntLiteral(1)),Assign(ArrayCell(Id(h),[BinaryOp(+,IntLiteral(3),CallStmt(Id(foo),[IntLiteral(2)]))]),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(b),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def testcase43(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: a;
            a = (5 + (20 - 8)*19 ) \ 3;
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(a))][Assign(Id(a),BinaryOp(\,BinaryOp(+,IntLiteral(5),BinaryOp(*,BinaryOp(-,IntLiteral(20),IntLiteral(8)),IntLiteral(19))),IntLiteral(3)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def testcase44(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: a = 5.0;
            If (a == 5.0 )|| (a >= 12.0 )|| (a <= 6.0 ) Then
                a = 12.0;
            EndIf.
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(a),FloatLiteral(5.0))][If(BinaryOp(||,BinaryOp(||,BinaryOp(==,Id(a),FloatLiteral(5.0)),BinaryOp(>=,Id(a),FloatLiteral(12.0))),BinaryOp(<=,Id(a),FloatLiteral(6.0))),[],[Assign(Id(a),FloatLiteral(12.0))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def testcase45(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: a = 5.0, destination = 8.0;
            Var: flag = True;
            While a < 10 && flag != False Do
                a = a +. 1.0;
                If a == 8.0 Then
                    flag = False;
                EndIf.
            EndWhile.
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(a),FloatLiteral(5.0)),VarDecl(Id(destination),FloatLiteral(8.0)),VarDecl(Id(flag),BooleanLiteral(true))][While(BinaryOp(&&,BinaryOp(<,Id(a),IntLiteral(10)),BinaryOp(!=,Id(flag),BooleanLiteral(false))),[],[Assign(Id(a),BinaryOp(+.,Id(a),FloatLiteral(1.0))),If(BinaryOp(==,Id(a),FloatLiteral(8.0)),[],[Assign(Id(flag),BooleanLiteral(false))])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def testcase46(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: a = 5.0;
            If a == 5.0 || a >= 12.0 && a <= 6.0 Then
                a = 12.0;
            EndIf.
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(a),FloatLiteral(5.0))][If(BinaryOp(&&,BinaryOp(||,BinaryOp(==,Id(a),FloatLiteral(5.0)),BinaryOp(>=,Id(a),FloatLiteral(12.0))),BinaryOp(<=,Id(a),FloatLiteral(6.0))),[],[Assign(Id(a),FloatLiteral(12.0))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def testcase47(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: a = True;
            Var: b = False;
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(a),BooleanLiteral(true)),VarDecl(Id(b),BooleanLiteral(false))][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def testcase48(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: i;
            Var: count = 100;
            For (i = 0 , i < 10 ,2 )Do
                If count == 105 Then
                    count = count + i;
                    Break;
                Else 
                    count = count + i;
                    Continue;
                EndIf.  
            EndFor.
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(i)),VarDecl(Id(count),IntLiteral(100))][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[If(BinaryOp(==,Id(count),IntLiteral(105)),[],[Assign(Id(count),BinaryOp(+,Id(count),Id(i))),Break()])Else([],[Assign(Id(count),BinaryOp(+,Id(count),Id(i))),Continue()])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def testcase49(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: i = 2;
            Var: count = 100;
            If count == 105 Then
                count = count + i;
            EndIf.
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(i),IntLiteral(2)),VarDecl(Id(count),IntLiteral(100))][If(BinaryOp(==,Id(count),IntLiteral(105)),[],[Assign(Id(count),BinaryOp(+,Id(count),Id(i)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def testcase50(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: i = 2;
            Var: count = 100;
            If count == 105 Then
                count = count + i;              
            Else 
                count = count + i;
            EndIf.  
        EndBody. """
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(i),IntLiteral(2)),VarDecl(Id(count),IntLiteral(100))][If(BinaryOp(==,Id(count),IntLiteral(105)),[],[Assign(Id(count),BinaryOp(+,Id(count),Id(i)))])Else([],[Assign(Id(count),BinaryOp(+,Id(count),Id(i)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    
    def testcase51(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: i = 2;
            Var: count = 100;
            If count == 105 Then
                count = count + i;    
            ElseIf count == 206 Then
                count = count + 2*i; 
            ElseIf count == 207 Then
                count = count + 3*i;  
            ElseIf count == 208 Then
                count = count + 4*i;   
            Else 
                count = count + i;
            EndIf.  
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(i),IntLiteral(2)),VarDecl(Id(count),IntLiteral(100))][If(BinaryOp(==,Id(count),IntLiteral(105)),[],[Assign(Id(count),BinaryOp(+,Id(count),Id(i)))])ElseIf(BinaryOp(==,Id(count),IntLiteral(206)),[],[Assign(Id(count),BinaryOp(+,Id(count),BinaryOp(*,IntLiteral(2),Id(i))))])ElseIf(BinaryOp(==,Id(count),IntLiteral(207)),[],[Assign(Id(count),BinaryOp(+,Id(count),BinaryOp(*,IntLiteral(3),Id(i))))])ElseIf(BinaryOp(==,Id(count),IntLiteral(208)),[],[Assign(Id(count),BinaryOp(+,Id(count),BinaryOp(*,IntLiteral(4),Id(i))))])Else([],[Assign(Id(count),BinaryOp(+,Id(count),Id(i)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def testcase52(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: i = 2;
            Var: count = 100;
            If count == 105 Then
                count = count + i;    
            ElseIf count == 206 Then
                count = count + 2*i;  
            Else 
                count = count + i;
            EndIf.  
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(i),IntLiteral(2)),VarDecl(Id(count),IntLiteral(100))][If(BinaryOp(==,Id(count),IntLiteral(105)),[],[Assign(Id(count),BinaryOp(+,Id(count),Id(i)))])ElseIf(BinaryOp(==,Id(count),IntLiteral(206)),[],[Assign(Id(count),BinaryOp(+,Id(count),BinaryOp(*,IntLiteral(2),Id(i))))])Else([],[Assign(Id(count),BinaryOp(+,Id(count),Id(i)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def testcase53(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: i = 2;
            Var: count = 100;
            If count == 105 Then
                count = count + i; 
                If count == 108 Then
                    count = count + i;   
                EndIf. 
            Else 
                count = count - i;
                If count == 99 Then
                    count = count + i;   
                EndIf. 
            EndIf.  
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(i),IntLiteral(2)),VarDecl(Id(count),IntLiteral(100))][If(BinaryOp(==,Id(count),IntLiteral(105)),[],[Assign(Id(count),BinaryOp(+,Id(count),Id(i))),If(BinaryOp(==,Id(count),IntLiteral(108)),[],[Assign(Id(count),BinaryOp(+,Id(count),Id(i)))])])Else([],[Assign(Id(count),BinaryOp(-,Id(count),Id(i))),If(BinaryOp(==,Id(count),IntLiteral(99)),[],[Assign(Id(count),BinaryOp(+,Id(count),Id(i)))])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def testcase54(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: flag = True, a =2;
            Var: count = 100;
            While count < 10 && flag != False Do
                count = count +. 10;
                If count == 80 Then
                    flag = False;
                EndIf.
            EndWhile.
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(flag),BooleanLiteral(true)),VarDecl(Id(a),IntLiteral(2)),VarDecl(Id(count),IntLiteral(100))][While(BinaryOp(&&,BinaryOp(<,Id(count),IntLiteral(10)),BinaryOp(!=,Id(flag),BooleanLiteral(false))),[],[Assign(Id(count),BinaryOp(+.,Id(count),IntLiteral(10))),If(BinaryOp(==,Id(count),IntLiteral(80)),[],[Assign(Id(flag),BooleanLiteral(false))])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def testcase55(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: flag = True, a =2;
            Var: count = 100;
            While count < 10 && flag != False Do
                Var: i =0;
                While i < count Do
                    count = count +. 10;
                    If count == 80 Then
                    flag = False;
                    EndIf.
                EndWhile.
            EndWhile.
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(flag),BooleanLiteral(true)),VarDecl(Id(a),IntLiteral(2)),VarDecl(Id(count),IntLiteral(100))][While(BinaryOp(&&,BinaryOp(<,Id(count),IntLiteral(10)),BinaryOp(!=,Id(flag),BooleanLiteral(false))),[VarDecl(Id(i),IntLiteral(0))],[While(BinaryOp(<,Id(i),Id(count)),[],[Assign(Id(count),BinaryOp(+.,Id(count),IntLiteral(10))),If(BinaryOp(==,Id(count),IntLiteral(80)),[],[Assign(Id(flag),BooleanLiteral(false))])])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def testcase56(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: flag = True, a =2;
            Var: count = 100;
            Do
                count = count +. 10;
                If count == 80 Then
                    flag = False;
                EndIf.
            While count < 10 && flag != False 
            EndDo.
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(flag),BooleanLiteral(true)),VarDecl(Id(a),IntLiteral(2)),VarDecl(Id(count),IntLiteral(100))][Dowhile([],[Assign(Id(count),BinaryOp(+.,Id(count),IntLiteral(10))),If(BinaryOp(==,Id(count),IntLiteral(80)),[],[Assign(Id(flag),BooleanLiteral(false))])],BinaryOp(&&,BinaryOp(<,Id(count),IntLiteral(10)),BinaryOp(!=,Id(flag),BooleanLiteral(false))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def testcase57(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: flag = True, a =2;
            Var: count = 100;
            Do
                Do
                    count = count +. 10;
                    If count == 80 Then
                        flag = False;
                    EndIf.
                While count < 10 && flag != False
                EndDo. 
            While count < 10 && flag != False 
            EndDo.
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(flag),BooleanLiteral(true)),VarDecl(Id(a),IntLiteral(2)),VarDecl(Id(count),IntLiteral(100))][Dowhile([],[Dowhile([],[Assign(Id(count),BinaryOp(+.,Id(count),IntLiteral(10))),If(BinaryOp(==,Id(count),IntLiteral(80)),[],[Assign(Id(flag),BooleanLiteral(false))])],BinaryOp(&&,BinaryOp(<,Id(count),IntLiteral(10)),BinaryOp(!=,Id(flag),BooleanLiteral(false))))],BinaryOp(&&,BinaryOp(<,Id(count),IntLiteral(10)),BinaryOp(!=,Id(flag),BooleanLiteral(false))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def testcase58(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            Var: flag = True, a =2;
            Var: a[10][10];
            For (i = 0 , i < 10 ,2 )Do
                For (i = 0 , i < 10 ,2) Do
                    a[i][j]  = i+j;
                EndFor.
            EndFor.
        EndBody. """
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(flag),BooleanLiteral(true)),VarDecl(Id(a),IntLiteral(2)),VarDecl(Id(a),[IntLiteral(10),IntLiteral(10)])][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[Assign(ArrayCell(Id(a),[Id(i),Id(j)]),BinaryOp(+,Id(i),Id(j)))])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def testcase59(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
            foo();
            fib();
            remove();
            get();
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][CallStmt(Id(foo),[]),CallStmt(Id(fib),[]),CallStmt(Id(remove),[]),CallStmt(Id(get),[])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    
    def testcase60(self):
        """Simple program: int main() {} """
        input = """
        Function: main
        Body:
            foo(1);
            fib(2+42+324 \ 234*24332);
            remove(3);
            get(4);
        EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][CallStmt(Id(foo),[IntLiteral(1)]),CallStmt(Id(fib),[BinaryOp(+,BinaryOp(+,IntLiteral(2),IntLiteral(42)),BinaryOp(*,BinaryOp(\,IntLiteral(324),IntLiteral(234)),IntLiteral(24332)))]),CallStmt(Id(remove),[IntLiteral(3)]),CallStmt(Id(get),[IntLiteral(4)])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def testcase61(self):
        """Simple program: int main() {} """
        input = """Function: fib
            Parameter: n
            Body:
            Var: str = "string";
            EndBody."""
        
        expect = """Program([FuncDecl(Id(fib)[VarDecl(Id(n))],([VarDecl(Id(str),StringLiteral(string))][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def testcase62(self):
        """Simple program: int main() {} """
        input = """
        Function: mummy
        Body:
            a = !a > b || c + d * e[2];
        EndBody."""
        
        expect = """Program([FuncDecl(Id(mummy)[],([][Assign(Id(a),BinaryOp(||,BinaryOp(>,UnaryOp(!,Id(a)),Id(b)),BinaryOp(+,Id(c),BinaryOp(*,Id(d),ArrayCell(Id(e),[IntLiteral(2)])))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    
    def testcase63(self):
        """Simple program: int main() {} """
        input = """
        Function: hello
            Parameter: n
            Body:
                If a == 1 Then
                    Return 1;
                EndIf.

                If a == 2 Then
                    Return 1.5;
                EndIf.

                If a == 3 Then
                    Return True;
                EndIf.

                If a == 4 Then
                    Return "hello";
                EndIf.
            EndBody.
        """
        
        expect = """Program([FuncDecl(Id(hello)[VarDecl(Id(n))],([][If(BinaryOp(==,Id(a),IntLiteral(1)),[],[Return(IntLiteral(1))]),If(BinaryOp(==,Id(a),IntLiteral(2)),[],[Return(FloatLiteral(1.5))]),If(BinaryOp(==,Id(a),IntLiteral(3)),[],[Return(BooleanLiteral(true))]),If(BinaryOp(==,Id(a),IntLiteral(4)),[],[Return(StringLiteral(hello))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def testcase64(self):
        """Simple program: int main() {} """
        input ="""
            Function: hello
            Parameter: n
            Body:
                If a == 1 Then
                    Return 1;
                EndIf.

                For (i = 0 , i < 10 ,2 )Do
                    Return i;
                EndFor.

                Do
                count = count +. 10;
                    If count == 80 Then
                        Return 5;
                    EndIf.
                While count < 10 && flag != False 
                EndDo.

                While count < 10 && flag != False Do
                    count = count +. 10;
                    Return "hello";
                EndWhile.
            EndBody.
        """
        
        expect = """Program([FuncDecl(Id(hello)[VarDecl(Id(n))],([][If(BinaryOp(==,Id(a),IntLiteral(1)),[],[Return(IntLiteral(1))]),For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[Return(Id(i))]),Dowhile([],[Assign(Id(count),BinaryOp(+.,Id(count),IntLiteral(10))),If(BinaryOp(==,Id(count),IntLiteral(80)),[],[Return(IntLiteral(5))])],BinaryOp(&&,BinaryOp(<,Id(count),IntLiteral(10)),BinaryOp(!=,Id(flag),BooleanLiteral(false)))),While(BinaryOp(&&,BinaryOp(<,Id(count),IntLiteral(10)),BinaryOp(!=,Id(flag),BooleanLiteral(false))),[],[Assign(Id(count),BinaryOp(+.,Id(count),IntLiteral(10))),Return(StringLiteral(hello))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def testcase65(self):
        """Simple program: int main() {} """
        input ="""
        Var: b = 48 \% 12 ;
        """
        
        expect = """Program([VarDecl(Id(b),BinaryOp(\%,IntLiteral(48),IntLiteral(12)))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def testcase66(self):
        """Simple program: int main() {} """
        input ="""
        Var: a;
        Var: b[3];
        Var: c[5][2];
        Var: d = 1813694;
        Var: e = 1e14;
        Var: str  = "Hello";
        Var: flag = True;
        Var: i = {{5,6},{4,7}};

        Function: test
        Parameter: x, y[3], z[4][5]
            Body:
                Var: m = 0, n = 1.45 , p = "", q = False;
                Var: sum = 0;
                While m <= 10 Do
                    For (i = 0 , i < d ,i + 1) Do
                    n = n + 3.14;
                    EndFor.
                EndWhile.
                sum = sum*2 + m + n + d;
            Return sum;
        EndBody.
        """
        
        expect = """Program([VarDecl(Id(a)),VarDecl(Id(b),[IntLiteral(3)]),VarDecl(Id(c),[IntLiteral(5),IntLiteral(2)]),VarDecl(Id(d),IntLiteral(1813694)),VarDecl(Id(e),FloatLiteral(100000000000000.0)),VarDecl(Id(str),StringLiteral(Hello)),VarDecl(Id(flag),BooleanLiteral(true)),VarDecl(Id(i),ArrayLiteral(ArrayLiteral(IntLiteral(5),IntLiteral(6)),ArrayLiteral(IntLiteral(4),IntLiteral(7)))),FuncDecl(Id(test)[VarDecl(Id(x)),VarDecl(Id(y)),VarDecl(Id(z))],([VarDecl(Id(m),IntLiteral(0)),VarDecl(Id(n),FloatLiteral(1.45)),VarDecl(Id(p),StringLiteral()),VarDecl(Id(q),BooleanLiteral(false)),VarDecl(Id(sum),IntLiteral(0))][While(BinaryOp(<=,Id(m),IntLiteral(10)),[],[For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),Id(d)),BinaryOp(+,Id(i),IntLiteral(1)),[],[Assign(Id(n),BinaryOp(+,Id(n),FloatLiteral(3.14)))])]),Assign(Id(sum),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(*,Id(sum),IntLiteral(2)),Id(m)),Id(n)),Id(d))),Return(Id(sum))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def testcase67(self):
        """Simple program: int main() {} """
        input ="""
        Function: fib
            Parameter: n
            Body:
                If n <= 1 Then
                    Return n;
                EndIf.

                Return fib(n-1) + fib(n-2);
            EndBody.
        Function: main
            Body:
                Var: n = 9;
                Return 0;
            EndBody.
        """
        
        expect = """Program([FuncDecl(Id(fib)[VarDecl(Id(n))],([][If(BinaryOp(<=,Id(n),IntLiteral(1)),[],[Return(Id(n))]),Return(BinaryOp(+,CallStmt(Id(fib),[BinaryOp(-,Id(n),IntLiteral(1))]),CallStmt(Id(fib),[BinaryOp(-,Id(n),IntLiteral(2))])))])),FuncDecl(Id(main)[],([VarDecl(Id(n),IntLiteral(9))][Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def testcase68(self):
        """Simple program: int main() {} """
        input ="""
        Function: tomcruise
        Body:
            a = (((a)));
        EndBody.
        """
        
        expect = """Program([FuncDecl(Id(tomcruise)[],([][Assign(Id(a),Id(a))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def testcase69(self):
        """Simple program: int main() {} """
        input ="""
        Var: x, y[1], z[1][1], q =54123421, u = 1e2142, a = "Hello", n = False, i = {{1,3},{1,2}};

Function: babyboo
    Parameter: a, b[1], c[1][1]
    Body:
        Var: a = 1, b = 1., c = "", d = True;
        While a < 10 Do
            Var: b = 1;
            While b < 10 Do
                quan = quan * bap;
                b = b + 1;
            EndWhile.
            sum = sum + count;
            bap = cui + 1;
            Var: count = 1;
        EndWhile.
        Var: sum = 0;
    EndBody.
        """
        
        expect = """Program([VarDecl(Id(x)),VarDecl(Id(y),[IntLiteral(1)]),VarDecl(Id(z),[IntLiteral(1),IntLiteral(1)]),VarDecl(Id(q),IntLiteral(54123421)),VarDecl(Id(u),FloatLiteral(inf)),VarDecl(Id(a),StringLiteral(Hello)),VarDecl(Id(n),BooleanLiteral(false)),VarDecl(Id(i),ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(3)),ArrayLiteral(IntLiteral(1),IntLiteral(2)))),FuncDecl(Id(babyboo)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))],([VarDecl(Id(a),IntLiteral(1)),VarDecl(Id(b),FloatLiteral(1.0)),VarDecl(Id(c),StringLiteral()),VarDecl(Id(d),BooleanLiteral(true)),VarDecl(Id(sum),IntLiteral(0))][While(BinaryOp(<,Id(a),IntLiteral(10)),[VarDecl(Id(b),IntLiteral(1)),VarDecl(Id(count),IntLiteral(1))],[While(BinaryOp(<,Id(b),IntLiteral(10)),[],[Assign(Id(quan),BinaryOp(*,Id(quan),Id(bap))),Assign(Id(b),BinaryOp(+,Id(b),IntLiteral(1)))]),Assign(Id(sum),BinaryOp(+,Id(sum),Id(count))),Assign(Id(bap),BinaryOp(+,Id(cui),IntLiteral(1)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def testcase70(self):
        """Simple program: int main() {} """
        input ="""
        Function: babyshark
            Body:
            EndBody.
        """
    
        expect = """Program([FuncDecl(Id(babyshark)[],([][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,370))


    def testcase71(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
            Body:
                a = -(-.1);
                a = 3-1;
            EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(a),UnaryOp(-,UnaryOp(-.,IntLiteral(1)))),Assign(Id(a),BinaryOp(-,IntLiteral(3),IntLiteral(1)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,371))


    def testcase72(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
        Body:
            Var: a = b;
            b = bamboo();
            Var: c = aloha(1,True,"hihihaha");
            d = hieuthu[1];
            e = eeniemineymoo()[1];
        EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(a),Id(b)),VarDecl(Id(c),CallStmt(Id(aloha),[IntLiteral(1),BooleanLiteral(true),StringLiteral(hihihaha)]))][Assign(Id(b),CallStmt(Id(bamboo),[])),Assign(Id(d),ArrayCell(Id(hieuthu),[IntLiteral(1)])),Assign(Id(e),CallStmt(Id(eeniemineymoo),[]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,372))


    def testcase73(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
        Body:
            a = {1,7,8,97,23,2};
            b = { 112.123, 2.312, 3.02123, 4.1231 };
            c = { True, False, False, True };
            d = { {1,2}, {3,4},{1,4,2} };
            e = {{{{{1}}}}};
            f = {{{{{1}}}}, {1}, 1};
        EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(a),ArrayLiteral(IntLiteral(1),IntLiteral(7),IntLiteral(8),IntLiteral(97),IntLiteral(23),IntLiteral(2))),Assign(Id(b),ArrayLiteral(FloatLiteral(112.123),FloatLiteral(2.312),FloatLiteral(3.02123),FloatLiteral(4.1231))),Assign(Id(c),ArrayLiteral(BooleanLiteral(true),BooleanLiteral(false),BooleanLiteral(false),BooleanLiteral(true))),Assign(Id(d),ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2)),ArrayLiteral(IntLiteral(3),IntLiteral(4)),ArrayLiteral(IntLiteral(1),IntLiteral(4),IntLiteral(2)))),Assign(Id(e),ArrayLiteral(ArrayLiteral(ArrayLiteral(ArrayLiteral(ArrayLiteral(IntLiteral(1))))))),Assign(Id(f),ArrayLiteral(ArrayLiteral(ArrayLiteral(ArrayLiteral(ArrayLiteral(IntLiteral(1))))),ArrayLiteral(IntLiteral(1)),IntLiteral(1)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,373))  

    def testcase74(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
    Body:
        Var :a = 1 * 1;
        b = a *. 1;
        c = 1 \ 1;
        d = b \. 1;
        Var: f = 1 % 1;
        g = c + 1;
        h = 1 +. 1;
        i = d - 1;
        j = 1 -. 1;
        k = 1 && 1;
        l = e || 1;
        m = 1 == 1;
        Var: n = f != 1;
        o = 1 =/= 1;
        p = 1 < 1;
        Var: q = g <. 1;
        r = 1 > 1;
        s = 1 >. 1;
        t = h <= 1;
        Var: u = 1 <=. 1;
        v = 1 >= 1;
        w = 1 >=. 1;
        x = !1;
        y = -1;
        z = -.1;
    EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(a),BinaryOp(*,IntLiteral(1),IntLiteral(1))),VarDecl(Id(f),BinaryOp(%,IntLiteral(1),IntLiteral(1))),VarDecl(Id(n),BinaryOp(!=,Id(f),IntLiteral(1))),VarDecl(Id(q),BinaryOp(<.,Id(g),IntLiteral(1))),VarDecl(Id(u),BinaryOp(<=.,IntLiteral(1),IntLiteral(1)))][Assign(Id(b),BinaryOp(*.,Id(a),IntLiteral(1))),Assign(Id(c),BinaryOp(\,IntLiteral(1),IntLiteral(1))),Assign(Id(d),BinaryOp(\.,Id(b),IntLiteral(1))),Assign(Id(g),BinaryOp(+,Id(c),IntLiteral(1))),Assign(Id(h),BinaryOp(+.,IntLiteral(1),IntLiteral(1))),Assign(Id(i),BinaryOp(-,Id(d),IntLiteral(1))),Assign(Id(j),BinaryOp(-.,IntLiteral(1),IntLiteral(1))),Assign(Id(k),BinaryOp(&&,IntLiteral(1),IntLiteral(1))),Assign(Id(l),BinaryOp(||,Id(e),IntLiteral(1))),Assign(Id(m),BinaryOp(==,IntLiteral(1),IntLiteral(1))),Assign(Id(o),BinaryOp(=/=,IntLiteral(1),IntLiteral(1))),Assign(Id(p),BinaryOp(<,IntLiteral(1),IntLiteral(1))),Assign(Id(r),BinaryOp(>,IntLiteral(1),IntLiteral(1))),Assign(Id(s),BinaryOp(>.,IntLiteral(1),IntLiteral(1))),Assign(Id(t),BinaryOp(<=,Id(h),IntLiteral(1))),Assign(Id(v),BinaryOp(>=,IntLiteral(1),IntLiteral(1))),Assign(Id(w),BinaryOp(>=.,IntLiteral(1),IntLiteral(1))),Assign(Id(x),UnaryOp(!,IntLiteral(1))),Assign(Id(y),UnaryOp(-,IntLiteral(1))),Assign(Id(z),UnaryOp(-.,IntLiteral(1)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,374))  

    def testcase75(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
    Body:
        Return 1234567865.456789098765;
    EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([][Return(FloatLiteral(1234567865.456789))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,375))  

    def testcase76(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
    Body:
        Return a[312321 \ 1231 + 12312][foo(12) + 19];
    EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([][Return(ArrayCell(Id(a),[BinaryOp(+,BinaryOp(\,IntLiteral(312321),IntLiteral(1231)),IntLiteral(12312)),BinaryOp(+,CallStmt(Id(foo),[IntLiteral(12)]),IntLiteral(19))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,376))  

    def testcase77(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
    Body:
        Return fooo(214567+214567-12345678 * 5678 \ 67890989 * 4567);
    EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([][Return(CallStmt(Id(fooo),[BinaryOp(-,BinaryOp(+,IntLiteral(214567),IntLiteral(214567)),BinaryOp(*,BinaryOp(\,BinaryOp(*,IntLiteral(12345678),IntLiteral(5678)),IntLiteral(67890989)),IntLiteral(4567)))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,377))  

    def testcase78(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
    Body:
        Return 1+2-3*4 \ 5+5 \ 1+21+54;
    EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([][Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLiteral(1),IntLiteral(2)),BinaryOp(\,BinaryOp(*,IntLiteral(3),IntLiteral(4)),IntLiteral(5))),BinaryOp(\,IntLiteral(5),IntLiteral(1))),IntLiteral(21)),IntLiteral(54)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,378))  


    def testcase79(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
    Body:
        Return a[12][12];
    EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([][Return(ArrayCell(Id(a),[IntLiteral(12),IntLiteral(12)]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,379))  

    def testcase80(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
    Body:
        Return abc(1231231,123123,{1,3,1,3,1,2})+ bts("quan");
    EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([][Return(BinaryOp(+,CallStmt(Id(abc),[IntLiteral(1231231),IntLiteral(123123),ArrayLiteral(IntLiteral(1),IntLiteral(3),IntLiteral(1),IntLiteral(3),IntLiteral(1),IntLiteral(2))]),CallStmt(Id(bts),[StringLiteral(quan)])))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,380))  
   

    def testcase81(self):
        """Simple program: int main() {} """
        input = """
            Function: delete
            Body:
                a = .756785e-123213;
            EndBody.
            """
        
        expect = """Program([FuncDecl(Id(delete)[],([][Assign(Id(a),FloatLiteral(0.0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def testcase82(self):
        """Simple program: int main() {} """
        input = """
        Function: delete
            Body:
                a = 0.756785e-123213;
            EndBody.
            """
        
        expect = """Program([FuncDecl(Id(delete)[],([][Assign(Id(a),FloatLiteral(0.0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    
    def testcase83(self):
        """Simple program: int main() {} """
        input = """
        Function: delete
            Body:
                a = 1.75675e-123213;
            EndBody.
        """
        
        expect = """Program([FuncDecl(Id(delete)[],([][Assign(Id(a),FloatLiteral(0.0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def testcase84(self):
        """Simple program: int main() {} """
        input ="""
            Function: manh
            Body:
                a = 1.75675e-123213;
            EndBody.
        """
        
        expect = """Program([FuncDecl(Id(manh)[],([][Assign(Id(a),FloatLiteral(0.0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def testcase85(self):
        """Simple program: int main() {} """
        input ="""
        Function: hcmut
        Body:
            a = 1.5675e123213;
        EndBody.
        """
        
        expect = """Program([FuncDecl(Id(hcmut)[],([][Assign(Id(a),FloatLiteral(inf))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def testcase86(self):
        """Simple program: int main() {} """
        input ="""
        Function: hcmut
        Body:
            a = 1.e-12;
        EndBody.
        """
        
        expect = """Program([FuncDecl(Id(hcmut)[],([][Assign(Id(a),FloatLiteral(1e-12))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def testcase87(self):
        """Simple program: int main() {} """
        input ="""
        Function: bku
        Body:
            a = 1.e12;
        EndBody.
        """
        
        expect = """Program([FuncDecl(Id(bku)[],([][Assign(Id(a),FloatLiteral(1000000000000.0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def testcase88(self):
        """Simple program: int main() {} """
        input ="""
        Function: aloha
        Body:
            a = 1.23;
        EndBody.
        """
        
        expect = """Program([FuncDecl(Id(aloha)[],([][Assign(Id(a),FloatLiteral(1.23))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def testcase89(self):
        """Simple program: int main() {} """
        input ="""
        Var: x, y[1], z[1][1], q =54123421, u = 1e2142, a = "Hello", n = False, i = {{1,3},{1,2}};

Function: babyboo
    Parameter: a, b[1], c[1][1]
    Body:
        Var: a = 1, b = 1.23, c = "", d = True;
        While a < 10 Do
            Var: b = 1;
            While b < 10 Do
                quan = quan * bap;
                b = b + 1;
            EndWhile.
            sum = sum + count;
            bap = cui + 1;
            Var: count = 1;
        EndWhile.
        Var: sum = 0;
    EndBody.
        """
        
        expect = """Program([VarDecl(Id(x)),VarDecl(Id(y),[IntLiteral(1)]),VarDecl(Id(z),[IntLiteral(1),IntLiteral(1)]),VarDecl(Id(q),IntLiteral(54123421)),VarDecl(Id(u),FloatLiteral(inf)),VarDecl(Id(a),StringLiteral(Hello)),VarDecl(Id(n),BooleanLiteral(false)),VarDecl(Id(i),ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(3)),ArrayLiteral(IntLiteral(1),IntLiteral(2)))),FuncDecl(Id(babyboo)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))],([VarDecl(Id(a),IntLiteral(1)),VarDecl(Id(b),FloatLiteral(1.23)),VarDecl(Id(c),StringLiteral()),VarDecl(Id(d),BooleanLiteral(true)),VarDecl(Id(sum),IntLiteral(0))][While(BinaryOp(<,Id(a),IntLiteral(10)),[VarDecl(Id(b),IntLiteral(1)),VarDecl(Id(count),IntLiteral(1))],[While(BinaryOp(<,Id(b),IntLiteral(10)),[],[Assign(Id(quan),BinaryOp(*,Id(quan),Id(bap))),Assign(Id(b),BinaryOp(+,Id(b),IntLiteral(1)))]),Assign(Id(sum),BinaryOp(+,Id(sum),Id(count))),Assign(Id(bap),BinaryOp(+,Id(cui),IntLiteral(1)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def testcase90(self):
        """Simple program: int main() {} """
        input ="""
        Function: babyshark
            Body:
            EndBody.
        """
    
        expect = """Program([FuncDecl(Id(babyshark)[],([][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,390))


    def testcase91(self):
        """Simple program: int main() {} """
        input ="""
        
        """
    
        expect = """Program([])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,391))


    def testcase92(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
        Body:
            While True Do
                Var: quan = "True";
                quan = "False";
                bFS(quan);
                If True Then
        ElseIf True Then
            If True Then
            ElseIf True Then
                If True Then
                ElseIf True Then
                ElseIf True Then
                    If True Then
                        Return 1;
                    ElseIf True Then
                        Return 2;
                    Else
                        Return 3;
                    EndIf.
                Else 
                EndIf.
                
            Else
            EndIf.
        Else
        EndIf.
        EndWhile.
        EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([][While(BooleanLiteral(true),[VarDecl(Id(quan),StringLiteral(True))],[Assign(Id(quan),StringLiteral(False)),CallStmt(Id(bFS),[Id(quan)]),If(BooleanLiteral(true),[],[])ElseIf(BooleanLiteral(true),[],[If(BooleanLiteral(true),[],[])ElseIf(BooleanLiteral(true),[],[If(BooleanLiteral(true),[],[])ElseIf(BooleanLiteral(true),[],[])ElseIf(BooleanLiteral(true),[],[If(BooleanLiteral(true),[],[Return(IntLiteral(1))])ElseIf(BooleanLiteral(true),[],[Return(IntLiteral(2))])Else([],[Return(IntLiteral(3))])])Else([],[])])Else([],[])])Else([],[])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,392))


    def testcase93(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
            Parameter: a,b,c,d[1],d[2],e[3],d[2][3]
            Body:
            EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(d)),VarDecl(Id(d)),VarDecl(Id(e)),VarDecl(Id(d))],([][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,393))  

    def testcase94(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
    Body:
        If True Then
        ElseIf True Then
            If True Then
            ElseIf True Then
                If True Then
                ElseIf True Then
                ElseIf True Then
                    If True Then
                        Return 1;
                    ElseIf True Then
                        Return 2;
                    Else
                        Return 3;
                    EndIf.
                Else 
                EndIf.
                
            Else
            EndIf.
        Else
        EndIf.
    EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([][If(BooleanLiteral(true),[],[])ElseIf(BooleanLiteral(true),[],[If(BooleanLiteral(true),[],[])ElseIf(BooleanLiteral(true),[],[If(BooleanLiteral(true),[],[])ElseIf(BooleanLiteral(true),[],[])ElseIf(BooleanLiteral(true),[],[If(BooleanLiteral(true),[],[Return(IntLiteral(1))])ElseIf(BooleanLiteral(true),[],[Return(IntLiteral(2))])Else([],[Return(IntLiteral(3))])])Else([],[])])Else([],[])])Else([],[])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,394))  

    def testcase95(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
    Body:
        While True Do
            Var: quan = "True";
            quan = "False";
            bFS(quan);
        EndWhile.
    EndBody. 
        """
    
        expect = """Program([FuncDecl(Id(main)[],([][While(BooleanLiteral(true),[VarDecl(Id(quan),StringLiteral(True))],[Assign(Id(quan),StringLiteral(False)),CallStmt(Id(bFS),[Id(quan)])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,395))  

    def testcase96(self):
        """Simple program: int main() {} """
        input ="""
        Function: lambda
    Body:
        Do
            Var: b = 11+24;
            foo(12);
        While True
        EndDo.
    EndBody.
        """
    
        expect = """Program([FuncDecl(Id(lambda)[],([][Dowhile([VarDecl(Id(b),BinaryOp(+,IntLiteral(11),IntLiteral(24)))],[CallStmt(Id(foo),[IntLiteral(12)])],BooleanLiteral(true))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,396))  

    def testcase97(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
    Body:
        For (i = 1 + 1, 1.0, -1) Do
        EndFor.
    EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([][For(Id(i),BinaryOp(+,IntLiteral(1),IntLiteral(1)),FloatLiteral(1.0),UnaryOp(-,IntLiteral(1)),[],[])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,397))  

    def testcase98(self):
        """Simple program: int main() {} """
        input ="""
        Function: bambo
    Body:
        For (i = 1, i < 10, i+1) Do
            Var: a;
            foo();
        EndFor.
    EndBody.
        """
    
        expect = """Program([FuncDecl(Id(bambo)[],([][For(Id(i),IntLiteral(1),BinaryOp(<,Id(i),IntLiteral(10)),BinaryOp(+,Id(i),IntLiteral(1)),[VarDecl(Id(a))],[CallStmt(Id(foo),[])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,398))  


    def testcase99(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
    Body:
        Continue;
    EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([][Continue()]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,399))  

    def testcase100(self):
        """Simple program: int main() {} """
        input ="""
        Function: main
    Body:
        Break;
    EndBody.
        """
    
        expect = """Program([FuncDecl(Id(main)[],([][Break()]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,400))  
   


    def testcase101(self):
        input = r"""
            Var: x = {123, {345, {567}}};
            Var: x = {True, False, "Hihihi", 0x1234};
            Var: x = {};
        """
        expect = Program([
            VarDecl(
                Id("x"), [],
                ArrayLiteral([
                    IntLiteral(123),
                    ArrayLiteral([IntLiteral(345), ArrayLiteral([IntLiteral(567)])])
                ])),
            VarDecl(
                Id("x"), [],
                ArrayLiteral([
                    BooleanLiteral(True),
                    BooleanLiteral(False),
                    StringLiteral("Hihihi"),
                    IntLiteral(4660)
                ])),
            VarDecl(Id("x"), [], ArrayLiteral([]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 401))
    
