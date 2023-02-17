i = 0
l = []
x = 0
y = 0
while i >= 0:
    i = int(input())
    l.append(i)
l.pop()
m = len(l)
while x < m:
    n = l[x]
    y = y + n
    x = x+1
media = y/m
print("%0.2f" %media)
