# loops
# while loops
# count=1
# while count <=5:
#     print("hello")
#     count +=1

# print(count)
 
# i = 0
# while i <=9:
#     print("Stiti")
#     i+=1

# # print from 1 to 100
# j=1
# while j<=100:
#     print(j)
#     j+=1
# #print from 100 to 1
# k=100
# while k >=1:
#     print(k)
#     k-=1 

# # print the multiplication table of a number n
# mul=int(input("Enter the number for your multiplication table"))
# s=1
# while s <=10:
#     print(mul,"x",s,"=",mul*s)
#     s+=1

# # print the squares from 1 to 10
# num=1
# while num<=10:
#     print(num*num)
#     num+=1

# # print the elements of the following list sing a loop
# # [1,4,9,16,25,36,59,64,81,100]
# num=[1,4,9,16,25,36,59,64,81,100]
# idx=0
# while idx < len(num):
#     print(num[idx])
#     idx+=1
# num2=[23,34,45,56,6,767,78,89,90]
# idx2=1
# while idx < len(num2):
#     print(num2[idx])
#     idx+=1
# num3=[2,3,4,5,6,7]
# idx3=1
# while(idx<len(num3)):
#     print(num[idx])
#     idx3+=1
# heros=["ironman","thor","spiderman","batman"]
# idx4=1
# while(idx4<len(heros)):
#     print(heros[idx4])
#     idx4+=1

# search for a number x n this tuple using loop:
# number=[1,4,9,16,25,36,49,64,81,100]
# x =int(input("Enter a number to search from the list : "))
# index=1
# while index < len(number) :
#     if(number[index] == x):
#         print("got the number")
        #  we can use  break here
#     else:
#         print("does not exist")
#     index+=1

# break and continue
# BREAK
# i=1
# while i <=5:
#     print(i)
#     if(i ==4):
#         break
#     i+=1
# print("end of loop")

# CONTINUE
# i=0
# while i <=5:
#     if(i ==4):
#         i+=1
#         continue    
        # except 4 all will be print            
    # print(i)
    # i+=1
# print odd number skip even numbers
# i= 0
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

#print even skip odd
i=0
while i <=10:
    if(i%2 != 0):
        i+=1
        continue
    print(i)
    i+=1