#Python basic algorithm 65 - 70

#65
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2==0 :
    print(a)
if b%2==0 :
    print(b)
if c%2==0 :
    print(c)

#66
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2==0 :
    print("even")
else :
    print("odd")
if b%2==0 :
    print("even")
else :
    print("odd")
if c%2==0 :
    print("even")
else :
    print("odd")

#67
n = input()
n = int(n)
if n < 0 :
    if n%2==0 :
        print("A")
    else :
        print("B")
else :
    if n%2==0 :
        print("C")
    else :
        print("D")

#68
n = input()
n = int(n)
if n>90 :
    print("A")
else :
    if n>=70 :
        print("B")
    else :
        if n>=40:
            print("C")
        else:
            print("D")

#69
n = input()
if n == "A" :
    print("best!!!")
else :
    if n == "B" :
        print("good!!")
    else :
        if n== "C":
            print("run!")
        else:
            if n=="D" :
                print("slowly~")
            else :
                print("what?")

#70
n = input()
n = int(n)

if n//3 == 1:
    print("spring")
else :
    if n//3==2:
        print("summer")
    else :
        if n//3==3:
            print("fall")
        else :
            print("winter")