# Q1] Write a program to ask the user to enter names of their 3 favorite movies and store them in a list .

movie1= input("Enter 1st movie:")
movie2= input("Enter 2nd movie:")
movie3= input("Enter 3rd movie:")
Movies= [movie1, movie2, movie3]
print(type(Movies))
print(Movies)

# Q2] Write a program to check if a list contain palindrome of  elements # (Hint: use copy() method) 

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))
list=[num1, num2, num3,]
print(type(list))
copy_list = list.copy()
copy_list.reverse()

if(copy_list==list):
    print("Palindrome")
else:
    print("Not a palindrome")

# Q3] Write a program to count the number of students with grade "A" in the following tuple

Grade=("C","D","A","A","B","B","A")
print("Their are",Grade.count("A"),"student who got A grade")

# 4] Store the above values in a list and sort them from "A" to "D"
Grade=["C","D","A","A","B","B","A"]
print(type(Grade))
Grade.sort()
print(Grade)
