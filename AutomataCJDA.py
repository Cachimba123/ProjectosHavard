import csv

class AutomataFD:
    def __init__(self, file_path=None):
        # Inicialización de todos los atributos
        self.Q = []              # Estados(Q)
        self.SIGMA = []          # Alfabeto(Sigma)
        self.DELTA = {}          # Funciones de transición(Delta)
        self.START_STATE = None  # Estado inicial
        self.ACCEPT_STATES = []  # Estado de aceptación
        self.ACTUAL_STATE = None # Estado actual

        if file_path:
            self.load_from_csv(file_path)

    def load_from_csv(self, file_path):
        """Cargar el autómata desde un archivo CSV."""
        with open(file_path, mode='r', newline='', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Alfabeto
            self.SIGMA = [char.strip() for char in headers[1:] if char.strip()]  #elementos vacíos
            print("Encabezados (Alfabeto):", self.SIGMA)  

            transitions_dict = {}
            for row in reader:
                state_from = row[0].strip().replace('*', '').replace('-', '').strip()
                if not state_from:  # filas estado vacío
                    continue

                if '*' in row[0]:
                    self.START_STATE = state_from#estado inicial
                    print("Estado inicial:", self.START_STATE)
                if '-' in row[0]:#estado de aceptacion
                    self.ACCEPT_STATES.append(state_from)
                    print("Estado(s) de aceptación:", self.ACCEPT_STATES)

                for i, input_char in enumerate(self.SIGMA, 1):  # Asegurarse de no salir del rango
                    if i < len(row):
                        state_to = row[i].strip()
                        if state_from not in transitions_dict:
                            transitions_dict[state_from] = {}
                        transitions_dict[state_from][input_char] = state_to
                        print(f"Transición desde {state_from} con '{input_char}' a {state_to}")

        self.DELTA = transitions_dict
        self.Q = list(transitions_dict.keys())
        self.ACCEPT_STATES = list(set(self.ACCEPT_STATES))  #eliminar duplicados
        print("Todos los estados (Q):", self.Q)
        print("Transiciones (DELTA):", self.DELTA)
        print("Estados de aceptación final:", self.ACCEPT_STATES)



    def iterateWord(self):
        """Pedir la cadena al usuario y validarla con el autómata."""
        cadena = input('Ingrese una cadena elaborada con el alfabeto {}: '.format(self.SIGMA))
        
        # recorremos la cadena
        self.ACTUAL_STATE = self.START_STATE  # Asegurarse de comenzar en el estado inicial cada vez
        for currentChar in cadena:
            print('Estoy en el caracter: ', currentChar)
            # Validar que los caracteres de la cadena pertenezcan al alfabeto
            if currentChar not in self.SIGMA:
                print('La cadena es invalida ya que', currentChar, 'no pertenece al alfabeto {}'.format(self.SIGMA))
                return False
            
            # Verificar si la transición es correcta
            nextChar = self.DELTA[self.ACTUAL_STATE].get(currentChar, "JACHI")
            print('Me voy a: ', nextChar)

            # Verificar si no apuntó a un estado indefinido (JACHI)
            if nextChar == "JACHI":
                print('La cadena es invalida ya que entramos a un estado indefinido')
                return False
            
            print('Estoy en {} con '.format(self.ACTUAL_STATE),currentChar, 'voy a -> ',nextChar)
            #Actualizar el estado
            self.ACTUAL_STATE = nextChar

        # Verificar si la cadena es correcta o no
        if self.ACTUAL_STATE in self.ACCEPT_STATES:
            print('La cadena "{}" es válida'.format(cadena))
            return True
        else:
            print('La cadena "{}" no es válida'.format(cadena))
            return False


def main_menu():
    automata = None
    while True:
        print("\n1. Generar autómata desde CSV")
        print("2. Ingresar y validar una cadena")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            file_path = input("Ingrese la ruta del archivo CSV: ").strip().replace('"', '')
            try:
                automata = AutomataFD(file_path)
                print("Autómata cargado correctamente.")
            except FileNotFoundError:
                print("No se encontró el archivo. Por favor, verifica la ruta e inténtalo de nuevo.")
            except Exception as e:
                print(f"Ocurrió un error al cargar el archivo: {e}")
        elif choice == '2':
            if automata is None:
                print("Primero debe cargar un autómata.")
            else:
                if automata.iterateWord():
                    print("La cadena es válida.")
                else:
                    print("La cadena no es válida.")
        elif choice == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main_menu()
