entrada = int(input())
testeResto = entrada % 2
imparAnterior = 0
parPosterior = 0
if(testeResto == 0):
    imparAnterior = entrada - 1
    parPosterior = entrada + 2
else:
    imparAnterior = entrada - 2
    parPosterior = entrada + 1
print(str(imparAnterior)+" "+str(parPosterior))
