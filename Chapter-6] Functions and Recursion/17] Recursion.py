# The program demonstrates the use of recursion in Python.
#Ex 1]
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)

show(5)

#Ex 2]
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return factorial(n-1)*n

print(factorial(5))

# Practice Question
# 1] Write a program to find the sum of first n numbers using recursion.
def sum(n):
    if (n==0):
        return 0
    return sum(n-1)+n

print(sum(5))
print(sum(6))

# write a recursive  function to print all elements  in a list.
def print_list(list, index=0):
    if (index == len(list)):
        return
    print(list[index])
    print_list(list, index + 1)

Fruits = ["Apple", "Banana", "Cherry", "Date"]
print_list(Fruits)