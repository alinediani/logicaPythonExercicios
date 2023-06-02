total = 0
valoresDoacao = float(input())
while valoresDoacao != -1.0:
    total += valoresDoacao
    valoresDoacao = float(input())
print(f'VC$ {total:.2f}')
print(f'R$ {total*2.50:.2f}')
