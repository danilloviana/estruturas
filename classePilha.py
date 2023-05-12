class Pilha:
    def __init__(self,tamanho):
        self.lista = []
        self.max = tamanho

    def empilha(self, x):
        self.lista.append(x)

    def desempilha(self):
        temp = self.lista[len(self.lista)-1]
        self.lista.pop()
        return temp

    def pilhaCheia(self):
        return len(self.lista) == self.max

    def pilhaVazia(self):
        return len(self.lista) == 0

    def topo(self):
        return self.lista[len(self.lista)-1]
    
    def exibir(self):
        return self.lista
