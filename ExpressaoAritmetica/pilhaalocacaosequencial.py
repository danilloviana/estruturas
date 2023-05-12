'''definindo a classe pilha
implementada em alocação sequencial
definindo um tamanho
'''
class Pilha:
    def __init__(self,tamanho=10):
        self.lista = []
        self.max = tamanho

    def empilha(self, x):
        self.lista.append(x)

    def pilhacheia(self):
        return len(self.lista) == self.max

    def desempilha(self):
        temp = self.lista[len(self.lista)-1]
        self.lista.pop()
        return temp

    def pilhavazia(self):
        return len(self.lista) == 0

    def elementodotopo(self):
        return self.lista[len(self.lista)-1]

    def getLista(self):
        return self.lista

    def getMax(self):
        return self.max

    def getTamanhoAtual(self):
        return len(self.lista)


