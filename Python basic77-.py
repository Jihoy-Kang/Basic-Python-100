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

