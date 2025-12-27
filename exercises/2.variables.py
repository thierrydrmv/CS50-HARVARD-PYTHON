def main():
    # exercise1()
    # exercise2()
    # exercise3()
    # exercise4()
    exercise5("LOTR", 4)


def exercise1():
    location = "Brooklyn, " + "NY"
    print(location)  # Brooklyn, NY

    quantity = 4 * 5 + 1
    print(quantity)  # 21


def exercise2():
    word = "bye"
    print(word + " felicia")  # bye felicia
    print(word)  # bye

    num = 10
    num = num * 2
    print(num)  # 20

    bottles_of_beer = 99
    around = bottles_of_beer - 1
    print(around)  # 98
    print(bottles_of_beer)  # 99


def exercise3():
    apple = ""
    print(apple)  # empty string

    apple = 5
    print(apple)  # 5

    apple + 1
    print(apple)  # 5

    apple += 1
    print(apple)  # 6

    banana = apple
    print(banana)  # 6

    banana = banana / 2
    print(banana)  # 3.0

    print(apple)  # 6


def exercise4():
    qty = 15 % 4
    print(qty)  # 3

    num = 38 + 3
    num += 1
    print(f"{num} is a great number")  # 42 is a great number

    is_num_even = num % 2 == 0
    print(f"{num} is even? {is_num_even}")  # 42 is even? True

    is_qty_even = qty % 2 == 0
    print(f"{qty} is even? {is_qty_even}")  # 3 is even? False


def exercise5(movie, views):
    # I watched <movie> around <views> times.
    print(f"I watched {movie} around {views} times.")


if __name__ == "__main__":
    main()
