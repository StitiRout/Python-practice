# loops
# while loops
count=1
while count <=5:
    print("hello")
    count +=1

print(count)
 
i = 0
while i <=9:
    print("Stiti")
    i+=1

# print from 1 to 100
j=1
while j<=100:
    print(j)
    j+=1
#print from 100 to 1
k=100
while k >=1:
    print(k)
    k-=1 

# print the multiplication table of a number n
mul=int(input("Enter the number for your multiplication table"))
s=1
while s <=10:
    print(mul,"x",s,"=",mul*s)
    s+=1

# print the squares from 1 to 10
num=1
while num<=10:
    print(num*num)
    num+=1

# print the elements of the following list sing a loop
# [1,4,9,16,25,36,59,64,81,100]
num=[1,4,9,16,25,36,59,64,81,100]
idx=0
while idx < len(num):
    print(num[idx])
    idx+=1
num2=[23,34,45,56,6,767,78,89,90]
idx2=1
while idx < len(num2):
    print(num2[idx])
    idx+=1