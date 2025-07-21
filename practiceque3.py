# Store the following word meaning in a python dictionary
dict_1={
    "tables" : ("a piece of furniture","list of facts and figures"),
    "cat" : "a small animal"
}
print(dict_1)


# you are given a list of subjects for students .Assume one classroom is required for 1 subject .
# how many classrooms are needed by all students
classroom={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(classroom)
print(len(classroom))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary .Start with an empty dictionary and add
# one by one .Use subject as key and marks as values
markings={}
mark1=int(input("Enter maths : "))
markings.update({"maths":mark1})
mark2=int(input("Enter phy : "))
markings.update({"phy":mark2})
mark3=int(input("Enter chem : "))
markings.update({"chem":mark3})
print(markings)

# Figure out a way to store 9 and 9.0 as separate valuess in the set(You can take help of built-in data types)
values={
    ("float",9.0),
    ("int",9)
}
print(values)