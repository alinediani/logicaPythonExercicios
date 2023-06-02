numero = int(input())
cont = 1
caractere = ""
while cont <= numero:
    caractere = chr(cont + 64)
    while len(caractere) < cont:
        caractere = caractere + str(chr(cont + 64))
    print(caractere)
    cont += 1