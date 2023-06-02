diaRealizouCompra = str(input())
prazoReceber = int(input())
recebimento = ''
if (prazoReceber == 0):
    recebimento = 'chega hoje!'
elif ((diaRealizouCompra == 'domingo'and prazoReceber == 1) or (diaRealizouCompra == 'terca'and prazoReceber == 6) or (diaRealizouCompra == 'quarta'and prazoReceber == 5) or (diaRealizouCompra == 'quinta'and prazoReceber == 4) or (diaRealizouCompra == 'sexta'and prazoReceber == 3) or (diaRealizouCompra == 'sabado'and prazoReceber == 2)):
    recebimento = 'sera entregue segunda'
elif ((diaRealizouCompra == 'domingo'and prazoReceber == 2) or (diaRealizouCompra == 'segunda' and prazoReceber == 1) or (diaRealizouCompra == 'quarta'and prazoReceber == 6) or (diaRealizouCompra == 'quinta'and prazoReceber == 5) or (diaRealizouCompra == 'sexta'and prazoReceber == 4) or (diaRealizouCompra == 'sabado'and prazoReceber == 3)):
    recebimento = 'sera entregue terca'
elif ((diaRealizouCompra == 'domingo'and prazoReceber == 3) or (diaRealizouCompra == 'segunda' and prazoReceber == 2) or (diaRealizouCompra == 'terca'and prazoReceber == 1) or (diaRealizouCompra == 'quinta'and prazoReceber == 6) or (diaRealizouCompra == 'sexta'and prazoReceber == 5) or (diaRealizouCompra == 'sabado'and prazoReceber == 4)):
    recebimento = 'sera entregue quarta'
elif ((diaRealizouCompra == 'domingo'and prazoReceber == 4) or (diaRealizouCompra == 'segunda' and prazoReceber == 3) or (diaRealizouCompra == 'terca'and prazoReceber == 2) or (diaRealizouCompra == 'quarta'and prazoReceber == 1) or (diaRealizouCompra == 'sexta'and prazoReceber == 6) or (diaRealizouCompra == 'sabado'and prazoReceber == 5)):
    recebimento = 'sera entregue quinta'
elif ((diaRealizouCompra == 'domingo'and prazoReceber == 5) or (diaRealizouCompra == 'segunda' and prazoReceber == 4) or (diaRealizouCompra == 'terca'and prazoReceber == 3) or (diaRealizouCompra == 'quarta'and prazoReceber == 2) or (diaRealizouCompra == 'quinta'and prazoReceber == 1) or (diaRealizouCompra == 'sabado'and prazoReceber == 6)):
    recebimento = 'sera entregue sexta'
elif ((diaRealizouCompra == 'domingo'and prazoReceber == 6) or (diaRealizouCompra == 'segunda' and prazoReceber == 5) or (diaRealizouCompra == 'terca'and prazoReceber == 4) or (diaRealizouCompra == 'quarta'and prazoReceber == 3) or (diaRealizouCompra == 'quinta'and prazoReceber == 2) or (diaRealizouCompra == 'sexta'and prazoReceber == 1)):
    recebimento = 'sera entregue sabado'
elif ((diaRealizouCompra == 'segunda' and prazoReceber == 6) or (diaRealizouCompra == 'terca'and prazoReceber == 5) or (diaRealizouCompra == 'quarta'and prazoReceber == 4) or (diaRealizouCompra == 'quinta'and prazoReceber == 3) or (diaRealizouCompra == 'sexta'and prazoReceber == 2) or (diaRealizouCompra == 'sabado'and prazoReceber == 1)):
    recebimento = 'sera entregue domingo'
print(recebimento)
