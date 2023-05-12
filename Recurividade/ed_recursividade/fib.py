def fib(n):
    if n <= 2:
        return 1
    if n > 2:
        return fib(n-1) + fib(n-2)


print("Resultado se n=6: ")
print(fib(6))
