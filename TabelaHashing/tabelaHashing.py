

class Hashing:
    def __init__(self,tamUniverso):
        self.size = tamUniverso
        self.hashing = []
        for slot in range(self.size):
            self.hashing.append([])

    #funcao de espalhamento
    def fhs(self,valor):
        return valor % self.size

    def insere(self,valor):
        slot = self.fhs(valor)
        self.hashing[slot].append(valor)

    def remove(self,valor):
        print("implementar")
        
    def busca(self,valor):
        print("implementar")

    def getHashing(self):
        return self.hashing
    


#hashing com os elementos:
lista=[54,15,7,78,14,95,21,46,33,9,62,87]

h = Hashing(5)
for x in lista:
    h.insere(x)

print(h.getHashing())
for tb in h.getHashing():
    print(tb)
        
