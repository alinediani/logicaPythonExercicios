while True:
    try:
        n,m = input().split()
        cont = 0
        for i in range(int(n),int(m)+1):
            if len(set(list(str(i)))) == len(str(i)):
                cont += 1
        print(cont)
    except:
        break