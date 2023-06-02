totalDivida = int(input())
valorMensal = int(input())
cont = 1

while totalDivida > 0:
    print(f'pagamento: {cont}')
    print(f'antes = {totalDivida}')
    totalDivida = totalDivida-valorMensal
    if totalDivida < 0:
        totalDivida = 0
    print(f'depois = {totalDivida}')
    print(f'-----')
    cont+=1