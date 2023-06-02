notaTrabalhos = float(input())
notaProvas = float(input())
media = (notaProvas + notaTrabalhos)/2
if(media >= 6):
    print('aprovado')
elif(notaTrabalhos >= 4):
    print('talvez com a sub')
else:
    print('reprovado')
