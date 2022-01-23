#Python basic algorithm 92

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
    d.append([])
    for j in range(20) :
        d[i].append(0)
n = int(input())
for i in range(n) :
    x, y = input().split()
    d[int(x)][int(y)] = 1

for i in range(1, 20) :
    for j in range(1, 20) :
        print(d[i][j],end=' ')
    print()