"""
print("Objective_1")
#First way
s1 = "Python"
print(s1)
#Second Way
s2 = eval(input("Enter a string with following proper input method: "))
print(s2)
"""


"""
print("Objective_2")
s2 = "iNeuron"
print(s2[0:5])
"""

"""
print("Objective_3")
s3 = "Hello Learners"
print(s3[2:6])
"""



"""
print("Objective_4")
a = "Learning"
b = "Python"
print("Concatenating two strings, a and b:",a+ " " +b)
"""


"""
print("Objective_5")
a = "iNeuron"
sum = 0
for i in a:
    sum = sum+1
print("The string contains total {} words", sum)
"""


"""
print("Objective_6")
s6 = "iNeuron"
print(s6[::-1])
"""



"""
print("Objective_7")
str = input("Enter a string: ")
sub_str = input("Enter the substring to check its containmnet in the main string: ")

if sub_str in str:
    print("Yes")
else:
    print("No")
"""



"""
print("Objective_8")
inpt = input("Enter a string: ")
count_num = 0
for i in inpt:
    #print(ord(i))
    if ord(i)<=48 or ord(i)>=57:
        count_num = count_num +1;

if(count_num>0):
    print("Yes, its contents also include non numeric value")
else:
    print("No, it doesn't contain any non-numeric value")
"""



"""
print("Objective_9")
inpt = input("Enter a string: ")
count_num = 0
for i in inpt:
    print(ord(i))
    if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
        count_num = count_num +1;

if(count_num>0):
    print("Yes, its contents also include alphabets also")
else:
    print("No, it doesn't contain any albhabet")
"""



"""
print("Objective_10")
int_inpt = int(input("Enter an interger"))
print("The type of the entered value is {}", type(int_inpt))
print("Changing the interger into a string")
int_inpt = str(int_inpt)
print("The new type of the entered value is {}", type(int_inpt))
"""