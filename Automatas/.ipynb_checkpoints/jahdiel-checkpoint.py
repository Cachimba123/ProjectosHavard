"""DETERMINISTA FINITE STATE M (DFSM)"""
class jahdiel:
    def __init__(self):
        """Inicializacion el DFSM"""
        self.Q=self.definir_estados()
        self.Sigma=self.definir_alfabeto()
        self.Delta=self.definir_transicion()
        self.EstadoInicial,EstadoAceptados=self.set_inicio_aceptacion()
        self.EstadoActual=None
    def set_inicio_aceptacion(self):
        """Pedir al usuario el estado de inicio y estados de aceptacion finales"""
        while(True):
            inicial=input("Dame el estado inicial del automata: ")
            aceptacion=input("Dame el o los estados de aceptacion: ").split()
            #Asegurate de que los estados que proporciono el USER son validos
            if(inicial in self.Q) and (set(aceptacion).issubset(set(self.Q))):
                return inicial,aceptacion
            else:
                print("Por favor debes proporcionar el estado inicial y el o los estados de aceptacion que deben estar en Q: {}.",format(self.Q))
        
