# Define patterns to valid data, pattern (regex)
# Library for regex
# . any character except a blank line
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetition
# ^ start with
# $ ends with
# {m} m repetitions
# {m,n} m-n repetitions
# [] especify the characters
# [^@] not @\
# \w word
import re

def main():
  print("Regular expressions")
  email()

def email():
  email = input("What's your email? ").strip()
  
  if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|edu)$", email, re.IGNORECASE):
    print("Valid")
  else:
    print("Invalid")

main()