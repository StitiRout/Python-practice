# File i/o
# reading
# f = open("demo.txt","r")
# data = f.read(5)
# print(data)
# print(type(data))
# line1 = f.readline()
# print(line1)
# line2=f.readline()
# print(line2)

# writing
g=open("demo.txt","w")
g.write("this a new line")

g1=open("demo.txt","a")
g1.write("this is added at the end of the line ")




# f.close()
g.close()