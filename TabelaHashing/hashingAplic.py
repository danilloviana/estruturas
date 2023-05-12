import tabelaHashing as th

#hashing com os elementos:
lista=[54,15,7,78,14,95,21,46,33,9,62,87]

h = th.Hashing(5)
for x in lista:
    h.insere(x)

print(h.getHashing())
for tb in h.getHashing():
    print(tb)
        
