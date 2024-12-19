from BaaxalXPythonParser import BaaxalXPythonParser
from BaaxalXPythonListener import BaaxalXPythonListener

class InBaaxalToPython(BaaxalXPythonListener):
    def __init__(self):
        self.output = []  # Almacena las líneas del código Python generado
        self.features = []  # Almacena las características identificadas
        self.indent_level = 0  # Manejo de indentación

    def _write(self, code):
        """Escribe una línea de código con la indentación adecuada."""
        self.output.append("    " * self.indent_level + code)

    def _log(self, feature_name, ctx):
        """Registra características del código."""
        text = ctx.getText() if ctx else "None"
        self.features.append(f"{feature_name}: {text}")

    def getOutput(self):
        """Devuelve el código Python generado como un string."""
        return "\n".join(self.output)

    def guardar_archivo(self, ruta_salida=".", nombre_archivo="TranslatedCode.py"):
        """Guarda el código Python generado en un archivo."""
        with open(f"{ruta_salida}/{nombre_archivo}", "w", encoding="utf-8") as file:
            file.write(self.getOutput())

    # Inicio y fin del programa
    def enterProgram(self, ctx: BaaxalXPythonParser.ProgramContext):
        self._write("def main():")
        self._log("Inicio del programa", ctx)
        self.indent_level += 1

    def exitProgram(self, ctx: BaaxalXPythonParser.ProgramContext):
        self.indent_level -= 1
        self._write('if __name__ == "__main__":')
        self.indent_level += 1
        self._write("main()")
        self._log("Fin del programa", ctx)

    # Asignación de variables
    def enterVar_assignment(self, ctx: BaaxalXPythonParser.Var_assignmentContext):
        if ctx.IDENTIFIER() and ctx.expr():
            var_name = ctx.IDENTIFIER().getText()
            value = ctx.expr().getText()
            self._write(f"{var_name} = {value}")
            self._log("Asignación de variable", ctx)
        else:
            self._log("Error: Asignación de variable incompleta", ctx)

    # Impresión de mensajes
    def enterPrint_statement(self, ctx: BaaxalXPythonParser.Print_statementContext):
        if ctx.expr():
            message = ctx.expr().getText()

            def format_part(part):
                part = part.strip()
                if part.startswith('"') and part.endswith('"'):  # Es una cadena literal
                    return part
                return f"str({part})"  # Es una variable o expresión

            if "+" in message:
                parts = message.split("+")
                formatted_message = " + ".join(format_part(part) for part in parts)
            else:
                formatted_message = format_part(message)

            self._write(f"print({formatted_message})")
            self._log("Impresión de mensaje", ctx)
        else:
            self._log("Error: Impresión sin expresión válida", ctx)

    # Entrada de datos
    def enterInput_statement(self, ctx: BaaxalXPythonParser.Input_statementContext):
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            self._write(f"{var_name} = input()")
            self._log("Entrada de datos", ctx)
        else:
            self._log("Error: Entrada de datos sin identificador", ctx)

    # Bucle while
    def enterWhile_loop(self, ctx: BaaxalXPythonParser.While_loopContext):
        if ctx.expr():
            condition = ctx.expr().getText().replace("Yéetel", " and ").replace("Wa", " or ")
            self._write(f"while {condition}:")
            self._log("Bucle while", ctx)
            self.indent_level += 1
        else:
            self._log("Error: Bucle while sin condición", ctx)

    def exitWhile_loop(self, ctx: BaaxalXPythonParser.While_loopContext):
        self.indent_level -= 1

    # Bucle for
    def enterFor_loop(self, ctx: BaaxalXPythonParser.For_loopContext):
        if ctx.IDENTIFIER() and ctx.expr():
            var_name = ctx.IDENTIFIER().getText()
            iterable = ctx.expr().getText()
            self._write(f"for {var_name} in {iterable}:")
            self._log("Bucle for", ctx)
            self.indent_level += 1
        else:
            self._log("Error: Bucle for sin identificador o iterable", ctx)

    def exitFor_loop(self, ctx: BaaxalXPythonParser.For_loopContext):
        self.indent_level -= 1

    # Funciones
    def enterFunction_definition(self, ctx: BaaxalXPythonParser.Function_definitionContext):
        if ctx.IDENTIFIER():
            func_name = ctx.IDENTIFIER(0).getText()
            params = ", ".join([param.getText() for param in ctx.IDENTIFIER()[1:-1]]) if len(ctx.IDENTIFIER()) > 1 else ""
            self._write(f"def {func_name}({params}):")
            self._log("Definición de función", ctx)
            self.indent_level += 1
        else:
            self._log("Error: Definición de función incompleta", ctx)

    def exitFunction_definition(self, ctx: BaaxalXPythonParser.Function_definitionContext):
        if ctx.IDENTIFIER() and len(ctx.IDENTIFIER()) > 1:
            return_var = ctx.IDENTIFIER()[-1].getText()
            self._write(f"return {return_var}")
            self._log(f"Retorno de función: {return_var}", ctx)
        else:
            self._log("Error: Función sin variable de retorno", ctx)
        self.indent_level -= 1

    # Condicionales
    def enterConditional_block(self, ctx: BaaxalXPythonParser.Conditional_blockContext):
        if ctx.WAJAAJ():  # Condicional if
            if ctx.expr():
                condition = ctx.expr().getText().replace("Yéetel", " and ").replace("Wa", " or ")
                self._write(f"if {condition}:")
                self._log("Bloque condicional (if)", ctx)
            else:
                self._log("Error: Condición del if incompleta", ctx)
        elif ctx.BAALE():  # Bloque else
            self._write("else:")
            self._log("Bloque condicional (else)", ctx)
        self.indent_level += 1

    def exitConditional_block(self, ctx: BaaxalXPythonParser.Conditional_blockContext):
        self.indent_level -= 1
        self._log("Cierre de condicional", ctx)
