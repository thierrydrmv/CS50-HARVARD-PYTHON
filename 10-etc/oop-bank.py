class Account:
    def __init__(self):
        # convention that is private because has a _
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, value):
        self._balance += value

    def widthdraw(self, value):
        self._balance -= value


def main():
    account = Account()
    print(f"Balance: {account.balance}")
    account.deposit(100)
    print(f"Balance: {account.balance}")
    account.widthdraw(50)
    print(f"Balance: {account.balance}")


if __name__ == "__main__":
    main()
