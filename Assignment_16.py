"""
print("Objective_1")
#Method_1
#t1 = ("Java", "Python", "SQL", "C")
t1 = "Java", "Python", "SQL", "C"
print("The entered tuple is, ", t1, "with type", type(t1))

#Method_2
t1 = []
count = int(input("Enter the number of members of the List"))
i = 0
while i<count:
    t1.append(input())
    i+=1
t1 = tuple(t1)
print(t1)
print(type(t1))

#Method_3
#For eval() enter the elements in proper format, like lists in [], tuple in {} and so on
t1 = eval(input("Enter the elements on tuple in proper format"))
print(t1)
print(type(t1))

#Method_4
#t1 = tuple(list(i for i in input("Enter the words separated by comma: ").split(",")))
t1 = tuple([i for i in input("Enter the words separated by comma: ").split(",")])
#t1 = tuple(t1)
print(t1)
print(type(t1))
"""

"""
print("Objective_2")
print("Forming a tuple with just one element")
t2 = (1,)
print("The type of the formed data is: ",type(t2))
"""

"""
print("Objective_3")
t3 = ("One", "two", "three")
t3 = t3[::-1]
print(t3)
print(type(t3))
"""

"""
print("Objective_4")
t4_1 = ("one","two","three")
t4_2 = ("four","five","six")
print("Tuples before swapping, t4_1:", t4_1, "and t4_2:",t4_2)
temp = t4_1
t4_1 = t4_2
t4_2 = temp
print("Tuples after swapping, t4_1:", t4_1, "and t4_2:",t4_2)
"""

"""
print("Objective_5")
t5 = eval(input("Enter the elements of the tuple in proper format"))
i = 0
count = 1
while i+1 < len(t5):
    if t5[i] == t5[i+1]:
        count+=1
    
    i+=1

if count == len(t5):
    print("The enetered has all the elements equal ")
else:
    print(("The enetered has not all the elements equal"))
"""


"""
print("Objective_6")
print("Dividing the contents of a tuple into separate variables")
t5 = (100,200,300,400)
a,b,c,d = t5
print("t5: ", t5,"has now become a:",a,"b:",b,"c:",c,"and d:",d)
"""


"""
print("Objective_7")
tuple1 = (1,2,3,4,5,6)
#Method_1
#tuple2 = [e for e in tuple1 if (e==3 or e==4)]
#Method_2
tuple2 = []
tuple2.append(tuple1[3])
tuple2.append(tuple1[4])
print(tuple2)
"""


"""
print("Objective_8")
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
tuple1 = list(tuple1)
l = len(tuple1)
temp = [y for x,y in tuple1]
temp.sort()
temp2 = []
i=j=0
while i<l:
    j=0
    while j<l:
        if (temp[i] == tuple1[j][1]):
            temp2.append(tuple1[j])
            break
        
        j = j+1
    i = i+1


tuple1 = tuple(temp2)
print(type(tuple1))
print(tuple1)
"""



"""
print("Objective_9")
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])
"""


"""
print("Objective_10")
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)
"""
