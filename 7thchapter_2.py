# deleting a file
# import os
# os.remove("sample.txt")

# practice question
# create a new file "practice.txt" using python .add the following data 
f=open("practice.txt","w")
f.write("hi everyone \n we are learning file i/o \n using python \n i like programming in python")

# WAF that replace all occurence of "python" with "java"
def fxn(): 
 with open("practice.txt","r") as f:
    data=f.read()
 new_data=data.replace("python","java")
 print(new_data)
fxn()
# Search if  the word "learning" exists in the file or not
def fxn2():
 word="learning"
 with open ("practice.txt","r") as f:
   data1=f.read()
   if(data1.find(word) != -1):
       print("found")
   else:
       print("not found")
fxn2()
# search for the exact line
def fxn2():
   word2="learning"
   data2 =True
   line=1
   with open("plaintxt","r") as f :
      while data2:
       data2=f.readline()
       if(word2 in data2):
         print(line)
       line+=1  
      