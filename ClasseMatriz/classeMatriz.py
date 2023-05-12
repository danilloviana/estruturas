
'''
Considere  uma matriz:
a)	Preencher a matriz com números aleatórios em alguma faixa
b)	Calcular e exibir a média aritmética dos valores da matriz.
c)	Criar  uma lista com os valores que são menores que a média dos valores da matriz.
d)	Calcular a soma dos elementos da diagonal secundária.  
e)	Calcular e exibir a soma dos elementos da diagonal principal.
'''
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
        
            
m4 = Matriz(4,4)
m5 = Matriz(5,2,30,50)
m4.exibeMatriz()
m5.exibeMatriz()





    
