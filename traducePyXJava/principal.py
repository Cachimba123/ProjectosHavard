from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from PythonXJavaLexer import PythonXJavaLexer
from PythonXJavaParser import PythonXJavaParser
from InPythonToJava import ListenerOperacion 

def main():
    path = input('Ingresa el nombre o la ruta: ')
    with open(path, 'r') as file:
        python_code = file.read()

    lexer = PythonXJavaLexer(InputStream(python_code))
    t_stream = CommonTokenStream(lexer)
    parser = PythonXJavaParser(t_stream)

    tree = parser.program()
    listener = ListenerOperacion()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Guarda el código Java generado en Programa.java
    listener.guardar_archivo(ruta_salida=".", nombre_archivo="TranslatedCode.java")

if __name__ == '__main__':
    main()
