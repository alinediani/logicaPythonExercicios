n = int(input())
c = 0
while c < n:
    soma = 0
    x = int(input())
    y = x
    while y > 0:
        if x % y == 0:
            soma = soma + y
            y = y - 1
        else:
            y = y - 1
    soma = soma - x
    if(soma == x):
        print(str(x) + " eh perfeito")
    else:
        print(str(x) + " nao eh perfeito")
    c = c + 1