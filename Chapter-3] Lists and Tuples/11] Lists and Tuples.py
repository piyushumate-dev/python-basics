# It demonstrates the use of lists in Python.
student=["Karan", 85, "Delhi"]

# Accessing the  elements of the list #
print(student[0]) #Output: Karan 
print(student[1]) #Output: 85
print(student[2]) #Output: Delhi

# Changing the elements of the list #
student[0]="Arjun"
student[1]=90
print(student) #Output: ['Arjun', 90, 'Delhi']

# Finding the length of the list #
print(len(student)) #Output: 3

# Accessing elements out of range #
# print(student[3]) # This will raise an IndexError: list index out of range

# List Slicing #
marks=[87,64,33,95,76]
print(marks[1:4]) #Output: [64, 33, 95]
print(marks[:5]) or print(marks[0:len(marks)])#Output: [87, 64, 33, 95, 76]
print(marks[-4:-1]) #Output: [64, 33, 95]

# List Methods #

# 1] list.append() - It adds an element at the end of the list.
list=[2 ,1 ,3]
list.append(4)
print(list) #Output: [2, 1, 3, 4]

# 2] list.insert(index, element) - It adds an element at the specified index.
list=[2 ,1 ,3, 4]
list.insert(1, 5)
print(list) #Output: [2, 5, 1, 3, 4]

# 3] list.sort() - It sorts the elements of the list in ascending order.
list=[2 ,1 ,3, 4]
list.sort()
print(list) #output: [1, 2, 3, 4]

# 4] list.sort(reverse=True) - It sorts the elements of the list in descending order.
list=[2 ,1 ,3, 4]
list.sort(reverse=True)
print(list) #output: [4, 3, 2, 1]

# 5] list.reverse() - It reverses the elements of the list.
list=[2 ,1 ,3, 4]
list.reverse()
print(list) #output: [4, 3, 1, 2]

# 6] list.remove(element) - It removes the first occurrence of the specified element from the list.
list=[2 ,1 ,3, 4]
list.remove(3)
print(list) #output: [2, 1, 4]

# 7] list.pop(index) - It removes the element at the specified index and returns it. If no index is specified, it removes and returns the last element.
list=[2 ,1 ,3, 4]
list.pop(1)
print(list) #output: [2, 3, 4]



##### TUPLES #####
# Tuple is kind of same as list , the methods of list can be done on tuple except item assingment .
# Tuple is immutable so we can only acess the data can't change it .