str1 ="this is a string. \n  i am reading chapter 2 of python."
print(str1)
# \n for next line 
# \t for tab
# concatenation
str2="Stiti"
str3="Rout"
print(str2+str3)
# length of string including space
print(len(str1))
# indexing
ch=str1[0]
print(ch)
# slicing
str =str1[1:5]
print(str)
str5 =str1[6:]
print(str5)
# negative indexing
str6="Apple and orange"
a=str6[-6:-1]
print(a)
# string fxns
line="i am a ethical hacker"
b=line.endswith("er")
c=line.find("r")
d=line.capitalize()
e=line.replace("ethical","white-hat")
f=line.count("am")
print(b)
print(c)
print(d)
print(e)
print(f)
