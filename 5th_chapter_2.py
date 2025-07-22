# for loop
list=[1,2,3,4,5,6,7,8,9,0]
for el in list :
    print(el)

#for loop with else is optional(where we use break)
else:
    print("end") 

tup=["potato","tomato","egg elephant","cucumber","bitter guard"]
for vegies in tup:
    print(vegies)

str="StitiRout"
for char in str:
    if(char=='i'):
        print(" 'i' found")
        break
    print(char)
else:
    print("not there")

# print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
num=[1,4,9,16,25,36,49,64,81,100]
for elements in num:
    print(elements)

# Search for a number x in this tuple using loop
# [1,4,9,16,25,36,49,64,81,100]
number =(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter a number : "))
for el in number:
    if(x==el):
        print("found")
    print(el)
else:
    print("not found")