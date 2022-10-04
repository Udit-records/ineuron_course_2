"""
print("Objective_1")
def f1(l1):
    l2 = list(set(l1))
    return l2
list_1 = eval(input("Enter a list with proper format: "))
print("The list with unique elements is", f1(list_1))
"""

"""
print("Objective_2")
def f2(n):
    i=2
    while i < n:
        if n%i == 0:
            flag = 'Non Prime'
            break
        i = i+1
    else:
        flag = 'Prime'
    
    
    
    return flag

N = int(input("Enter a number (greater than 1) to check whether its prime or Not: "))
print("The entered number", N,"is a",f2(N),"Number")
"""


"""
print("Objective_3")
def f3(n):
    n_new = []
    for i in n:
        if i%2 == 0:
            n_new.append(i)
        
    return n_new

my_list = eval(input("Enter a list of numbers in a proper format: "))
print("The entered list with only even numbers is: ",f3(my_list))
"""


"""
print("Objective_4")
def f4(s):
    i=0
    s_len = len(s)//2
    for i in range(s_len):
        if s[i]!=s[(len(s)-1)-i]:
            flag = "Not Palindrome"
            break
        i=i+1
    else:
        flag = "Palindrome"

    return flag

S = eval(input("Enter a list of string in proper format: "))
print("The entered list of elements",f4(S))
"""


"""
print("Objective_5")
def f5(a,b,c):
    mn = min([a,b,c])
    return mn

A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))

print("The minimum of the entered three number is",f5(A,B,C))
"""


"""
print("Objective_6")
def f6():
    list_square = []
    for i in range(1,31):
        list_square.append(i**2)

    return list_square

print("The square of the first 30 natural number is",f6())
"""


"""
print("Objective_7")
def f7_1(N):
    return (N**2)
def f7_2(N1,N2):
    sq_sum = f7_1(N1) + f7_1(N2)
    return sq_sum

print("We are going to use one function inside other")
print("First one will square the number")
print("While second one will add them")
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
print("The sum of square of two numbers is ",f7_2(a,b))
"""


"""
print("Objective_8")
def f8(s):
    lower = []
    upper = []
    for i in s:
        if 97 <= ord(i) <= 122:
            lower.append(i)

        if 65 <= ord(i) <= 90:
            upper.append(i)

    print("The strings with upper case are: ",upper)
    print("The strings with lower case are: ",lower)

S = input("Enter a string: ")
f8(S)
"""


"""
print("Objective_9")
def f9(s):
    uni_s = [ord(i) for i in s.lower()]

    for r in range(97,123):
        if r not in uni_s:
            print(r)
            print("The entered string is not a panagram")
            break;
            
    else:
       print("The entered string is a panagram")
    
S = input("Enter a string to check whether its panagram or not: ")
f9(S)
"""


"""
print("Objective_10")
def f10(s1,s2):
    s1_lower = sorted([i for i in s1.lower()])
    s2_lower = sorted([i for i in s2.lower()])
    s1_temp = []
    s2_temp = []

    for i in s1_lower:
        if ord(i) in range(97,123):
            s1_temp.append(i)

    for i in s2_lower:
        if ord(i) in range(97,123):
            s2_temp.append(i)

    print(s1_temp)
    print(s2_temp)
    if s1_temp == s2_temp:
        print("The entered strings are Anagram of eachother")
    else:
        print("The entered strings are not Anagram of eachother")

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
f10(s1,s2)
"""
