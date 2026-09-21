# program demonstrates the use of nesting in conditional statements in Python.
Age= int(input("Enter your age:"))

if(Age>=18):
    if(Age>80):
        print("You are to old to Drive")
    else:
        print("You are eligible to Drive")
elif(Age<18):
    print("You are not eligible to Drive")

    
""" Explaination: In this program, we first check if the age is greater than or equal to 18.
If it is, we then check if the age is greater than 80. 
If it is, we print that the person is too old to drive.
If not, we print that the person is eligible to drive.
This demonstrates how we can nest conditional statements within each other to create more complex logic."""