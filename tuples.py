# tuple
number = (2,3,7,5,0,1,2)
print(type(number))
num=(32,)
print(type(num))
numb=(4)
print(type(numb))
# tuple slicing
print(number[1:5])
# tuple method
print(number.index(0))
print(number.count(2))

# practice que on tuple
# WAP TO COUNT THE NUMBER OF THE STUDENTS WITH THE "A" GRADE IN THE FOLLOWING TUPLE
grade = ("A","B","C","A","A","D","B")
print(grade.count("A"))

# Store the above values in a list and sort them from a to d
grade = ["A","B","C","A","A","D","B"]
grade.sort()
print(grade)
