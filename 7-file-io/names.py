def main():
    # name = input("What's your name? ")
    # write_data(name)
    read_file()


def write_data(name):
    # w write
    # a append
    # r read default
    # with ensures that the file will be closed
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")


def read_file():
    names = []
    with open("names.txt") as file:
        for line in file:
            # rstrip -> remove trailing characters from the right (end) of a string.
            names.append(line.rstrip())

        for name in sorted(names, reverse=True):
            print(name)


main()
