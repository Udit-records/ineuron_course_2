"""
print("Objective_1")
#d1 = dict(name="Anonymous", age=28, gender="Male", Qualification = "Btech")
d1 = {"name":"Anonymous", "age":28, "gender":"Male", "Qualification":"Btech"}
print(d1)
print(type(d1))
"""


"""
print("Objective_2")
#d2 = dict(name="Anonymous", age=28, gender="Male", Qualification = "Btech")
d2 = {"name":"Anonymous", "age":28, "gender":"Male", "Qualification":"Btech"}
print("Accessing the dictionary values: ",d2["name"])
"""


"""
print("Objective_3")
#d3 = dict(name="Anonymous", age=28, gender="Male", Qualification = "Btech")
d3 = {"name":"Anonymous", "age":28, "gender":"Male", "Qualification":"Btech"}
print("Accessing the dictionary values using values() method of the class dict")
print(d3.values())
"""


"""
print("Objective_4")
#d4 = dict(name="Anonymous", age=28, gender="Male", Qualification = "Btech")
d4 = {"name":"Anonymous", "age":28, "gender":"Male", "Qualification":"Btech"}
print("Accessing a dictionary value by referring key of the dictionary")
d4["name"] = "Anonymous"
print(d4)
"""


"""
print("Objective_5")
#d5 = dict(name="Anonymous", age=28, gender="Male", Qualification = "Btech")
d5 = {"name":"Anonymous", "age":28, "gender":"Male", "Qualification":"Btech"}
#Method_1
[print(k) for k in d5.keys()]
#Method_2
for k in d5:
    print(k)
#Method_3
print("Accessing the dictionary keys using keys() method of the class dict")
print(d5.keys())
"""


"""
print("Objective_6")
d6 = dict(Detail_1=dict(name="Anonymous_1", age=28, gender="Male"), Detail_2=dict(name="Anonymous_2", age=29, gender="Female"),Detail_3=dict(name="Anonymous_3", age=30, gender="Male"))
#d6 = {"Detail_1":{"Name":"Anonymous_1","Age":28}, "Detail_2":{"Name":"Anonymous_2","Age":29},"Detail_3":{"Name":"Anonymous_3","Age":30}}
print("Creating a nested dictionary")
print(d6["Detail_1"])
"""


"""
print("Objective_7")
d7_1 = dict(Detail_1=dict(Name="Anonymous_1",Age=28))
d7_2 = dict(Detail_2=dict(Name="Anonymous_2",Age=29))
d7_3 = dict(Detail_3=dict(Name="Anonymous_3",Age=30))
d7 = dict(Detail_1=d7_1, Detail_2=d7_2,Detail_3=d7_3)
#d7_1 = {"Detail_1":{"Name":"Anonymous_1","Age":28}}
#d7_2 = {"Detail_2":{"Name":"Anonymous_2","Age":29}}
#d7_3 = {"Detail_3":{"Name":"Anonymous_3","Age":30}}
#d7 = {"Detail_1":d7_1, "Detail_2":d7_2,"Detail_3":d7_3}

print("Creating a nested dictionary")
print(d7["Detail_1"])
"""


"""
print("Objective_8")
name = ["Anonymous_1","Anonymous_2","Anonymous_3"]
age= [18,25,44]
#Method_1
#d8 = {name[0]:age[0],name[1]:age[1],name[2]:age[2]}

#Method_2
d8_temp = {}
k = 0
while k<3:
    d8_temp[name[k]] = age[k]
    k= k+1

print(d8_temp)
"""

"""
print("Objective_9")
detail_1 = dict(name1="Anonymous_1",name2="Anonymous_2",name3="Anonymous_3")
detail_2= dict(name4="Anonymous_4",name5="Anonymous_5",name6="Anonymous_6")
#Method_1
#for k in detail_2:
#    detail_1[k] = detail_2[k]

#Method_2
#for k,v in detail_2.items():
#   detail_1[k] = v

#Method_3
for k in detail_2.keys():
    detail_1[k] = detail_2[k]

print(detail_1)
"""


"""
print("Objective_10")
sample_dict = {'C': 92,'Java': 66,'Python': 85}
temp = min(sample_dict.values())
#temp.sort()
#list_x = [print(x) for x,y in sample_dict]
print(temp)

for i in sample_dict:
    if sample_dict[i]==temp:
        print(i)
"""
