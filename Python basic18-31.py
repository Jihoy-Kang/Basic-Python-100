#Python basic algorithm 25 - 31

#25 : print sum of integer
a, b = input().split()
c = int(a) + int(b)
print(c)

#26 print sum of real number
a = input()
b = input()
c = float(a) + float(b)
print(c)

#27 print hexademical 1
a = input()
n = int(a)
print('%x'%n)

#28 print hexademical 2
a = input()
n = int(a)
print('%X'%n)

#29 print octal 1
a = input()
n = int(a, 16)
print('%o'%n)

#30 print unicode number
n = ord(input())
print(n)

#31 print unicode character
c = int(input())
print(chr(c))