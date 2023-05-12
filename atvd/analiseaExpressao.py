import classepilha

opc = 0
while opc != 9:
    opc = int(input("1-Nova expressão \n2-Grupo \n9-Fim \nSelecione: "))

    if opc == 1:
        expressao = input("Digite uma expressão: ")
        simbolo = str()

        i = 0

        valido = True

        p = classepilha.Pilha()

        while i < len(expressao):
            simbolo = expressao[i]
            if ((simbolo=='{') or (simbolo=='[') or (simbolo=='(')):
                    p.empilha(simbolo)
            else:
                if ((simbolo=='}') or(simbolo==']') or (simbolo==')')):
                    
                        if p.pilhaVazia():
                            valido = False

                        elif (simbolo=='}') and (p.elementoDoTopo() == '{'):
                            p.desempilha()

                        elif (simbolo==']') and (p.elementoDoTopo()=='['):
                            p.desempilha()

                        elif (simbolo==')') and (p.elementoDoTopo()=='('):
                            p.desempilha()

                        else:
                            print("  ")

            i += 1

        if p.pilhaVazia() and valido:
            print("Expressão Correta")

        else:
            print("Expressão Incorreta")

    elif opc == 2:
        print('Cintia Karolliny \nEverson Vieira \nLetícia Barros \nSabrina Allexia')

    elif opc == 9:
        print('Fim...')

    else:
        print('Opção inválida...')
