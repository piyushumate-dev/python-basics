#Q1] Store the following word meanings in a python dictionary.
# table="a peice of furniture" , "list of fact and figures"
# cat="a small animal"
Dict= {
    "table" : ["a peice of furniture","list of fact and figures"] ,
    "cat" : "a small animal"
}
print((Dict))

#Q2] Write a program to enter marks of three subjects from user and store them in a dictionary. start with an empty dictionary and add one by one. use subject name as key and marks as values.
marks={}
x=int(input("Enter physics marks:"))
marks.update({"physics": x })
x=int(input("Enter chemistry marks:"))
marks.update({"chemistry": x})
x=int(input("Enter maths marks:"))
marks.update({"maths": x })
print(marks)

#Q3] Figure out a way to store 9 and 9.0 as a seperate values in a set.
values={
       ("float" , 9.0),
       ("int" , 9)
}

print(type(values))
print(values)
#### OR ####
values={9 , "9.0"}
print(values)