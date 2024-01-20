# strings can be enclosed in double or single quotes

print('Today is a good day to learn python')
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes in string"')

# In python there is no diff between "" '' but one should start and end with the same

# we can also concatenate string using longer once using +

print('hello' + 'world')


# storing string in variables and concatenating them.

greeting = 'Hello'
name = 'Bruce'

# if we want a space, we can add that too
print(greeting +' '+ name)

# using input function to take a value from the user

name1 = input('Please enter your name :>')
# takes the value from the user and assignes that to the variable name.
print(greeting + '' + name1)


# ***************************************************************************************** #

age = 24
print(age)
name = 'Charles'
print(name)


# Python is strongly typed and dynamically typed.

print(type(greeting))   # of type str
print(type(age))        # of type int

# They are automatically declared the kind of information storing.

age = 1
print(age)
print(type(age))

# rebound the variable to a value.


# Python is a strongly typed language.

# for example, if we try to add a string to and int, it will show error so hence Python is not a weakly typed language

print(name + 'is' + age + 'years old')  # will show error.

# Python does not have type declaration.




