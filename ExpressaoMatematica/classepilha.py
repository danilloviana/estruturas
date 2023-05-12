class pilha:
    def __init__(self):
        self.lista = []

    def empilha(self, x):
        self.lista.append(x)

    def desempilha(self):
        temp = self.lista[len(self.lista)-1]
        self.lista.pop()
        return temp


    def pilhaVazia(self):
        return len(self.lista) == 0


    def elementoDoTopo(self):
        return self.lista[len(self.lista)-1]
