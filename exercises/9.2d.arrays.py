def main():
  # example()
  # exercise1()
  # exercise2()
  # exercise3()
  # exercise4()
  # exercise5()
  # exercise6()
  # exercise7()
  exercise8()
  # exercise9()
  # exercise10()

def example():
  array = ['a', 'b'], ['c', 'd', 'e']
  for i in range(0, len(array)):
    print(array[i])
    for y in range(0, len(array[i])):
      print(array[i][y])

def exercise1():
  # Write a function `print2d` that accepts a two-dimensional array as an argument. The function
  # should print all inner elements of the array.
  def print2d(array):
    for i in range(0, len(array)):
      for j in range(0, len(array[i])):
        print(array[i][j])

  print2d([["a", "b", "c", "d"], ["e", "f"], ["g", "h", "i"]])
  # prints
  #  a
  #  b
  #  c
  #  d
  #  e
  #  f
  #  g
  #  h
  #  i

  print2d([[9, 3, 4], [11], [42, 100]])
  # prints
  #  9
  #  3
  #  4
  #  11
  #  42
  #  100

def exercise2():
  # Write a function `make_matrix(m, n, value)` that accepts three arguments. The function should return
  # a 2-dimensional array of height `m` and width `n` that contains the `value` as every element.
  def make_matrix(m, n, value):
    new_array = []
    for i in range(0, m):
      new_line = []
      for y in range(0, n):
        new_line.append(value)
      new_array.append(new_line)
    return new_array

  print(make_matrix(3, 5, None))
  # [
  #   [ None, None, None, None, None ],
  #   [ None, None, None, None, None ],
  #   [ None, None, None, None, None ]
  # ]

  print(make_matrix(4, 2, "x"))
  # [
  #   [ 'x', 'x' ],
  #   [ 'x', 'x' ],
  #   [ 'x', 'x' ],
  #   [ 'x', 'x' ]
  # ]

  print(make_matrix(2, 2, 0))
  # [
  #   [ 0, 0 ],
  #   [ 0, 0 ]
  # ]

def exercise3():
  # Write a function `total_product(array)` that accepts a 2D array of numbers. The function should return
  # the total product of all numbers in the array.
  def total_product(array):
    total = 1
    for i in range(0, len(array)):
      for y in range(0, len(array[i])):
        total *= array[i][y]
    return total

  print(total_product([[3, 5, 2], [6, 2]])) # 360

  print(total_product([[4, 6], [2, 3], [1, 2]])) # 288

def exercise4():
  # Write a function `two_sum_pairs(numbers, target)` that accepts an array of numbers and a target number
  # as arguments. The function should return a 2D array containing all unique pairs of elements that
  # sum to the target.
  def two_sum_pairs(numbers, target):
    new_array = []
    for i in range(0, len(numbers)):
      for y in range(i + 1, len(numbers)):
        new_line = []
        if numbers[i] + numbers[y] == target:
          new_line.append(numbers[i])
          new_line.append(numbers[y])
          new_array.append(new_line)
    return new_array

  print(two_sum_pairs([2, 3, 4, 6, 5], 8)) # [ [2, 6], [3, 5] ]
  print(two_sum_pairs([10, 7, 4, 5, 2], 12)) # [ [10, 2], [7, 5] ]
  print(two_sum_pairs([3, 9, 8], 11)) # [ [3, 8] ]
  print(two_sum_pairs([3, 9, 8], 10)) # [ ]

def exercise5():
  # Write a function `zipper` that accepts two arrays as arguments. The function should return a 2D
  # array containing pairs of elements at the same indices. You can assume that the arrays have the 
  # same length.
  def zipper(array1, array2):
    new_array = []
    for i in range(0, len(array1)):
      new_line = []
      new_line.append(array1[i])
      new_line.append(array2[i])
      new_array.append(new_line)
    return new_array
  
  print(zipper(["a", "b", "c", "d"], [-1, -2, -3, -4]))
  # [
  #   ['a', -1],
  #   ['b', -2],
  #   ['c', -3],
  #   ['d', -4],
  # ]

  print(zipper(["whisper", "talk", "shout"], ["quiet", "normal", "loud"]))
  # [
  #   ['whisper', 'quiet'],
  #   ['talk', 'normal'],
  #   ['shout', 'loud'],
  # ]

def exercise6():
  # 😭 
  # Write a function `remove_dupes` that accepts an array as an argument. The function should return a
  # new array where each element only appears once.
  def remove_dupes(array):
    new_array = []
    for i in array:
      if i not in new_array:
        new_array.append(i)
    return new_array
      
  print(remove_dupes(["x", "y", "y", "x", "z"])) # ['x', 'y', 'z']
  print(remove_dupes([False, False, True, False])) # [False, True]
  print(remove_dupes([42, 5, 7, 42, 7, 3, 7, 7])) # [42, 5, 7, 3]

def exercise7():
  # Write a function `remove_vowels` that accepts a string as an argument. The function should return
  # a version of the string where all vowels are removed.
  def remove_vowels(string):
    new_string = ""
    for i in string:
      if i not in vowels():
        new_string += i
    return new_string

  print(remove_vowels("jello")) # jll
  print(remove_vowels("sensitivity")) # snstvty
  print(remove_vowels("cellar door")) # cllr dr

def exercise8():
  # Write a function `spam` that accepts a 2D array as an argument. The array contains pairs as elements.
  # The first element of every pair is a number and the second element is a word. The function should
  # return a string containing the words repeated the specified number of times. See the examples.
  def spam(array):
    new_string = []

    for i in range(0, len(array)):
      for y in range(0, array[i][1]):
          new_string.append(array[i][0])

    return " ".join(new_string)

  print(spam([["hi", 3], ["bye", 2]])) # 'hi hi hi bye bye'

  print(spam([["cat", 1], ["dog", 2], ["bird", 4]])) # 'cat dog dog bird bird bird bird'

def exercise9():
  # Write a function `remove_first_vowel` that accepts a string as an argument. The function should return
  # the string with it's first vowel removed.
  def remove_first_vowel(string):
    new_string = ""
    count = 0
    for i in string:
      if count == 0:
        if i in vowels():
          count += 1
          continue
      new_string += i
    return new_string
  
  print(remove_first_vowel("volcano")) # 'vlcano'
  print(remove_first_vowel("celery")) # 'clery'
  print(remove_first_vowel("juice")) # 'jice'

def exercise10():
  # Write a function `shorten_long_words` that accepts a sentence string as an argument. The function
  # should return the same sentence where words longer than 4 characters have their vowels removed.
  def shorten_long_words(string):
    array_string = string.split(" ")
    new_string = ""
    for i in range(0, len(array_string)):
      if len(array_string[i]) > 4:
        for y in range(0, len(array_string[i])):
          if array_string[i][y] not in vowels():
            new_string += array_string[i][y]
        array_string[i] = new_string
      new_string = ""

    return " ".join(array_string)

  print(shorten_long_words("they are very noble people")) # 'they are very nbl ppl'
  print(shorten_long_words("stick with it")) # 'stck with it'
  print(shorten_long_words("ballerina, you must have seen her")) # 'bllrna, you must have seen her'

def vowels():
  return ["a", "e", "i", "o", "u"]

main()