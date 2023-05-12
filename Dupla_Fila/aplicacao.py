
import duplafila

tamanho = int(input("Digite o tamanho:"))
df = duplafila.DuplaFila(tamanho)

opc = 1
while opc != 9:
    print("Dupla Fila")
    print("1 - insere no final")
    print("2 - insere no início")
    print("3 - remove no final")
    print("4 - remove no inicio")
    print("5 - primeiro")
    print("6 - último")
    print("7 - exibir a fila")
    print("9 - fim")
    opc=int(input("Selecione:"))
    if opc == 1:
        if df.filacheia():
            print("Fila cheia!!!!")
        else:
            x=int(input("Digite o valor:"))
            df.inserefinal(x)
            print("Inserção com sucesso!!")
    elif opc==2:
        if df.filacheia():
            print("Fila cheia!!!!")
        else:
            x=int(input("Digite o valor:"))
            df.insereinicio(x)
            print("Inserção com sucesso!!")
    elif opc==3:
        if df.filavazia():
            print("Fila vazia!!!")
        else:
            print(f"Removido do final: {df.removefinal()}")
    elif opc==4:
        if df.filavazia():
            print("Fila vazia!!!")
        else:
            print(f"Removido do inicio: {df.removeinicio()}")         
    elif opc==5:
        if df.filavazia():
            print("Fila vazia!!!")
        else:
            print(f"Primeiro: {df.primeiro()}")    
    elif opc==6:
        if df.filavazia():
            print("Fila vazia!!!")
        else:
            print(f"Último: {df.ultimo()}")
    elif opc==7:
        if df.filavazia():
            print("Fila vazia!!!")
        else:
            mfila=df.getLista()
            print("Elementos da dupla-fila")
            for x in mfila:
                print(x, end=" ")
            print("")
    elif opc==9:
        print("Fim de execução")

    else:
        print("opção inválida.....!")




    
        
