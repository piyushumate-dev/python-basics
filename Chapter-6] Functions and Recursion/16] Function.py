# The program demonstrates the use of functions in Python.
"""
a=2
b=5
sum = a + b
print("Sum of", a, "and", b, "is:", sum)

## more lines of code is present.

a=26
b=55
sum = a + b
print("Sum of", a, "and", b, "is:", sum)


## more lines of code is present.

a=98
b=68
sum = a + b
print("Sum of", a, "and", b, "is:", sum)
"""
# To avoid this type of code repetition, we can use functions to perform the same task.
#Example 1]

def sum(a,b):
    s=a+b
    print("Sum of", a, "and", b, "is:", s)
    return s
     

sum(2,89)

## more lines of code is present.
 
sum(26,55)

## more lines of code is present.

sum(26866,5686)

# Example 2]

def print_hello():
    print("Hello World")

print_hello()
## more lines of code is present.
print_hello()
## more lines of code is present.
print_hello()

# Example 3]

# Calculate average of three numbers using function.
def average(a,b,c):
    avg=(a+b+c)/3
    print("Average of", a, ",", b, "and", c, "is:", avg)
    return avg

average(2,5,8)
### more lines of code is present.
average(26,55,89)

## Default Parameter Value

def multiply(a,b):
    product=a*b
    print("Product of", a, "and", b, "is:", product)
    return product

# multiply() # This will give an error because the function multiply() requires two arguments but none are provided.
multiply(2,5) # This will work fine and print the product of 2 and 5.
# To avoid this error, we can provide default values for the parameters a and b in the function definition.
def multiply(a=1,b=1):
    product=a*b
    print("Product of", a, "and", b, "is:", product)
    return product

multiply() # This will now work fine and print the product of 1 and 1.

#def multiply(a=1,b):# This will give an error because the parameter b does not have a default value but is placed after a parameter with a default value.
#def multiply(a,b=1):# This will work fine because the parameter b has a default value and is placed after a parameter without a default value.
# default parameter values are always given from right to left. If a parameter has a default value, all parameters to its right must also have default values.

## Practice Questions :

# Q1] Write a function to print the lenght of a list. (list is the parameter)
def print_list(list):
    length = len(list)
    print("Length of the list is:", length)
    return length

print_list([1,2,3,4,5])
print_list(["apple", "banana", "cherry"])

# Q2] Write a function to print the elements of a list in a single line. (list is the parameter)

def print_elements(list):

    for element in list:
        print(element, end=" ")
    print() # for new line after printing all elements
    return

print_elements([1,2,3,4,5,6,7,8])

# Q3] Write a function to find the factorial of n (n is the parameter)
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
        print("Factorial of",n,"is:" , fact)

    return fact

factorial(5)

# Q4] Write a function to convert USD into INR (USD is the parameter)
def convert_usd_to_inr(USD):
    INR = USD * 83
    print(USD, "USD is equal to", INR, "INR")
    return INR

convert_usd_to_inr(100)

# Q5] 
def predict(n):
    if n%2==0:
        print(n, "is an even number")
    else:
        print(n, "is an odd number")


predict(5)
predict(10)