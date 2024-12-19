def main():
    print("Iniciando programa de prueba de Ba'axal")
    Numero1 = 5
    Numero2 = 10
    Resultado = 0
    print("Variables inicializadas")
    print("Numero1: " + str(Numero1))
    print("Numero2: " + str(Numero2))
    while Numero1<=Numero2 and Resultado<50:
        Resultado = Resultado+Numero1
        print("Sumando Numero1: " + str(Numero1) + ", Resultado: " + str(Resultado))
        Numero1 = Numero1+1
    print("Fin del bucle while")
    print("Resultado final: " + str(Resultado))
    def Maximo(a, b):
        if a>b:
            max = a
        else:
            max = b
        return max
    MaxValor = Maximo(7,14)
    print("El máximo entre 7 y 14 es: " + str(MaxValor))
    print("Recorriendo lista de números:")
    for x in [1,2,3,4,5]:
        print("Número: " + str(x))
    print("Ingresa un número:")
    edad = input()
    Entrada = edad
    if Entrada>10 or Entrada==0:
        print("El número es mayor que 10 o igual a 0")
    else:
        print("El número no cumple las condiciones")
    print("Programa finalizado")
if __name__ == "__main__":
    main()