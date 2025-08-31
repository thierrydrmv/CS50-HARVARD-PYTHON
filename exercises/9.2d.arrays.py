def main():
  # example()
  # exercise1()
  # exercise2()
  # exercise3()
  # exercise4()
  exercise5()

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

main()