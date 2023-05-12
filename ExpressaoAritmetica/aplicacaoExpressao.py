import pilhaalocacaosequencial as pilha

p=pilha.Pilha(50)

##inserir um menu para o usuario
'''
1-nova expressao
2-o grupo
9-fim
'''

expressao = input("Digite sua expressão:")
i=0
valido=True
while i < len(expressao):
    #s representa o simbolo da expressao
    s = expressao[i]
    #se ( (símbolo='{') ou (símbolo='[') ou (símbolo='(') ) entao
    if s in ["{", "[", "("]:
        p.empilha(s)
    else:
        #se ((símbolo='}') ou (símbolo=']') ou (símbolo=')')) entao
        if s in ["}", "]", ")"]:
            if p.pilhavazia():
                valido=False
            else:
                if s=="}" and p.elementodotopo() == "{":
                    p.desempilha()
                else:
                    if s=="]" and p.elementodotopo() == "[":
                        p.desempilha()
                    else:
                        if s==")" and p.elementodotopo() == "(":
                            p.desempilha()
                        else:
                            break
    i = i+1
#fim while
if p.pilhavazia() and valido:
    print('Expressão Correta')
else:
    print('Expressão Incorreta')




