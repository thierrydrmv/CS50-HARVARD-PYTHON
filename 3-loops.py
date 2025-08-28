# The ability in code todo something repeatedly

def main():
  # repeat(4, 'meow')
  # write_fruit()
  # repeat_with_for()
  # print("meow\n" * 3, end='')
  # test()
  # words()
  # programmer()
  mario(4)


def repeat(number, word):
  while number != 0:
    print(word)
    number -= 1

# list => array
def write_fruit():
  for i in ["orange", "apple", "grape"]:
    print(i)

def get_number():
  while True:
    number = int(input("How many times? "))
    if number > 0:
      return number

# _ => it's a variable that's not used
def repeat_with_for():
  number = get_number()
    
  for _ in range(number):
    print("meow")
# range create a sequence of numbers starting from 1
# range(start, stop, step)replaces for in another languages with range you can control
# start value, end value and frequency
# ex: 
def words():
  words_list = ["a", "b", "c", "d", "e", "f", "g"]
  for i in range(0, len(words_list), 2):
    print(words_list[i])

def test():
  workers = ["Hobert", "Maria", "Bob"]

  for i in range(len(workers)):
    print(f"{i} - {workers[i]}")

def programmer():
  #dictionary
  workers = [
    {"Id": 0, "Name": "Thierry", "Stack": "Python", "Age": 27, "Country": "Brazil"},
    {"Id": 1, "Name": "Bob", "Stack": "Python", "Age": 21, "Country": "Italy"},
    {"Id": 2, "Name": "Maria", "Stack": "Php", "Age": 31, "Country": "Spanish"},
    {"Id": 3, "Name": "Jose", "Stack": None, "Age": 20, "Country": "Brazil"}
  ]
  for worker in workers:
    print(worker["Id"], worker["Name"], worker["Stack"], worker["Age"], worker["Country"], sep=", ")

def mario(num):
  # height
  # for _ in range(num):
  #   print("#")

  # width
  # print("#" * num)

  # cubes
  for i in range(num):
    for j in range(num):
      print("#", end="")
    print()

  # stairs
  for i in range(num):
    print("#"* (i + 1))


main()