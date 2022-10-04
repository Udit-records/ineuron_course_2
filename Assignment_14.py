"""
print("Objective_1:First N natural numbers")
#Method_1
#num_1 = list(i for i in range(1,int(input("Enter the number of terms(N): "))+1))
num_1 = list(range(1,int(input("Enter the number of terms(N): "))+1))
print(num_1)
#Method_2
num = []
[num.append(i) for i in range(1,int(input("Enter the number of terms(N): "))+1)]
print(num)
"""



"""
print("Objective_2:First N odd natural numbers")
#Method_1
num_1 = list((i*2)+1 for i in range(1,int(input("Enter the number of terms(N): "))+1))
print(num_1)
#Method_2
num = []
[num.append((i*2)+1) for i in range(1,int(input("Enter the number of terms(N): "))+1)]
print(num)
"""



"""
print("Objective_3:First N even natural numbers")
#Method_1
num_1 = list(i*2 for i in range(1,int(input("Enter the number of terms(N): "))+1))
print(num_1)
#Method_2
num = []
[num.append(i*2) for i in range(1,int(input("Enter the number of terms(N): "))+1)]
print(num)
"""



"""
print("Objective_4:Greatest number in the list of numbers")
num_list = [1,2,3,4,5,6,7,8,9,10]
print(max(num_list))
"""



"""
print("Objective_5:Smallest number in the list of numbers")
num_list = [1,2,3,4,5,6,7,8,9,10]
print(min(num_list))
"""



"""
print("Objective_6:Sum of the numbers in the list")
num_list = [1,2,3,4,5,6,7,8,9,10]
print(sum(num_list))
"""



"""
print("Objective_7:The list without non zero elements")
num_list = [1,2,3,4,0,6,7,8,9,10]
non_zero_list = [i for i in num_list if i!=0]
non_zero_list_1 = list(i for i in num_list if i!=0)
print(non_zero_list)
print(non_zero_list_1)
"""



"""
print("Objective_8:The list distinct elements and their frequency")
distinct_list = [1,2,3,1,2,3,"python","SQL","Cpp","python","SQL"]
diff_element = []
diff_count = []
count =0

for i in distinct_list:
    if i in diff_element:
        print("Nopes")
    elif i not in diff_element:
        diff_count.append(distinct_list.count(i))
        diff_element.append(i)
    

j = 0
while j < len(diff_element):
    print(diff_element[j],"appered",diff_count[j],"times")
    j = j+1
"""



"""
print("Objective_9:Occurence of the enetered element")
distinct_list = [1,2,3,1,2,3,"python","SQL","Cpp","python","SQL"]
same_index = []
count=0
element = input("Enterted the element to find its occurences in the list: ")

i=0
for i in distinct_list:
    if str(i) == element:
        same_index.append(count)
        
    count = count+1

print("The element",element, "appeared in the indices ",same_index,"of the the list")
"""


print("Objective_10: Sorting the entered list")
distinct_list = ["python","SQL","Cpp","python","SQL"]

print(sorted(distinct_list))

