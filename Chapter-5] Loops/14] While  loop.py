# program demonstrate the use of while loop
# Example 1]
count=1
while count <=5:
    print("One life , why aren't we running like we are on fire")
    count += 1
print(count)

# Example 2]
count=5
while count >=1:
    print("One life , why aren't we running like we are on fire")
    count -= 1
print(count)
print("loop ended")


# Practice Question .
# 1] Print number from 1 to 100 .
num=1
while num <=100:
    print(num)
    num +=1

# 2] Print number from 100 to 1 .
num=100
while num >=1:
    print(num)
    num -= 1

# 3] Print the multiplication table of a number n.
n = int(input("Enter number:"))
i= 1
while i<=10:
    print(n*i)
    i+= 1


# 4]  Print the elements of the following list using a loop.
nums=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx=0
while idx < len(nums):
    print(nums[idx])
    idx += 1

# 5] Search for a number in this tuple using loop .
nums=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100 , 4, 4, 4,)
x = int(input("Enter x :"))
i=0
while i < len(nums):
    if (nums[i] == x):
        print ("Found at index" , i)
    else:
        print("Finding")
    i += 1

### Break and Continue in while loop ###
# 1] Break

# Example 1]
i=1
while i<=5:
    print(i)
    if (i==3):
        break
    i += 1
print("end loop")

# Example 2]
nums=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100 , 4, 4, 4,)
x = int(input("Enter x :"))
i=0
while i < len(nums):
    if (nums[i] == x):
        print ("Found at index" , i)
        break
    else:
        print("Finding")
    i += 1
print("End loop")

# 2] Continue

# Example 1]
i=1
while i<=5:
    if (i==3):
       i += 1
       continue #skip
    print(i)
    i += 1

# Example 2] Print odd numbers only
i=1
while i<=10:
    if (i%2==0):
       i += 1
       continue #skip
    print(i)
    i += 1

# Example 3] Print even numbers only
i=1
while i<=10:
    if (i%2 !=0):
       i += 1
       continue #skip
    print(i)
    i += 1