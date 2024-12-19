from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from BaaxalXPythonLexer import BaaxalXPythonLexer
from BaaxalXPythonParser import BaaxalXPythonParser
from InBaaxalToPython import InBaaxalToPython

def main():
    try:
        # Solicita el archivo de entrada en lenguaje Ba'axal
        path = input('Ingresa el nombre o la ruta del archivo Baaxal: ')
        with open(path, 'r', encoding="utf-8") as file:
            baaxal_code = file.read()

        # Procesamiento con ANTLR
        lexer = BaaxalXPythonLexer(InputStream(baaxal_code))
        token_stream = CommonTokenStream(lexer)
        parser = BaaxalXPythonParser(token_stream)
        tree = parser.program()

        # Listener para traducir a Python
        traductor = InBaaxalToPython()
        walker = ParseTreeWalker()
        walker.walk(traductor, tree)

        # Guarda el archivo generado
        traductor.guardar_archivo(nombre_archivo="TranslatedCode.py")
        print("Archivo traducido con éxito a 'TranslatedCode.py'")

    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except Exception as e:
        print(f"Error durante la conversión: {e}")

if __name__ == "__main__":
    main()
