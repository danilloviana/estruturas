def dig(n):
    if abs(n) <= 9:
        return 1
    if abs(n) > 9:
        return 1 + dig(n / 10)

print(dig(532))
print(dig(3324567))
