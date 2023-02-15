valor = float(input())
intervalo = str()
if(valor >= 0 and valor <= 25) :
    intervalo = "Intervalo [0,25]"
elif(valor > 25 and valor <= 50) :
    intervalo = "Intervalo (25,50]"
elif(valor > 50 and valor <= 75) :
    intervalo = "Intervalo (50,75]"
elif(valor > 75 and valor <= 100) :
    intervalo = "Intervalo (75,100]"
else:
    intervalo = "Fora de intervalo"
print(intervalo)