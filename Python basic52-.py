#Python basic algorithm 52 -

#52
n = int(input())
print(bool(n))

#53
a = bool(int(input()))
print(not a)

#54
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

#55
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

#56
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

#57
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and d) or (not c and not d))

#58
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print(not c and not d)

#59 bitwise not
a = int(input())
print(~a)

#60 bitwise and
a, b = input().split()
a = int(a)
b = int(b)
print(a&b)

#61 bitwise or
a, b = input().split()
a = int(a)
b = int(b)
print(a|b)

#62 bitwise xor
a, b = input().split()
a = int(a)
b = int(b)
print(a^b)

#63 
a, b = input().split()
a = int(a)
b = int(b)
print(a if(a >=b) else b)

#64
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a if(a<b and a<c) else b if(b<a and b<c) else c)

