n = int(input())
c = 0
while c < n:
    j = 0
    m = 0
    pj = 0
    pm = 0
    while j < 3:
        j1,j2 = list(map(int,input().split()))
        pj = (j1*j2) + pj
        j = j + 1
    while m < 3:
        m1,m2 = list(map(int,input().split()))
        pm = (m1*m2) + pm
        m = m + 1
    if(pm > pj):
        print("MARIA")
    elif(pj > pm):
        print("JOAO")
    c = c + 1