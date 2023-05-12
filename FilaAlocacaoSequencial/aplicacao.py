
'''
aplicação: criar uma pilha de números inteiros
onde o tamanho da pilha será definida pelo usuário
'''

import classefila

tamanho = 0

p = classefila.Fila(tamanho)

opc = 0
while opc != 9:
    opc = int(input("1-Nome \n2- O primeiro foi atendido? \n3-Mostrar o próximo da fila \n4-Mostrar a fila completa \n9-Finalizar \nSelecione: "))
    
    if opc == 1:
            string = input("Digite o nome:")
            p.empilha(string)
            print("Entrou na fila.\n")
            

    elif opc==2:
        if p.pilhavazia():
            print("Fila vazia\n")
        else:
            print(f"Saiu da fila: {p.desempilha()}\n")
    elif opc==3:
        if p.pilhavazia():
            print("A fila está vazia.\n")
        else:
            print(f"Primeiro(a) da fila: {p.elementodotopo()}\n")
    elif opc==4:
        if p.pilhavazia():
            print("Fila vazia\n")
        else:
            #print(p.getLista())
            pilhaatual = p.getLista()
            for x in pilhaatual:
                print(x,"\n")
    elif opc == 9:
        print("Acabou.")

    else:
        print("Opção inválida\n")
        

        
        
            
