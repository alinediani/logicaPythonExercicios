while True:
    try:
        epr = []
        ehd = []
        intrusos = []
        na = int(input())
        cont = 0
        while cont < na:
            nm, c = list(input().split())
            if (c == "EPR"):
                epr.append(c)
            elif (c == "EHD"):
                ehd.append(c)
            else:
                intrusos.append(c)
            cont = cont + 1
        print("EPR: " + str(len(epr)))
        print("EHD: " + str(len(ehd)))
        print("INTRUSOS: " + str(len(intrusos)))
    except EOFError:
        break
