def main():
    # can pass a function to sorted that returns the key
    # data = sorted(read_csv("students.csv"), key=get_name)
    # lambda is a anonymous funtion, if you only use it in one case, you don't need to name it
    data = sorted(read_csv("students.csv"), key=lambda student: int(student["age"]))
    # write_csv("students.csv")
    print(data)


# is called by the sorted function to compare the values
def get_name(student):
    return student["name"]


def read_csv(path):
    data = []
    with open(path) as file:
        for line in file:
            name, age = line.rstrip().split(",")
            student = {"name": name, "age": age}
            data.append(student)
    return data


def write_csv(path):
    name = input("What's your name? ")
    age = input("How old are you? ")
    with open(path, "a") as file:
        file.write(f"{name},{age}\n")


main()
