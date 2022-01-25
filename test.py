d = []
a, b = map(int, input().split())
for i in range(a) :
    d.append([])
    for j in range(b) :
        d[i].append(0)

n = int(input())
for i in range(n) :
    l, c, x, y = map(int, input().split())
    for j in range(l) :
        if c == 0:
            d[x-1][y-1+j] = 1
        else :
            d[x-1+j][y-1] = 1


for i in range(a) :
    for j in range(b) :
        print(d[i][j], end=' ')
    print()