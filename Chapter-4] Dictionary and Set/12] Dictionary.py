# The program demonstrate the use of Dictionary in python.

Info= {
    "name":"piyush",
    "cgpa":9.8,
    "marks":[98, 97, 99],
}
print(type(Info))
print(Info)

# Acessing the value ;
print(Info["name"]) # piyush
print(Info["cgpa"]) # 9.8
print(Info["marks"])# [98, 97, 99]

# Assigning the value ;
Info["name"]= "Ayush"
Info["cgpa"]= 9.9
Info["marks"]= [99, 98, 99]
print(Info)

# We can create a null dictionary and over the period of time we can add data in it.
Null_dict={}
print(Null_dict)
Null_dict["name"]="piyush"
print(Null_dict)

# Nested dictionary.
student= {
    "name":"piyush",
    "subjects": {
        "physics":98,
        "chemistry":99,
        "maths":100,
                       }
}
print(student)
print(student["subjects"])
print(student["subjects"] ["maths"]) # usecase of Nested dictionary #

# Dictionary Methods
student= {
    "name":"piyush",
    "subjects": {
        "physics":98,
        "chemistry":99,
        "maths":100,
                       }
}

# 1] dict.keys() 
print(student.keys())
print(list(student.keys()))
print(tuple(student.keys()))

# 2] dict.values()
print(student.values())
print(list(student.values()))
print(tuple(student.values()))

# 3] dict.items()
print(student.items())
print(list(student.items()))
print(tuple(student.items()))

# 4] dict.get("key")
print(student.get("name"))
print(student.get("subjects"))
print(student.get("subjects"))

# 5] dict.update(newd dict) or dict.updates("key":"values")
Biodata= {"age":18 , "height":"5.4 inch"}
student.update(Biodata)
print(student)