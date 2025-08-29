def main():
  print("Arrays")
  # exercise1()
  # exercise2()
  # exercise3()
  # exercise4()
  # exercise5()
  # exercise6()
  exercise7()

def exercise1():
  # Write a function `total` that accepts an array of numbers as an argument. The function should return
  # the total sum of all elements of the array.
  def total(array):
    total = 0
    for i in array:
      total += i
    return total
  print(total([3, 2, 8])) # 13
  print(total([-5, 7, 4, 6])) # 12
  print(total([7])) # 7
  print(total([])) # 0

def exercise2():
  # Write a function `stay_positive` that accepts an array of numbers as an argument. The function should
  # return an array containing only the positive numbers.
  def stay_positive(array):
    new_array = []

    for i in array:
      if i > 0:
        new_array.append(i)
    return new_array

  print(stay_positive([10, -4, 3, 6])) # [10, 3, 6]
  print(stay_positive([-5, 11, -40, 30.3, -2])) # [11, 30.3]
  print(stay_positive([-11, -30])) # []

def exercise3():
  # Write a function `bleep_vowels` that accepts a string as an argument. The function should return
  # a new string where all vowels are replaced with `*`s. Vowels are the letters a, e, i, o, u.
  def bleep_vowels(string):
    new_string = ""
    for i in string:
      if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        new_string += "*"
      else:
        new_string += i
    return new_string

  print(bleep_vowels("skateboard")) # 'sk*t*b**rd'
  print(bleep_vowels("slipper")) # 'sl*pp*r'
  print(bleep_vowels("range")) # 'r*ng*'
  print(bleep_vowels("brisk morning")) # 'br*sk m*rn*ng'

def exercise4():
  # Write a function `filter_long_words` that accepts an array of strings as an argument. The function
  # should return a new array containing only the strings that are less than 5 characters long.
  def filter_long_words(array):
    new_array = []
    for i in array:
      if len(i) < 5:
        new_array.append(i)
    return new_array


  print(filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]))
  # ['kale', 'cat', 'axe']

  print(filter_long_words(["disrupt", "pour", "trade", "pic"]))
  # ['pour', 'pic']

def exercise5():
  # Write a function `num_odds` that accepts an array of numbers as an argument. The function should
  # return a number representing the count of odd elements in the array.
  def num_odds(numbers_array):
    total_odds = 0
    for i in range(0, len(numbers_array)):
      if numbers_array[i] % 2 != 0:
        total_odds += 1
    return total_odds

  print(num_odds([4, 7, 2, 5, 9])) # 3
  print(num_odds([11, 31, 58, 99, 21, 60])) # 4
  print(num_odds([100, 40, 4])) # 0

def exercise6():
  # Write a function `string_to_lengths` that accepts an array of strings as an argument. The function
  # should return a new array containing the lengths of the elements of the original array.
  def string_to_lengths(strings_array):
    new_array = []
    for i in range(0, len(strings_array)):
      new_array.append(len(strings_array[i]))
    return new_array

  print(string_to_lengths(["belly", "echo", "irony", "pickled"]))
  # [5, 4, 5, 7]

  print(string_to_lengths(["on", "off", "handmade"]))
  # [2, 3, 8]

def exercise7():
  # Write a function `divisors` that accepts a number as an argument. The function should return an
  # array containing all positive numbers that can divide into the argument.
  def divisors(number):
    new_array = []
    for i in range(number + 1):
      if i > 0 and number % i == 0: 
        new_array.append(i)
    return new_array

  print(divisors(15)) # [1, 3, 5, 15]
  print(divisors(7)) # [1, 7]
  print(divisors(24)) # [1, 2, 3, 4, 6, 8, 12, 24]

main()