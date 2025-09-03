from functools import reduce

# HOF -> a function that returns a function or take a function as argument
def main():
  # exercise1()
  # exercise2()
  # exercise3()
  # exercise4()
  # exercise5()
  # exercise6()
  # exercise7()
  # exercise8()
  # exercise9()
  exercise10()

def exercise1():
  arr = ['mashy', 'brando', 'thanasi']
  res = map(lambda s : s[1:2].upper(), arr)
  print(list(res))
  
def exercise2():
  friends = ['nader', 'matty', 'jennifer', 'lora']

  chosen = max(friends, key=len)

  print(chosen)

def exercise3():
  is_even = lambda n : n % 2 == 0
  is_odd = lambda n : n % 2 != 0

  nums1 = [42, 3, 8, 9]
  print(list(filter(is_even, nums1)))
  print(list(map(is_odd, nums1)))

def exercise4():
  # every in js = all in python
  # some in js = any in python
  doggos = [
    { "name": 'bella', "type": 'canine', "age": 4, "breed": 'yorkshire terrier' },
    { "name": 'manny', "type": 'canine', "age": 2, "breed": 'pug' },
    { "name": 'yoshi', "type": 'canine', "age": 3, "breed": 'german shepherd' },
    { "name": 'blossom', "type": 'canine', "age": 3, "breed": 'german shepherd' }
  ]
  
  result1 = all(dog["type"] == "canine" for dog in doggos)

  print(result1) # True

  result2 = all(dog["breed"] == "german shepherd" for dog in doggos)

  print(result2) # False

  result3 = any(dog["breed"] == "german shepherd" for dog in doggos)

  print(result3) # True

  is_old = lambda p: p["age"] > 5

  result4 = any(is_old(dog) for dog in doggos)

  print(result4) # False

def exercise5():
  nums = [3, 7, 2, 9]
  # accumulator and currently
  res1 = reduce(lambda acc, curr: acc + curr, nums)

  print(res1)

  res2 = reduce(lambda acc, curr: acc + curr, nums, -10)

  print(res2)

  res3 = reduce(lambda acc, curr: acc if acc < curr else curr, nums)

  print(res3)

def exercise6():
  # Write a function `for_each_sum` that accepts an array of numbers as an argument and returns the total
  # sum of all numbers.
  def for_each_sum(array):
    return reduce(lambda acc, curr: acc + curr, array, 0)

  print(for_each_sum([10, 3, 5])) # 18
  print(for_each_sum([-6, 7, 9, 4])) # 14
  print(for_each_sum([])) # 0

def exercise7():
  # Write a function `pick_adults` that accepts an array of person objects and returns the objects that 
  # have an age of at least 18.
  def pick_adults(people):
      return list(filter(lambda p: p["age"] > 17, people))

  print(pick_adults([
    { "name": 'alice', "age": 22 },
    { "name": 'bob', "age": 37 },
    { "name": 'pam', "age": 16 },
    { "name": 'jim', "age": 18 }
  ])) 
  # [ { name: 'alice', age: 22 }, { name: 'bob', age: 37 }, { name: 'jim', age: 18 } ]

  print(pick_adults([
    { "name": 'betty', "age": 23 },
    { "name": 'ben', "age": 15 },
    { "name": 'yansi', "age": 21 }
  ])) 
  # [ { name: 'betty', age: 23 }, { name: 'yansi', age: 21 } ]

def exercise8():
  # Write a function `word_map` that accepts a sentence string and an object as arguments. The function
  # should return a new sentence where words that exist as keys in the object are replaced with their
  # corresponding values.
  def word_map(sentence, object):
    words = sentence.split(" ")
    new_sentence = []
    for word in words:
      if word in object:
        new_sentence.append(object[word])
      else:
        new_sentence.append(word)
    return " ".join(new_sentence)

  print(word_map('open the pod bay doors', {"pod": 'ship', "open": 'close'})) 
  # 'close the ship bay doors'

  print(word_map('breakfast food is good', {"breakfast": 'brunch', "good": 'great'})) 
  # 'brunch food is great'

def exercise9():
  # Write a function `common_elements` that accepts two arrays as arguments. The function should
  # return a new array containing the elements that are found in both input arrays.
  def common_elements(array1, array2):
    new_array = []
    for i in array1:
      if i in array2:
        new_array.append(i)
    return new_array

  print(common_elements(['a', 'b', 'c'], ['c', 'a'])) # ['a', 'c']
  print(common_elements(['cat', 'dog', 'mouse', 'fish'], ['dog', 'rat'])) # ['dog']
  print(common_elements(['skip', 'jump'], ['swim', 'hop'])) # []

def exercise10():
  # Write a function `get_initials` that accepts an array of students as an argument. The function should
  # return an array containing the initials of each student.
  def get_initials(students):
    new_array = []
    for i in students:
      new_array.append(f"{i["first"][:1]}{i["last"][:1]}".upper())
    return new_array

  students1 = [
    { "first": 'ada', "last": 'yonath', "subject": 'chemistry' },
    { "first": 'nelly', "last": 'sachs', "subject": 'literature' },
    { "first": 'rosalyn', "last": 'yallow', "subject": 'medicine' }
  ]
  print(get_initials(students1)) # ['AY', 'NS', 'RY']


  students2 = [
      { "first": 'margaret', "last": 'knight' },
      { "first": 'ellen', "last": 'ochoa' },
  ]
  print(get_initials(students2)) # ['MK', 'EO']

if __name__ == "__main__":
  main()