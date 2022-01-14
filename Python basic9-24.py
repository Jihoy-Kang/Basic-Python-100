#Python basic algorithm 9 - 24

#9 : input() function
a = input()
print(a)

#10 : Print a integer with input() fuction
n = input()
n = int(n)
print(n)

#11 : print a real number with input() fuction
f = input()
f = float(f)
print(f)

#12 : print a and b in order
a = input()
b = input()
print(a)
print(b)

#13 : print a and b in reverse order
a = input()
b = input()
print(b)
print(a)

#14 : print real number 3 time
f = input()
f = float(f)
print(f)
print(f)
print(f)

#15 : print a and b with input and split function
a, b = input().split()
print(a)
print(b)

#16 : print a and b in reverse order with input and split function
a, b = input().split()
print(b)
print(a)

#17 : print a value 3 times in a line
s = input()
print(s, s, s)

#18 :
a, b = input().split(':')
print(a,b, sep =':')

#19 print date in reverse order with input()
y, m, d = input().split('.')
print(d, m, y, sep ='-')

#20 print a resident registration number
a, b = input().split('-')
print(a,b, sep='')

#21 
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

#22
s = input()
print(s[0:2], s[2:4], s[4:6])

#23
h, m ,s = input().split(':')
print(m)

#24
w1, w2 = input().split()
s = w1 + w2
print(s)

