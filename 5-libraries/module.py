def main():
    hello("World")
    goodbye("World")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


# when importing from another file will not be called
if __name__ == "__main__":
    main()
