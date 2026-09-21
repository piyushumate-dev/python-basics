# Q-1 # write a proogram to input two numbers and print their sum, difference, product.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
sum=a+b
difference=a-b
product=a*b
print("sum:",sum)
print("difference:",difference)
print("product:",product)

# Q-2 # Write a program to input a side of a square and print it's area.
side=float(input("Enter the side of the square:"))
area=side*side        # instead of side*side we can write side**2 #
print("Area of the square:", area)

# Q-3 # Write a program to input two floating point numbers and print their average.
a=float(input("Enter first  number:"))
b=float(input("Enter second number:"))
Average=(a+b)/2
print("Average of the two numbers is :", Average)

# Q-4 # Write a program to input two integer number a and b and print true if a is greater than or equal to b if not print false.
a=int(input("Enter a :"))
b=int(input("Enter b :"))
print(a>=b) 
# Alternative way to print the result is using if else statement: 
# 1]
#   if(a>=b):
#         print("True")
#   else:
#         print("False")
# 2]
#   print("True") if(a>=b) else print("False")


####DOUGHT####
a=int(input("a:"))
b=int(input("b:"))
if (type(a)!= int or type(b)!= int): # For invalid Input #
    print("please enter Valid input")
elif (a>=b):
    print("True")   
elif (a<b):
    print("False")  

