# function and recursion
# FUNCTION
# def calc_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# calc_sum(34,56)

# def mul(a,b):
#     multy=a*b
#     print(multy)
#     return multy
# mul(9,0)

# def hello():
#     print("hello")
# hello()

# find the average of 3 numbers
# def avg(a,b):
#     average=(a+b)/2
#     print(average)
#     return average
# avg(23,45)

# TYPES OF FXN
# built-in and user-defined
# Built-in
# print("stitirout",end=" ")
# user-defined
# written by programmer

# Default parameters
# def div(a=1,b=1):
#     print(a/b)
#     return a/b
# div()
# def div(a,b=1):
#     print(a/b)
#     return a/b
# div(4)

# WAP to print the length of a list (list of the parameter)
# city=["delhi","noida","pune","chennai","bbsr"]
# def city_count():
#     output=len(city)
#     print(output)
#     return output
# city_count()

# 2nd simplest way
# hero=("thor","spiderman","kriss","ironman","superman","captain america")
# def hero_count(hero):
#     print(len(hero))
# hero_count()

# WAF to print the elements of a list in a single line.(list is the parameters)
# hero=("thor","spiderman","kriss","ironman","superman","captain america")
# in simple way
# print(hero[0],end=" ")
# print(hero[1],end=" ")
# print(hero[2],end=" ")
# print(hero[3],end=" ")
# print(hero[4],end=" ")
# print(hero[5],end=" ")
# if we use fxn
# def single(hero):
#     for el in hero:
#         print(el,end=" ")
# single(hero)
# print()

# WAF to find the factorial of n (n is the parameter)
# n=int(input("Enter a number : "))
# def fact(n):
#     p=1
#     for el in range(1,n+1):
#        p *= el
#     print(p)
# fact(n)

# waf to convert usd to inr
# x=int(input("Enter the dollar number : "))
# def inr_count(x):
#   one_dollar = 83
#   rupee=x*one_dollar
#   print(rupee,"in inr")
#   return rupee
# inr_count(x)

# waf to take a number and print wheather it is an odd or even number 
number = int(input("Enter a number"))
def odd_or_even(number):
    if(number%2==0):
        print("even")
    else:
        print("odd")
odd_or_even(number)