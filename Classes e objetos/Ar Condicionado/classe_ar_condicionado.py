'''
projeto ar condicionado
'''
#Ar condicionado
class ArCondicionado:

    def __init__(self):
    self.ligado = False
    self.temperatura = 0

#funcionalidades
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False

    def aumentar(self):
        self.temperatura =+ 1
    def diminuir(self):
        self.temperatura = -1

    def pegarvalortemperatura(self):
        return self.temperatura = self.temperatura

    def pegarligadodesligado(self)
        return self.ligado
