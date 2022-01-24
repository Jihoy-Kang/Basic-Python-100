d = []
for i in range(20) :
    d.append([])
    for j in range(20) :
        d[i].append(0)

n = int(input())
for i in range(n) :
    a, b = input().split()
    for j in range(1, 20) :
        d[j][int(a)] = 1
        d[j][int(b)] = 1  
        d[int(a)][j] = 1
        d[int(b)][j] = 1


for i in range(1,20) :
    for j in range(1,20) :
        print(d[i][j], end=' ')
    print()


