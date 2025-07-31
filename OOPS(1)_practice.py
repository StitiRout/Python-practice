# Practice questions of OOPS(1)
# Create student class takes name and marks of 3 subjects as an arguments in constructor then create a method to print thre avg
class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def average(self):
        sum=0
        for el in self.mark:
            sum+=el
            avg=sum/3
        print("hii,",self.name,"your average mark is  : ",avg)  
s1=Student("Marrie ",[88,78,68])
s1.average()

s1.name="Tony"
s1.average()