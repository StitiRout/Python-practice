# for loop
# list=[1,2,3,4,5,6,7,8,9,0]
# for el in list :
#     print(el)

# #for loop with else is optional(where we use break)
# else:
#     print("end") 

# tup=["potato","tomato","egg elephant","cucumber","bitter guard"]
# for vegies in tup:
#     print(vegies)

# str="StitiRout"
# for char in str:
#     if(char=='i'):
#         print(" 'i' found")
#         break
#     print(char)
# else:
#     print("not there")

# print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
# num=[1,4,9,16,25,36,49,64,81,100]
# for elements in num:
#     print(elements)

# Search for a number x in this tuple using loop
# [1,4,9,16,25,36,49,64,81,100]
# number =(1,4,9,16,25,36,49,64,81,100)
# x=int(input("Enter a number : "))
# for el in number:
#     if(x==el):
#         print("found")
#         break
#     print(el)
# else:
#     print("not found")

# Range
# print(range(10))
# sequence=range(10)
# print(sequence[0])
# print(sequence[1])
# print(sequence[2])
# print(sequence[3])
# print(sequence[4])
# print(sequence[5])
# for el in sequence:
#     print(el)
#     # for stop
# for el in range(20):         
#     print(el)
#     # for start,stop
# for el in range(1,20):
#     print(el)
    # for start,stop,step
# for el in range(1,20,2):
#     print(el)

# print the even numbers
# for el in range(10):
#     if(el%2==0):
#      print(el)
    #or 
# for el in range(0,10,2):
#    print(el)

# print number from 1 to 100

# for el in range(1,100,1):
#     print(el)

# print number from 1000 to 1
# for el in range(1000,0,-1):
#     print(el)

#print the multiplication  table of a number n
x =int(input("enter a number :"))
for el in range(0,11):
    print(x,"x",el,"=",x*el)  