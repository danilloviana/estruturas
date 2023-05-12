#Classe Televisão
class Televisao:

    def __init__(self, marca , modelo , tamanho):
        self.marca = marca
        self.modelo = modelo
        self.tamanho = tamanho
        
    def ligar(self):
        print('Estou Ligando!')

    def desligar(self):
        print('Estou Desligando!')

    def exibir_informacoes_da_tv(self):
        print(self.marca , self.modelo ,self.tamanho)


