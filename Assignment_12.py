"""
print("Objective_1")
N = int(input("Enter a number: "))
print("The entered quantity has type: ",type(N))
print("Changing the entered number into string format")
N = str(N)
print("The new format of the entered number is: ",type(N))
N = N[::-1]
print("The entered number in the reverse order: ",N)
"""

"""
print("Objective_2")
N = int(input("Enter a number: "))
i = 2;
while (i < N):
    if N%i == 0:
        flag = 1
        break
    i+=1
else:
    flag = 0

if flag == 0:
    print("The entered number is a prime number")
else:
    print("The entered number is not a prime number")
"""


"""
print("Objective_3")
N = 2
i = 2;
while (N<100):
    i=2
    while (i < N):
        if N%i == 0:
            flag = 1
            break
        i+=1
    else:
        flag = 0

    if flag == 0:
        print(N)

    N+=1
"""


"""
print("Objective_5")
N = int(input("Enter a number: "))
i = 2;
N = N+1
flag = 1
while (flag!=0):
    i=2
    while (i < N):
        if N%i == 0:
            flag = 1
            break
        i+=1
    else:
        flag = 0

    if flag == 0:
        print(N)

    N+=1
"""


"""
print("Objective_6")
T = int(input("Enter the number of terms: "))
N = 2
i = 2
count = 1
while (count <= T):
    i=2
    while (i < N):
        if N%i == 0:
            flag = 1
            break
        i+=1
    else:
        flag = 0
        count = count+1

    if flag == 0:
        print(N)

    N+=1
"""

"""
print("Objective_7")
fst = int(input("Enter the first number: "))
scnd = int(input("Enter the second number: "))
if fst>scnd:
    lrge=fst
    smlr = scnd
elif (fst<scnd):
    lrge = scnd
    smlr = fst

i = 2
while (i < lrge):
    if lrge%i == 0 and smlr%i == 0:
        flag = 1
        break
    i+=1
else:
    flag = 0

if flag == 0:
    print("The entered numbers are co-prime numbers")
else:
    print("The entered number are not co-prime numbers")
"""

"""
print("Objective_8")
N = int(input("Enter the number of terms(N): "))
f = 0
s = 1
count=3
print("0\n1")
while (count<= N) and (count>=2):
    l = s
    s = (f + s)
    f = l
    count = count+1
    print(s)
"""

"""
print("Objective_9")
f = int(input("Enter first number: "))
s = int(input("Enter second number: "))
N = 1
while (N%f!=0) or (N%s!=0):
    N = N+1

print(N)
"""

"""
print("Objective_10")
f = int(input("Enter first number: "))
s = int(input("Enter second number: "))
if f>s:
    sml=s
elif f<s:
    sml=f
HCF = 1
N = 2
while (N<=sml):
    if ((f%N==0) and (s%N==0)):
        HCF = N

    N = N+1
    flag = 0

print("The HCF is: ",HCF)
"""