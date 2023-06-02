a = int(input())
b = int(input())
i = a
p = 0
while i <= b:
    cont = 1
    cont2 = 0
    while cont <= i:
        if i % cont == 0:
            cont2 = cont2 + 1
        cont +=1
    if cont2 == 2:
        print(i)
        p += 1
    cont2 = 0
    i += 1
print(f'primos: {p}')



