student = {
    "name": "Anu",  #key : value pairs
    "age": 21,
    "course": "Python"
}
print(student)

student = dict(name="Anu", age=21) #Creating a dictionary dict()
print(student)

#Empty dictionary
student = {}
print(student)

#Accessing values
student = {
    "name": "Anu",
    "age": 21,
    "course": "Python"
}
print(student["name"])
print(student["age"])

#Accessing values Using get()
print(student.get("name"))
print(student.get("city"))
print(student.get("city", "Not available"))

#Adding and updating values
#Add a new key
student = {
    "name": "Anu",
    "age": 21
}
student["city"] = "Bengaluru"
print(student)
#Change an existing value
student["age"] = 22
print(student)
#Change an existing value Using update()
student.update({"age": 23, "course": "Python"})
print(student)
#You can also write
student.update(city="Mysuru", status="Active")
#Removing dictionary values
#pop()
student = {
    "name": "Anu",
    "age": 21,
    "city": "Mysuru"
}
result = student.pop("age")
print(result)
print(student)

#popitem()
student = {
    "name": "Anu",
    "age": 21,
    "city": "Mysuru"
}

student.popitem()
print(student)

#del
student = {
    "name": "Anu",
    "age": 21
}
del student["age"]
print(student)

#clear()
student = {
    "name": "Anu",
    "age": 21
}

student.clear()
print(student)

#keys(), values(), items()
student = {
    "name": "Anu",
    "age": 21,
    "course": "Python"
}
print(student.keys()) #get all keys
print(student.values()) #get all values
print(student.items()) #get both keys and values

print(list(student.keys()))
print(list(student.values())) #Convert to list
print(list(student.items()))

#Checking membership using in and not in
student = {
    "name": "Anu",
    "age": 21
}

print("name" in student)
print("Anu" in student)  #in checks keys by default, not values.
print("Anu" in student.values())
print("city" not in student)

#Dictionary keys must be hashable
data = {
    10: "Integer",
    2.5: "Float",
    "name": "String",
    (1, 2): "Tuple"
}
print(data)

#Duplicate keys
student = {
    "name": "Anu",
    "age": 20,
    "age": 22
}
print(student)

#Duplicate values are allowed
scores = {
    "Rahul": 90,
    "Anu": 90,
    "Kiran": 85
}
print(scores)

#nested dictionary
students = {
    "student1": {
        "name": "Rahul",
        "age": 22
    },
    "student2": {
        "name": "Anu",
        "age": 21
    }
}
print(students)

#Accessing nested values
print(students["student1"]["name"])
print(students["student2"]["age"])

#Updating nested values
students["student1"]["age"] = 23
print(students["student1"])

#List inside a dictionary
student = {
    "name": "Rahul",
    "subjects": ["Python", "SQL", "Linux"],
    "marks": [85, 90, 88]
}

print(student["subjects"])
print(student["subjects"][0])
print(student["marks"][1])

#Dictionary inside a list
students = [
    {"name": "Rahul", "age": 22},
    {"name": "Anu", "age": 21},
    {"name": "Kiran", "age": 23}
]

print(students[0]["name"])
print(students[1]["age"])

#Copying a dictionary — copy()
original = {
    "name": "Anu",
    "age": 21
}

copied = original.copy()
print(original)
print(copied)
print(original == copied)
print(original is copied)