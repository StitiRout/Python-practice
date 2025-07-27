# RECURSION
# reverse n to 1
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)

# factorial
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(9))

# Write a recursive funcion to calculate the sum of firt n natural numbers
# def natural_num(n):
#     if(n==0):
#         return 
#     return natural_num(n-1)+n
# sum = natural_num(5)
# print(sum)

# write a recursive fxn to print all elements in a list ,HINT: use list and index as parameters
fruit=["apple","mango","grapes","tangerines"]
def abc(list,idx=0):
    if (idx==len(list)):
        return
    print(list[idx])
    abc(list,idx+1)
print(abc(fruit))