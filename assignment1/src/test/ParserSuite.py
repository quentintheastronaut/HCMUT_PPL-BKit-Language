import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    """1. Variable declaration"""

    def test1(self):
        """ Var declaration successfull """
        input = "Var:a=6;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,101))

    def test2(self):
        """ Var declaration fail - Missing ID """
        input = "Var:a=0,9=6;"
        expect = "Error on line 1 col 8: 9"
        self.assertTrue(TestParser.checkParser(input,expect,102))

    def test3(self):
        """Many Var declaration fail """
        input = "Var:a=1,b=2,c=3;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,103))

    def test4(self):
        """Missing SM ; """
        input = """Var:a=1,b=2,c=3"""
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,104))

    def test5(self):
        """Missing CM , """
        input = """Var:a=1b=2,c=3"""
        expect = "Error on line 1 col 7: b"
        self.assertTrue(TestParser.checkParser(input,expect,105))

    def test6(self):
        """Many Types of Declaration"""
        input = """
        Var: a = 5,b = 6, c = 9;
        Var: h = b;
        Var: pi = 3.14 , x = 1.2 ,y = 10. ,z = 8.9;
        Var: map[4] = {1,2,3,4};
        Var: flag = True;
        Var: str = "string";
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,106))


    def test7(self):
        """Array declaration"""
        input = """
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c[2] = {1,2,3};
        Var: m,n[10];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,107))

    def test8(self):
        """Array declaration - fail """
        input = """
        Var: b[[2]][3] = {{2,3,4},{4,5,6}};
        """
        expect = "Error on line 2 col 15: ["
        self.assertTrue(TestParser.checkParser(input,expect,108))

    def test9(self):
        """Array declaration - missing '{' or  '}' """
        input = """
        Var: b[2][3] = {2,3,4,{4,5,6;
        """
        expect = "Error on line 2 col 23: {"
        self.assertTrue(TestParser.checkParser(input,expect,109))

    def test10(self):
        """String declaration  """
        input = """
        Var: name = "Dang Nhat Quan";
        Var: studentID = "K1813694";
        Var: classID = "KH1040";
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,110))

    def test11(self):
        """Boolean declaration"""
        input = """
        Var: flag = True;
        Var: flag = False;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,111))

    def test12(self):
        """Boolean declaration - fail """
        input = """
        Var: flag = TrueFalse;
        """
        expect = "Error on line 2 col 24: False"
        self.assertTrue(TestParser.checkParser(input,expect,112))

    def test13(self):
        """Float declaration """
        input = """
        Var: pi = 3.14;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,113))

    def test14(self):
        """Float declaration - redundant point . """
        input = """
        Var: pi = 3..14;
        """
        expect = "Error on line 2 col 20: ."
        self.assertTrue(TestParser.checkParser(input,expect,114))    

    def test15(self):
        """Var declaration - wrong spelling """
        input = """
        Varr: pi = 3..14;
        """
        expect = "Error on line 2 col 11: r"
        self.assertTrue(TestParser.checkParser(input,expect,115))

    """2. Function declaration"""
    def test16(self):
        """Func declaration """
        input = """
        Function: fib
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,116))

    def test17(self):
        """Func declaration - missing body """
        input = """
        Function: fib
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,117))

    def test18(self):
        """Func declaration - Fibonacci function """
        input = """
        Function: fib
            Parameter: n
            Body:
                If n <= 1 Then
                    Return n;
                EndIf.

                Return fib(n-1)+fib(n-2);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,118)) 

    def test19(self):
        """Func declaration - Fibonacci function - missing dot '.' ending"""
        input = """
        Function: fib
            Parameter: n
            Body:
                If n <= 1 Then
                    Return n;
                EndIf.

                Return fib(n-1)+fib(n-2);
            EndBody
        """
        expect = "Error on line 11 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,119)) 

    def test20(self):
        """Func declaration - Fibonacci function - missing dot '.' ending"""
        input = """
        Function: fib
            Parameter: n
            Body:
                If n <= 1 Then
                    Return n;
                EndIf.

                Return fib(n-1)+fib(n-2);
            EndBody
        """
        expect = "Error on line 11 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,120))

    def test21(self):
        """Func declaration - Fibonacci function - missing keyword Parameter"""
        input = """
        Function: fib
            n
            Body:
                If n <= 1 Then
                    Return n;
                EndIf.

                Return fib(n-1)+fib(n-2);
            EndBody.
        """
        expect = "Error on line 3 col 12: n"
        self.assertTrue(TestParser.checkParser(input,expect,121))

    def test22(self):
        """Func declaration - Fibonacci function - assignment """
        input = """
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
                print(fib(n));
                read();
                Return 0;
            EndBody.

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,122))
    
    """3. Type and value"""
    def test23(self):
        """ Testing Integer operators"""
        input = """
        Function: main
            Body:
                Var: array[10];
                For i = 0 , i < 10 ,2 Do
                    a[i] = i;
                EndFor.    
            EndBody.

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,123))

    def test24(self):
        """ Testing float operators"""
        input = """
        Function: main
            Body:
                Var: a = 1.;
                If a >. 5. Then 
                    a = 4. +. 1.;
                ElseIf a <. 5. Then
                    a = 4. -. 1.;
                Else 
                    a = 5.;
                EndIf.
            EndBody.

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,124))
    
    def test25(self):
        """ Testing float operators - """
        input = """
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,125))

    def test26(self):
        """Testing Array declaration with many types of array """
        input = """
        Var: a = {True,False};
        Var: b = {"String1","String2"};
        Var: c = {9.23,8.5};
        Var: d = {2,1,4};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,126))

    def test27(self):
        """Testing Array declaration - different types in same array """
        input = """
        Var: a = {"String",True};
        """
        expect = "Error on line 2 col 17: {"
        self.assertTrue(TestParser.checkParser(input,expect,127))

    def test28(self):
        """ Array declaration - array's element assignment """
        input = """
        Var: a[100];
        
        Function: main
        Body:
            a[foo(12)+3*5-6] = 123;
            a[foo(12)+3*5+6] = 432;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,128))


    def test29(self):
        """ Array declaration - array's element assignment """
        input = """
        Var: a[100];
        
        Function: main
        Body:
            a[foo(12)+3*5-6] = 123;
            a[foo(12)+3*5+6] = 432;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,129))

    def test30(self):
        """ Assignment Statement """
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
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,130))
   
    def test31(self):
        """ Assignment Statement - wrong operator """
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
            d := True;
            e[x] = 0;
            e[a] = 1;
            Var: h[100];
            h[3 + foo(2)] = a[b[2][3]] + 4;
        EndBody.
        """
        expect = "Error on line 20 col 14: :"
        self.assertTrue(TestParser.checkParser(input,expect,131))

    """4. Association """
    def test32(self):
        """ Association """
        input = """
        Function: main
        Body:
            Var: a;
            a = (5 + (20 - 8)*19 )\\3;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,132))

    def test33(self):
        """Testing boolean's operator && """
        input = """
        Function: main
        Body:
            Var: a = 5.0;
            If a == 5.0 || a >= 12.0 || a <= 6.0 Then
                a = 12.0;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,133))

    def test34(self):
        """Testing boolean's operator && """
        input = """
        Function: main
        Body:
            Var: a = 5.0, destination = 8.0;
            Var: flag = True;
            While a < 10 && flag != False Do
                a = a +. 1.0;
                If a == 8.0 Then
                    flag = False;
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,134))

    def test35(self):
        """Testing boolean """
        input = """
        Function: main
        Body:
            Var: a = 5.0;
            If a == 5.0 || a >= 12.0 && a <= 6.0 Then
                a = 12.0;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,135))

    def test36(self):
        """Testing boolean missing operator """
        input = """
        Function: main
        Body:
            Var: a = 5.0;
            If a == 5.0 a >= 12.0 && a <= 6.0 Then
                a = 12.0;
            EndIf.
        EndBody.
        """
        expect = "Error on line 5 col 24: a"
        self.assertTrue(TestParser.checkParser(input,expect,136))
    
    def test37(self):
        """Testing boolean missing operator """
        input = """
        Function: main
        Body:
            Var: a = 5.0;
            If a == 5.0 a >= 12.0 && a <= 6.0 Then
                a = 12.0;
            EndIf.
        EndBody.
        """
        expect = "Error on line 5 col 24: a"
        self.assertTrue(TestParser.checkParser(input,expect,137))

    def test38(self):
        """Testing association - fail because it's not a expr """
        input = """
        Function: main
        Body:
            Var: a = 5.0;
            If a == 5.0 || a >= 12.0 && a <= 6.0 Then
                a = (((34 => 0-) < 6*(5 || 90)) =//= (4*9 - 5 >< 1)) == 1 ;
            EndIf.
        EndBody.
        """
        expect = "Error on line 6 col 26: ="
        self.assertTrue(TestParser.checkParser(input,expect,138))

    """5. Keyword"""
    def test39(self):
        """True False keyword"""
        input = """
        Function: main
        Body:
            Var: a = True;
            Var: b = False;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,139))

    def test40(self):
        """ Break and Continue Statement"""
        input = """
        Function: main
        Body:
            Var: i;
            Var: count = 100;
            For i = 0 , i < 10 ,2 Do
                If count == 105 Then
                    count = count + i;
                    Break;
                Else 
                    count = count + i;
                    Continue;
                EndIf.  
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,140))

    def test40(self):
        """ Break and Continue Statement - fail"""
        input = """
        Function: main
        Body:
            Var: i;
            Var: count = 100;
            For i = 0 , i < 10 ,2 Do
                If count == 105 Then
                    count = count + i;
                    break;
                Else 
                    count = count + i;
                    Continue;
                EndIf.  
            EndFor.
        EndBody.
        """
        expect = "Error on line 9 col 25: ;"
        self.assertTrue(TestParser.checkParser(input,expect,140))

    def test41(self):
        """ Break and Continue Statement - missing SM ;"""
        input = """
        Function: main
        Body:
            Var: i;
            Var: count = 100;
            For i = 0 , i < 10 ,2 Do
                If count == 105 Then
                    count = count + i;
                    Break
                Else 
                    count = count + i;
                    Continue;
                EndIf.  
            EndFor.
        EndBody.
        """
        expect = "Error on line 10 col 16: Else"
        self.assertTrue(TestParser.checkParser(input,expect,141))

    def test42(self):
        """ Break and Continue Statement - missing SM ;"""
        input = """
        Function: main
        Body:
            Var: i;
            Var: count = 100;
            For i = 0 , i < 10 ,2 Do
                If count == 105 Then
                    count = count + i;
                    Break
                Else 
                    count = count + i;
                    Continue;
                EndIf.  
            EndFor.
        EndBody.
        """
        expect = "Error on line 10 col 16: Else"
        self.assertTrue(TestParser.checkParser(input,expect,142))
    
    """6. If statement"""
    def test43(self):
        """ If statement - single if"""
        input = """
        Function: main
        Body:
            Var: i = 2;
            Var: count = 100;
            If count == 105 Then
                count = count + i;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,143))

    def test44(self):
        """ If statement - if-else"""
        input = """
        Function: main
        Body:
            Var: i = 2;
            Var: count = 100;
            If count == 105 Then
                count = count + i;              
            Else 
                count = count + i;
            EndIf.  
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,144))

    def test45(self):
        """ If statement - if-elseif-else """
        input = """
        Function: main
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
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,145))

    def test46(self):
        """ If statement - if-elseif-else """
        input = """
        Function: main
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
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,146))

    def test47(self):
        """ If statement fail with 2 else statement """
        input = """
        Function: main
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
            Else 
                count = count - i;
            EndIf.  
        EndBody.
        """
        expect = "Error on line 16 col 12: Else"
        self.assertTrue(TestParser.checkParser(input,expect,147))
    
    def test48(self):
        """ If statement fail : missing endif """
        input = """
        Function: main
        Body:
            Var: i = 2;
            Var: count = 100;
            If count == 105 Then
                count = count + i;    
            
        EndBody.
        """
        expect = "Error on line 9 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,148))

    def test49(self):
        """ If statement inside a if """
        input = """
        Function: main
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
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,149))

    """7. While statement"""
    def test50(self):
        """ While statement """
        input = """
        Function: main
        Body:
            Var: flag = True, a =2;
            Var: count = 100;
            While count < 10 && flag != False Do
                count = count +. 10;
                If count == 80 Then
                    flag = False;
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,150))
    
    def test51(self):
        """ While statement inside a While statement  """
        input = """
        Function: main
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
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,151))

    def test52(self):
        """ While statement fail : missing endwhile"""
        input = """
        Function: main
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
            
        EndBody.
        """
        expect = "Error on line 15 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,152))

    """7. Do-While statement"""
    def test53(self):
        """ Do-While statement """
        input = """
        Function: main
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
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,153))
    
    def test54(self):
        """ Do-While statement inside a Do-While statement  """
        input = """
        Function: main
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
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,154))

    def test55(self):
        """ Do-While statement fail : missing enddo"""
        input = """
        Function: main
        Body:
            Var: flag = True, a =2;
            Var: count = 100;
            Do
                count = count +. 10;
                If count == 80 Then
                    flag = False;
                EndIf.
            While count < 10 && flag != False 
            
        EndBody.
        """
        expect = "Error on line 13 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,155))

    """8. For statement"""
    def test56(self):
        """ For statement """
        input = """
        Function: main
        Body:
            Var: flag = True, a =2;
            Var: a[10];
            For i = 0 , i < 10 ,2 Do
                a[i] = i;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,156))
    
    def test57(self):
        """ For statement inside a For statement  """
        input = """
        Function: main
        Body:
            Var: flag = True, a =2;
            Var: a[10][10];
            For i = 0 , i < 10 ,2 Do
                For i = 0 , i < 10 ,2 Do
                    a[i][j]  = i+j;
                EndFor.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,157))

    def test58(self):
        """ Forstatement fail : missing endfor"""
        input = """
        Function: main
        Body:
            Var: flag = True, a =2;
            Var: a[10];
            For i = 0 , i < 10 ,2 Do
                a[i] = i;
            
        EndBody.
        """
        expect = "Error on line 9 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,158))

    """9. Funcall"""   
    def test59(self):
        """ Forstatement fail : missing endfor"""
        input = """
        Function: main
        Body:
            foo();
            fib();
            remove();
            get();
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,159))

    
    def test60(self):
        """ Func call missing ( or ) """
        input = """
        Function: main
        Body:
            foo();
            fib();
            remove();
            get(;
        EndBody.
        """
        expect = "Error on line 7 col 16: ;"
        self.assertTrue(TestParser.checkParser(input,expect,160))

    def test61(self):
        """ Func call with agruement """
        input = """
        Function: main
        Body:
            foo(1);
            fib(2+42+324\\234*24332);
            remove(3);
            get(4);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,161))

    def test62(self):
        """ Func call with fail agruement """
        input = """
        Function: main
        Body:
            foo(*);
            fib(&);
            remove(!);
            get());
        EndBody.
        """
        expect = "Error on line 4 col 16: *"
        self.assertTrue(TestParser.checkParser(input,expect,162))

    def test63(self):
        """ Func with return """
        input = """
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
                print(fib(n));
                read();
                Return 0;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,163))

    def test64(self):
        """ Func with error return """
        input = """
        Function: fib
            Parameter: n
            Body:
                If n <= 1 Then
                    Return n;
                EndIf.

                Return *;
            EndBody.
        
        """
        expect = "Error on line 9 col 23: *"
        self.assertTrue(TestParser.checkParser(input,expect,164))

    def test65(self):
        """ Func with error return """
        input = """
        Function: fib
            Parameter: n
            Body:
                If n <= 1 Then
                    Return n;
                EndIf.

                Return *;
            EndBody.
        
        """
        expect = "Error on line 9 col 23: *"
        self.assertTrue(TestParser.checkParser(input,expect,165))

    def test66(self):
        """ Character set """
        input = """
        Function: fib
            Parameter: n
            Body:
            Var: str = "string \\t";
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,166))

    def test67(self):
        """ Character set """
        input = """
        Function: fib
            Parameter: n
            Body:
            Var: str = "string \\r \\t \\\\ \\n \\f";
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,167))

    def test68(self):
        """ Commment line"""
        input = """
        ** this is comment ** 
        Function: fib
            Parameter: n
            Body:
            Var: str = "string \\r \\t \\\\ \\n";
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,168))

    def test69(self):
        """ Comment block """
        input = """
        ** this is comment 
         * hello
         * block commment
        ** 
        Function: fib
            Parameter: n
            Body:
            Var: str = "string \\r \\t \\\\ \\n";
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,169))

    def test70(self):
        """ Comment block """
        input = """
        ** this is comment 
        hello
        block commment
        **
        Function: fib
            Parameter: n
            Body:
            Var: str = "string \\r \\t \\\\ \\n";
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,170))

    def test71(self):
        """ Aissgnment - fail : missing assign op"""
        input = """
        Function: fib
            Parameter: n
            Body:
                Var: str = "string";
                str  "this is a string";
            EndBody.
        """
        expect = "Error on line 6 col 21: this is a string"
        self.assertTrue(TestParser.checkParser(input,expect,171))

    def test72(self):
        """ Var declaration - fail  """
        input = """
        Function: fib
            Parameter: n
            Body:
            Var: str = string \\r \\t \\\\ \\n;
            EndBody.
        """
        expect = """Error on line 5 col 37: \\"""
        self.assertTrue(TestParser.checkParser(input,expect,172))
    
    def test73(self):
        """ Array declaration - fail : missing { """
        input = """
        Function: fib
            Parameter: n
            Body:
            Var: array = {1,2,3;
            EndBody.
        """
        expect = "Error on line 5 col 25: {"
        self.assertTrue(TestParser.checkParser(input,expect,174))

    def test74(self):
        """ Statement """
        input = """
        Function: fib
            Parameter: n
            Body:
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,174))

    def test75(self):
        """ Statement """
        input = """
        Function: fib
            Parameter: n
            Body:
                Var: r = 10., v;
                v = (4. \. 3.) = 3.14 *. r *. r *. r;
            EndBody.
        """
        expect = "Error on line 6 col 31: ="
        self.assertTrue(TestParser.checkParser(input,expect,175))

    def test76(self):
        """ Error function in function"""
        input = """
        Function: fib
            Parameter: n
            Body:
                Function: foo
                    Parameter: a[5], b
                    Body:
                        Var: i = 0;
                        While (i < 5)
                            a[i] = b +. 1.0;
                            i = i + 1;
                        EndWhile.
                    EndBody.
            EndBody.
        """
        expect = "Error on line 5 col 16: Function"
        self.assertTrue(TestParser.checkParser(input,expect,176))

    def test77(self):
        """ Function missing name """
        input = """
        Function:
            Parameter: n
            Body:
                Function: foo
                    Parameter: a[5], b
                    Body:
                        Var: i = 0;
                        While (i < 5)
                            a[i] = b +. 1.0;
                            i = i + 1;
                        EndWhile.
                    EndBody.
            EndBody.
        """
        expect = "Error on line 3 col 12: Parameter"
        self.assertTrue(TestParser.checkParser(input,expect,177))

    def test78(self):
        """ Return multi time """
        input = """
        Function: hello
            Parameter: n
            Body:
                n = 0 + 1813694;
                Return ;
                Return n;
            EndBody.
        """
        expect = "Error on line 7 col 16: Return"
        self.assertTrue(TestParser.checkParser(input,expect,178))

    def test79(self):
        """ Return + break """
        input = """
        Function: hello
            Parameter: n
            Body:
                n = 0 + 1813694;
                Return Break;
            EndBody.
        """
        expect = "Error on line 6 col 23: Break"
        self.assertTrue(TestParser.checkParser(input,expect,179))

    def test80(self):
        """ Return + continue """
        input = """
        Function: hello
            Parameter: n
            Body:
                n = 0 + 1813694;
                Return Continue;
            EndBody.
        """
        expect = "Error on line 6 col 23: Continue"
        self.assertTrue(TestParser.checkParser(input,expect,180))

    def test81(self):
        """ Return multi time in different Statement """
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,181))

    def test82(self):
        """ Return multi time in different loop Statement """
        input = """
        Function: hello
            Parameter: n
            Body:
                If a == 1 Then
                    Return 1;
                EndIf.

                For i = 0 , i < 10 ,2 Do
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,182))


    def test83(self):
        """ Only comment """
        input = """
        Function: hello
            Parameter: n
            Body:
                If a == 1 Then
                    Return 1;
                EndIf.

                For i = 0 , i < 10 ,2 Do
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
        **
        """
        expect = "Error on line 27 col 8: <EOF>"

    def test82(self):
        """ Return multi time in different loop Statement """
        input = """
        Function: hello
            Parameter: n
            Body:
                If a == 1 Then
                    Return 1;
                EndIf.

                For i = 0 , i < 10 ,2 Do
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,182))


    def test84(self):
        """ Only comment """
        input = """
        Var: a =6;
        *****
        ** ***
        *** **
        """
        expect = "Error on line 4 col 13: *"
        self.assertTrue(TestParser.checkParser(input,expect,184))

    def test85(self):
        """  Missing CM"""
        input = """
        Var: a 3456789=-098767890-=6;
        *****
        ** ***
        *** **
        """
        expect = "Error on line 2 col 15: 3456789"
        self.assertTrue(TestParser.checkParser(input,expect,185))

    def test86(self):
        """  Missing { }"""
        input = """
        Var: a[5][5][5] = {2,234,23,2,2,,4,4}{23,3,,5,5,4,5};
        
        """
        expect = "Error on line 2 col 26: {"
        self.assertTrue(TestParser.checkParser(input,expect,186))

    def test87(self):
        """ Assignment wrong literal"""
        input = """
        Var: a[5][5][5] = "string" ;
        
        """
        expect = "Error on line 2 col 26: string"
        self.assertTrue(TestParser.checkParser(input,expect,187))

    def test88(self):
        """ Module """
        input = """
        Var: b = 48 \\% 12 ;
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,188))

    def test89(self):
        """ Unclosed string - token stringlit error """
        input = """
        Var: b = "string ;
        
        """
        expect = "string ;"
        self.assertTrue(TestParser.checkParser(input,expect,189))

    def test90(self):
        """ Missing { """
        input = """
        Var: b = {2,4,5,6 ;
        
        """
        expect = "Error on line 2 col 17: {"
        self.assertTrue(TestParser.checkParser(input,expect,190))

    def test91(self):
        """ Unclosed array - token stringlit error """
        input = """
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
                    For i = 0 , i < d ,i + 1 Do
                    n = n + 3.14;
                    EndFor.
                EndWhile.
                sum = sum*2 + m + n + d;
            Return sum;
        EndBody.
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,191))


    def test92(self):
        """ Unclosed array - token stringlit error """
        input = """
        Function: hellodoraemon
        Body:
            Parameter: n
        EndBody.
        
        """
        expect = "Error on line 4 col 12: Parameter"
        self.assertTrue(TestParser.checkParser(input,expect,192))

    def test93(self):
        """ Body in Body error """
        input = """
        Function: hellokitty
        Body:
            Body:
                Var: a =7;
            EndBody.
        EndBody.
        
        """
        expect = "Error on line 4 col 12: Body"
        self.assertTrue(TestParser.checkParser(input,expect,193))

    def test94(self):
        """ Missing { } """
        input = """
        Var: b[2][4] = {2,4,5,6},{1,3,4,3};
        
        """
        expect = "Error on line 2 col 33: {1,3,4,3}"
        self.assertTrue(TestParser.checkParser(input,expect,194))

    

    def test95(self):
        """ Unclosed array - token stringlit error """
        input = """
        ** hello *
        """
        expect = ""
        self.assertTrue(TestParser.checkParser(input,expect,195))

    def test96(self):
        """ Unclosed array - token stringlit error """
        input = """
        Function: main
        Body:
            Var: str = "This string have \\t";
            Var: str = "This string have \\f";
            Var: str = "This string have \\r";
            Var: str = "This string have \\b";
            Var: str = "This string have \\\\";
            Var: str = "This string have \\'";
            Var: str = "This string have '"";
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,196))

    def test97(self):
        """ If statement missing Then """
        input = """
        Function: main
        Body:
            If i == 12 
                i += 1
            EndIf.
        EndBody.
        """
        expect = "Error on line 5 col 16: i"
        self.assertTrue(TestParser.checkParser(input,expect,197))

    def test98(self):
        """ Do not have += operator """
        input = """
        Function: main
        Body:
            If i == 12 Then
                i += 1
            EndIf.
        EndBody.

        """
        expect = "Error on line 5 col 18: +"
        self.assertTrue(TestParser.checkParser(input,expect,198))

    def test99(self):
        """ NOT '!' operator """
        input = """
        Function: main
        Body:
            Var: a = True;
            Var: b = !a;
        EndBody.
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,199 ))

    def test100(self):
        """ Missing main function """
        input = """
        Var: b = True;
        a = !b;
        
        """
        expect = "Error on line 3 col 8: a"
        self.assertTrue(TestParser.checkParser(input,expect,200))

    def test201(self):
        """ Missing main function """
        input = """
        Var: a[1] = B;
        """
        expect = ""
        self.assertTrue(TestParser.checkParser(input,expect,201))

    