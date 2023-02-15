a,b = list(map(int,input().split()))
testesMultiplos = int()
resultado = str()
if (a > b):
    testesMultiplos = a % b
else:
    testesMultiplos = b % a
if (testesMultiplos == 0):
    resultado = "Sao Multiplos"
else:
    resultado = "Nao sao Multiplos"
print(resultado)

