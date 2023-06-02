n1 = 10
n2 = 5
if n1 % n2 > 1:
    print("t")
    if 3+5/n2>4:
        print("t")
        print(n1)
    else:
        print("f")
else:
    print("f")
    if n1//n2>1:
        print("t")
        n2 = n1+5
    else:
        print("f")
        n1 = n2+5
if 2 + n1 /2 * 3 >= 18:
    print("t")
    n2 =n2%n1
else:
    print("f")
    n1 = n1%n2
print(n1+n2)
print(n1)
print(n2)