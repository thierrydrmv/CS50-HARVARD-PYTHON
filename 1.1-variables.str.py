# Code that solves small problems but that can be composed to solve big problems

print('Hello, World')
"""
 argument: is an input for a function (parameters)
 side effects: print in the terminal Hello, World
"""

# remove spaces around like trim() assignment => rewrite and capitalize user's name
name = input('What\'s your name?\n').strip().title()

# split user's name into name and last name

first, last = name.split(' ')

# name = name.strip().title()

# Capitalize user name
# name = name.capitalize()
# you can use title to capitalize first letter of each word => name.title()

print("Welcome", name + ", how old are you?")

# trying things
def ageAnswer(age):
  if int(age) > 17:
    print("You are an adult.")
  else:
    print("You are a minor.")

ageAnswer(input())

# override the end parameter to not break to the next line
print("Hello ", end="")
print(name)

# new way of using string -> string is str
# f to format string literal
# a concise and convenient way to embed expressions 
# and variables directly within string literals

print(f"Hello, {first}")