# n=1
# mul=int(input("Enter a number"))
# print("Multiplication table is")
# while n <=10 :
#     print(mul,"x",n,"=",mul*n)
#     n+=1
# o=1
# div=int(input("Enter a number"))
# print("Division of the number is")
# while o <=10:
#     print(div,"%",o,"=",div/o)
#     o+=1
# p=1
# while p<=100:
#     print(p*p)
#     p+=1
# num=[21,22,23,24,25,26,27,28,29,30]
# index=0
# while index<=len(num):
#     print(num[index])
#     index+=1
# num2=[31,32,33,34,35,36,37,38,39,40]
# idx=0
# search=int(input("Enter the number you want to search:"))
# while idx<=len(num2):
#     if num2[idx]==search :
#        print("found")
#        break
#     idx+=1
# for el in range(20):
#     print(el)
# for el in range(12):
#     if (el%2==0) :
#         print(el)
# id=1
# n=int(input("Enter a number"))
# sum=0
# while id >= n:
#     sum+=id
#     print(sum)
# n =int(input("enter a number :"))
# i=1
# sum=0
# while i <= n:
#     sum+=i
#     print(sum)   
# z=int(input("Enter a number:"))
# product=1
# for el in range(1,z+1):
#     product*=el
#     print(product)
# def cal_sum(a,b):
#     sum=a+b
#     print(sum)
# cal_sum(2,3)
# def hello():
#     print("hello")
# hello()
# def avg(a,b,c):
#     avrg=(a+b+c)/3
#     print(avrg)
# avg(45,67,89)
# print("StitiRout",end=" ")
# city=["delhi","mumbai","noida","bbsr"]
# def city_count():
#     output=len(city)
#     print(output)
#     return output
# city_count()
# rupee=int(input("Enter the amount"))
# def rupee_converter():
#     dollar=84
#     rupees=rupee*dollar
#     print(rupees)
#     return rupees
# rupee_converter()
# def show(n):
#     if n==1:
#         return 1
#     else:
#         print(n)
#         show(n-1)
# show(10)
def nwe():
    with open("section.txt","w") as g:
       g.write("I am a girl")
       with open("section.txt","r") as g:
        data2=g.replace("girl","boy")
        print(data2)
nwe()