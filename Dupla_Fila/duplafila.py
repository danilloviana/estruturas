

class DuplaFila:
    def __init__(self,tamanho):
        self.lista = []
        self.max = tamanho

    def inserefinal(self, x):
        self.lista.append(x)

    def insereinicio(self,x):
        self.lista.insert(0,x)

    def filacheia(self):
        return len(self.lista) == self.max

    def removeinicio(self):
        temp = self.lista.pop(0)
        return temp
    
    def removefinal(self):
        temp = self.lista.pop()
        return temp
   
    def filavazia(self):
        return len(self.lista) == 0

    def primeiro(self):
        return self.lista[0]

    def ultimo(self):
        return self.lista[len(self.lista)-1]

    def getLista(self):
        return self.lista



    
