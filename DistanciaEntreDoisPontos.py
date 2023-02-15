x1,y1 = list(map(float,input().split()))
x2,y2 = list(map(float,input().split()))
distanciaX = (x2-x1)*(x2-x1)
distanciaY = (y2-y1)*(y2-y1)
distanciaRaiz = (distanciaX + distanciaY) ** 0.5
print("%0.4f" %distanciaRaiz)