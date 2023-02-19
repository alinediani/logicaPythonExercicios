dias = int(input())
cont = 0
cont2 = 0
while cont < dias:
    f = int(input())
    while cont2 < f:
        feedback = int(input())
        if(feedback == 1):
            print("Rolien")
        elif(feedback == 2):
            print("Naej")
        elif(feedback == 3):
            print("Elehcim")
        elif(feedback == 4):
            print("Odranoel")
        cont2 = cont2 + 1
    cont2 = 0
    cont = cont + 1