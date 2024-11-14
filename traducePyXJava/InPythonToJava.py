from antlr4 import *
from PythonXJavaParser import PythonXJavaParser
from PythonXJavaListener import PythonXJavaListener
import os

class ListenerOperacion(PythonXJavaListener):
    def __init__(self):
        self.codigo_java = ["public class Programa {"]
        self.current_function = []
        self.function_call_args = []  #Argumentos funcion

    def enterFunction(self, ctx:PythonXJavaParser.FunctionContext):
        function_name = ctx.IDENTIFIER().getText()
        self.current_function = [f"    public static int {function_name}("]

    def exitFunction(self, ctx:PythonXJavaParser.FunctionContext):
        #'return resultado;'
        if any("int resultado =" in line for line in self.current_function):
            self.current_function.append("        return resultado;")
        self.current_function.append("    }")
        self.codigo_java.extend(self.current_function)

    def enterParams(self, ctx:PythonXJavaParser.ParamsContext):
        params = ["int " + param.getText() for param in ctx.IDENTIFIER()]
        self.current_function.append(", ".join(params) + ") {")

    def exitVar_assign(self, ctx:PythonXJavaParser.Var_assignContext):
        ident = ctx.IDENTIFIER().getText()
        expr = self.translateExpr(ctx.expr())
        self.current_function.append(f"        int {ident} = {expr};")

    def enterReturn_statement(self, ctx:PythonXJavaParser.Return_statementContext):
        expr = self.translateExpr(ctx.expr()) if ctx.expr() else ""
        self.current_function.append(f"        return {expr};")

    def enterFunction_call(self, ctx:PythonXJavaParser.Function_callContext):
        #Captura los argumentos de la función (operaciones)
        self.function_call_args = [self.translateExpr(arg) for arg in ctx.expr()]

    def exitProgram(self, ctx:PythonXJavaParser.ProgramContext):
        self.codigo_java.append("    public static void main(String[] args) {")
        
        #Inserta la función con argumentos 
        args_str = ", ".join(self.function_call_args)
        self.codigo_java.append(f"        System.out.println(operaciones({args_str}));")
        
        self.codigo_java.append("    }")
        self.codigo_java.append("}")

    def translateExpr(self, exprCtx):
        if exprCtx is None:
            return ""
        if isinstance(exprCtx, PythonXJavaParser.ExprContext):
            left = self.translateExpr(exprCtx.expr(0)) if exprCtx.expr(0) else ""
            right = self.translateExpr(exprCtx.expr(1)) if exprCtx.expr(1) else ""
            if exprCtx.PLUS():
                return f"{left} + {right}"
            elif exprCtx.MULTIPLY():
                return f"{left} * {right}"
            elif exprCtx.REST():
                return f"{left} - {right}"
            elif exprCtx.DIVIDE():
                return f"{left} / {right}"
            return exprCtx.getText()  #Numeros-iden
        return exprCtx.getText()  #res

    def get_codigo_java(self):
        return "\n".join(self.codigo_java)

    def guardar_archivo(self, ruta_salida=".", nombre_archivo="translatedCode.java"):
        ruta_archivo = os.path.join(ruta_salida, nombre_archivo)
        try:
            with open(ruta_archivo, "w") as archivo:
                archivo.write(self.get_codigo_java())
            print("Archivo Java generado exitosamente en: " + ruta_archivo)
        except Exception as e:
            print("Error al guardar el archivo: " + str(e))
