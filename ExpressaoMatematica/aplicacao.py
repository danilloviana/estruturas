import classepilha

expressao = str(input("Digite a expressão: "))
p = classepilha.pilha()
i = 0
valido = True

while i < len(expressao):
    simbolo = expressao[i]
    if ((simbolo=='{') or (simbolo=='[') or (simbolo=='(')):
            p.empilha(simbolo)
    else:
        if ((simbolo=='}') or(simbolo==']') or (simbolo==')')):
                if p.pilhaVazia():
                    valido = False
                else:
                    if (simbolo=='}') and (p.elementoDoTopo() == '{'):
                        p.desempilha()
                    else:
                        if (simbolo==']') and (p.elementoDoTopo()=='['):
                            p.desempilha()
                        else:
                            if (simbolo==')') and (p.elementoDoTopo()=='('):
                                p.desempilha()
                            else:
                                print(" ")




                                

    i = i+1
if valido and p.pilhaVazia():
    print('Expressão Correta')
else:
    print('Expressão Incorreta')
