
import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    """1. 10 Testcase for Character set"""
    def test01(self):
        self.assertTrue(TestLexer.checkLexeme(""" ""","<EOF>",1))
    def test02(self):
        self.assertTrue(TestLexer.checkLexeme("""\t""","<EOF>",2))
    def test03(self):
        self.assertTrue(TestLexer.checkLexeme("""\r""","<EOF>",3))
    def test04(self):
        self.assertTrue(TestLexer.checkLexeme("""\n""","<EOF>",4))
    def test05(self):
        self.assertTrue(TestLexer.checkLexeme("""\f""","<EOF>",5))
    

    def test06(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",6))

    def test07(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,7))

    def test08(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",8))
    
    def test09(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",9))

    def test10(self):
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",10))

    
    """2. 10 Testcase for Array"""
    def test11(self):
        self.assertTrue(TestLexer.checkLexeme("a[5] = {{1,2,3,4,5},{1,2}}","a,[,5,],=,{{1,2,3,4,5},{1,2}},<EOF>",11))
    def test12(self):
        self.assertTrue(TestLexer.checkLexeme("Var: array[6] = {1,2,3,4,5,6},b[9];","Var,:,array,[,6,],=,{1,2,3,4,5,6},,,b,[,9,],;,<EOF>",12))
    def test13(self):
        self.assertTrue(TestLexer.checkLexeme("Var: stack[2][3] = {{1,2,3},{4,5,6}};","Var,:,stack,[,2,],[,3,],=,{{1,2,3},{4,5,6}},;,<EOF>",13))
    def test14(self):
        self.assertTrue(TestLexer.checkLexeme("Var: myQueue[6] = {{0,9,6,4,2,3,4}{}","""Var,:,myQueue,[,6,],=,{,{0,9,6,4,2,3,4},{},<EOF>""",14))
    def test15(self):
        self.assertTrue(TestLexer.checkLexeme("Var: list[3] = {1.65,6.34,hassad};","Var,:,list,[,3,],=,{,1.65,,,6.34,,,hassad,},;,<EOF>",15))
    def test16(self):
        self.assertTrue(TestLexer.checkLexeme("""Varr: pOint[4] = {"a","a","h"}""","""Var,r,:,pOint,[,4,],=,{"a","a","h"},<EOF>""",16))
    def test17(self):
        self.assertTrue(TestLexer.checkLexeme("""var: hello[2] ={"2",True}""","""var,:,hello,[,2,],=,{,2,,,True,},<EOF>""",17))
    def test18(self):
        self.assertTrue(TestLexer.checkLexeme("flagList[3] = {True,False}","flagList,[,3,],=,{True,False},<EOF>",18))
    def test19(self):
        self.assertTrue(TestLexer.checkLexeme("""** this is not a array token ** error[4]={True,1.65,"hehe",8}""" ,"""error,[,4,],=,{,True,,,1.65,,,hehe,,,8,},<EOF>""",19))
    def test20(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: a[2] = {1,2}, b[1] = {True}, c = {1.5,2.5} , d = {"abc","xyz"} , e[2] = {True,"False"}""","""Var,:,a,[,2,],=,{1,2},,,b,[,1,],=,{True},,,c,=,{1.5,2.5},,,d,=,{"abc","xyz"},,,e,[,2,],=,{,True,,,False,},<EOF>""",20))

    """3. 10 Testcase for Identifiers - done""" 
    def test21(self):
        self.assertTrue(TestLexer.checkLexeme("bc123","bc123,<EOF>",21))
    def test22(self):
        self.assertTrue(TestLexer.checkLexeme("qSFGBqGHWQ1357126GH13","qSFGBqGHWQ1357126GH13,<EOF>",22))
    def test23(self):
        self.assertTrue(TestLexer.checkLexeme("Eadasvsasdsbfg","Error Token E",23))
    def test24(self):
        self.assertTrue(TestLexer.checkLexeme("printPrefix","printPrefix,<EOF>",24))
    def test25(self):
        self.assertTrue(TestLexer.checkLexeme("func1","func1,<EOF>",25))
    def test26(self):
        self.assertTrue(TestLexer.checkLexeme("MTKH1040","Error Token M",26))
    def test27(self):
        self.assertTrue(TestLexer.checkLexeme("quan260402","quan260402,<EOF>",27))
    def test28(self):
        self.assertTrue(TestLexer.checkLexeme("02543eE45234234","02543,eE45234234,<EOF>",28))
    def test29(self):
        self.assertTrue(TestLexer.checkLexeme("bc123","bc123,<EOF>",29))
    def test30(self):
        self.assertTrue(TestLexer.checkLexeme("Quan","Error Token Q",30))


    """4. 20 Testcase for Keywords"""
    def test31(self):
        self.assertTrue(TestLexer.checkLexeme("""
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact(n-1);
                EndIf.
            EndBody. 

        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody.

        ""","""Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>""",31))
    def test32(self):
        self.assertTrue(TestLexer.checkLexeme("""
            Var: a=5;
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            Var: c,d = 6,e,f;
            Var: m,n[10];
        ""","""Var,:,a,=,5,;,Var,:,b,[,2,],[,3,],=,{{2,3,4},{4,5,6}},;,Var,:,c,,,d,=,6,,,e,,,f,;,Var,:,m,,,n,[,10,],;,<EOF>""",32))
    def test33(self):
        self.assertTrue(TestLexer.checkLexeme("""
        Function: foo
        Parameter: a[5],b
        Body:
            Var: i =0;
            While i<5 Do
                a[i] = b +. 10;
                i = i + 1;
            EndWhile.
        EndBody.
        ""","""Function,:,foo,Parameter,:,a,[,5,],,,b,Body,:,Var,:,i,=,0,;,While,i,<,5,Do,a,[,i,],=,b,+.,10,;,i,=,i,+,1,;,EndWhile,.,EndBody,.,<EOF>""",33))
    def test34(self):
        self.assertTrue(TestLexer.checkLexeme("""
        If bool_of_string("True") Then
            a = int_of_string(read());
            b = float_of_int(a + 2.0;
        EndIf.
        ""","""If,bool_of_string,(,True,),Then,a,=,int_of_string,(,read,(,),),;,b,=,float_of_int,(,a,+,2.0,;,EndIf,.,<EOF>""",34))
    def test35(self):
        self.assertTrue(TestLexer.checkLexeme("""
        Body:
            Var: r = 10. , v;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody.
        ""","""Body,:,Var,:,r,=,10.,,,v,;,v,=,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,EndBody,.,<EOF>""",35))
    def test36(self):
        self.assertTrue(TestLexer.checkLexeme("""
        For i = 0 , i < 10 ,2 Do
            writeln(i);
        EndFor.
        ""","""For,i,=,0,,,i,<,10,,,2,Do,writeln,(,i,),;,EndFor,.,<EOF>""",36))
    def test37(self):
        self.assertTrue(TestLexer.checkLexeme("""
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

        ""","""Function,:,fib,Parameter,:,n,Body,:,If,n,<=,1,Then,Return,n,;,EndIf,.,Return,fib,(,n,-,1,),+,fib,(,n,-,2,),;,EndBody,.,Function,:,main,Body,:,Var,:,n,=,9,;,print,(,fib,(,n,),),;,read,(,),;,Return,0,;,EndBody,.,<EOF>""",37))
    def test38(self):
        self.assertTrue(TestLexer.checkLexeme("""
        Function: fib
            Parameter: n
            Body:
                Var: f[n + 1],i;

                f[0] = 0;
                f[1] = 1;

                For i = 2 , i <= n , i = i + 1 Do 
                    f[i] = f[i - 1] + f[i - 2];
                EndDO

                Return f[n];
            EndBody.

        Function: main
            Body:
                Var: n = 9;
                print(fib(n));
                read();
                Return 0;
            EndBody.

        ""","""Function,:,fib,Parameter,:,n,Body,:,Var,:,f,[,n,+,1,],,,i,;,f,[,0,],=,0,;,f,[,1,],=,1,;,For,i,=,2,,,i,<=,n,,,i,=,i,+,1,Do,f,[,i,],=,f,[,i,-,1,],+,f,[,i,-,2,],;,Error Token E""",38))
    def test39(self):
        self.assertTrue(TestLexer.checkLexeme("""
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
                print(add(a,b));
                print(sub(a,b));
                Return 0;
            EndBody.

        ""","""Function,:,add,Parameter,:,a,,,b,Body,:,Var,:,x,=,0.0,;,x,=,a,+.,b,;,Return,x,;,EndBody,.,Function,:,sub,Parameter,:,a,,,b,Body,:,Var,:,x,=,0.0,;,x,=,a,-.,b,;,Return,x,;,EndBody,.,Function,:,main,Body,:,Var,:,a,=,9.0,,,b,=,2.0,;,print,(,add,(,a,,,b,),),;,print,(,sub,(,a,,,b,),),;,Return,0,;,EndBody,.,<EOF>""",39))
    def test40(self):
        self.assertTrue(TestLexer.checkLexeme("""
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
                print(mul(a,b));
                print(div(a,b));
                Return 0;
            EndBody.

        ""","""Function,:,mul,Parameter,:,a,,,b,Body,:,Var,:,x,=,0.0,;,x,=,a,*.,b,;,Return,x,;,EndBody,.,Function,:,div,Parameter,:,a,,,b,Body,:,Var,:,x,=,0.0,;,x,=,a,\.,b,;,Return,x,;,EndBody,.,Function,:,main,Body,:,Var,:,a,=,9.0,,,b,=,2.0,;,print,(,mul,(,a,,,b,),),;,print,(,div,(,a,,,b,),),;,Return,0,;,EndBody,.,<EOF>""",40))
    
    """4.b. 20 Testcase for String literals"""
    def test41(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string" ""","""This is a string,<EOF>""",41))
    def test42(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \\t" ""","""This is a string containing tab \\t,<EOF>""",42))
    def test43(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing backspace \\b" ""","""This is a string containing backspace \\b,<EOF>""",43))
    def test44(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing form feed \\f" ""","""This is a string containing form feed \\f,<EOF>""",44))
    def test45(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing carriage return \\r" ""","""This is a string containing carriage return \\r,<EOF>""",45))
    def test46(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing newline \\n" ""","""This is a string containing newline \\n,<EOF>""",46))
    def test47(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing backslash \\\\" ""","""This is a string containing backslash \\\\,<EOF>""",47))
    def test48(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing \\' single quote " ""","""This is a string containing \\' single quote ,<EOF>""",48))
    def test49(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing double quote '"" ""","""This is a string containing double quote '",<EOF>""",49))
    def test50(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'"" ""","""He asked me: '"Where is John?'",<EOF>""",50))


    """5. 10 Testcase for Operator - done"""
    def test51(self):
        self.assertTrue(TestLexer.checkLexeme("+ +.","+,+.,<EOF>",51))
    def test52(self):
        self.assertTrue(TestLexer.checkLexeme("- -.","-,-.,<EOF>",52))
    def test53(self):
        self.assertTrue(TestLexer.checkLexeme("* *.","*,*.,<EOF>",53))
    def test54(self):
        self.assertTrue(TestLexer.checkLexeme("\\ \\.","\\,\\.,<EOF>",54))
    def test55(self):
        self.assertTrue(TestLexer.checkLexeme("<= <=.","<=,<=.,<EOF>",55))
    def test56(self):
        self.assertTrue(TestLexer.checkLexeme(">= >=.",">=,>=.,<EOF>",56))
    def test57(self):
        self.assertTrue(TestLexer.checkLexeme("> >. < <.",">,>.,<,<.,<EOF>",57))
    def test58(self):
        self.assertTrue(TestLexer.checkLexeme("=/=","=/=,<EOF>",58))
    def test59(self):
        self.assertTrue(TestLexer.checkLexeme("==","==,<EOF>",59))
    def test60(self):
        self.assertTrue(TestLexer.checkLexeme("++.--.**.\\.\\<=>=><>>.<<.=/===","+,+.,-,-.,Unterminated Comment",60))


    """6. 10 Testcase for Separators - done"""
    def test61(self):
        self.assertTrue(TestLexer.checkLexeme(",",",,<EOF>",61))
    def test62(self):
        self.assertTrue(TestLexer.checkLexeme("(","(,<EOF>",62))
    def test63(self):
        self.assertTrue(TestLexer.checkLexeme(")","),<EOF>",63))
    def test64(self):
        self.assertTrue(TestLexer.checkLexeme("{","{,<EOF>",64))
    def test65(self):
        self.assertTrue(TestLexer.checkLexeme("}","},<EOF>",65))
    def test66(self):
        self.assertTrue(TestLexer.checkLexeme("[","[,<EOF>",66))
    def test67(self):
        self.assertTrue(TestLexer.checkLexeme("]","],<EOF>",67))
    def test68(self):
        self.assertTrue(TestLexer.checkLexeme(":",":,<EOF>",68))
    def test69(self):
        self.assertTrue(TestLexer.checkLexeme(";",";,<EOF>",69))
    def test70(self):
        self.assertTrue(TestLexer.checkLexeme(".",".,<EOF>",70))

    """7. 10 Testcase for Int literal - done"""
    def test71(self):
        self.assertTrue(TestLexer.checkLexeme("0X0402","0X0402,<EOF>",71))
    def test72(self):
        self.assertTrue(TestLexer.checkLexeme("0","0,<EOF>",72))
    def test73(self):
        self.assertTrue(TestLexer.checkLexeme("-0","-,0,<EOF>",73))
    def test74(self):
        self.assertTrue(TestLexer.checkLexeme("0XABC","0XABC,<EOF>",74))
    def test75(self):
        self.assertTrue(TestLexer.checkLexeme("0o567","0o567,<EOF>",75))
    def test76(self):
        self.assertTrue(TestLexer.checkLexeme("0O1349123","0O134,9123,<EOF>",76))
    def test77(self):
        self.assertTrue(TestLexer.checkLexeme("0x180976","0x180976,<EOF>",77))
    def test78(self):
        self.assertTrue(TestLexer.checkLexeme("0zX12912123","0,zX12912123,<EOF>",78))
    def test79(self):
        self.assertTrue(TestLexer.checkLexeme("0X123","0X123,<EOF>",79))
    def test80(self):
        self.assertTrue(TestLexer.checkLexeme("180976e-1233112","180976e-1233112,<EOF>",80))
        
    """8. 10 Testcase for Float literal - done"""
    def test81(self):
        self.assertTrue(TestLexer.checkLexeme("1e-12","1e-12,<EOF>",81))    
    def test82(self):
        self.assertTrue(TestLexer.checkLexeme("+2.2","+,2.2,<EOF>",82))
    def test83(self):
        self.assertTrue(TestLexer.checkLexeme("-1123441.012e-12112","-,1123441.012e-12112,<EOF>",83))
    def test84(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3","12.0e3,<EOF>",84))
    def test85(self):
        self.assertTrue(TestLexer.checkLexeme("0.000000001","0.000000001,<EOF>",85))
    def test86(self):
        self.assertTrue(TestLexer.checkLexeme("1.0E+12","1.0E+12,<EOF>",86))
    def test87(self):
        self.assertTrue(TestLexer.checkLexeme("+24245.04242422001","+,24245.04242422001,<EOF>",87))
    def test88(self):
        self.assertTrue(TestLexer.checkLexeme("-0.23478268342","-,0.23478268342,<EOF>",88))
    def test89(self):
        self.assertTrue(TestLexer.checkLexeme("12E3","12E3,<EOF>",89))
    def test90(self):
        self.assertTrue(TestLexer.checkLexeme("1.0","1.0,<EOF>",80))

    """9. 5 Testcase for Boolen literal - done"""
    def test91(self):
        self.assertTrue(TestLexer.checkLexeme("TRUE","Error Token T",91))
    def test92(self):
        self.assertTrue(TestLexer.checkLexeme("FALSE","Error Token F",92))
    def test93(self):
        self.assertTrue(TestLexer.checkLexeme("False","False,<EOF>",93))
    def test94(self):
        self.assertTrue(TestLexer.checkLexeme("false ","false,<EOF>",94))
    def test95(self):
        self.assertTrue(TestLexer.checkLexeme("True","True,<EOF>",95))
   
    """10. 5 Testcase for Comment """
    def test96(self):
        self.assertTrue(TestLexer.checkLexeme("""
        ** This is a single-line comment. **
        ** This is a
        * multi-line
        * comment.
        **
        ""","<EOF>",96))
    def test97(self):
        self.assertTrue(TestLexer.checkLexeme("** this is comment","Unterminated Comment",97))
    def test98(self):
        self.assertTrue(TestLexer.checkLexeme("""
        ** ***
        *** **
        *****
        ""","*,<EOF>",98))
    def test99(self):
        self.assertTrue(TestLexer.checkLexeme("** hello **","<EOF>",99))
    def test100(self):
        self.assertTrue(TestLexer.checkLexeme("""** 00.00 \te6 **""","<EOF>",100))
    


