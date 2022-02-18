x = []
y = []
for i in range(3):
    a, b = map(int,input().split())
    if a in x:
        x.pop(x.index(a))  # x.remove(a)
    else:
        x.append(a)
    if b in y:
        y.pop(y.index(b))
    else:
        y.append(b)
print(x[0], y[0])  #print(*x, *y)