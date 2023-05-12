class Fila:
    def __init__(self,tamanho):
        self.lista = []
        self.max = tamanho

    def inserir(self, x):
        self.lista.append(x)

    def remover(self):
        temp = self.lista[0]
        self.lista.pop(0)
        return temp

    def primeiro(self):
        return self.lista[0]

    def filaVazia(self):
        return len(self.lista) == 0

    def exibir(self):
        return self.lista
