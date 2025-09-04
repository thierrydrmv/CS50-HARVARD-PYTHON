balance = 0

def main():
  print(F"Balance: {balance}")
  deposit(100)
  print(F"Balance: {balance}")
  withdraw(50)
  print(F"Balance: {balance}")

def deposit(value):
  global balance
  balance += value

def withdraw(value):
  global balance
  balance -= value

if __name__ == "__main__":
  main()