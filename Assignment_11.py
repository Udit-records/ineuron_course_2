"""
print("Objective_1")
N = int(input("Enter the number of terms(N): "))
i = 1
while (i<=N):
    print(i)
    i = i+1
"""

"""
print("Objective_2")
N = int(input("Enter the number of terms(N): "))
i = 1
while (i<=N):
    print(i**2)
    i = i+1
"""

"""
print("Objective_3")
N = int(input("Enter the number of terms(N): "))
i = 1
while (i<=N):
    print(i**3)
    i = i+1
"""

"""
print("Objective_4")
N = int(input("Enter the number of terms(N): "))
i = 0
while (i<N):
    print((2*i)+1)
    i = i+1
"""

"""
print("Objective_5")
N = int(input("Enter the number of terms(N): "))
i = 1
while (i<=N):
    print(2*i)
    i = i+1
"""

"""
print("Objective_6")
f = 1
for i in range(int(input("Enter the number(N) to calculate its factorial: ")),0,-1):
    f = f * i
print("The factorial is",f)
"""

"""
print("Objective_7")
N = int(input("Enter a number: "))
print("The entered quantity has type: ",type(N))
print("Changing the entered number into string format")
N = str(N)
print("The new format of the entered number is: ",type(N))
count = 0
for i in N:
    count = (count + 1)

print("The number of digits the entered number has: ",count)
"""

"""
print("Objective_8")
N = int(input("Enter a number: "))
print("The entered quantity has type: ",type(N))
print("Changing the entered number into string format")
N = str(N)
print("The new format of the entered number is: ",type(N))
sum = 0
for i in N:
    sum = sum + int(i)

print("The sum of the digits of the entered number is: ",sum)
"""

"""
print("Objective_9")
N = int(input("Enter a number: "))
print("Finding binary by using bin() function: ",bin(N))
binary = ""
while (N>=1):
    d = N%2
    N = N//2
    binary = binary + str(d)

binary = binary[::-1]
print("Finding binary without using bin() function: ",binary)
"""

"""
print("Objective_10")
N = int(input("Enter a number: "))
print("Finding octal by using oct() function: ",oct(N))
octal = ""
while (N>=1):
    d = N%8
    N = N//8
    octal = octal + str(d)

octal = octal[::-1]
print("Finding octal without using oct() function: ",octal)
"""