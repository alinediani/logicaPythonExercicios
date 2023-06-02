a = int(input())
b = int(input())
if(a>b):
    print('Nenhuma tabuada no intervalo!')
else:
    for i in range(a,b+1):
        for j in range(1,11):
            print(f'{i} x {j} = {i*j}')
        print(f'----------')
