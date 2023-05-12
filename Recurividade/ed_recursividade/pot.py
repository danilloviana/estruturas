import math
def pot(x,n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / pot(x,abs(n))
    if n >= 0:
        return x * pot(x, n - 1)

print("Resultado de 2 elevado a 5: ")
print(pot(2,5))
print(" ")
print("Resultado de 3 elevado a 4: ")
print(pot(3,4))
