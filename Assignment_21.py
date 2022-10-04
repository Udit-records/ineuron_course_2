"""
print("Objective_1")
N = int(input("Enter the number of terms(N): "))
def f1(i,N):
    if i == N:
        print(N)
    else:
        print(i)
        f1(i+1,N)

f1(1,N)
"""



"""
print("Objective_2")
N = int(input("Enter the number of terms(N): "))
def f2(N):
    if N==1:
        print(1)
    else:
        print(N)
        f2(N-1)

f2(N)
"""



"""
print("Objective_3")
N = int(input("Enter the number of terms(N): "))
def f3(i,N):
    if i == N:
        print((2*N)+1)
    else:
        print((2*i)+1)
        f3(i+1,N)

f3(0,N-1)
"""



"""
print("Objective_4")
N = int(input("Enter the number of terms(N): "))
def f4(N):
    if N==1:
        print(1)
    else:
        print((2*N)-1)
        f4(N-1)

f4(N)
"""


"""
print("Objective_5")
N = int(input("Enter the number of terms(N): "))
def f5(i,N):
    if i == N:
        print(2*i)
    else:
        print(2*i)
        f5(i+1,N)

f5(1,N)
"""


"""
print("Objective_6")
N = int(input("Enter the number of terms(N): "))
def f6(N):
    if N==1:
        print(2)
    else:
        print(2*N)
        f6(N-1)

f6(N)
"""


"""
print("Objective_7")
N = int(input("Enter the number of terms(N): "))
def f7(i,N):
    if i == N:
        print(N**2)
    else:
        print(i**2)
        f7(i+1,N)

f7(1,N)
"""


"""
print("Objective_8")
N = int(input("Enter the number of terms(N): "))
def f8(i,N):
    if i == N:
        print(N**3)
    else:
        print(i**3)
        f8(i+1,N)

f8(1,N)
"""



"""
print("Objective_9")
N = int(input("Enter the number of terms(N): "))
M = int(input("Enter the number(N) to get its multiplicaiton: "))
def f9(i,N,M):
    if i == N:
        print(i*M)
    else:
        print(i*M)
        f9(i+1,N,M)

f9(1,N,M)
"""


"""
print("Objective_10")
N = int(input("Enter a number: "))

def f10(N):
    if (N%10 == N):
        print(N,end="")
    else:
        print(N%10,end="")
        N = N//10
        f10(N)

f10(N)
"""