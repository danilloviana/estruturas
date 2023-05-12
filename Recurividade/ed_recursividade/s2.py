def s2(m,n):
    if n == m:
        return m
    if m < n:
        return m + s2(m + 1,n)

print("Função S2:")
print("Soma dos valores de 1 a 10: ")
print(s2(1,10))

print("Soma dos valores de 10 até 15: ")
print(s2(10,15))
