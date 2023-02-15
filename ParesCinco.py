listaInteiros = []
valoresPares = 0
i = 0
j = 0
for i in range(0,5) :
    listaInteiros.append(int(input()))
    ++i
for j in range(0,5):
    testeResto = listaInteiros[j] % 2
    if (testeResto == 0) :
        valoresPares = valoresPares + 1
    ++j
print(str(valoresPares) + " valores pares")