import random
import classePilha
import classeFila

i = 0
x = 0
tamanho = int(input("Digite o tamanho da fila: "))

fila7 = classeFila.Fila(tamanho)

#a) insere indices na fila
while i < tamanho:
   fila7.inserir(random.randint(35,75))
   i+= 1

#b) exibe pilha
print(fila7.exibir())

#c) transfere para pilha
pilha7 = classePilha.Pilha(tamanho)

while x < tamanho:
    pilha7.empilha(fila7.primeiro())
    fila7.remover()
    x+=1
    
#d) exibir fila
print(pilha7.exibir())
