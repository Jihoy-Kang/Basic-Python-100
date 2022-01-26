mz = []
for i in range(10) :
    mz.append([])
    for j in range(10) :
        mz[i].append(0)

for i in range(10) :
    mz[i] = list(map(int, input().split()))

r = int(1)
d = int(1)
if mz[r][d+1] == 0 :
    mz[r][d] = 1
    r = r + 1
elif mz[r][d] == 1 :
    d = d + 1






        
for i in range(10) :
    for j in range(10) :
        print(mz[i][j], end=' ')
    print()