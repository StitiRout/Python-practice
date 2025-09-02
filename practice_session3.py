class Student:
    name="Stiti"
    age=20
    section="2M1"
    year="3rd"
a=Student()
print(a.name)
print(a.age)
print(a.section)
print(a.year)
class family:
    family_name="Rout"
    def __init__(self,name,identity,age):
        self.name=name
        self.identity=identity
        self.age=age
a=family("BhagabanRout","Grandpaa",75)
b=family("GodavariRout","Grandma",75)
print(a.name)
print(a.identity)
print(a.age)
print(b.name)
print(b.identity)
print(b.age)
class marking:
    def __init__(self,name,mark,age):
        self.name=name
        self.mark=mark
        self.age=age
    def hello(self):
        print("Hello,my name is ",self.name," . I am ",self.age," years old ."," I got ",self.mark," marks .")
    def markss(self):
        return self.mark
c=marking("Stiti",100,20)
c.hello()
print(c.markss())

class car :
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clause=False
    def starting(self):
        self.brk=True
        self.clause=True
        print("Car started")
d=car()
d.starting()
class bank :
    def __init__(self,acc_number,password):
        self.acc_number=acc_number
        self.password=password
    def private(self):
        print(self.__password)
e=bank("1234567890","qw23vg")
print(e.acc_number)
print(e.private)  