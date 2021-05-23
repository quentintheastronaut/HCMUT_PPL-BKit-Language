

import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

from main.bkit.checker.StaticError import Parameter, Variable
from main.bkit.utils.AST import ArrayCell, ArrayLiteral, BinaryOp, BooleanLiteral, CallExpr, CallStmt, Dowhile, FloatLiteral, FuncDecl, Id, IntLiteral, Program, StringLiteral, VarDecl

class CheckSuite(unittest.TestCase):

    def testcase400(self):
        """Simple program: main"""
        input = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],IntLiteral(3)),VarDecl(Id("a"),[],None),FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )])
        expect = str(Redeclared(Variable(),"a"))
        self.assertTrue(TestChecker.test(input,expect,400))

    def testcase401(self):
        """Simple program: main"""
        input = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],IntLiteral(3)),VarDecl(Id("c"),[],IntLiteral(3)),VarDecl(Id("d"),[],IntLiteral(3)),FuncDecl(Id("a"),[],([],[])),FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )])
        expect = str(Redeclared(Function(),"a"))
        self.assertTrue(TestChecker.test(input,expect,401))

    def testcase402(self):
        """Simple program: main"""
        input = Program([
                VarDecl(Id("b"),[],IntLiteral(3)),
                FuncDecl(
                    Id("a"),
                    [VarDecl(Id("a"),[],None),VarDecl(Id("a"),[],None)],
                    (
                        [
                            VarDecl(Id("c"),[],IntLiteral(3)),
                            VarDecl(Id("b"),[],IntLiteral(3)),
                            VarDecl(Id("c"),[],IntLiteral(3))],[])),
                            
                            FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )])
        expect = str(Redeclared(Parameter(),"a"))
        self.assertTrue(TestChecker.test(input,expect,402))

    def testcase403(self):
        """Simple program: main"""
        input = Program([VarDecl(Id("b"),[],IntLiteral(3)),FuncDecl(Id("a"),[VarDecl(Id("a"),[],None)],([VarDecl(Id("c"),[],IntLiteral(3)),VarDecl(Id("b"),[],IntLiteral(3)),VarDecl(Id("c"),[],IntLiteral(3))],[])),
        FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )])
        expect = str(Redeclared(Variable(),"c"))
        self.assertTrue(TestChecker.test(input,expect,403))

    def testcase404(self):
        """Simple program: main"""
        input = Program([VarDecl(Id("a"),[],IntLiteral(3)),VarDecl(Id("b"),[],IntLiteral(3)),FuncDecl(Id("c"),[],([],[Assign(Id("d"),IntLiteral(3))])),
        FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )])
        expect = """Undeclared Identifier: d"""
        self.assertTrue(TestChecker.test(input,expect,404))

    def testcase405(self):
        """Simple program: main"""
        input = Program(
            [
                VarDecl(Id("a"),[],None),
                FuncDecl(
                    Id("c"),
                    [],
                    (
                        [

                        ],
                        [
                            Assign(Id("a"),IntLiteral(3)),
                            CallStmt(Id("foo"),[IntLiteral(2),IntLiteral(3)])
                        ]
                    )
                ),
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )
            ]
        )
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input,expect,405))

    def testcase406(self):
        """Simple program: main"""
        input = """Function: main
                   Body: 
                        foo();
                   EndBody.
                   """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,406))

    def testcase407(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(
                    Id("main")
                    ,[]
                    ,(
                        [],
                        [
                            CallStmt(Id("printStrLn"),[])
                        ]
                    )
                )
            ]
        )
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,407))
    
    def testcase408(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,408))

    def testcase409(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,409))

    def testcase410(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,410))


    # 10 testcase trong bài name:

    def testcase411(self):
        """Simple program: main"""
        input = x = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),FuncDecl(Id("a"),[],([],[])),
        FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )])
        expect = """Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input,expect,411))

    def testcase412(self):
        """Simple program: main"""
        input = Program(
            [
                VarDecl(Id("b"),[],None),
                FuncDecl(
                    Id("a"),
                    [VarDecl(Id("a"),[],None)],
                    (
                        [
                            VarDecl(Id("c"),[],None),
                            VarDecl(Id("b"),[],None),
                            VarDecl(Id("c"),[],None)
                        ],
                        []
                    )
                ),
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )
            ]
        )
        expect = """Redeclared Variable: c"""
        self.assertTrue(TestChecker.test(input,expect,412))

    def testcase413(self):
        """Simple program: main"""
        input = Program([VarDecl(Id("b"),[],None),FuncDecl(Id("a"),[VarDecl(Id("m"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("m"),[],None)],([],[])),FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )])
        expect = """Redeclared Parameter: m"""
        self.assertTrue(TestChecker.test(input,expect,413))

    def testcase414(self):
        """Simple program: main"""
        input = Program([VarDecl(Id("b"),[],None),FuncDecl(Id("a"),[VarDecl(Id("m"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("d"),[],None)],([VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],None)],[])),FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )])
        expect = """Redeclared Variable: d"""
        self.assertTrue(TestChecker.test(input,expect,414))

    def testcase415(self):
        """Simple program: main"""
        input = Program([VarDecl(Id("b"),[],None),FuncDecl(Id("a"),[VarDecl(Id("m"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("d"),[],None)],([VarDecl(Id("c"),[],None),FuncDecl(Id("d"),[],([],[]))],[])),FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )])
        expect = """Redeclared Function: d"""
        self.assertTrue(TestChecker.test(input,expect,415))

    def testcase416(self):
        """Simple program: main"""
        input = Program([VarDecl(Id("b"),[],None),FuncDecl(Id("a"),[VarDecl(Id("m"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("d"),[],None)],([VarDecl(Id("c"),[],None),FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([VarDecl(Id("x"),[],None)],[]))],[])),FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )])
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input,expect,416))

    def testcase417(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("b"),[],None),
                FuncDecl(
                    Id("a"),
                    [
                        VarDecl(Id("m"),[],None),
                        VarDecl(Id("b"),[],None),
                        VarDecl(Id("d"),[],None)
                    ],
                    (
                        [
                            VarDecl(Id("c"),[],None),
                            FuncDecl(
                                Id("foo"),
                                [
                                    VarDecl(Id("x"),[],None)
                                ],
                                (
                                    [
                                        VarDecl(Id("y"),[],None),
                                        VarDecl(Id("z"),[],None)
                                    ],
                                    [
                                        Assign(Id("x"),IntLiteral(3)),
                                        Assign(Id("y"),IntLiteral(3)),
                                        CallStmt(Id("foo"),[IntLiteral(1)]),
                                        Assign(Id("c"),IntLiteral(3)),
                                        Assign(Id("m"),IntLiteral(3)),
                                        CallStmt(Id("a"),[IntLiteral(2),IntLiteral(2),IntLiteral(2)]),
                                    ]
                                )
                            )
                        ],
                        [
                            CallStmt(Id("foo"),[IntLiteral(3)]),
                            Assign(Id("d"),IntLiteral(3)),
                            Assign(Id("z"),IntLiteral(3))
                        ]
                    )
                ),
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )
            ]
        )
        expect = """Undeclared Identifier: z"""
        self.assertTrue(TestChecker.test(input,expect,417))

    def testcase418(self):
        """Simple program: main"""
        input = Program(
            [
                VarDecl(Id("b"),[],None),
                FuncDecl(
                    Id("a"),
                    [
                        VarDecl(Id("m"),[],None),
                        VarDecl(Id("b"),[],None),
                        VarDecl(Id("n"),[],None)
                    ],
                    (
                        [
                            VarDecl(Id("c"),[],None),
                            VarDecl(Id("d"),[],None)
                        ],
                        [
                            Assign(Id("b"),IntLiteral(3)),
                            Assign(Id("c"),IntLiteral(3)),
                            Assign(Id("d"),IntLiteral(3)),
                            Assign(Id("m"),IntLiteral(3)),
                            Assign(Id("q"),IntLiteral(3)),
                            Assign(Id("n"),IntLiteral(3))
                        ]
                    )
                ),
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )
            ]
        )
        expect = """Undeclared Identifier: q"""
        self.assertTrue(TestChecker.test(input,expect,418))

    def testcase419(self):
        """Simple program: main"""
        
        input = x = Program(
                    [
                        VarDecl(Id("b"),[],None),
                        FuncDecl(
                            Id("a"),
                            [VarDecl(Id("m"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("d"),[],None)],
                            (
                                [
                                    VarDecl(Id("c"),[],None),
                                    FuncDecl(
                                        Id("foo"),
                                        [VarDecl(Id("x"),[],None)],
                                        (
                                            [
                                                VarDecl(Id("y"),[],None),
                                                VarDecl(Id("z"),[],None)
                                            ],
                                            [
                                                Assign(Id("y"),IntLiteral(3)),
                                                Assign(Id("x"),IntLiteral(3)),
                                                CallStmt(Id("foo"),[IntLiteral(1)]),
                                                Assign(Id("c"),IntLiteral(3)),
                                                Assign(Id("m"),IntLiteral(3)),
                                                CallStmt(Id("a"),[IntLiteral(2),IntLiteral(2),IntLiteral(3)])
                                            ]
                                        )
                                    ),
                                    FuncDecl(
                                        Id("foo1"),
                                        [],
                                        (
                                            [

                                            ],
                                            [
                                                CallStmt(Id("foo"),[IntLiteral(2)]),
                                                Assign(Id("d"),IntLiteral(3)),
                                                Assign(Id("x"),IntLiteral(3)),
                                            ]
                                        )
                                    )
                                ],
                                [
                                    CallStmt(Id("foo1"),[]),
                                    Assign(Id("d"),IntLiteral(3)),
                                    CallStmt(Id("foo1"),[])
                                ]
                             )
                        ),
                        FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )
                    ]
        )
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input,expect,419))

    def testcase420(self):
        """Simple program: main"""
        input = Program(
            [
                VarDecl(Id("a"),[],IntLiteral(3)),
                VarDecl(Id("b"),[],IntLiteral(3)),
                FuncDecl(
                    Id("c"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("a"),IntLiteral(3)),
                            Assign(Id("a"),IntLiteral(3)),
                            Assign(Id("b"),IntLiteral(3))])
                ),

                            FuncDecl(
                                Id("e"),
                                [],
                                (
                                    [],
                    [
                                        Assign(Id("a"),IntLiteral(3)),
                                        Assign(Id("d"),IntLiteral(3)),
                                        Assign(Id("b"),IntLiteral(3))])
                    ),

                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )

            ]
        )
        expect = """Undeclared Identifier: d"""
        self.assertTrue(TestChecker.test(input,expect,420))


    def testcase421(self):
        """Simple program: main"""
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                FuncDecl(
                    Id("foo"),
                    [
                        VarDecl(Id("y"),[],None),
                        VarDecl(Id("z"),[],None)
                    ],
                    (
                        [],
                        [
                            CallStmt(Id("foo"),[IntLiteral(3),Id("x")])
                        ]
                    )
                ),
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )
            ]
        )
        expect = """Type Cannot Be Inferred: CallStmt(Id(foo),[IntLiteral(3),Id(x)])"""
        self.assertTrue(TestChecker.test(input,expect,421))

    def testcase422(self):
        """Simple program: main"""
      
        input = Program(
            [
                VarDecl(Id("t"),[],None),
                FuncDecl(
                    Id("foo"),
                    [
                        VarDecl(Id("x"),[],None)
                    ],
                    (
                        [

                        ],
                        [
                            Assign(Id("t"),FloatLiteral(2)),
                            CallStmt(Id("foo"),[Id("t")]),
                            CallStmt(Id("foo"),[IntLiteral(2)])
                        ]
                    )
                ),
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )
            ]
        )
        expect = """Type Mismatch In Statement: CallStmt(Id(foo),[IntLiteral(2)])"""
        self.assertTrue(TestChecker.test(input,expect,422))

    def testcase423(self):
        """Simple program: main"""
       
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            FuncDecl(
                                Id("foo"),
                                [VarDecl(Id("x"),[],None)],
                                (
                                    [],
                                    [Assign(Id("x"),FloatLiteral(2))]
                                )
                            ),
                        ],
                        [
                            Assign(Id("x"),FloatLiteral(2)),
                            Assign(Id("x"),IntLiteral(3)),
                            CallStmt(Id("foo"),[Id("x")])
                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Statement: Assign(Id(x),IntLiteral(3))"""
        self.assertTrue(TestChecker.test(input,expect,423))

    def testcase424(self):
        """Simple program: main"""
      
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            FuncDecl(
                                Id("foo"),
                                [VarDecl(Id("y"),[],None)],
                                (
                                    [
                                        
                                    ],
                                    [
                                        Assign(Id("y"),FloatLiteral(2)),
                                    ]
                                )
                            ),
                        ],
                        [
                            Assign(Id("x"),IntLiteral(3)),
                            CallStmt(Id("foo"),[Id("x")])
                            
                        ]
                    )
                ),
                
            ]
        )
        expect = """Type Mismatch In Statement: CallStmt(Id(foo),[Id(x)])"""
        self.assertTrue(TestChecker.test(input,expect,424))

    def testcase425(self):
        """Simple program: main"""
      
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                

                FuncDecl(
                    Id("foo"),
                    [],
                    (
                        [
                            VarDecl(Id("y"),[],None)

                        ],
                        [
                            Assign(Id("x"),IntLiteral(3)),
                            Assign(Id("x"),Id("y")),
                            Assign(Id("y"),BooleanLiteral(True))
                        ]
                    )
                ),

                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        []
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Statement: Assign(Id(y),BooleanLiteral(true))"""
        self.assertTrue(TestChecker.test(input,expect,425))

    def testcase426(self):
        """Simple program: main"""
     
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                

                FuncDecl(
                    Id("foo"),
                    [],
                    (
                        [
                            VarDecl(Id("y"),[],None)

                        ],
                        [
                            Assign(Id("x"),IntLiteral(3)),
                            Assign(Id("x"),Id("y")),
                            
                        ]
                    )
                ),

                FuncDecl(
                    Id("foo1"),
                    [],
                    (
                        [],
                        []
                    )
                )
                
                
            ]
        )
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input,expect,426))

    def testcase427(self):
        """Simple program: main"""
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
            

                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("x"),Id("y"))
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Cannot Be Inferred: Assign(Id(x),Id(y))"""
        self.assertTrue(TestChecker.test(input,expect,427))

    def testcase428(self):
        """Simple program: main"""
        input = Program(
            [
                VarDecl(Id("x"),[],None),
            

                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [Assign(Id("x"),BinaryOp("+",IntLiteral(3),BooleanLiteral(True)))]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Expression: BinaryOp(+,IntLiteral(3),BooleanLiteral(true))"""
        self.assertTrue(TestChecker.test(input,expect,428))

    def testcase429(self):
        """Simple program: main"""
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                VarDecl(Id("z"),[],None),
            

                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("x"),BinaryOp("||",BinaryOp("&&",Id("x"),Id("y")),BinaryOp("||",BooleanLiteral(False),BinaryOp(">",Id("z"),IntLiteral(3))))),
                            Assign(Id("z"),Id("x"))
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Statement: Assign(Id(z),Id(x))"""
        self.assertTrue(TestChecker.test(input,expect,429))

    def testcase430(self):
        """Simple program: main"""
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                VarDecl(Id("z"),[],None),
            

                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("x"),FloatLiteral(3.0)),
                            Assign(Id("x"),Id("y")),
                            Assign(Id("z"),BinaryOp(">",IntLiteral(3),Id("y")))
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Expression: BinaryOp(>,IntLiteral(3),Id(y))"""
        self.assertTrue(TestChecker.test(input,expect,430))

    def testcase431(self):
        """Simple program: main"""
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                VarDecl(Id("z"),[],None),
            

                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("x"),UnaryOp("-.",IntLiteral(3.0))),
                            
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Expression: UnaryOp(-.,IntLiteral(3.0))"""
        self.assertTrue(TestChecker.test(input,expect,431))

    def testcase432(self):
        """Simple program: main"""
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                VarDecl(Id("z"),[],None),
            

                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("x"),UnaryOp("-",FloatLiteral(3.0))),
                            
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Expression: UnaryOp(-,FloatLiteral(3.0))"""
        self.assertTrue(TestChecker.test(input,expect,432))

    def testcase433(self):
        """Simple program: main"""
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                VarDecl(Id("z"),[],None),
            

                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("x"),UnaryOp("-",FloatLiteral(3.0))),
                            
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Expression: UnaryOp(-,FloatLiteral(3.0))"""
        self.assertTrue(TestChecker.test(input,expect,433))

    def testcase433(self):
        """Simple program: main"""
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                VarDecl(Id("z"),[],None),
            

                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("y"),FloatLiteral(3.0)),
                            Assign(Id("x"),UnaryOp("!",Id("y"))),
                            
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Expression: UnaryOp(!,Id(y))"""
        self.assertTrue(TestChecker.test(input,expect,433))

    def testcase434(self):
        """Simple program: main"""
       
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                VarDecl(Id("z"),[],None),
                FuncDecl(
                    Id("foo"),
                    [
                        VarDecl(Id("a"),[],None),
                        VarDecl(Id("b"),[],None),
                        VarDecl(Id("c"),[],None)
                    ],
                    (
                        [],
                        [
                            Assign(Id("a"),IntLiteral(3)),
                            Assign(Id("b"),IntLiteral(3)),
                            Assign(Id("c"),IntLiteral(3)),
                            Return(FloatLiteral(5.5))
                        ]
                    )
                ),
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("x"),IntLiteral(3)),
                            Assign(Id("z"),IntLiteral(3)),
                            Assign(Id("x"),CallExpr(Id("foo"),[Id("z"),Id("z"),Id("z")])),
                            
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Statement: Assign(Id(x),CallExpr(Id(foo),[Id(z),Id(z),Id(z)]))"""
        self.assertTrue(TestChecker.test(input,expect,434))


    def testcase435(self):
        """Simple program: main"""
       
        input = Program(
            [
                VarDecl(Id("x"),[2],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),
                
                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            
                        ]
                    )
                )
                
                
            ]
        )
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,435))

    def testcase436(self):
        """Simple program: main"""
     
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                VarDecl(Id("z"),[],None),
                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("x"),FloatLiteral(3.0)),
                            Assign(Id("y"),BooleanLiteral(True)),
                            Assign(Id("x"),CallExpr(Id("float_of_int"),[UnaryOp("-.",IntLiteral(3.0))])),
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Expression: UnaryOp(-.,IntLiteral(3.0))"""
        self.assertTrue(TestChecker.test(input,expect,436))

    def testcase437(self):
        """Simple program: main"""

        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                VarDecl(Id("z"),[],None),
                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            
                            Assign(Id("y"),BooleanLiteral(True)),
                            Assign(Id("x"),CallExpr(Id("string_of_int"),[UnaryOp("-",IntLiteral(3.0))])),
                            CallStmt(Id("print"),[Id("y")])
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Statement: CallStmt(Id(print),[Id(y)])"""
        self.assertTrue(TestChecker.test(input,expect,437))

    def testcase438(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                VarDecl(Id("z"),[],None),
                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            
                            Assign(Id("y"),BooleanLiteral(True)),
                            Assign(Id("x"),CallExpr(Id("string_of_int"),[UnaryOp("-",IntLiteral(3.0))])),
                            CallStmt(Id("printLn"),[]),
                            CallStmt(Id("printLn"),[Id("y")])
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Statement: CallStmt(Id(printLn),[Id(y)])"""
        self.assertTrue(TestChecker.test(input,expect,438))

    def testcase439(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                VarDecl(Id("z"),[],None),
                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            
                            Assign(Id("y"),BooleanLiteral(True)),
                            Assign(Id("x"),CallExpr(Id("string_of_int"),[UnaryOp("-",IntLiteral(3.0))])),
                            CallStmt(Id("printLn"),[]),
                            CallStmt(Id("printLn"),[Id("y")])
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Statement: CallStmt(Id(printLn),[Id(y)])"""
        self.assertTrue(TestChecker.test(input,expect,439))

    def testcase440(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                VarDecl(Id("z"),[],None),
                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            CallStmt(Id("printLn"),[]),
                            CallStmt(Id("print"),[StringLiteral("Alo ban ei")]),
                            CallStmt(Id("print"),[BinaryOp("||",BinaryOp("&&",Id("x"),Id("y")),BinaryOp("||",BooleanLiteral(False),BinaryOp(">",Id("z"),IntLiteral(3))))])
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Statement: CallStmt(Id(print),[BinaryOp(||,BinaryOp(&&,Id(x),Id(y)),BinaryOp(||,BooleanLiteral(false),BinaryOp(>,Id(z),IntLiteral(3))))])"""
        self.assertTrue(TestChecker.test(input,expect,440))

    def testcase441(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                VarDecl(Id("z"),[],None),
                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            CallStmt(Id("printLn"),[]),
                            CallStmt(Id("print"),[StringLiteral("Alo ban ei")]),
                            CallStmt(
                                Id("printStrLn"),
                                [
                                    CallExpr(
                                        Id("string_of_float"),
                                        [
                                            BinaryOp("||",BinaryOp("&&",Id("x"),Id("y")),BinaryOp("||",BooleanLiteral(False),BinaryOp(">",Id("z"),IntLiteral(3))))
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Expression: CallExpr(Id(string_of_float),[BinaryOp(||,BinaryOp(&&,Id(x),Id(y)),BinaryOp(||,BooleanLiteral(false),BinaryOp(>,Id(z),IntLiteral(3))))])"""
        self.assertTrue(TestChecker.test(input,expect,441))

    def testcase442(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                VarDecl(Id("z"),[],None),
                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            CallStmt(Id("printLn"),[]),
                            CallStmt(Id("print"),[StringLiteral("Alo ban ei")]),
                            CallStmt(
                                Id("printStrLn"),
                                [
                                    CallExpr(
                                        Id("bool_of_string")
                                        ,
                                            [CallExpr(
                                                Id("string_of_bool"),
                                                [
                                                    BinaryOp("||",BinaryOp("&&",Id("x"),Id("y")),BinaryOp("||",BooleanLiteral(False),BinaryOp(">",Id("z"),IntLiteral(3))))
                                                ]
                                            )
                                        ]
                                        
                                    )
                                ]
                            )
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Statement: CallStmt(Id(printStrLn),[CallExpr(Id(bool_of_string),[CallExpr(Id(string_of_bool),[BinaryOp(||,BinaryOp(&&,Id(x),Id(y)),BinaryOp(||,BooleanLiteral(false),BinaryOp(>,Id(z),IntLiteral(3))))])])])"""
        self.assertTrue(TestChecker.test(input,expect,442))

    def testcase443(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                

                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("x"),IntLiteral(3)),

                            Assign(Id("y"),CallExpr(Id("float_of_int"),[Id("x")])),

                            CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("y")])])
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Expression: CallExpr(Id(string_of_int),[Id(y)])"""
        self.assertTrue(TestChecker.test(input,expect,443))

    def testcase444(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None),
                

                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("x"),BooleanLiteral(False)),
                            Assign(Id("y"),StringLiteral("True")),
                            Assign(Id("x"),CallExpr(Id("bool_of_string"),[Id("y")])),
                            CallStmt(Id("print"),[CallExpr(Id("bool_of_string"),[Id("y")])])
                            
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Statement: CallStmt(Id(print),[CallExpr(Id(bool_of_string),[Id(y)])])"""
        self.assertTrue(TestChecker.test(input,expect,444))

    def testcase445(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[],None),
                

                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("x"),StringLiteral("True")),
                            CallStmt(Id("print"),[CallExpr(Id("string_of_bool"),[CallExpr(Id("bool_of_string"),[Id("x")])])]),
                            CallStmt(Id("printLn"),[Id("x")])
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Statement: CallStmt(Id(printLn),[Id(x)])"""
        self.assertTrue(TestChecker.test(input,expect,445))

    def testcase446(self):
        """Simple program: main"""

        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                

                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            
                            Assign(Id("y"),ArrayCell(Id("x"),[IntLiteral(0)])),
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Statement: Assign(Id(y),ArrayCell(Id(x),[IntLiteral(0)]))"""
        self.assertTrue(TestChecker.test(input,expect,446))

    def testcase447(self):
        """Simple program: main"""

        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                
                VarDecl(Id("z"),[],IntLiteral(3)),

                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            
                            Assign(Id("z"),ArrayCell(Id("x"),[IntLiteral(0),FloatLiteral(1)])),
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Expression: ArrayCell(Id(x),[IntLiteral(0),FloatLiteral(1)])"""
        self.assertTrue(TestChecker.test(input,expect,447))

    def testcase448(self):
        """Simple program: main"""
        
        input = Program(
            [
                
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                FuncDecl(
                    Id("foo"),
                    [],
                    (
                        [],
                        [
                            Return(Id("y"))
                        ]
                    )

                ),
                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            
                            Assign(Id("z"),ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(0),IntLiteral(1)])),
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Statement: Assign(Id(z),ArrayCell(CallExpr(Id(foo),[]),[IntLiteral(0),IntLiteral(1)]))"""
        self.assertTrue(TestChecker.test(input,expect,448))

    def testcase449(self):
        """Simple program: main"""
        
        input = Program(
            [
                
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                
                FuncDecl(
                    Id("foo"),
                    [],
                    (
                        [],
                        [
                            Return(Id("y"))
                        ]
                    )

                ),
                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("y"),BinaryOp("+.",Id("a"),CallExpr(Id("foo"),[])))
                        ]
                    )
                )
                
                
            ]
        )
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,449))

    def testcase450(self):
        """Simple program: main"""
        
        input = Program(
            [
                
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                
                VarDecl(Id("z"),[],IntLiteral(3)),
                
                FuncDecl(
                    Id("foo"),
                    [VarDecl(Id("z"),[],IntLiteral(3))],
                    (
                        [],
                        [

                            
                            Return(Id("y"))
                        ]
                    )

                ),
                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(Id("z"),ArrayCell(CallExpr(Id("foo"),[Id("z")]),[IntLiteral(1)]))
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Statement: Assign(Id(z),ArrayCell(CallExpr(Id(foo),[Id(z)]),[IntLiteral(1)]))"""
        self.assertTrue(TestChecker.test(input,expect,450))

    def testcase451(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [VarDecl(Id("manh"),[],BooleanLiteral(True)),],
                        [
                            If([(Id("z"),[VarDecl(Id("manh"),[],None)],[Assign(Id("z"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))])],([],[]))
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Type Mismatch In Statement: If(Id(z),[VarDecl(Id(manh))],[Assign(Id(z),IntLiteral(5)),Assign(Id(y),BinaryOp(+.,Id(a),Id(a)))])Else([],[])"""
        self.assertTrue(TestChecker.test(input,expect,451))

    def testcase452(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            If(
                                [
                                    (Id("m"),[VarDecl(Id("manh"),[],None)],[Assign(Id("manh"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                    (Id("n"),[VarDecl(Id("alo"),[],None)],[Assign(Id("alo"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                    (Id("p"),[VarDecl(Id("bien"),[],None)],[Assign(Id("alo"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                    (Id("q"),[VarDecl(Id("hang"),[],None)],[Assign(Id("hang"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))])
                                ],
                                (
                                    [],
                                    []
                                )
                            )
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Undeclared Identifier: alo"""
        self.assertTrue(TestChecker.test(input,expect,452))

    def testcase453(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            If(
                                [
                                    (Id("m"),[VarDecl(Id("manh"),[],None)],[Assign(Id("manh"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                    (Id("n"),[VarDecl(Id("alo"),[],None)],[Assign(Id("alo"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                    (Id("p"),[VarDecl(Id("bien"),[],None)],[Assign(Id("bien"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                    (Id("q"),[VarDecl(Id("hang"),[],None)],[Assign(Id("hang"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))])
                                ],
                                (
                                    [VarDecl(Id("huhu"),[],None)],
                                    [Assign(Id("hihi"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]
                                )
                            )
                        ]
                    )
                )
                
                
            ]
        )
        expect = """Undeclared Identifier: hihi"""
        self.assertTrue(TestChecker.test(input,expect,453))

    def testcase454(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            If(
                                [
                                    (Id("m"),[VarDecl(Id("manh"),[],None)],[Assign(Id("manh"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                    (Id("n"),[VarDecl(Id("alo"),[],None)],[Assign(Id("alo"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                    (Id("p"),[VarDecl(Id("bien"),[],None)],[Assign(Id("bien"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                    (Id("q"),[VarDecl(Id("hang"),[],None)],[Assign(Id("hang"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))])
                                ],
                                (
                                    [VarDecl(Id("hihi"),[],None)],
                                    [Assign(Id("hihi"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+",Id("hihi"),Id("hihi")))]
                                )
                            )
                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Statement: Assign(Id(y),BinaryOp(+,Id(hihi),Id(hihi)))"""
        self.assertTrue(TestChecker.test(input,expect,454))

    def testcase455(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            If(
                                [
                                    (Id("m"),[VarDecl(Id("manh"),[],None)],[Assign(Id("manh"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                    (Id("n"),[VarDecl(Id("alo"),[],None)],[Assign(Id("alo"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                    (Id("p"),[VarDecl(Id("bien"),[],None)],[Assign(Id("bien"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                    (Id("z"),[VarDecl(Id("hang"),[],None)],[Assign(Id("hang"),IntLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))])
                                ],
                                (
                                    [VarDecl(Id("hihi"),[],None)],
                                    [Assign(Id("hihi"),IntLiteral(5)),Assign(Id("z"),BinaryOp("+",Id("hihi"),Id("hihi")))]
                                )
                            )
                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Statement: If(Id(m),[VarDecl(Id(manh))],[Assign(Id(manh),IntLiteral(5)),Assign(Id(y),BinaryOp(+.,Id(a),Id(a)))])ElseIf(Id(n),[VarDecl(Id(alo))],[Assign(Id(alo),IntLiteral(5)),Assign(Id(y),BinaryOp(+.,Id(a),Id(a)))])ElseIf(Id(p),[VarDecl(Id(bien))],[Assign(Id(bien),IntLiteral(5)),Assign(Id(y),BinaryOp(+.,Id(a),Id(a)))])ElseIf(Id(z),[VarDecl(Id(hang))],[Assign(Id(hang),IntLiteral(5)),Assign(Id(y),BinaryOp(+.,Id(a),Id(a)))])Else([VarDecl(Id(hihi))],[Assign(Id(hihi),IntLiteral(5)),Assign(Id(z),BinaryOp(+,Id(hihi),Id(hihi)))])"""
        self.assertTrue(TestChecker.test(input,expect,455))

    def testcase456(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            For(
                                Id("m"),
                                IntLiteral(3),
                                BinaryOp("<",Id("z"),IntLiteral(10)),
                                BinaryOp("+",Id("z"),IntLiteral(1)),
                                ([],[])
                            )
                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Statement: For(Id(m),IntLiteral(3),BinaryOp(<,Id(z),IntLiteral(10)),BinaryOp(+,Id(z),IntLiteral(1)),[],[])"""
        self.assertTrue(TestChecker.test(input,expect,456))

    def testcase457(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            For(
                                Id("z"),
                                FloatLiteral(3),
                                BinaryOp("<",Id("z"),IntLiteral(10)),
                                BinaryOp("+",Id("z"),IntLiteral(1)),
                                ([],[])
                            )
                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Statement: For(Id(z),FloatLiteral(3),BinaryOp(<,Id(z),IntLiteral(10)),BinaryOp(+,Id(z),IntLiteral(1)),[],[])"""
        self.assertTrue(TestChecker.test(input,expect,457))

    def testcase458(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            For(
                                Id("z"),
                                IntLiteral(3),
                                BinaryOp("<",Id("z"),IntLiteral(10)),
                                BinaryOp("+.",Id("y"),FloatLiteral(5)),
                                ([],[])
                            )
                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Statement: For(Id(z),IntLiteral(3),BinaryOp(<,Id(z),IntLiteral(10)),BinaryOp(+.,Id(y),FloatLiteral(5)),[],[])"""
        self.assertTrue(TestChecker.test(input,expect,458))

    def testcase459(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            For(
                                Id("z"),
                                IntLiteral(3),
                                BinaryOp("+.",Id("y"),FloatLiteral(5)),
                                BinaryOp("+.",Id("y"),FloatLiteral(5)),
                                ([],[])
                            )
                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Statement: For(Id(z),IntLiteral(3),BinaryOp(+.,Id(y),FloatLiteral(5)),BinaryOp(+.,Id(y),FloatLiteral(5)),[],[])"""
        self.assertTrue(TestChecker.test(input,expect,459))

    def testcase460(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("h"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            For(
                                Id("z"),
                                IntLiteral(3),
                                BinaryOp(">.",Id("y"),FloatLiteral(5)),
                                BinaryOp("+",Id("h"),IntLiteral(5)),
                                (
                                    [
                                        VarDecl(Id("mot_cai_bien"),[],FloatLiteral(3)),
                                        VarDecl(Id("z"),[],FloatLiteral(3))
                                    ],
                                    [
                                        Assign(
                                            Id("z"),
                                            BinaryOp(
                                                "+.",
                                                CallExpr(Id("float_of_int"),[Id("z")]),
                                                Id("z")
                                            )
                                        )
                                    ]
                                )
                            )
                            
                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Expression: CallExpr(Id(float_of_int),[Id(z)])"""
        self.assertTrue(TestChecker.test(input,expect,460))

    def testcase461(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("h"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            For(
                                Id("z"),
                                IntLiteral(3),
                                BinaryOp(">.",Id("y"),FloatLiteral(5)),
                                BinaryOp("+",Id("h"),IntLiteral(5)),
                                (
                                    [
                                        VarDecl(Id("mot_cai_bien"),[],FloatLiteral(3)),
                                        VarDecl(Id("z"),[],FloatLiteral(3))
                                    ],
                                    [
                                        Assign(
                                            Id("z"),
                                            BinaryOp(
                                                "+.",
                                                CallExpr(Id("float_of_int"),[Id("h")]),
                                                Id("z")
                                            )
                                        )
                                    ]
                                )
                            ),
                            Assign(Id("mot_cai_bien"),FloatLiteral(5.0))
                        ]
                    )
                )
                
            ]
        )
        expect = """Undeclared Identifier: mot_cai_bien"""
        self.assertTrue(TestChecker.test(input,expect,461))

    def testcase462(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("h"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            For(
                                Id("z"),
                                IntLiteral(3),
                                BinaryOp(">.",Id("y"),FloatLiteral(5)),
                                BinaryOp("+",Id("h"),IntLiteral(5)),
                                (
                                    [
                                        VarDecl(Id("mot_cai_bien"),[],FloatLiteral(3)),
                                        VarDecl(Id("z"),[],FloatLiteral(3))
                                    ],
                                    [
                                        Assign(
                                            Id("z"),
                                            BinaryOp(
                                                "+",
                                                CallExpr(Id("float_of_int"),[Id("h")]),
                                                Id("z")
                                            )
                                        )
                                    ]
                                )
                            ),
                            Assign(Id("y"),FloatLiteral(5.0))
                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(float_of_int),[Id(h)]),Id(z))"""
        self.assertTrue(TestChecker.test(input,expect,462))

    def testcase463(self):
        """Simple program: main"""
        
        input = """
            Function: main
            Body:
                Var: a[1] = {1}, b[1] = {2}, c[3]={1,2,3};
                a = b;
                a = c;
            EndBody.
        """
        expect = """Type Mismatch In Statement: Assign(Id(a),Id(c))"""
        self.assertTrue(TestChecker.test(input,expect,463))

    def testcase464(self):
        """Simple program: main"""
        
        input = """
        Var: a,b,c,d,e[2];
        
        Function: foo
        Parameter: a,b
        Body:
            Var: i = 0;
    
        EndBody.
        
        Function: main
        Body:
            Var: x = 0;
            a = 1;
            b = 12.6;
            c = "string";
            d = True;
            e[x] = 0;
            e[b] = 1;
            Var: h[100];
            
        EndBody."""
        expect = """Type Mismatch In Expression: ArrayCell(Id(e),[Id(b)])"""
        self.assertTrue(TestChecker.test(input,expect,464))

    def testcase465(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("h"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(Id("i"),[],None),
                            VarDecl(Id("j"),[],None)
                        
                        ],
                        [
                            For(
                                Id("i"),
                                IntLiteral(0),
                                BinaryOp(">",Id("i"),IntLiteral(10)),
                                BinaryOp("+",Id("i"),IntLiteral(1)),
                                (
                                    [
                                        VarDecl(Id("mot_cai_bien"),[],FloatLiteral(3)),
                                        VarDecl(Id("z"),[],FloatLiteral(3))
                                    ],
                                    [
                                        For(
                                            Id("j"),
                                            IntLiteral(0),
                                            BinaryOp(">",Id("j"),IntLiteral(10)),
                                            BinaryOp("+",Id("j"),IntLiteral(1)),
                                            (
                                                [
                                                    VarDecl(Id("mot_cai_bien"),[],FloatLiteral(3)),
                                                    VarDecl(Id("z"),[],FloatLiteral(3)),
                                                    VarDecl(Id("indside"),[],FloatLiteral(3))
                                                ],
                                                [
                                                    Assign(
                                                        Id("z"),
                                                        FloatLiteral(5.5)
                                                    )
                                                ]
                                            )
                                        ),
                                        Assign(Id("inside"),FloatLiteral(5.0))
                                    ]
                                )
                            ),
                            Assign(Id("y"),FloatLiteral(5.0))
                        ]
                    )
                )
                
            ]
        )
        expect = """Undeclared Identifier: inside"""
        self.assertTrue(TestChecker.test(input,expect,465))

    def testcase466(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("h"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(Id("i"),[],None),
                            VarDecl(Id("j"),[],None)
                        
                        ],
                        [
                            For(
                                Id("i"),
                                IntLiteral(0),
                                BinaryOp(">",Id("i"),IntLiteral(10)),
                                BinaryOp("+",Id("i"),IntLiteral(1)),
                                (
                                    [
                                        VarDecl(Id("mot_cai_bien"),[],FloatLiteral(3)),
                                        VarDecl(Id("z"),[],FloatLiteral(3))
                                    ],
                                    [
                                        If(
                                            [
                                                (Id("m"),[VarDecl(Id("manh"),[],None)],[Assign(Id("manh"),FloatLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                                (Id("n"),[VarDecl(Id("alo "),[],None)],[Assign(Id("alo "),FloatLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                                (Id("p"),[VarDecl(Id("bien"),[],None)],[Assign(Id("bien"),FloatLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                                (Id("q"),[VarDecl(Id("hang"),[],None)],[Assign(Id("hang"),FloatLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))])
                                            ],
                                            (
                                                [VarDecl(Id("hihi"),[],None)],
                                                [
                                                    Assign(Id("hihi"),IntLiteral(5)),
                                                    Assign(Id("z"),BinaryOp("+",Id("z"),Id("z")))
                                                ]
                                            )
                                        )
                                        
                                    ]
                                )
                            ),
                            Assign(Id("y"),FloatLiteral(5.0))
                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Expression: BinaryOp(+,Id(z),Id(z))"""
        self.assertTrue(TestChecker.test(input,expect,466))

    def testcase467(self):
        """Simple program: main"""
       
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("h"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(Id("i"),[],None),
                            VarDecl(Id("j"),[],None)
                        
                        ],
                        [
                            For(
                                Id("i"),
                                IntLiteral(0),
                                BinaryOp(">",Id("i"),IntLiteral(10)),
                                BinaryOp("+",Id("i"),IntLiteral(1)),
                                (
                                    [
                                        VarDecl(Id("mot_cai_bien"),[],FloatLiteral(3)),
                                        VarDecl(Id("z"),[],FloatLiteral(3))
                                    ],
                                    [
                                        If(
                                            [
                                                (Id("m"),[VarDecl(Id("manh"),[],None)],[Assign(Id("manh"),FloatLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                                (Id("n"),[VarDecl(Id("alo "),[],None)],[Assign(Id("alo "),FloatLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                                (Id("p"),[VarDecl(Id("bien"),[],None)],[Assign(Id("bien"),FloatLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                                (Id("q"),[VarDecl(Id("hang"),[],None)],[Assign(Id("hang"),FloatLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))])
                                            ],
                                            (
                                                [VarDecl(Id("hihi"),[],None)],
                                                [
                                                    Assign(Id("hihi"),IntLiteral(5)),
                                                    Assign(Id("z"),BinaryOp("+.",Id("z"),Id("z")))
                                                ]
                                            )
                                        ),
                                        If(
                                            [
                                                (Id("m"),[VarDecl(Id("manh"),[],None)],[Assign(Id("manh"),FloatLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                                (Id("n"),[VarDecl(Id("alo "),[],None)],[Assign(Id("alo "),FloatLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                                (Id("p"),[VarDecl(Id("bien"),[],None)],[Assign(Id("bien"),FloatLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))]),
                                                (Id("q"),[VarDecl(Id("hang"),[],None)],[Assign(Id("hang"),FloatLiteral(5)),Assign(Id("y"),BinaryOp("+.",Id("a"),Id("a")))])
                                            ],
                                            (
                                                [VarDecl(Id("hihi"),[],None)],
                                                [
                                                    Assign(Id("hihi"),IntLiteral(5)),
                                                    Assign(Id("hihi"),BinaryOp("+",Id("m"),Id("n")))
                                                ]
                                            )
                                        )


                                        
                                    ]
                                )
                            ),
                            Assign(Id("y"),FloatLiteral(5.0))
                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Expression: BinaryOp(+,Id(m),Id(n))"""
        self.assertTrue(TestChecker.test(input,expect,467))

    def testcase468(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("h"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(Id("i"),[],None),
                            VarDecl(Id("j"),[],None)
                        
                        ],
                        [
                            For(
                                Id("i"),
                                IntLiteral(0),
                                BinaryOp(">",Id("i"),IntLiteral(10)),
                                BinaryOp("+",Id("i"),IntLiteral(1)),
                                (
                                    [
                                        VarDecl(Id("mot_cai_bien"),[],FloatLiteral(3)),
                                        VarDecl(Id("z"),[],FloatLiteral(3))
                                    ],
                                    [
                                        For(
                                            Id("i"),
                                            IntLiteral(0),
                                            BinaryOp(">",Id("i"),Id("q")),
                                            BinaryOp("+",Id("i"),IntLiteral(1)),
                                            (
                                                [
                                                    VarDecl(Id("mot_cai_bien"),[],FloatLiteral(3)),
                                                    VarDecl(Id("z"),[],FloatLiteral(3))
                                                ],
                                                [
                                                    

                                                    
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),
                            Assign(Id("y"),FloatLiteral(5.0))
                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Expression: BinaryOp(>,Id(i),Id(q))"""
        self.assertTrue(TestChecker.test(input,expect,468))

    def testcase469(self):
        """Simple program: main"""
       
        input = Program(
            [
                VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("y"),[],FloatLiteral(4.0)),
                VarDecl(Id("a"),[],FloatLiteral(4.0)),
                VarDecl(Id("z"),[],IntLiteral(3)),
                VarDecl(Id("h"),[],IntLiteral(3)),
                VarDecl(Id("m"),[],BooleanLiteral(True)),
                VarDecl(Id("n"),[],BooleanLiteral(True)),
                VarDecl(Id("p"),[],BooleanLiteral(True)),
                VarDecl(Id("q"),[],BooleanLiteral(True)),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(Id("i"),[],None),
                            VarDecl(Id("j"),[],None)
                        
                        ],
                        [
                            Assign(ArrayCell(Id("x"),[Id("z")]),Id("y"))
                            
                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Statement: Assign(ArrayCell(Id(x),[Id(z)]),Id(y))"""
        self.assertTrue(TestChecker.test(input,expect,469))

    def testcase470(self):
        """Simple program: main"""
      
        input = Program(
            [
                VarDecl(Id("arr"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("float"),[],FloatLiteral(4.0)),
                VarDecl(Id("int"),[],IntLiteral(3)),
                VarDecl(Id("bool"),[],BooleanLiteral(True)),
                VarDecl(Id("str"),[],StringLiteral("Quan cute")),

            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            
                        ],
                        [
                           While(
                                Id("str"),
                                (
                                    [

                                    ],
                                    [

                                    ]
                                )
                            )

                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Statement: While(Id(str),[],[])"""
        self.assertTrue(TestChecker.test(input,expect,470))

    def testcase471(self):
        """Simple program: main"""
    
        input = Program(
            [
                VarDecl(Id("arr"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("float"),[],FloatLiteral(4.0)),
                VarDecl(Id("int"),[],IntLiteral(3)),
                VarDecl(Id("bool"),[],BooleanLiteral(True)),
                VarDecl(Id("str"),[],StringLiteral("Quan cute")),

            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            
                        ],
                        [
                           While(
                                Id("arr"),
                                (
                                    [

                                    ],
                                    [

                                    ]
                                )
                            )

                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Statement: While(Id(arr),[],[])"""
        self.assertTrue(TestChecker.test(input,expect,471))


    def testcase472(self):
        """Simple program: main"""
       
        input = Program(
            [
                VarDecl(Id("arr"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("float"),[],FloatLiteral(4.0)),
                VarDecl(Id("int"),[],IntLiteral(3)),
                VarDecl(Id("bool"),[],BooleanLiteral(True)),
                VarDecl(Id("str"),[],StringLiteral("Quan cute")),

            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            
                        ],
                        [
                           While(
                                Id("bool"),
                                (
                                    [
                                        VarDecl(Id("a"),[],IntLiteral(1)),
                                        VarDecl(Id("b"),[],IntLiteral(2)),
                                        VarDecl(Id("c"),[],IntLiteral(3)),
                                        VarDecl(Id("d"),[],IntLiteral(4))
                                    ],
                                    [
                                        Assign(Id("a"),IntLiteral(1)),
                                        Assign(Id("b"),IntLiteral(2)),
                                        Assign(Id("c"),IntLiteral(3)),
                                        Assign(Id("d"),IntLiteral(4)),
                                        Assign(ArrayCell(Id("arr"),[Id("a")]),Id("b"))
                                    ]
                                )
                            ),
                            Assign(Id("a"),IntLiteral(1))

                        ]
                    )
                )
                
            ]
        )
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input,expect,472))

    def testcase473(self):
        """Simple program: main"""
      
        input = Program(
            [
                VarDecl(Id("arr"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("float"),[],FloatLiteral(4.0)),
                VarDecl(Id("int"),[],IntLiteral(3)),
                VarDecl(Id("bool"),[],BooleanLiteral(True)),
                VarDecl(Id("str"),[],StringLiteral("Quan cute")),

            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            
                        ],
                        [
                           While(
                                Id("bool"),
                                (
                                    [
                                        VarDecl(Id("a"),[],IntLiteral(1)),
                                        VarDecl(Id("b"),[],IntLiteral(2)),
                                        VarDecl(Id("c"),[],IntLiteral(3)),
                                        VarDecl(Id("d"),[],IntLiteral(4))
                                    ],
                                    [
                                        Assign(Id("a"),IntLiteral(1)),
                                        Assign(Id("b"),IntLiteral(2)),
                                        Assign(Id("c"),IntLiteral(3)),
                                        Assign(Id("d"),IntLiteral(4))
                                    ]
                                )
                            ),
                            Assign(Id("a"),IntLiteral(1))

                        ]
                    )
                )
                
            ]
        )
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input,expect,473))

    def testcase474(self):
        """Simple program: main"""
     
        input = Program(
            [
                VarDecl(Id("arr"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("float"),[],FloatLiteral(4.0)),
                VarDecl(Id("int"),[],IntLiteral(3)),
                VarDecl(Id("bool"),[],BooleanLiteral(True)),
                VarDecl(Id("str"),[],StringLiteral("Quan cute")),
                
                FuncDecl(
                    Id("foo"),
                    [VarDecl(Id("a"),[],IntLiteral(3))],
                    (
                        [],
                        [
                            Return(Id("a"))
                        ]
                    )

                ),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            
                        ],
                        [
                           While(
                                Id("bool"),
                                (
                                    [
                                        VarDecl(Id("a"),[],IntLiteral(1)),
                                        VarDecl(Id("b"),[],IntLiteral(2)),
                                        VarDecl(Id("c"),[],IntLiteral(3)),
                                        VarDecl(Id("d"),[],IntLiteral(4))
                                    ],
                                    [
                                        Assign(Id("a"),IntLiteral(1)),
                                        Assign(Id("b"),IntLiteral(2)),
                                        Assign(Id("c"),IntLiteral(3)),
                                        Assign(Id("d"),IntLiteral(4)),
                                        While(
                                            Id("bool"),
                                            (
                                                [
                                                    VarDecl(Id("a"),[],IntLiteral(1)),
                                                    VarDecl(Id("b"),[],IntLiteral(2)),
                                                    VarDecl(Id("c"),[],IntLiteral(3)),
                                                    VarDecl(Id("d"),[],IntLiteral(4))
                                                ],
                                                [
                                                    Assign(Id("a"),IntLiteral(1)),
                                                    Assign(Id("b"),IntLiteral(2)),
                                                    Assign(Id("c"),IntLiteral(3)),
                                                    Assign(Id("d"),IntLiteral(4))
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),
                            Assign(Id("int"),CallExpr(Id("foo"),[BinaryOp("+",Id("int"),IntLiteral(1))]))

                        ]
                    )
                )
                
            ]
        )
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,474))

    def testcase475(self):
        """Simple program: main"""
    
        input = Program(
            [
                VarDecl(Id("arr"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("float"),[],FloatLiteral(4.0)),
                VarDecl(Id("int"),[],IntLiteral(3)),
                VarDecl(Id("bool"),[],BooleanLiteral(True)),
                VarDecl(Id("str"),[],StringLiteral("Quan cute")),
                
                FuncDecl(
                    Id("foo"),
                    [VarDecl(Id("a"),[],IntLiteral(3))],
                    (
                        [],
                        [
                            Return(Id("a"))
                        ]
                    )

                ),
            
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            
                        ],
                        [
                           While(
                                Id("bool"),
                                (
                                    [
                                        VarDecl(Id("a"),[],IntLiteral(1)),
                                        VarDecl(Id("b"),[],IntLiteral(2)),
                                        VarDecl(Id("c"),[],IntLiteral(3)),
                                        VarDecl(Id("d"),[],IntLiteral(4))
                                    ],
                                    [
                                        Assign(Id("a"),IntLiteral(1)),
                                        Assign(Id("b"),IntLiteral(2)),
                                        Assign(Id("c"),IntLiteral(3)),
                                        Assign(Id("d"),IntLiteral(4)),
                                        While(
                                            Id("bool"),
                                            (
                                                [
                                                    VarDecl(Id("a"),[],IntLiteral(1)),
                                                    VarDecl(Id("b"),[],IntLiteral(2)),
                                                    VarDecl(Id("c"),[],IntLiteral(3)),
                                                    VarDecl(Id("d"),[],IntLiteral(4))
                                                ],
                                                [
                                                    Assign(Id("a"),IntLiteral(1)),
                                                    Assign(Id("b"),IntLiteral(2)),
                                                    Assign(Id("c"),IntLiteral(3)),
                                                    Assign(Id("d"),IntLiteral(4))
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),
                            
                            Assign(Id("int"),CallExpr(Id("foo"),[BinaryOp("+",Id("int"),IntLiteral(1))])),
                            Assign(Id("str"), UnaryOp("!", BinaryOp("==", Id("int"), IntLiteral(1)))),
                        ]
                    )
                )
                
            ]
        )
        expect = """Type Mismatch In Statement: Assign(Id(str),UnaryOp(!,BinaryOp(==,Id(int),IntLiteral(1))))"""
        self.assertTrue(TestChecker.test(input,expect,475))

    def testcase476(self):
        """Simple program: main"""
       
        input = Program(
            [
                VarDecl(Id("arr"),[1],ArrayLiteral([IntLiteral(2)])),
                VarDecl(Id("float"),[],FloatLiteral(4.0)),
                VarDecl(Id("int"),[],IntLiteral(3)),
                VarDecl(Id("bool"),[],BooleanLiteral(True)),
                VarDecl(Id("str"),[],StringLiteral("Quan cute")),
                
                
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            
                        ],
                        [
                           While(
                                Id("bool"),
                                (
                                    [
                                        VarDecl(Id("a"),[],IntLiteral(1)),
                                        VarDecl(Id("b"),[],IntLiteral(2)),
                                        VarDecl(Id("c"),[],IntLiteral(3)),
                                        VarDecl(Id("d"),[],IntLiteral(4))
                                    ],
                                    [
                                        Assign(Id("a"),IntLiteral(1)),
                                        Assign(Id("b"),IntLiteral(2)),
                                        Assign(Id("c"),IntLiteral(3)),
                                        Assign(Id("d"),IntLiteral(4)),
                                        While(
                                            Id("bool"),
                                            (
                                                [
                                                    VarDecl(Id("a"),[],IntLiteral(1)),
                                                    VarDecl(Id("b"),[],IntLiteral(2)),
                                                    VarDecl(Id("c"),[],IntLiteral(3)),
                                                    VarDecl(Id("d"),[],IntLiteral(4))
                                                ],
                                                [
                                                    Assign(Id("a"),IntLiteral(1)),
                                                    Assign(Id("b"),IntLiteral(2)),
                                                    Assign(Id("c"),IntLiteral(3)),
                                                    Assign(Id("d"),IntLiteral(4))
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),
                            
                            Assign(Id("int"),CallExpr(Id("foo"),[BinaryOp("+",Id("int"),IntLiteral(1))])),
                            Assign(Id("bool"), UnaryOp("!", BinaryOp("==", Id("int"), IntLiteral(1)))),
                        ]
                    )
                ),
                FuncDecl(
                    Id("foo"),
                    [VarDecl(Id("a"),[],IntLiteral(3))],
                    (
                        [],
                        [
                            Return(Id("a"))
                        ]
                    )

                ),

                
            ]
        )
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,476))


    def testcase477(self):
        """Simple program: main"""
        
        input = Program(
            [
                VarDecl(Id("int"),[],IntLiteral(3)),
                FuncDecl(
                    Id("main"),
                    [],
                    ([],[
                        Assign(Id("int"),CallExpr(Id("d"),[BinaryOp("+",Id("int"),IntLiteral(1))]))
                    ])
                ),
                FuncDecl(
                    Id("d"),
                    [],
                    ([],[
                        Assign(Id("int"),CallExpr(Id("c"),[BinaryOp("+",Id("int"),IntLiteral(1))])),
                    ])
                ),
                FuncDecl(
                    Id("c"),
                    [],
                    ([],[
                        Assign(Id("int"),CallExpr(Id("b"),[BinaryOp("+",Id("int"),IntLiteral(1))])),
                    ])
                ),
                FuncDecl(
                    Id("b"),
                    [],
                    ([],[
                        Assign(Id("int"),CallExpr(Id("a"),[BinaryOp("+",Id("int"),IntLiteral(1))])),
                    ])
                ),
                FuncDecl(
                    Id("a"),
                    [],
                    ([],[Assign(Id("int"),BinaryOp("+",Id("int"),IntLiteral(1)))])
                )
                
            
            ]
        )
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,477))

    def testcase478(self):
        """Simple program: main"""
        
        input = Program(
            [
                
                FuncDecl(
                    Id("main"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3)),
                        Assign(Id("int"),CallExpr(Id("d"),[BinaryOp("+",Id("int"),IntLiteral(2))])),
                        
                    ])
                ),
                FuncDecl(
                    Id("d"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3)),
                        Assign(Id("int"),CallExpr(Id("c"),[BinaryOp("+",Id("int"),IntLiteral(2))])),
                        
                    ])
                ),
                FuncDecl(
                    Id("c"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3)),
                        
                        Assign(Id("int"),CallExpr(Id("b"),[BinaryOp("+",Id("int"),IntLiteral(1))])),
                        
                    ])
                ),
                FuncDecl(
                    Id("b"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3)),
                        
                        Assign(Id("int"),CallExpr(Id("a"),[BinaryOp("+",Id("int"),IntLiteral(1))]))
                    ])
                ),
                FuncDecl(
                    Id("a"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3)),
                        Assign(Id("int"),CallExpr(Id("c"),[BinaryOp("+",Id("int"),IntLiteral(1))])),
                        Assign(Id("int"),CallExpr(Id("b"),[BinaryOp("+",Id("int"),IntLiteral(1))])),
                        
                    ]

                    )
                )
                
            
            ]
        )
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,478))

    def testcase479(self):
        """Simple program: main"""
       
        input = Program(
            [
                FuncDecl(
                    Id("foo"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3)),
                        Assign(Id("int"),CallExpr(Id("foo"),[BinaryOp("+",Id("int"),IntLiteral(2))])),
                        
                    ])
                ),
                
                FuncDecl(
                    Id("main"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3)),
                        Assign(Id("int"),CallExpr(Id("foo"),[BinaryOp("+",Id("int"),IntLiteral(3))])),
                        
                    ])
                )
                
            
            ]
        )
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,480))

    def testcase480(self):
        """Simple program: main"""
        
        input = Program(
            [
                FuncDecl(
                    Id("rotateRight"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3))
                        
                        
                    ])
                ),

                FuncDecl(
                    Id("rotateLeft"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3))
                        
                        
                    ])
                ),

                FuncDecl(
                    Id("inorder"),
                    [VarDecl(Id("int"),[],None)],
                    ([
                        VarDecl(Id("left"),[],None),
                        VarDecl(Id("right"),[],None)
                    ],[

                        Assign(Id("left"),IntLiteral(1)),
                        Assign(Id("right"),IntLiteral(1)),
                        Assign(Id("left"),CallExpr(Id("inorder"),[BinaryOp("+",Id("left"),IntLiteral(3))])),
                        Assign(Id("right"),CallExpr(Id("inorder"),[BinaryOp("+",Id("right"),IntLiteral(3))])),
                        
                    ])
                ),
                
                FuncDecl(
                    Id("main"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3)),
                        Assign(Id("int"),CallExpr(Id("foo"),[BinaryOp("+",Id("int"),IntLiteral(3))])),
                        
                    ])
                )
                
            
            ]
        )
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input,expect,480))

    def testcase481(self):
        """Simple program: main"""
        
        input = Program(
            [
                FuncDecl(
                    Id("rotateLeft"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3))
                        
                        
                    ])
                ),

                FuncDecl(
                    Id("rotateLeft"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3))
                        
                        
                    ])
                ),

                FuncDecl(
                    Id("inorder"),
                    [VarDecl(Id("int"),[],None)],
                    ([
                        VarDecl(Id("left"),[],None),
                        VarDecl(Id("right"),[],None)
                    ],[

                        Assign(Id("left"),IntLiteral(1)),
                        Assign(Id("right"),IntLiteral(1)),
                        Assign(Id("left"),CallExpr(Id("inorder"),[BinaryOp("+",Id("left"),IntLiteral(3))])),
                        Assign(Id("right"),CallExpr(Id("inorder"),[BinaryOp("+",Id("right"),IntLiteral(3))])),
                        
                    ])
                ),
                
                FuncDecl(
                    Id("main"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3)),
                        Assign(Id("int"),CallExpr(Id("rotateRight"),[BinaryOp("+",Id("int"),IntLiteral(3))])),
                        Assign(Id("int"),CallExpr(Id("rotateLeft"),[BinaryOp("+",Id("int"),IntLiteral(3))])),
                        
                        
                    ])
                )
                
            
            ]
        )
        expect = """Redeclared Function: rotateLeft"""
        self.assertTrue(TestChecker.test(input,expect,481))

    def testcase482(self):
        """Simple program: main"""
        
        input = Program(
            [
                FuncDecl(
                    Id("rotateLeft"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3))
                        
                        
                    ])
                ),

                FuncDecl(
                    Id("rotateRight"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3))
                        
                        
                    ])
                ),

                FuncDecl(
                    Id("inorder"),
                    [VarDecl(Id("int"),[],None)],
                    ([
                        VarDecl(Id("left"),[],None),
                        VarDecl(Id("right"),[],None)
                    ],[

                        Assign(Id("left"),IntLiteral(1)),
                        Assign(Id("right"),IntLiteral(1)),
                        Assign(Id("left"),CallExpr(Id("inorder"),[BinaryOp("+",Id("left"),IntLiteral(3))])),
                        Assign(Id("right"),CallExpr(Id("inorder"),[BinaryOp("+",Id("right"),IntLiteral(3))])),
                        
                    ])
                ),
                
                FuncDecl(
                    Id("main"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3)),
                        Assign(Id("int"),CallExpr(Id("rotateRight"),[BinaryOp("+",Id("int"),IntLiteral(3))])),
                        Assign(Id("int"),CallExpr(Id("rotateLeft"),[BinaryOp("+",Id("int"),IntLiteral(3))])),
                        CallStmt(Id("rotateRight"),[BinaryOp("+",Id("int"),IntLiteral(3))]),
                        CallStmt(Id("rotateLeft"),[BinaryOp("+",Id("int"),IntLiteral(3))]),
                        CallStmt(Id("foofoo"),[BinaryOp("+",Id("int"),IntLiteral(3))])
                    ])
                )
                
            
            ]
        )
        expect = """Undeclared Function: foofoo"""
        self.assertTrue(TestChecker.test(input,expect,482))

    def testcase483(self):
        """Simple program: main"""
      
        input = Program(
            [
                FuncDecl(
                    Id("rotateLeft"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3))
                        
                        
                    ])
                ),

                FuncDecl(
                    Id("rotateRight"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3))
                        
                        
                    ])
                ),

                FuncDecl(
                    Id("inorder"),
                    [VarDecl(Id("int"),[],None)],
                    ([
                        VarDecl(Id("left"),[],None),
                        VarDecl(Id("right"),[],None)
                    ],[

                        Assign(Id("left"),IntLiteral(1)),
                        Assign(Id("right"),IntLiteral(1)),
                        Assign(Id("left"),CallExpr(Id("inorder"),[BinaryOp("+",Id("left"),IntLiteral(3))])),
                        Assign(Id("right"),CallExpr(Id("inorder"),[BinaryOp("+",Id("right"),IntLiteral(3))])),
                        
                    ])
                ),
                
                FuncDecl(
                    Id("main"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3)),
                        Assign(Id("int"),CallExpr(Id("rotateRight"),[BinaryOp("+",Id("int"),IntLiteral(3))])),
                        Assign(Id("int"),CallExpr(Id("rotateLeft"),[BinaryOp("+",Id("int"),IntLiteral(3))])),
                        CallStmt(Id("rotateRight"),[BinaryOp("+",Id("int"),IntLiteral(3))]),
                        CallStmt(Id("rotateLeft"),[BinaryOp("+.",FloatLiteral(5.0),FloatLiteral(5.0))]),
                        
                    ])
                )
                
            
            ]
        )
        expect = """Type Mismatch In Statement: CallStmt(Id(rotateLeft),[BinaryOp(+.,FloatLiteral(5.0),FloatLiteral(5.0))])"""
        self.assertTrue(TestChecker.test(input,expect,483))

    def testcase484(self):
        """Simple program: main"""
    
        input = Program(
            [
                FuncDecl(
                    Id("rotateLeft"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3))
                        
                        
                    ])
                ),

                FuncDecl(
                    Id("rotateRight"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3))
                        
                        
                    ])
                ),

                FuncDecl(
                    Id("inorder"),
                    [VarDecl(Id("int"),[],None)],
                    ([
                        VarDecl(Id("left"),[],None),
                        VarDecl(Id("right"),[],None)
                    ],[

                        Assign(Id("left"),IntLiteral(1)),
                        Assign(Id("right"),IntLiteral(1)),
                        Assign(Id("left"),CallExpr(Id("inorder"),[BinaryOp("+",Id("left"),IntLiteral(3))])),
                        Assign(Id("right"),CallExpr(Id("inorder"),[BinaryOp("+",Id("right"),IntLiteral(3))])),
                        
                    ])
                ),
                
                FuncDecl(
                    Id("main"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3)),
                        Assign(Id("int"),CallExpr(Id("rotateRight"),[BinaryOp("+",Id("int"),IntLiteral(3))])),
                        Assign(Id("int"),CallExpr(Id("rotateLeft"),[BinaryOp("+",Id("int"),IntLiteral(3))])),
                        CallStmt(Id("rotateRight"),[BinaryOp("+",Id("int"),IntLiteral(3))]),
                        CallStmt(Id("rotateLeft"),[CallExpr(Id("int_of_float"),[BinaryOp("+.",FloatLiteral(5.0),FloatLiteral(5.0))])]),
                        
                    ])
                )
                
            
            ]
        )
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,484))

    def testcase485(self):
        """Simple program: main"""
   
        input = Program(
            [
                FuncDecl(
                    Id("rotateLeft"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3))
                        
                        
                    ])
                ),

                FuncDecl(
                    Id("rotateRight"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3))
                        
                        
                    ])
                ),

                FuncDecl(
                    Id("inorder"),
                    [VarDecl(Id("int"),[],None)],
                    ([
                        VarDecl(Id("left"),[],None),
                        VarDecl(Id("right"),[],None)
                    ],[

                        Assign(Id("left"),IntLiteral(1)),
                        Assign(Id("right"),IntLiteral(1)),
                        Assign(Id("left"),CallExpr(Id("inorder"),[BinaryOp("+",Id("left"),IntLiteral(3))])),
                        Assign(Id("right"),CallExpr(Id("inorder"),[BinaryOp("+",Id("right"),IntLiteral(3))])),
                        
                    ])
                ),
                
                FuncDecl(
                    Id("main"),
                    [VarDecl(Id("int"),[],None)],
                    ([],[
                        Assign(Id("int"),IntLiteral(3)),
                        Assign(Id("int"),CallExpr(Id("rotateRight"),[BinaryOp("+",Id("int"),IntLiteral(3))])),
                        Assign(Id("int"),CallExpr(Id("rotateLeft"),[BinaryOp("+",Id("int"),IntLiteral(3))])),
                        CallStmt(Id("rotateRight"),[BinaryOp("+",Id("int"),IntLiteral(3))]),
                        CallStmt(Id("rotateLeft"),[CallExpr(Id("int_of_float"),[BinaryOp("+.",FloatLiteral(5.0),FloatLiteral(5.0))])]),
                        
                    ])
                )
                
            
            ]
        )
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,485))


    def testcase486(self):
        """Simple program: main"""
     
        input = """
        Function: sum
            Parameter: a, b
            Body:
                Return a + b;
            EndBody.

        Function: foo
            Parameter: x
            Body:
                Return x;
            EndBody.

        Function: main
            Body:
                Var: b = 5.6;
                b = sum(1, 3.14);
            EndBody.
        """
        expect = """Type Mismatch In Statement: CallStmt(Id(sum),[IntLiteral(1),FloatLiteral(3.14)])"""
        self.assertTrue(TestChecker.test(input,expect,486))

    def testcase487(self):
        """Simple program: main"""
  
        input = Program([
            FuncDecl(
                Id("main"),
                [],
                (
                    [
                        VarDecl(Id("a"),[1],None),
                        VarDecl(Id("b"),[2],None),
                    ],
                    [
                        Assign(ArrayCell(Id("a"), [IntLiteral(0)]), ArrayCell(Id("b"), [IntLiteral(0), IntLiteral(0)]))
                    ]
                )
            )
        ])
        expect = """Type Cannot Be Inferred: Assign(ArrayCell(Id(a),[IntLiteral(0)]),ArrayCell(Id(b),[IntLiteral(0),IntLiteral(0)]))"""
        self.assertTrue(TestChecker.test(input,expect,487))

    def testcase488(self):
        """Simple program: main"""
     
        input = Program([
            FuncDecl(
                Id("main"),
                [],
                (
                    [
                        VarDecl(Id("a"),[],None),
                        VarDecl(Id("b"),[1],None),
                    ],
                    [
                        Assign(Id("a"), ArrayCell(Id("b"), [IntLiteral(0)]))
                    ]
                )
            )
        ])
        expect = str(TypeCannotBeInferred(Assign(Id("a"), ArrayCell(Id("b"), [IntLiteral(0)]))))
        self.assertTrue(TestChecker.test(input,expect,488))

    def testcase489(self):
        """Simple program: main"""
     
        input = """
        Function: main
        Body:
            Var: bool = True, int = 1, float = 1., string = "quan";
            Var: x1;
            Var: x2;
            Var: x3;
            Var: x4;
            Var: x5;
            Var: x6;
            Var: x7;
            Var: x8;
            Var: x9;
            Var: x10;
            Var: x11;
            Var: x12;
            Var: x13;
            Var: x14;
            Var: x15;
            Var: x16;
            Var: x17;
            Var: x18;
            Var: x19;
            Var: x20;
            Var: x21;
            Var: x22;
            Var: x23;
            Var: x24;
            Var: x25;
            Var: x26;
            Var: x27;
            Var: x28;
            Var: x29;
            Var: x30;
            Var: x31;
            Var: x32;
            Var: x33;
            Var: x34;
            Var: x35;
            Var: x36;
            Var: x37;
            Var: x38;
            Var: x39;
            Var: x40;
            Var: x41;
            Var: x42;
            Var: x43;
            Var: x44;
            Var: x45;
            Var: x46;
            Var: x47;
            bool = !x1;
            int = -x2;
            float = -.x3;
            bool = x4 || x5;
            bool = x6 && x7;
            bool = x8 == x9;
            bool = x10 != x11;
            bool = x12 < x13;
            bool = x14 > x15;
            bool = x16 <= x17;
            bool = x18 >= x19;
            bool = x20 =/= x21;
            bool = x22 <. x23;
            bool = x24 >. x25;
            bool = x26 <=. x27;
            bool = x28 >=. x29;
            int = x30 + x31;
            int = x32 - x33;
            int = x34 * x35;
            int = x36 \ x37;
            int = x38 % x39;

            float = x40 +. x41;
            float = x42 -. x43;
            float = x44 *. x45;
            float = x46 \. x47;
        EndBody.

        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,489))

    def testcase490(self):
        """Simple program: main"""
    
        input = """
            Function: main
            Body:
                Var: i ;

                For (i = 0, i < 10, i+1) Do
                EndFor.

                If i > 12 Then
                Else
                EndIf.

                While i <= 12 Do
                EndWhile.

                Do
                While i<=12 EndDo.
            EndBody.

            """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,490))


    def testcase491(self):
        """Simple program: main"""
    
        input = """
        Function: main
            Body:
                Var: i = True,a = 0;

                While True Do
                    While a <= 12 Do
                        a = a +. 1;

                    EndWhile.

                EndWhile.

            EndBody.

            """
        expect = """Type Mismatch In Expression: BinaryOp(+.,Id(a),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,491))

    def testcase492(self):
        """Simple program: main"""
 
        input = """
            Function: main
            Body:
                Var: i = True,a = 0;

                While True Do
                    If a == 0 Then printStr("quan cute so 1");
                    Elseif a > 0 Then printStr("quan cung cute so 1");
                    Else printStr("quan van cute so 1"); 
                    EndIf

                EndWhile.

            EndBody.

            """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,492))

        
    def testcase492(self):
        """Simple program: main"""
    
        input = """
            Function: main
            Body:
                Var: i = True,a = 0;

                While a Do
                    If a == 0 Then printStr("quan cute so 1");
                    Elseif a > 0 Then printStr("quan cung cute so 1");
                    Else printStr("quan van cute so 1"); EndIf

                EndWhile.

            EndBody.

            """
        expect = """Type Mismatch In Statement: While(Id(a),[],[If(BinaryOp(==,Id(a),IntLiteral(0)),[],[CallStmt(Id(printStr),[StringLiteral(quan cute so 1)])])Else([],[])])"""
        self.assertTrue(TestChecker.test(input,expect,492))


    def testcase493(self):
        """Simple program: main"""
      
        input = """
            Function: main
            Body:
                Var: quan;
                quan = !(quan == 1 || quan > 12);
            EndBody.

            """
        expect = """Type Mismatch In Statement: Assign(Id(quan),UnaryOp(!,BinaryOp(||,BinaryOp(==,Id(quan),IntLiteral(1)),BinaryOp(>,Id(quan),IntLiteral(12)))))"""
        self.assertTrue(TestChecker.test(input,expect,493))

    def testcase494(self):
        """Simple program: main"""
       
        input = """
            Function: foo
            Parameter: x, y
            Body:
                Return x*y;
            EndBody.

        Function: fibonacci
            Parameter: a, b, c
            Body:
                Return a + foo(b, c);
            EndBody.

        Function: main
            Body:
                Var: h = 1;
                
            EndBody.
            """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,494))

    def testcase495(self):
        """Simple program: main"""
        
        input = Program([
            FuncDecl(
                Id("main"),
                [],
                (
                    [VarDecl(Id("i"),[],None),VarDecl(Id("bool"),[],BooleanLiteral(True))],
                    [
                        Dowhile(
                            (
                                [

                                ],
                                [
                                    For(
                                    Id("i"),
                                    IntLiteral(3),
                                    BinaryOp("<",Id("i"),IntLiteral(10)),
                                    BinaryOp("+",Id("i"),IntLiteral(1)),
                                    ([],[])
                            )
                                ]
                            ),
                            BinaryOp(">",Id("i"),IntLiteral(12))
                            
                        )
                    ]
                )
            )

        ])
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,495))


    def testcase496(self):
        """Simple program: main"""
       
        input = Program([
            FuncDecl(
                Id("main"),
                [],
                (
                    [VarDecl(Id("i"),[],None),VarDecl(Id("bool"),[],BooleanLiteral(True))],
                    [
                        Dowhile(
                            (
                                [

                                ],
                                [
                                   While(
                                            Id("bool"),
                                            (
                                                [
                                                    VarDecl(Id("a"),[],IntLiteral(1))
                                                ],
                                                [
                                                    Assign(Id("i"),IntLiteral(1))
                                                ]
                                            )
                                        )
                                ]
                            ),
                            BinaryOp(">",Id("i"),IntLiteral(12))
                            
                        )
                    ]
                )
            )

        ])
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,496))


    def testcase497(self):
        """Simple program: main"""
       
        input = Program([
            FuncDecl(
                Id("main"),
                [],
                (
                    [VarDecl(Id("i"),[],None),VarDecl(Id("bool"),[],BooleanLiteral(True))],
                    [
                        Dowhile(
                            (
                                [

                                ],
                                [
                                    If(
                                        [
                                            (Id("bool"),[VarDecl(Id("hung"),[],None)],[Assign(Id("quan"),IntLiteral(5)),Assign(Id("i"),BinaryOp("+",Id("i"),Id("i")))])
                                        ],
                                        (
                                            [],
                                            []
                                        )
                                    )
                                ]
                            ),
                            BinaryOp(">",Id("i"),IntLiteral(12))
                            
                        )
                    ]
                )
            )

        ])
        expect = """Undeclared Identifier: quan"""
        self.assertTrue(TestChecker.test(input,expect,497))

    def testcase498(self):
        """Simple program: main"""
        
        input = """
        
        Function: main
            Body:
                Var: i = 12;
                Do

                While i EndDo.
                
            EndBody.
            """
        expect = """Type Mismatch In Statement: Dowhile([],[],Id(i))"""
        self.assertTrue(TestChecker.test(input,expect,498))

    def testcase499(self):
        """Simple program: main"""
      
        input = """
        
        Function: main
            Body:
                Do

                While i<=12 EndDo.
                
            EndBody.
            """
        expect = """Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input,expect,499))
