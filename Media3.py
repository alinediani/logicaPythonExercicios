n1,n2,n3,n4 = list(map(float,input().split()))
media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10
print("Media: %0.1f" %media)
if(media >= 7.0) :
    print("Aluno aprovado.")
elif(media >= 5.0 and media <= 6.9) :
    print("Aluno em exame.")
    notaExame = float(input())
    print("Nota do exame: %0.1f" %notaExame)
    media2 = (media+notaExame)/2
    if(media2 >= 5.0) :
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %0.1f" %media2)
else:
    print("Aluno reprovado.")