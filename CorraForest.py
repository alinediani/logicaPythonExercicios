i = 0
cont = 0
soma = 0
lista = []
while i == 0:
    j = int(input())
    lista.append(j)
    if j < 0:
        i = 1
        break
    soma = soma + j
    cont += 1
media = soma/cont
print(f'MEDIA:{media: .2f}')
for i in lista:
    if i < media and i >= 0:
        print(i)