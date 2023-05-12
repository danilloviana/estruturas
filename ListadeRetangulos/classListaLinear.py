#abstracao de uma lista linear
#de tamanho pré-definido

class ListaLinear:
    def __init__(self,tamanho):
        self.lista=[]
        self.tamanho = tamanho

    def inserir(self, x):
        self.lista.append(x)

    def remover(self):
        self.lista.pop()

    def isFull(self):
        return self.tamanho == len(self.lista)
        '''poderia fazer assim:
        if self.tamanho == len(self.lista):
            return True
        else:
            return False
        '''
        
    def isEmpty(self):
        return len(self.lista) == 0
        '''poderia fazer assim:
        if len(self.lista) == 0:
            return True
        else:
            return False
        '''

    def getLista(self):
        return self.lista
    
'''testando
mlista=Lista(5)
mlista.inserir(4)
'''
