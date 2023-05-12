import math
def mdc(x,y):
    if x == y:
        return x
    if x < y:
        return mdc(y,x)
    if x > y:
        return mdc(x-y,y)

print("Resultado do Máximo divisor de (64,14): ")
print(mdc(64,14))
