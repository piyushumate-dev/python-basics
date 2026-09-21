# Program demonstrates the Type Conversion and Type Casting in Python.

# Type Conversion (Conversion of int to float)
a=2
b=4.25
sum=a+b # 2.0 + 4.25 = 6.25 , 2 is converted to float autumatically.
print(type(a))
print(type(b))
print(sum)                  

# ERROR # # Type Conversion (Conversion of string to float) 
a="2"
b=4.25
sum=a+b
print(type(a))
print(type(b))
print(sum)

# Type Casting (Conversion of string to int or float)
a=1
b=int("2")   # here float() could also be used on the place of int() # string "2" is converted to int using int() function manually.
sum=a+b # 1 + 2 = 3
print(type(a)) 
print(type(b))
print(sum)