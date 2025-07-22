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
