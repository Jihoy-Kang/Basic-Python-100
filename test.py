n = input()
n = int(n, 16)
i = 0
m = 0
for i in range(1, 16) :
    m = n*i
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
