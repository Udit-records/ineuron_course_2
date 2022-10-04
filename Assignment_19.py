"""
print("Objetive_1")
def f1():
    print("MySirG")

f1()
"""


"""
print("Objective_2")
def f2(a,b):
    print(a)
    print(b)

f2(2,4)
"""


"""
print("Objective_3")
def f3(*t):
    for i in t:
        print(i)

f3(1,2,3,4,5)
"""


"""
print("Objective_4")
def f4(a,b,c):
    print(a)
    print(b)
    print(c)

f4(5,c=4,b=10)
"""


"""
print("Objective_5")
def f5(a):
    for i in a:
        print(i)

my_list = [1,3,'d','f']
f5(my_list)
"""


"""
print("Objective_6")

def f6(l):
    mx = max(l)
    return mx

my_list = [i for i in input("Enter the four numbers separated by commas: ").split(',')]

print("The maximum of the entered four numbers is ",f6(my_list))
"""


"""
print("Objective_7")
def f7(l):
    sum = 0
    for i in l:
        sum = sum + int(i)
    return sum

my_list = [i for i in input("Enter the four numbers separated by commas: ").split(',')]
print(my_list)

print("The sum of the entered four numbers is ",f7(my_list))
"""


"""
print("Objective_8")
def f8(l):
    prod = 1
    for i in l:
        prod = prod * int(i)
    return prod

my_list = [i for i in input("Enter the four numbers separated by commas: ").split(',')]
print(my_list)

print("The sum of the entered four numbers is ",f8(my_list))
"""


"""
print("Objective_9")
def f9(n,l,h):
    if n in range(l,h):
        return "Present"
    if n not in range(l,h):
        return "Absent"

print("Enter the range limits")
l = int(input("Enter the lower range: "))
h = int(input("Enter the higher range: "))
n = int(input("Enter the number to check its availability: "))

print("The number",n,"is",f9(n,l,h),"in the given range")
"""


"""
print("Objective_10")
def f10(n):
    if n%2 == 0:
        return "Divisible"
    if n%2 != 0:
        return "Not Divisible"

n = int(input("Enter the number to check its divisibility by 2: "))

print("The number",n,"is",f10(n),"by 2")
"""