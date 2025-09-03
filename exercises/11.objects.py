def main():
  # exercise1()
  # exercise2()
  # exercise3()
  # exercise4()
  # exercise5()
  # exercise6()
  # exercise7()
  exercise8()

def exercise1():
  movie = {
    "title": "Fight Club",
    "year": 1999,
    "genre": ["drama", "thriller"],
    "starring": ["Brad Pitt", "Edward Norton"],
  }
  print(movie["year"]) # 1999
  print(movie["title"]) # Fight Club
  print(movie["genre"]) #["drama", "thriller"]
  print(movie["genre"][0]) # drama
  print(movie["genre"][1]) # thriller

  # print(movie["duration"]) # KeyError
  print(movie["starring"][1]) # Edward Norton
  print(len(movie["starring"])) # 2

def exercise2():
  restaurant = {
    "name": "Bob's Burgers",
    "location": "123 Ocean Avenue",
    "owners": ["Bob Belcher", "Linda Belcher"],
    "established": 2011,
    "menu": ["burgers", "fries", "shakes"],
  }

  print("owners" in restaurant) # True
  print("employees" in restaurant) # False

  someKey = "menu"
  print(someKey in restaurant) # True

  print(restaurant["menu"]) # ["burgers", "fries", "shakes"]
  print(restaurant[someKey]) # ["burgers", "fries", "shakes"]

  print("fries" in restaurant["menu"]) # True

def exercise3():
  dog = {
    "name": "Manny",
    "age": 5,
    "breed": "pug",
    "color": "fawn",
    "favoriteFoods": ["bacon"],
  }

  print(dog["age"]) # 5
  print(dog["breed"]) # "pug"
  print(dog["favoriteFoods"]) # ["bacon"]

  dog["age"] += 1
  dog["breed"] = dog["breed"].upper()
  dog["favoriteFoods"].append("sausage")

  print(dog["age"]) # 6
  print(dog["breed"]) # "PUG"
  print(dog["favoriteFoods"]) # ["bacon", "sausage"]

  for property in dog:
    print(property)
    # "name" "age" "breed" "color" "favoriteFoods"
  

def exercise4():
  recipe = {
    "name": "Old Fashioned Pancakes",
    "difficulty": "easy",
    "tasty": True,
    "ingredients": ["eggs", "milk", "butter", "flour", "sugar"],
  }

  print(recipe["name"]) # "Old Fashioned Pancakes"
  print(len(recipe["ingredients"])) # 5
  # print(recipe.calories) # has no attribute

  someVariable = "difficulty"
  print(recipe[someVariable]) # easy

  for i in range(0, len(recipe["ingredients"])):
    print(recipe["ingredients"][i])
  # eggs, milk, butter, flour, sugar

def exercise5():
  # Create a function `email_parse` that accepts an email address string as an argument. The function
  # should return an object containing `username` and `domain` as keys. See the examples.
  # You can assume that the argument will be a valid email address.
  def email_parse(string):
    new_string = string.split("@")
    return {"username": new_string[0], "domain": new_string[1]}

  print(email_parse("coolcoder42@goodmail.com"))
  # { username: 'coolcoder42', domain: 'goodmail.com' }

  print(email_parse("az@woohoomail.com"))
  # { username: 'az', domain: 'woohoomail.com' }

  print(email_parse("1337pr0graMmer@coldmail.edu"))
  # { username: '1337pr0graMmer', domain: 'coldmail.edu' }

def exercise6():
  # Write a function `key_pair(obj1, obj2, key)` that accepts two objects and a key string as arguments.
  # The function should return an array containing the values of the given key in `obj1` and `obj2`.
  # See the examples.
  def key_pair(obj1, obj2, key):
    new_array = []
    new_array.append(obj1[key])
    new_array.append(obj2[key])
    return new_array

  cat1 = { "name": "jinkee", "breed": "calico" }
  cat2 = { "name": "garfield", "breed": "red tabby" }

  print(key_pair(cat1, cat2, "breed")) # [ 'calico', 'red tabby' ]
  print(key_pair(cat1, cat2, "name")) # [ 'jinkee', 'garfield ]

  sport1 = { "name": "volleyball", "team": True }
  sport2 = { "name": "golf", "team": False }
  print(key_pair(sport1, sport2, "team")) # [ True, False ]

def exercise7():
  # Create a function `element_quantities` that accepts an object as an argument. The object contains
  # elements as keys and quantities as values. The function should return an array containing the elements
  # appearing with the correct quantities. See the examples.
  def element_quantities(obj):
    new_array = []
    for i in obj:
      for _ in range(0, obj[i]):
        new_array.append(i)
    return new_array

  quantities1 = { "cat": 3, "bird": 1, "dog": 2 }
  print(element_quantities(quantities1)) # ['cat', 'cat', 'cat', 'bird, 'dog', 'dog']

  quantities2 = { "blue": 3, "brown": 1 }
  print(element_quantities(quantities2)) # ['blue', 'blue', 'blue', 'brown']

def exercise8():
  # Write a function `max_object_value` that accepts an object as an argument. Write a function that
  # returns an array containing the key, value pair for the largest value within the object. You can
  # assume that all values are numbers and there are no ties.
  def max_object_value(obj):
    array = []
    value = 0
    for i in obj:
      if value < obj[i]:
        value = obj[i]
        array = [i, obj[i]]
    return array

  print(max_object_value({ "a": 5, "b": 2, "c": 6, "d": 7, "e": 4 })) # ['d', 7]
  print(max_object_value({ "lychee": 11, "rambutan": 13, "papaya": 9 })) # ['rambutan', 13]

if __name__ == "__main__":
  main()