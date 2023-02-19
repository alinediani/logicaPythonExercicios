n = int(input())
c = 0
while c < n:
    divisores = []
    x = int(input())
    y = x
    while y > 0:
        if x % y == 0:
            divisores.append(y)
            y = y - 1
        else:
            y = y - 1
    if(len(divisores) > 2):
        print(str(x) + " nao eh primo")
    else:
        print(str(x) + " eh primo")
    c = c + 1