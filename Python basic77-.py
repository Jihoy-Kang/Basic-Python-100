#Python basic algorithm 77 - 

#77
n = int(input())
s = 0
for i in range(1, n+1):
    if i%2 == 0 :
        s = s + i 
print(s)

#78
n = 0
while n != 'q' :
    n = input()
    if n != 'q':
        print(n)
    else : print(n)

#79
n = int(input())
t = 1
a = 0
while t <= n :
    a = a + 1
    t = t + a
print(a)

#80
n, m = input().split()
n = int(n)
m = int(m)
for i in range(1, n+1) :
    for j in range(1, m+1) :
        print(i, j)

#81
n = input()
n = int(n, 16)
i = 0
m = 0
for i in range(1, 16) :
    m = n*i
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

#82
n = int(input())
for i in range(1, n+1) :
    if i%10 == 3 :
        print('X')
    elif i%10 == 6 :
        print('X')
    elif i%10 == 9 :
        print('X')
    else :
        print(i)

#83
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

for i in range(0, a) :
    for j in range(0, b) :
        for h in range(0, c) :
            print(i, j, h)
print(a*b*c)

#84
h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)
print(format(h*b*c*s/8/1024/1024, '.1f'),'MB')