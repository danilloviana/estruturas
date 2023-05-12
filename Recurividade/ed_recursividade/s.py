def s(m,n):
    if n == m:
        return m
    if m < n:
        return s(m, n - 1) + n
print("Função S:")
print("Soma dos números de 10 até 15: ")
print(s(10,15))
