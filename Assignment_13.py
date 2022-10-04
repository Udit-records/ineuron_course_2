"""
print("Objective_1\n")
#Method_1
#list_1 = ["Java","Python","SQL","C"]


#Method_2
list_1 = []
count = int(input("Enter the number of members of the List"))
i=0
while i<count:
    list_1.append(input())
    i+=1

print(list_1)

#Method_3
#list_1 = eval(input())
print(list_1)


#Method_4
#list_1 = list(i for i in input("Enter the words separated by comma: ").split(","))
list_1 = [i for i in input("Enter the words separated by comma: ").split(",")]
print("The entered list is ", list_1, "with type, type(list_1")
"""


"""
print("Objective_2\n")
#Method_1
#list_1 = ["Java","Python","SQL","C"]



#Method_2
list_1 = []
count = int(input("Enter the number of members of the List: "))
i=0
while i<count:
    list_1.append(input())
    i+=1



#Method_3
#list_1 = eval(input("Enter the input in the form list\n"))

#Method_4
#list_1 = list(input())

print(type(list_1))
"""


"""
print("Objective_3\n")
mylist = ["Java", "C", "Python"]
print(mylist[2])
"""

"""
print("Objective_4\n")
thislist = ["Java","SQL","C","Reactnative","Javascript","Python"]
print("\"thislist\" before replacement:\n",thislist)
thislist[thislist.index("SQL")] = "NoSQL"
thislist[thislist.index("Reactnative")] = "Flutter"
print("\"thislist\" post-replacement: ")
print(thislist)
"""


"""
print("Objective_5\n")
mylist = ["Java", "SQL","C","Reactnative"]
print("\"mylist\" before adding:\n",mylist)
mylist.append("Python")
print(mylist)
"""


"""
print("Objective_6\n")
firstlist = ["Java","Python","SQL"]
secondlist = ["C","Cpp","NoSQL"]
firstlist = firstlist + secondlist
print("The list after appending:",firstlist)
"""


"""
print("Objective_7\n")
thislist = ["Java","SQL","C","Reactnative","Javascript","Python"]

#Method_1
for i in thislist:
    print(i)

#Method_2
j=0
while j< len(thislist):
    print(thislist[j])
    j+=1
"""


"""
print("Objective_8\n")
thislist = ["Java","SQL","C","Reactnative","Javascript","Python"]

#Method_1
print("\"thislist\" after sorting: ",sorted(thislist))

#Method_2
thislist.sort()
print("\"thislist\" after sorting: ",thislist
"""


"""
print("Objective_9\n")
my_city_list = []
count = int(input("Enter the number of members of the List: "))
i=0
while i<count:
    my_city_list.append(input())
    i+=1

print(my_city_list)
"""


"""
print("Objective_10\n")
my_number_list = []
count = int(input("Enter the number of members of the List: "))
i=0
while i<count:
    my_number_list.append(int(input()))
    i+=1

print(my_number_list)
"""




