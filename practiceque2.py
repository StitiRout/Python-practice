# que on list
# WAP TO ASK USER TO ENTER NAMES OF THEIR 3 FAVORTE MOVIES AND STORE THEM IN A LIST
movies=[]
movie1=input("Enter your first favorite movies")
print(movie1)
movie2=input("Enter your second favorite movies")
print(movie2)
movie3=input("Enter your third favorite movies")
print(movie3)
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

# another way to answer
movies =[]
movies.append(input("Enter 1st movie"))
movies.append(input("enter your second movie"))
movies.append(input("enter your 3rd movie"))
print(movies)


# WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS 
# PALINDROM= SAAMNE SE OR PICHE SE SAME HO
palindrome = [1,2,3,2,1]
copy = palindrome.copy()
copy.reverse()

if(copy == palindrome) :
    print("yes it is a palindrome")
else:
    print("no,it is not a palindrome ")    
  
