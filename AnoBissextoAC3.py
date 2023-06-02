anoInicio = int(input())
anoFim = int(input())
cont = anoInicio
qtde = 0
while cont <= anoFim:
    if((cont % 4 == 0 and cont % 100 != 0)or (cont % 400 == 0)):
        print(cont)
        qtde += 1
    cont += 1
print(f'bissextos: {qtde}')