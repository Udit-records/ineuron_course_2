"""
print("Objective_1")
s = eval(input("Enter a set with proper format: "))

it = iter(s)
while True:
    try:    
        print(next(it))
    except:
        break;
"""


"""
print("Objective_2")
N = int(input("Enter the number of terms: "))
def f2(N):
    while N:
        yield (2*N)-1
        N = N-1


for i in f2(N):
    print(i)
"""


"""
print("Objective_3")
N = int(input("Enter the number of terms: "))
def f3(N):
    while N:
        yield (2*N)
        N = N-1


for i in f3(N):
    print(i)
"""


"""
print("Objective_4")
N = int(input("Enter the number of terms: "))
def f4(N):
    while N:
        yield N**2
        N = N-1


for i in f4(N):
    print(i)
"""


"""
print("Objective_5")
N = int(input("Enter the number of terms of the fibonacci series: "))
def f5(N):
    i=1
    a=0
    b=1
    while i<=N:
        yield a
        a,b=b,a+b
        i = i+1


for i in f5(N):
    print(i)
"""


"""
print("Objective_6")
N = int(input("Enter N to get the first N prime numbers : "))
def f6(N):
    n=1
    i=2
    while n<=N:
        temp = 2
        while temp<i:
            if i%temp == 0:
                break
            temp = temp+1
        else:
            yield i
            n = n+1
        i = i+1
      
for i in f6(N):
    print(i)
"""


"""
print("Objective_7")

def f7():
    a=0
    b=1
    while True:
        choice = input("Do you want to print next element, enter[y/n]: ")
        if choice == 'y':
            yield a
            a,b=b,a+b
        else:
            print("Terminating the iteration")
            break

for i in f7():
    print(i)
"""


"""
print("Objective_8")
def f8():
    n=1
    i=2
    while True:
        
        
            temp = 2
            while temp<i:
                if i%temp == 0:
                    break
                temp = temp+1
            else:
                choice = input("Do you want to print next prime number, enter[y/n]: ")
                if choice == 'y':
                    yield i
                    n = n+1
                else:
                    print("Terminating the iteration")
                    break
            i = i+1
        
      
for i in f8():
    print(i)
"""


"""
print("Objective_9")
def decor_tri_peri(tri_peri_func):
    def tri_check(a,b,c):
        sides = [a,b,c]
        sides.sort()
        if sides[0]+sides[1]> sides[2]:
            print("The triangle is valid")
            tri_peri_func(a,b,c)
        else:
            print("The triangle is invalid")

    return tri_check


@decor_tri_peri
def tri_peri(a,b,c):
    print("The perimeter of the triangle is: ",a+b+c)

a = int(input("Enter first side of the triangle: "))
b = int(input("Enter second side of the triangle: "))
c = int(input("Enter third side of the triangle: "))
tri_peri(a,b,c)
"""


"""
print("Objective_10")

def decor_HCF_check(HCF_check_func):
    def coprime_check(a,b):
        i = HCF_check_func(a,b)
        if i == 1:
            print("The entered two number are coprimes")
        else:
            print("The entered two number are not coprimes")
        
        print("The HCF of {} and {} is {}".format(a,b,i))
    return coprime_check


@decor_HCF_check
def HCF_check(a,b):
    HCF = 1
    i=1
    while i<=min(a,b):
        if (a%i == 0 and b%i == 0 and 1<i<=min(a,b)):
            HCF = i

        i = i+1

    return HCF

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
HCF_check(a,b)
"""