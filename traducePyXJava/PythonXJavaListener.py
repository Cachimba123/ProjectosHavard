# Generated from PythonXJava.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonXJavaParser import PythonXJavaParser
else:
    from PythonXJavaParser import PythonXJavaParser

# This class defines a complete listener for a parse tree produced by PythonXJavaParser.
class PythonXJavaListener(ParseTreeListener):

    # Enter a parse tree produced by PythonXJavaParser#program.
    def enterProgram(self, ctx:PythonXJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by PythonXJavaParser#program.
    def exitProgram(self, ctx:PythonXJavaParser.ProgramContext):
        pass


    # Enter a parse tree produced by PythonXJavaParser#function.
    def enterFunction(self, ctx:PythonXJavaParser.FunctionContext):
        pass

    # Exit a parse tree produced by PythonXJavaParser#function.
    def exitFunction(self, ctx:PythonXJavaParser.FunctionContext):
        pass


    # Enter a parse tree produced by PythonXJavaParser#params.
    def enterParams(self, ctx:PythonXJavaParser.ParamsContext):
        pass

    # Exit a parse tree produced by PythonXJavaParser#params.
    def exitParams(self, ctx:PythonXJavaParser.ParamsContext):
        pass


    # Enter a parse tree produced by PythonXJavaParser#indented_block.
    def enterIndented_block(self, ctx:PythonXJavaParser.Indented_blockContext):
        pass

    # Exit a parse tree produced by PythonXJavaParser#indented_block.
    def exitIndented_block(self, ctx:PythonXJavaParser.Indented_blockContext):
        pass


    # Enter a parse tree produced by PythonXJavaParser#statement.
    def enterStatement(self, ctx:PythonXJavaParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonXJavaParser#statement.
    def exitStatement(self, ctx:PythonXJavaParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonXJavaParser#var_assign.
    def enterVar_assign(self, ctx:PythonXJavaParser.Var_assignContext):
        pass

    # Exit a parse tree produced by PythonXJavaParser#var_assign.
    def exitVar_assign(self, ctx:PythonXJavaParser.Var_assignContext):
        pass


    # Enter a parse tree produced by PythonXJavaParser#print_statement.
    def enterPrint_statement(self, ctx:PythonXJavaParser.Print_statementContext):
        pass

    # Exit a parse tree produced by PythonXJavaParser#print_statement.
    def exitPrint_statement(self, ctx:PythonXJavaParser.Print_statementContext):
        pass


    # Enter a parse tree produced by PythonXJavaParser#return_statement.
    def enterReturn_statement(self, ctx:PythonXJavaParser.Return_statementContext):
        pass

    # Exit a parse tree produced by PythonXJavaParser#return_statement.
    def exitReturn_statement(self, ctx:PythonXJavaParser.Return_statementContext):
        pass


    # Enter a parse tree produced by PythonXJavaParser#function_call.
    def enterFunction_call(self, ctx:PythonXJavaParser.Function_callContext):
        pass

    # Exit a parse tree produced by PythonXJavaParser#function_call.
    def exitFunction_call(self, ctx:PythonXJavaParser.Function_callContext):
        pass


    # Enter a parse tree produced by PythonXJavaParser#expr.
    def enterExpr(self, ctx:PythonXJavaParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonXJavaParser#expr.
    def exitExpr(self, ctx:PythonXJavaParser.ExprContext):
        pass



del PythonXJavaParser