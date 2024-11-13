class automatasFD:
    def __init__(self):
        self.Q=self.definir_estados()
        self.SIGMA=self.definir_alfabeto()
        self.DELTA=self.definir_trancision()
        self.START_STATE,self.ACCEPT_STATE=self.set_start_accept()
        self.EstadoActual = None
    
    def set_start_accept(self):
        while(True):
            start= input("Dame el estado inicial del automata: ")
            accept=input("Dame el o los estados de aceptacion: ").split()
            if(start in self.Q ) and (set(accept).issubset(set(self.Q))):
                return start,accept
            else:
                print("porfavor dame los estados iniciales y de acceptacion")

    def definir_estados(self):
        Q_in=input("Dame el conjunto de estados, separados por espacios en blanco").split()
        print("STATES: {}".format(Q_in))
        return Q_in
    
    def definir_alfabeto(self):
        SIGMA_in=input("Dame el alfabeto del automata, separado por espacios en blanco").split()
        print("ALPHABET : {}".format(SIGMA_in))
        return SIGMA_in
    
    def definir_trancision(self):
        trans_dic={
            q: {a:"JACHI" for a in self.SIGMA} for q in self.Q
        }
        for key,dic_alfabeto in trans_dic.items():
            print("Estoy en el estado {}. Escribir JACHI si no deseas si no existe el estado de transicion".format(key))
            for alfabeto ,transi_state in dic_alfabeto.items():
                trans_dic[key][alfabeto]=input("Dame la transicion de ({},{}) ".format(key,alfabeto))

        for key,dic_alfabeto in trans_dic.items():
            for alfabeto ,transi_state in dic_alfabeto.items():
                print("({},{}) -> {}".format(key,alfabeto,transi_state))

        return trans_dic
    
    def recorrer_automata(self,w):
        self.EstadoActual=self.START_STATE
        for x in w:
            verificar_estado=self.DELTA[self.EstadoActual][x]
            if(verificar_estado=='JACHI'):
                return False
            self.EstadoActual=verificar_estado
        if self.EstadoActual in self.ACCEPT_STATE:
             return True
        
        return False

if __name__ == "__main__": 
    print("Automata de estado finito determinista")
    m = automatasFD()
    while(True):
        input_w=list(input("Dame la cadena:"))
        print("Cadena aceptada {}".format(input_w) if m.recorrer_automata(input_w) else "Cadena rechazada")
        res=input("Si quieres agregar mas cadenas aprieta y: ")
        if(res.upper()!="Y"):
            break

        
    
            
            




