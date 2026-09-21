# It demonstrate the use of String Function.

#1] str.endswith("value") : It returns True if the string ends with the specified value, otherwise False.
str= "I am studying python from Apnacollege"
print(str.endswith("college")) # True
print(str.endswith("Apna")) # False

#2] str.capitalize() : It returns a copy of the string with its first character capitalized and the rest lowercased.
str= "i am studying python from apnacollege"
print(str.capitalize()) # I am studying python from apnacollege

#3] str.replace("old value","new value") : It returns a copy of the string with all occurrences of the old value replaced by the new value.
str= "I am studying python from Apnacollege"
print(str.replace("Apnacollege", "Python in 30 days github repo")) # I am studying python from Python in 30 days github repo

#4] str.find("value") : It returns the lowest index of the substring if it is found in the string. If it is not found, it returns -1.
str= "I am studying python from Apnacollege"    
print(str.find("Apnacollege")) # 26
print(str.find("python")) # 14   

#5] str.count("value") : It returns the number of occurrences of the substring in the string.
str= "I am studying python from Apnacollege"
print(str.count("python")) # 1
print(str.count("o")) # 3