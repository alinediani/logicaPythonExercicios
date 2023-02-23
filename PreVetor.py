lista = []
n = int(input())
lista.append(n)
for i in range(1,10):
    n = n * 2
    lista.append(n)
cont = 0
for j in lista:
    print("N["+str(cont)+"] = "+str(j))
    cont += 1