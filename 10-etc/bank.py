balance = 0


def main():
    print(f"Balance: {balance}")
    deposit(100)
    print(f"Balance: {balance}")
    withdraw(50)
    print(f"Balance: {balance}")


def deposit(value):
    global balance
    balance += value


def withdraw(value):
    global balance
    balance -= value


if __name__ == "__main__":
    main()
