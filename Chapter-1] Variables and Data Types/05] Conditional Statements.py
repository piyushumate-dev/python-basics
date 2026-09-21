# Program demonstrates the use of conditional statements in Python.
# By using the example of traffic light, we can understand the use of if, elif and else statements in Python.
Light_Colour = input("Colour :")
if(Light_Colour == "Red" or Light_Colour == "red"):
    print("Stop")
elif(Light_Colour == "Yellow" or Light_Colour == "yellow"):
    print("Get Ready")
elif(Light_Colour == "Green" or Light_Colour == "green"):
    print("Go")
else:
    print("Light is Broken")

# By using the example of school grading system, we can understand the use of if, elif and else statements in Python.
School_Marks= int(input("Enter Your marks:"))
if (School_Marks>90 and School_Marks<=100):
    print("Your Grade is A")
elif(School_Marks>80 and School_Marks<=90):
    print("Your Grade is B")
elif(School_Marks>70 and School_Marks<=80):
    print("Your Grade is C")
elif(School_Marks<70 and School_Marks>=0):
    print("Your Grade is D")
else:
    print("  WOW!, What an acheivement! You have scored ",School_Marks, "marks. Please check your marks again.")

# It is a program that takes three numbers as input and prints the greatest number among them using conditional statements in Python.
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if(a>b and a>c):
    print("a is the greatest")
elif(b>c and b>a):    
    print("b is the greatest")
elif(c>a and c>b):
    print("c is the greatest")

# It is a program that checks if a number is a multiple of 7.
Num=int(input("Enter your number:"))
if( Num % 7 ==0):
    print("The number is Multiple of 7")
else:
    print("The number is not Multiple of 7")
    
# It demonsterates the use of "Single line if-else" ( Ternary Operator ) conditional statements in Python.
Food = input("Food :")
print("Yes") if(Food=="Cake" or Food=="cake") else print("No")


#It demonsterates the use of "Clever if-else" (Ternary) conditional statements in Python.

#Example 1]
Age = int(input("Age :"))
Vote = ("Yes, you can vote", "No, you can't vote") [Age < 18]
print(Vote)

#Example 2]
Salary = float(input("Salary :"))
Tax = (Salary * 0.1, Salary * 0.2)[Salary > 50000]
print("You have to pay tax of" , Tax)