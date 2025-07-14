# dictionary 
info = {
    "key " : "values",
    "name" : "stiti",
    "learning" : "coding"
}
print(info)
# things we can use in dictionary are ---
student = { 
    "name " : "Shree",
    "sl no" : 42,
    "cgpa"  : 8.6,
    "is_pass" : True,
    "language" : ["java","python","javascript","sql"],     
    "programming" : ("java","python")
}
print(student)
print(type(student))
print(info["name"])
print(student["name "])
print(student["sl no"])
print(student["cgpa"])
print(student["is_pass"])
print(student["language"])
print(student["programming"])
print(info["key "])
print(info["learning"])
# null dictionary
null_dict={}
print(null_dict)

# Nested python
girls={
    "total" : 6,
    "score" : {
        "maths" : 82,
        "phy" :77,
        "chem" :65,
        "eng" :89,
        "pe" : 92
    }
}
print(girls["total"])
print(girls["score"]["eng"])
print(girls["score"]["maths"])

# Dictonary Methods
print(girls.keys())
print(girls.values())
print(girls.items())
girls.get("chem")
print(girls)
girls.update({"hindi" : 67})
print(girls)

