lista = []
for i in range (0,10):
    a = int(input())
    if a <= 0:
        a = 1
    lista.append(a)
cont = 0
for j in lista:
    print("X["+str(cont)+"] = "+str(j))
    cont += 1