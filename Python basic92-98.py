#Python basic algorithm 92 - 98

#92
n = int(input())
a = input().split()

for i in range(n) :
    a[i] = int(a[i])

d = []
for i in range(24) :
    d.append(0)

for i in range(n) :
    d[a[i]] += 1
for i in range(1, 24) :
    print(d[i], end=' ')

#93
n = int(input())
a = input().split()

for i in range(n-1,-1,-1) :
    print(a[i], end=' ')

#94
n = int(input())
a = input().split()
b = int(a[0])
for i in range(n) :
    if int(a[i]) <= b :
        b = int(a[i])
print(b)

#95
d = []
for i in range(20) :
    d.append([]) #변수d에 리스트 추가
    for j in range(20) :
        d[i].append(0) # d변수의 i번째 리스트에 0 추가
n = int(input())
for i in range(n) :
    x, y = input().split()
    d[int(x)][int(y)] = 1 #변수 x번째 리스트의 y번째 요소를 1로 변환

for i in range(1, 20) :
    for j in range(1, 20) :
        print(d[i][j],end=' ')
    print()

#96
d = []
for i in range(20) :
    d.append([])
    for j in range(20) :
        d[i].append(0)

for i in range(19) :
    d[i] = list(map(int, input().split()))

n = int(input())
for i in range(n) :
    x, y = map(int, input().split())
    for j in range(19) :
        if d[j][y-1] == 0 :
            d[j][y-1] = 1
        else :
            d[j][y-1] = 0
        
        if d[x-1][j] == 0 :
            d[x-1][j] = 1
        else :
            d[x-1][j] = 0

for i in range(19) :
    for j in range(19) :
        print(d[i][j], end =' ')
    print()x
#97
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
    
#98