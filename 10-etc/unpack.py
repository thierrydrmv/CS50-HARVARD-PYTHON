def main():
    # try1()
    # try2()
    # try3()
    # try4()
    # try5()
    # try6()
    try7()


def try1():
    # unpacking with * - *args, **kargs => can received x parameters
    def total(gold, silver, brass):
        return (gold * 17 + silver) * 29 + brass

    coins = {"gold": 1, "silver": 32, "brass": 111}
    coins_array = [1, 32, 111]

    print(total(**coins), "Brass")
    print(total(*coins_array), "Brass")


def try2():
    # variable number of arguments
    # args returns a tuple
    # kargs returns a dictionary
    def f(*args, **kargs):
        print("Named:", kargs)

    f(gold=100, silver=50, brass=25)


def try3():
    def yell(*words):
        # list comprehension
        uppercased = [word.upper() for word in words]
        print(*uppercased)

    yell("buenos", "dias")


def try4():

    doggos = [
        {"name": "bella", "type": "canine", "age": 4, "breed": "yorkshire terrier"},
        {"name": "manny", "type": "canine", "age": 2, "breed": "pug"},
        {"name": "yoshi", "type": "canine", "age": 3, "breed": "german shepherd"},
        {"name": "blossom", "type": "canine", "age": 3, "breed": "german shepherd"},
    ]

    def filter_dogs():
        # list comprehension
        german_shepard = [
            dog["name"] for dog in doggos if dog["breed"] == "german shepherd"
        ]
        print(german_shepard)

    def is_shepard(s):
        return s["breed"] == "german shepherd"

    def filter_shepard():
        filter_shepard = filter(is_shepard, doggos)
        for shepard in filter_shepard:
            print(shepard["name"])

    filter_shepard()

    # filter_dogs()


def try5():
    students = ["Bob", "Maria", "Jose"]
    # list comprehension
    phd = [{"name": student, "phd": True} for student in students]
    # dict comprehension
    phd_dict = {student: True for student in students}

    print(phd)
    print(phd_dict)


def try6():
    students = ["Bob", "Maria", "Jose"]
    # enumerate
    for i, student in enumerate(students):
        print(i + 1, student)


def try7():
    # generators
    n = int(input("How many sheep? "))
    for i in sheep(n):
        print(i)


def sheep(n):
    for i in range(n):
        # yield makes returns 1 row per time, memory is limited
        # return a iterator
        yield "🐑" * i


if __name__ == "__main__":
    main()
