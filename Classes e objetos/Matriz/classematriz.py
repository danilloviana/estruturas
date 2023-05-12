
import random
class Matriz:
    def __init__(self,linha,coluna,faixaI=1,faixaF=15):
        self.lin=linha
        self.col=coluna
        self.m=[]
        for ln in range(self.lin):
            lista=[]
            for cl in range(self.col):
                lista.append(random.randint(faixaI,faixaF))
            self.m.append(lista)

    def exibeMatriz(self):
        for i in range(len(self.m)):
            for j in range(len(self.m[0])):
                print(self.m[i][j],end="  ")
            print()
        
            






    
