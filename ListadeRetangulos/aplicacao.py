#aplicacao de uma lista linear
#de retangulos

import classListaLinear
import classRetangulo

tamanho = int(input("Digite o tamanho da lista:"))

minhalista = classListaLinear.ListaLinear(tamanho)
opc=0
while opc != 9:
    print("Lista de Retangulos e quadrados")
    print("1 - insere")
    print("2 - remove")
    print("3 - exibir a lista")
    print("9 - finalizar")
    opc=int(input("Selecione uma opção:"))
    if opc==1:
        #inserir
        if minhalista.isFull():
            print("A lista está cheia, não podemos inserir....!")
        else:
            base = int(input("Digite a base:"))
            altura= int(input("Digite a altura:"))
            r = classRetangulo.Retangulo(base,altura)
            minhalista.inserir(r)
            print("Inserção realizada com sucesso!")
    elif opc==2:
        #remover
        if minhalista.isEmpty():
            print("Lista vazia, não podemos remover....!")
        else:
            minhalista.remover()
            print("Remoção realizada com sucesso!")
    elif opc==3:
        #exibindo a lista de retângulos
        if minhalista.isEmpty():
            print("A lista está vazia....")
        else:
            #Atenção
            #res - é uma lista obtida através da função getLista()
            #observando que esta lista é uma lista de retângulos.
            res = minhalista.getLista()
            #exibindo os elementos retângulos da lista
            #onde retang é uma variável do tipo retângulo de nossa lista....
            #vamos exibir as particularidades de cada retângulo
            print("----------------------------------")
            
            for retang in res:
                print(f"Base.....: {retang.base}")
                print(f"Altura...: {retang.altura}")
                print(f"Perímetro: {retang.perimetro()}")
                print(f"Área.....: {retang.area()}")
                if retang.isQuadrado():
                    print("Temos um quadrado na lista")
                print("----------------------------------")
    elif opc==9:
            #fim
            print("Fim....")
    else:
            #opcao errada
            print("opção invalida")
        
        
    

