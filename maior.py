maior = 0
posicao = 0
a = {}
while 100 > posicao:
    i = int(input())
    if(maior < i):
        maior = i
        a[i] = posicao
    posicao = posicao + 1
print(maior)
print(a[maior]+1)