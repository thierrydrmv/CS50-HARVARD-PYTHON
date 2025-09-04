def main():
    name = input("What's your name? ")
    createFun(name)
    createFun()

    print("Square is: ", square())


# def is short for define (create a function)
def createFun(to="Robert"):  # default value in def
    # formatted string literals
    # f-string
    print(f"Hello, {to}")


def square():
    x = int(input("What is the value? "))
    # pow (n, 2) same
    return x**2


# python interpretor is literal, the function has to already exists to use or...

main()

# scope -> variable only exists in the scope that has been created ex: name
