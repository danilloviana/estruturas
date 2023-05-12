# classe Triangulo
import math


class Triangulo:
    def __init__(self, ladoA=3, ladoB=4, ladoC=5):
        self.a = ladoA
        self.b = ladoB
        self.c = ladoC

    def isTriangulo(self):
        return (self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b)

    def perimetro(self):
        return self.a + self.b + self.c

    def area(self):
        sp = (self.a + self.b + self.c) / 2
        area = math.sqrt(sp * (sp - self.a) * (sp - self.b) * (sp - self.c))
        return area

    def tipoTriangulo(self):
        if self.a == self.b == self.c:
            tipo = "Equilátero"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            tipo = "Isósceles"
        else:
            tipo = "Escaleno"
        return tipo










