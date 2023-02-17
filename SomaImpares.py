x = int(input())
y = int(input())
x1 = x
y1 = y
soma = 0
if(x>y):
    while x > y:
        if(y % 2 != 0 and y != y1):
            soma = soma + y
        y = y + 1
else:
    while y > x:
        if(x % 2 != 0 and x != x1):
            soma = soma + x
        x = x +1
print(soma)