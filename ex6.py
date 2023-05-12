import random
import classePilha
import classeFila

i = 0
x = 0
tamanho = int(input("Digite o tamanho da pilha: "))

pilha6 = classePilha.Pilha(tamanho)

#a) insere indices na pilha
while i < tamanho:
   pilha6.empilha(random.randint(10,90))
   i+= 1

#b) exibe pilha
print(pilha6.exibir())

#c) transfere para fila
fila6 = classeFila.Fila(tamanho)

while x < tamanho:
    fila6.inserir(pilha6.topo())
    pilha6.desempilha()
    x+=1
#d) exibir fila
print(fila6.exibir())
