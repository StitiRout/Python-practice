# question1
str1=input("Enter your name:")
print(str1)
print("length of your name is  ",len(str1))
# question2
print(str1.find("prangya"))
print(str1.count("pr"))
# question3
a=int(input("Enter your age"))
if(a>18):
    print("you are able to vote")
elif(a<=18):
    print("you are not able to vote")
else:
    print("invalid input")        
# traffic problem
light =str(input("Enter the traffic light : "))
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("wait")
elif(light=="green"): 
    print("go")   
else:
   print("invalid input") 
# grading problem
mark=int(input("Enter the student's mark : "))
if(mark>=90):
    print("grade: A")
elif(mark>=80 and mark<=90):
    print("grade: B")
elif(mark>=70 and mark<=80):
    print("grade: C")
else:
    print("grade: D")
# question4
num=int(input("Enter an number: "))
if(num%7==0):
    print("this is a multiple of 7")
else:
    print("this is not a multiple of 7")  
    
#question5
number=int(input("Enter a number : "))
if(number%2==0):
    print("number is even")
else:
    print("number is odd")
    
#question6
g1=int(input("Enter the  first numbers"))  
g2=int(input("Enter the  second numbers"))
g3=int(input("Enter the third numbers"))

if(g1>=g2 and g1>=g3):
    print("first number is largest",g1)
elif(g2>=g3):
    print("Second number is largest",g2) 
else:
    print("third is largest",g3)   