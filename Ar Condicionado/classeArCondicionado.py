'''
projeto: controle remoto de ar condicionado

'''
#Ar condicionado
class ArCondicionado:
    #características ou atributos       
    def __init__(self):
       self.ligado = False
       self.temperatura  = 0

    #funcionalidades ou métodos
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def aumentar(self):
        self.temperatura += 1
        
    def diminuir(self):
        self.temperatura = self.temperatura - 1

    def pegarvalortemperatura(self):
        return self.temperatura
        
    def pegarligadodeslidago(self):
        return self.ligado

    
