# Write code to test your code, good practice to maintain quality overtime and
# by doing this keep the code working with new changes


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(x):
    return x * x


def sum(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def division(x, y):
    return x / y


if __name__ == "__main__":
    main()
