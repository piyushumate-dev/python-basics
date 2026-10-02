# program demonstrate the use of for loop

#for loop
# Ex 1] 
nums=[1, 2, 3, 5, 4, 9, 6, 7, 8, 9, 10]
for val in nums:
    print(val)

# Ex 2] 
movies=["spiderman", "doomsday", "spiderverse", "avengers"]
for name in movies:
    print(name)

# Ex 3] 
str= "piyushumate"
for char in str:
    print(char)

# Practice Questions #
# Q1] print the elements of the following list using a loop
nums= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
for val in nums:
    print(val)

# Q2] Search for a number x in this tuple using loop 
nums= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
x=int(input("Enter x :"))
i=0
for el in nums:
    if(el==x):
        print("Found",x,"at index",i)
        break
    else:
        print("Finding")
        i+=1

#Range function
# Ex 1] 
for i in range(10):
    print(i)
# Ex 2]
for i in range(2,10):
    print(i)
# Ex 3] print even numbers from 2 to 100
for i in range(2,101,2):
    print(i)
# Ex 4] print odd numbers from 1 to 100
for i in range(1,100,2):
    print(i)
# Ex 5] print table of 3
for i in range(3,31,3):
    print(i)

#Practice Questions 
# Q1] print the numbers from 1 to 100
for i in range(1,101,1):
    print(i)
# Q2] print the numbers from 100 to 1
for i in range(100,0,-1):
    print(i)
# Q3] print the multiplication table of a number n
n=int(input("Enter n :"))
for i in range(n,n*10+1,n):
    print(i)
    ### OR ###
for i in range(1,11):
    print(n*i)

# Pass statement
# Ex 1]
for i in range(1,11):
    pass
print("This loop is not workig beacause we use pass statement , so it will not print anything")

