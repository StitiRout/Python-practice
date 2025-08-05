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
# IF YOU WANT TO CHANGE THE NAME
s1.name="Tony"
s1.average()

# Create account class with 2 attributes- baalance and account no. creat methods for debit,creadit annd printing balance
class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
    def debit(self,amount):
        self.balance=self.balance-amount
        print(amount,"rupees debited")
        print("final balance : ",self.balance)
    def credit(self,amount):
        self.balance=self.balance+amount
        print(amount,"rupees credited")
        print("final balance : ",self.balance)
    def final_balance(self):
        return self.balance
s1=Account(100000000,1234567890)
print(s1.balance)
print(s1.acc_no)
s1.debit(2000)
s1.credit(90000)
print(s1.final_balance())