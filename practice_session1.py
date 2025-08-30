str1= "Stiti prangya rout "
a=str1.endswith("out")
print(a)
b=str1.find("S")
print(b)
c=str1.replace("rout","priyadarshani")
print(c)
d=str1[1:5]
print(d)
e=str1.capitalize()
print(e)
f=str1.count("rout")
print(f)
g=3.14
g=str(a)
print(type(g))
# h=int(input("Enter a number"))
# i=int(input("Enter another number"))
# sum=h+i
# print(sum)
list=[23,24,25,26,27,28,29]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.pop(0)
print(list)
list.append(22)
print(list)
list.insert(0,21)
print(list)
list.remove(22)
print(list)
tuple1=(67,78,89)
print(tuple1.index(89))
print(tuple1.count(78))
student = {
    "name" :"Stiti",
    "age" :20,
    "section" :"M1",
    "programming" :["Python","java","sql"],
    "current cgpa"  : 8.73
}
print(student)
print(student["name"])
family ={
    "Father" :"DK ROUT",
    "Mother" :"S ROUT",
    "Grand" : {
        "Father":"B ROUT",
        "Mother":"G ROUT"
    }
}
print(family)
print(family["Father"])
print(family["Mother"])
print(family["Grand"],["Mother"])
print(family["Grand"],["Father"])