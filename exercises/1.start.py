def main():
  # exercise1()
  # exercise2()
  # exercise3()
  # exercise4()

def exercise1():
  print("river" + "town") # rivertown
  print("cat" + "dog") # catdog
  print("New" + " York") # New York
  print("runner's knee" + "not") # runner's kneenot
  print("man" + "bear" + "pig") # manbearpig

def exercise2():
  print(2 + 3) # 5
  print(10 - 15) # -5
  print(4 + 1 - 5) # 0
  print(4 * 3) # 12

  print(7 / 2) # 3.5
  print(4 + 2 * 3) # 10
  print((4 + 2) * 3) # 18
  print(5 % 2) # 1

  print(6 % 2) # 0
  print(7 % 2) # 1
  print(8 % 2) # 0
  print(19 % 8) # 3

  print(24 % 8) # 0
  print(7 % 4) # 3
  print(4 % 7) # 4
  print(5 + (10 % 5)) # 5
  print((5 + 10) % 5) # 0

def exercise3():
  print(False) # False
  print(not True) # False
  print(not False) # True
  print(not not True) # True

  print(False and False) # False
  print(False and True) # False
  print(True and False) # False
  print(True and True) # True

  print(False or False) # False
  print(False or True) # True
  print(True or False) # True
  print(True or True) # True

  print(not False or False) # True
  print(False or (True and True)) # True
  print(False or not(True and True)) # False
  print(not True and (False or True)) # False

def exercise4():
  print(True == False) # False
  print(False == False) # True
  print(False != True) # True
  print(not True == False) # True

  print(2 + 3 == 5) # True
  print(4 < 0) # False
  print(10 >= 10) # True
  print(10.3 >= 10) # True

  print(100 / 2 == 50) # True
  print(100 % 2 == 0) # True
  print(11 % 2 == 0) # False
  print(7.0 == 7) # True

  print(13 % 5 > 0) # True
  print("potato" == "potato") # True
  print("Tomato" == "tomato") # False
  print("42" == 42) # False
  print(5 > 3 and 1 == 0) # false

main()