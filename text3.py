d = []
for i in range(20) :
    d.append([])
    for j in range(20) :
        d[i].append(0)

n = int(input())
for i in range(n) :
    a, b = input().split()
    for j in range(1, 20) :
        if d[j][int(a)] == 0 :
            d[j][int(a)] = 1
        else : d[j][int(a)] = 0

        if d[int(b)][j] == 0 :
            d[int(b)][j] = 1
        else : d[int(b)][j] = 0

for i in range(1,20) :
    for j in range(1,20) :
        print(d[i][j], end=' ')
    print()


