#Classe Quadrilátero

class Quadrilatero:
    def __init__(self, base=4, altura=5):
        self.base=base
        self.altura=altura

        def perimetro (self):
            return ('Perimetro= 'self.base * 2) +(self.altura *2)

        def area(self):
            return ('Area= ', self.base * self.altura)

        def tipodeqadrilatero(self):
            if self.base == self.altura:
                return ('É quadrado')
            return  ('Não é quadrado')



