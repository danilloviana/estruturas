
'''
aplicação: criar uma pilha de números inteiros
onde o tamanho da pilha será definida pelo usuário
'''

import classepilha

tamanho = int(input("Digite o tamanho da pilha:"))

p = classepilha.Pilha(tamanho)

opc = 0
while opc != 9:
    opc = int(input("1-empilha 2-desempilha 3-topo 4-exibe 9-fim \nSelecione: "))
    
    if opc == 1:
        if p.pilhacheia():
            print("Pilha cheia...")
        else:
            n = int(input("Digite o número:"))
            p.empilha(n)
            print("Empilhamento com sucesso")

    elif opc==2:
        if p.pilhavazia():
            print("Pilha vazia")
        else:
            print(f"Desempilhado: {p.desempilha()}")
    elif opc==3:
        if p.pilhavazia():
            print("A pilha está vazia....")
        else:
            print(f"topo da pilha: {p.elementodotopo()}")
    elif opc==4:
        if p.pilhavazia():
            print("Pilha vazia....")
        else:
            #print(p.getLista())
            pilhaatual = p.getLista()
            for x in pilhaatual:
                print(x)
    elif opc == 9:
        print("fim....")

    else:
        print("opção inválida")
        

        
        
            
