"""
print("Objective_1")
m = int(input("Enter the month number to get the number days in that month: "))
match m:
    case 1:
        print("The month has 31 days")
    case 2:
        print("The month has 28/29 days")
    case 3:
        print("The month has 31 days")
    case 4:
        print("The month has 30 days")
    case 5:
        print("The month has 31 days")
    case 6:
        print("The month has 30 days")
    case 7:
        print("The month has 31 days")
    case 8:
        print("The month has 31 days")
    case 9:
        print("The month has 30 days")
    case 10:
        print("The month has 31 days")
    case 11:
        print("The month has 30 days")
    case 12:
        print("The month has 31 days")
"""


"""
print("Objective_2")
i = int(input("Enter the first number: "))
j = int(input("Enter the second number: "))
calc = input("Enter the operator symbol to perform respective operation: ")
match calc:
    case '+':
        print("Addition:", i+j)
    case '-':
        print("Subtraction:", abs(i-j))
    case '*':
        print("Multiplication:",i*j)
    case '/':
        print("Division:", i/j)
    case _:
        print("No operation for the entered the operator")

"""


"""
print("Objective_3")
a = input("Enter the first side: ")
b = input("Enter the second side: ")
c = input("Enter the third side: ")
print("\n1 to check isosceles condition \n2 to check right angled condiiton\n3 to check equliateral condititon\n0 to EXIT\n")
i=1;
while (i is not 0):
    choice = int(input())

    match choice:
        case 1:
            if (a == b) and (a != c):
                print("The triangle is isosceles in nature");
            elif (a is c) and (a is not b):
                print("The triangle is isosceles in nature");
            elif (b is c) and (b is not a):
                print("The triangle is isosceles in nature");
            else:
                print("The triangle is not an isosceles triangle");
                    
        case 2:
            if ((a**2)==((b**2) + (c**2))):
                print("The traingle has right angle");
            elif ((b**2)==((c**2) + (a**2))):
                print("The traingle has right angle");
            elif ((c**2)==((a**2) + (b**2))):
                print("The traingle has right angle");
            else:
                print("The traingle has no right angle");

        case 3:
            if (a==b and b==c):
                print("The triangle is an equilateral triangle")
            else:
                print("The triangle is an equilateral triangle")
            
        case 0:
            i = 0;

        case _:
            print("Enter a valid input")

"""


"""
print("Objective_4")
age = int(input("Enter age: "))

if age<10:
    flag = "kid";
elif 10<= age <20:
    flag = "teen"
elif 20<= age <40:
    flag = "young"
elif 40<= age <60:
    flag = "experienced"
elif 60<=age:
    flag = "senior citizen"

match flag:

    case "kid":
        print("The user is a ",flag)
    
    case "teen":
        print("The user is a ",flag)

    case "young":
        print("The user is a ",flag)

    case "experienced":
        print("The user is a ",flag)

    case "senior citizen":
        print("The user is a ",flag)
"""


"""
print("Objective_5")
n = int(input("Enter a number: "));

if n%2 == 0:
    flag = 1
else:
    if n>0:
        flag = 2
    else:
        flag = 3
match flag:
    case 1:
        print("Saurabh Shukla")

    case 2:
        print("Aditya Choudhary")

    case 3:
        print("Prateek Jain")
"""


"""
print("Objective_6")
s = input("Enter something (without unnecesaary white space or blank space unless required): ")
flag = 0
for i in s:
    if " " in s:
        flag = 0
        break
else:
    flag = 1;

match flag:
    case 1:
        print("It is a single word string")
    case 0:
        print("It is a multiword word string")
"""


"""
print("Objective_7")
n = int(input("Enter a number: "))
if (n>0):
    flag = "+"
elif (n<0):
    flag = "-"
elif (n==0):
    flag = "0"
    

match flag:
    case "+":
        print("The enter number is positive")

    case "-":
        print("The enter number is negative")

    case "0":
        print("The enter number is zero")

"""


"""
print("Objective_8")
f = input("Enter first string: ")
s = input("Enter second string: ")

if (f>s):
    flag = 1
elif (f<s):
    flag = 2
else:
    flag = 0

match flag:
    case 1:
        print(f,"comes after",s)
    case 2:
        print(s,"comes after",f)
    case 0:
        print(f,"and",s,"are the same")
"""



"""
print("Objective_9")
y = int(input("Enter a year: "))

if (y%)

match y/4:
    case 

"""


"""
print("Objective_10")
i = input("What colour do you like the most?? ")

match i:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thursday")
    case "black":
        print("Friday")
    case "red":
        print("Saturday")
    case _:
        print("Sunday")
"""
