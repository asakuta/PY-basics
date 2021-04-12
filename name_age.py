import math

def nameAge(data):
    name=input("Name: ")
    if name is not "":
        age=input("Age: ")
        data.insert(len(data), {"name": name, "age": age})
        nameAge(data)
    if name is "":
        for item in data:
            result=item["name"]+": "+item["age"]
            print(result)

data=[]
nameAge(data)