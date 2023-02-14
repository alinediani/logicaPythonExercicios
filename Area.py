a = "%0.1f" %float(input())
b = "%0.1f" %float(input())
c = "%0.1f" %float(input())
triangulo = (float(a)*float(c))/2
circulo = (float(c)*float(c))*3.14159
trapezio = ((float(a)+float(b))*float(c))/2
quadrado = float(b)*float(b)
retangulo = float(a)*float(b)
trianguloC= "%0.3f" %triangulo
circuloC = "%0.3f" %circulo
trapezioC = "%0.3f" %trapezio
quadradoC = "%0.3f" %quadrado
retanguloC = "%0.3f" %retangulo
print("TRIANGULO : "+trianguloC)
print("CIRCULO : "+circuloC)
print("TRAPEZIO : "+trapezioC)
print("QUADRADO : "+quadradoC)
print("RETANGULO : "+retanguloC)