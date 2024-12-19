# Generated from BaaxalXPython.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BaaxalXPythonParser import BaaxalXPythonParser
else:
    from BaaxalXPythonParser import BaaxalXPythonParser

# This class defines a complete listener for a parse tree produced by BaaxalXPythonParser.
class BaaxalXPythonListener(ParseTreeListener):

    # Enter a parse tree produced by BaaxalXPythonParser#program.
    def enterProgram(self, ctx:BaaxalXPythonParser.ProgramContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#program.
    def exitProgram(self, ctx:BaaxalXPythonParser.ProgramContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#statement.
    def enterStatement(self, ctx:BaaxalXPythonParser.StatementContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#statement.
    def exitStatement(self, ctx:BaaxalXPythonParser.StatementContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#comment.
    def enterComment(self, ctx:BaaxalXPythonParser.CommentContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#comment.
    def exitComment(self, ctx:BaaxalXPythonParser.CommentContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#var_assignment.
    def enterVar_assignment(self, ctx:BaaxalXPythonParser.Var_assignmentContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#var_assignment.
    def exitVar_assignment(self, ctx:BaaxalXPythonParser.Var_assignmentContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#print_statement.
    def enterPrint_statement(self, ctx:BaaxalXPythonParser.Print_statementContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#print_statement.
    def exitPrint_statement(self, ctx:BaaxalXPythonParser.Print_statementContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#input_statement.
    def enterInput_statement(self, ctx:BaaxalXPythonParser.Input_statementContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#input_statement.
    def exitInput_statement(self, ctx:BaaxalXPythonParser.Input_statementContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#conditional_block.
    def enterConditional_block(self, ctx:BaaxalXPythonParser.Conditional_blockContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#conditional_block.
    def exitConditional_block(self, ctx:BaaxalXPythonParser.Conditional_blockContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#while_loop.
    def enterWhile_loop(self, ctx:BaaxalXPythonParser.While_loopContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#while_loop.
    def exitWhile_loop(self, ctx:BaaxalXPythonParser.While_loopContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#for_loop.
    def enterFor_loop(self, ctx:BaaxalXPythonParser.For_loopContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#for_loop.
    def exitFor_loop(self, ctx:BaaxalXPythonParser.For_loopContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#function_definition.
    def enterFunction_definition(self, ctx:BaaxalXPythonParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#function_definition.
    def exitFunction_definition(self, ctx:BaaxalXPythonParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#expr.
    def enterExpr(self, ctx:BaaxalXPythonParser.ExprContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#expr.
    def exitExpr(self, ctx:BaaxalXPythonParser.ExprContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#logical_expr.
    def enterLogical_expr(self, ctx:BaaxalXPythonParser.Logical_exprContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#logical_expr.
    def exitLogical_expr(self, ctx:BaaxalXPythonParser.Logical_exprContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#relational_expr.
    def enterRelational_expr(self, ctx:BaaxalXPythonParser.Relational_exprContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#relational_expr.
    def exitRelational_expr(self, ctx:BaaxalXPythonParser.Relational_exprContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#additive_expr.
    def enterAdditive_expr(self, ctx:BaaxalXPythonParser.Additive_exprContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#additive_expr.
    def exitAdditive_expr(self, ctx:BaaxalXPythonParser.Additive_exprContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#multiplicative_expr.
    def enterMultiplicative_expr(self, ctx:BaaxalXPythonParser.Multiplicative_exprContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#multiplicative_expr.
    def exitMultiplicative_expr(self, ctx:BaaxalXPythonParser.Multiplicative_exprContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#power_expr.
    def enterPower_expr(self, ctx:BaaxalXPythonParser.Power_exprContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#power_expr.
    def exitPower_expr(self, ctx:BaaxalXPythonParser.Power_exprContext):
        pass


    # Enter a parse tree produced by BaaxalXPythonParser#base.
    def enterBase(self, ctx:BaaxalXPythonParser.BaseContext):
        pass

    # Exit a parse tree produced by BaaxalXPythonParser#base.
    def exitBase(self, ctx:BaaxalXPythonParser.BaseContext):
        pass



del BaaxalXPythonParser