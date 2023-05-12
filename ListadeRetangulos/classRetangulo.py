
#abstração de retangulos

class Retangulo:

    def __init__(self,base=2,altura=4):
        self.base=base
        self.altura=altura

    def perimetro(self):
        return 2*self.base + 2*self.altura

    def area(self):
        return self.base * self.altura

    def isQuadrado(self):
        if self.base == self.altura:
            return  True
        else:
            return False

''' teste
r = Retangulo(5,5)
print("Area:",r.area())
print("Perimetro:",r.perimetro())
if r.isQuadrado():
      print("Quadrado")
'''





      
