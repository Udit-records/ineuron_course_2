"""
print("Objective_1")
N = int(input("Enter the number of terms(N): "))
def f1(N):
    if N==1:
        return 1
    else:
        return N + f1(N-1)

print(f1(N))
"""


"""
print("Objective_2")
N = int(input("Enter the number of terms(N): "))
def f2(N):
    if N==1:
        return 1
    else:
        return ((2*N)-1) + f2(N-1)

print(f2(N))
"""


"""
print("Objective_3")
N = int(input("Enter the number of terms(N): "))
def f3(N):
    if N==1:
        return 2
    else:
        return (2*N) + f3(N-1)

print(f3(N))
"""


"""
print("Objective_4")
N = int(input("Enter the number of terms(N): "))
def f4(N):
    if N==1:
        return 1
    else:
        return (N**2) + f4(N-1)

print(f4(N))
"""


"""
print("Objective_5")
N = int(input("Enter the number of terms(N): "))
def f5(N):
    if N==1:
        return 1
    else:
        return (N**3) + f5(N-1)

print(f5(N))
"""


"""
print("Objective_6")
N = int(input("Enter the number of terms(N): "))
def f1(N):
    if N==1:
        return 1
    else:
        return N * f1(N-1)

print(f1(N))
"""


"""
print("Objective_7")
N = int(input("Enter a number: "))

def f7(N):
    if (N%10 == N):
        return N
    else:
        M = N//10
        return (N%10) + f7(M)

print(f7(N))
"""


"""
print("Objective_8")
N = int(input("Enter a number: "))
L = []
def f8(N,L):
    if N==1:
        return L.append(1)
    else:
        L.append(N%2)
        N = N//2
        f8(N,L)
        return L

BIN = f8(N,L)
BIN.reverse()
#print("The Binary of",N,"is",BIN)
[print(i,end="") for i in BIN if (i==0 or i==1)]
"""


"""
print("Objective_9")
N = int(input("Enter a number: "))
L = []
def f9(N,L):
    if N<=1:
        return L.append(1)
    else:
        L.append(N%8)
        N = N//8
        f9(N,L)
        return L

OCT = f9(N,L)
OCT.reverse()
#print(OCT)
[print(i,end="") for i in OCT if (0 <= i <= 7)]
"""


"""
print("Objective_10")
N = int(input("Enter the value of N: "))
print("The",N,"th term of the Fibonacci series is: ", end="")
def f10(a,b,i,N):
    if i==N:
        print(a)
    else:
        temp = a+b
        a = b
        b = temp
        i = i+1
        f10(a,b,i,N)

f10(0,1,1,N)
"""

