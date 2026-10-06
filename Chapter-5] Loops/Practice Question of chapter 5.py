# Practice Question 
# 1] Write a programm to find a sum of first n numbers. (using while Loop)
n = int(input("Enter n :"))
sum=0
i=1
while i<=n:
    sum += i
    i += 1  
print("Sum of first", n, "numbers is:", sum)

##OR##
n = int(input("Enter n :"))
sum=0
for i in range(1,n+1):
    sum += i
print("Sum of first", n, "numbers is:", sum)

# 2]  Write a programm to find the factorial of the first n numbers. (using for Loop)
n = int(input("Enter n :"))
i=1
fact= 1
while i<=n:
    fact *=i
    i +=1
print("Factorial of", n, "is:", fact)

###OR###

n = int(input("Enter n :"))
fact= 1
for i in range(1,n+1):
    fact *= i
print("Factorial of", n, "is:", fact)