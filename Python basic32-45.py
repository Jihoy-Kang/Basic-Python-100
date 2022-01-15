#Python basic algorithm 32 - 45

#32 : 
n = input()
n = int(n)
print(-n)

#33
n = ord(input())
print(chr(n+1))

#34
a, b = input().split()
c = int(a) - int(b)
print(c)

#35
a, b = input().split()
m = float(a) * float(b)
print(m)

#36
w, n = input().split()
print(w*int(n))

#37
n = input()
s = input()
print(int(n)*s)

#38
a, b = input().split()
print(int(a)**int(b))

#39
a, b = input().split()
print(float(a)**float(b))

#40
a, b = input().split()
print(int(a)//int(b))

#41
a, b = input().split()
print(int(a)%int(b))

#42
a=float(input())
print(format(a, ".2f"))

#43
a, b = input().split()
c = float(a) / float(b)
print(format(c, ".3f"))

#44
a, b = input().split()
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)//int(b))
print(int(a)%int(b))
c = float(a)/float(b)
print(format(c,".2f"))

#45
a, b, c = input().split()
d = int(a) + int(b) + int(c)
e = d /3
print(d, format(e,".2f"))