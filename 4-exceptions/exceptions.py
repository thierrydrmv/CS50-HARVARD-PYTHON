# Write code defensively to catch errors and handle them properly
def main():
    print("Exceptions")
    first_exception()


def first_exception():
    num = get_int("What's x? ")
    print(f"x is {num}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass  # just keep going without returning the error
            print("x is not an integer")


main()
