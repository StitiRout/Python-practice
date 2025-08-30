# OOPS part 1
# class
class Student :
    name = "Harsh kumar"
# object
s1=Student()
print(s1.name)

class Automobile :
    brand="Maserati"
    color = "Blue"
    version="Levante"
    price="1.50 cr in INR"
s2=Automobile()
print(s2.brand)
print(s2.color)
print(s2.version)
print(s2.price)
print(s2,end=" ")

#__init__() FXN
# Constuctor 
class Student :
    name = "Harsh kumar"
# default constructor
    def __init__(self):
        print(self)
        print("adding new student")
   

s1=Student()
print(s1.name)

class Student :
    def __init__(self,fullname):
# parameterized constructor
       self.name=fullname
       print("adding new student")
   

s1=Student("Stiti")
print(s1.name)
s2=Student("Saswoti")
print(s2.name)

class Family:
    family_name="Rout"
    def __init__(self,name,identity,age):
        self.name=name
        self.identity=identity
        self.age=age
m1=Family("Bhagaban Rout","Father",75)
print(m1.name,m1.identity,m1.age)
m2=Family("Dk Rout","son",47)
print(m2.name,m2.identity,m2.age)
m3=Family("Tapas sd Rout","grandson",23)
print(m3.name,m3.identity,m3.age)
print(m3.family_name)

# Methods
class Rout:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    def hello(self):
        print("hello ",self.name," and my age is ",self.age)
    def get_marks(self):
        return self.mark
R1=Rout("StitiRout",20,100)
R1.hello()
print(R1.get_marks())

class car:
   def __init__(self):
      self.acc=False
      self.brk=False
      self.clutch=False
   def start(self):
      self.clutch=True
      self.brk=True
      print("Car started")
s1=car()
car.start()

# Static method
class hell:
   @staticmethod
   def hello():
      print("hello")








