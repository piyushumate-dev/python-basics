# Basic Operations on String

# 1] Concatenation
str1="piyush" 
str2="umate"
final_str= str1 + str2  # piyushumate
print(final_str)

# 2] Length of String ( Function: len(str) )
str1="piyush" 
str2="umate"
print(len(str1))
print(len(str2))
final_str1= str1 + str2  # piyushumate. 
final_str2= str1 + " " + str2 # piyush umate
print(len(final_str1))
print(len(final_str2))
print(final_str1)
print(final_str2)

# 3] Indexing
str= "piyush umate" 
print(str[4])
print(str[0])
print(str[3])
print(str[6])

# 4] Slicing
str = "piyush umate" 
print(str[2:6])
print(str[:7])
print(str[0:10])
print(str[0:12]) # or print(str[0:len(str)]) or print(str[:12]) or print(str[:]) # piyush umate

# Slicing (Negative Index)
str = "piyush"
print(str[-4:-3])
print(str[-4:-1])
print(str[-6:len(str)]) # or print(str[-6:])


