#Python basic algorithm 71 - 76

#71
n =1
while n != 0 :
    n = int(input())
    if n != 0 :
        print(n)

#72
n = int(input())
while n != 0 :
    print(n)
    n = n -1

#73
n = int(input())
while n != 0 :
    n = n -1
    print(n)

#74
c = ord(input())
t = ord('a')
while t<=c :
    print(chr(t), end=' ')
    t = t + 1

#75
c = int(input())
t = 0
while t <= c :
    print(int(t))
    t = t + 1

#76
n = int(input())
for i in range(n+1) :
    print(i)
