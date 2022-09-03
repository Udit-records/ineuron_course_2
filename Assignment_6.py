"""
print("Objective_1")
n = int(input("Enter a number: "))
if (n>0):
    print("The number is positive")
else:
    print("The number is Non positive")
"""

"""
print("Objective_2")
n = int(input("Enter a number: "))
if ((n%5) == 0):
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")
"""

"""
print("Objective_3")
n = int(input("Enter a number: "))
if ((n%2) == 0):
    print("The number is Even")
else:
    print("The number is Odd")
"""

"""
print("Objective_4")
f = int(input("Enter first number: "))
s = int(input("Enter second number: "))
if (f>s):
    print(f,"is greater than",s)
elif (f<s):
    print(s,"is greater than",f)
else:
    print("Both the number are equal")
"""

"""
print("Objective_5")
f = input("Enter first word: ")
s = input("Enter second word: ")
if (f>s):
    print(f,"comes after",s)
elif (f<s):
    print(s,"comes after",f)
else:
    print("Both the words are the same")
"""

"""
print("Objective_6")
n = int(input("Enter a number: "))
if (99<n<1000):
    print("The entered number has three digits")
else:
    print("The entered number is not a three digit number")
"""

"""
print("Objective_7")
n = int(input("Enter a number: "))
if (n>0):
    print("The entered number is a positive number")
elif(n<0):
    print("The entered number is a negative number")
else:
    print("The entered number is 0")
"""

"""
print("Objective_8")
a = int(input("Enter the coefficent of x2: "))
b = int(input("Enter the coefficent of x: "))
c = int(input("Enter the constant term: "))
d = (b**2) - (4*a*c)

if (d>0):
    print("The quadratic equation has two real and distinct roots")
elif (d<0):
    print("The quadratic equation has two complex and conjugate roots")
else:
    print("The quadratic equation has real and equal roots")
"""

"""
print("Objective_9")
y = int(input("Enter a year: "))
if (y%100 == 0):
    if (y%400 == 0):
        print("The entered year is a leap year")
    else:
        print("The entered year is not a leap year")
elif (y%4 == 0):
    print("The entered year is a leap year")
else:
    print("The entered year is not a leap")
"""

"""
print("Objective_10")
f = int(input("Enter the first numnber: "))
s = int(input("Enter the second numnber: "))
t  = int(input("Enter the third numnber: "))
if (f>s):
    if (f>t):
        print(f,"is the greatest")
    else:
        print(t,"is the greatest")
else:
    if (s>t):
        print(s,"is the greatest")
    else:
        print(t,"is the greatest")
"""

"""
print("Objective_11")
m = int(input("Enter the month value: "))
m_31 = {1,3,5,7,8,10,12}
m_30 = {4,6,9,11}
if (m in m_31):
    print("The entered month has 31 days")
elif (m in m_30):
    print("The entered month has 30 days")
else:
    print("THe entered month has 28/29 days")
"""

"""
print("Objective_12")
c = complex(input())
if (c.real > c.imag):
    print("Real part is greater than imaginary")
elif (c.real < c.imag):
    print("Imaginary part is greater than real")
else:
    print("Imaginary part is equal to real")
"""