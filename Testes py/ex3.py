palavra = input("Digite uma palavra: ")
contador = 0

for letra in palavra:
    if letra in "aeiouAEIOUáéíóúÁÉÍÓÚ":
        contador += 1

print("Sua frase tem {} vogais".format(contador)) 
