mz = []
for i in range(10) :
    mz.append([])
    for j in range(10) :
        mz[i].append(0)

for i in range(10) :
    mz[i] = list(map(int, input().split()))

d = 0
for i in range(10) :
    for j in range(10) :
        if mz[i][j] == 0 :
            mz[i][j] = 9
       
     
for i in range(10) :
    for j in range(10) :
        print(mz[i][j], end=' ')
    print()