def main():
    # exercise1()
    # exercise2()
    # exercise3()
    # exercise4()
    # exercise5()
    # exercise6()
    # exercise7()
    # exercise8()
    # exercise9()
    # exercise10()
    # exercise11()
    # exercise12()
    # exercise13()
    # exercise14()
    # exercise15()
    # exercise16()
    # exercise17()
    # exercise18()
    # exercise19()
    # exercise20()
    # exercise21()
    # exercise22()
    exercise23()


def exercise1():
    print("hello")  # hello
    for _ in range(5):
        print("code")  # code code code code code
    print("goodbye")  # goodbye


def exercise2():
    print("hi")  # hi
    for i in range(3, 7, 1):
        print("program")  # program program program program
        print(i)  # 3 4 5 6
    print("bye")  # bye


def exercise3():
    def foo():
        for i in range(10, 0, -2):
            print(i)

    print("begin")  # begin
    foo()  # 10 8 6 4 2
    print("end")  # end
    foo()  # 10 8 6 4 2


def exercise4():
    word = "street"
    for i in range(len(word)):
        print(i)
        print(word[i])


def exercise5():
    total = 0
    for i in range(1, 5):
        total += 1
        print(total)

    print("grand total:", total)


def exercise6():
    # Write a function `one_to_four` that prints all whole numbers from one to four, inclusive. The function
    # takes in no arguments and doesn't need to return any value. It should just print to the terminal.

    def one_to_four():
        for i in range(1, 5):
            print(i)

    one_to_four()
    # prints
    #  1
    #  2
    #  3
    #  4


def exercise7():
    # Write a function `count_up(max)` that accepts a max number as an argument. The function should print
    # all numbers from 1 up to and including the max. The function doesn't need to return any value. It
    # should just print to the terminal.
    def count_up(max):
        for i in range(1, max + 1):
            print(i)

    count_up(5)
    # prints
    #  1
    #  2
    #  3
    #  4
    #  5

    count_up(3)
    # prints
    #  1
    #  2
    #  3


def exercise8():
    # Write a function `min_to_max(min, max)` that accepts two numbers as arguments. The function should
    # print all numbers from min to max inclusive. The function doesn't need to return any value. It
    # should just print to the terminal.
    def min_to_max(num1, num2):
        for i in range(num1, num2 + 1):
            print(i)

    min_to_max(5, 9)
    # prints
    #  5
    #  6
    #  7
    #  8
    #  9

    min_to_max(11, 13)
    # prints
    #  11
    #  12
    #  13

    min_to_max(20, 11)


def exercise9():
    # Write a function `string_iterate` that accepts a string as an argument. The function should print out
    # each character of the string, one by one. The function doesn't need to return any value. It should
    # just print to the terminal.
    def string_iterate(string):
        for i in range(0, len(string)):
            print(string[i])

    string_iterate("celery")
    # prints
    #  c
    #  e
    #  l
    #  e
    #  r
    #  y

    string_iterate("hat")
    # prints
    #  h
    #  a
    #  t


def exercise10():
    # Write a function `evens(max)` that accepts a max number as an argument. The function should print
    # all positive even numbers that are less than the max.
    def evens(num):
        for i in range(0, num, 2):
            if i > 0:
                print(i)

    evens(11)
    # prints
    #  2
    #  4
    #  6
    #  8
    #  10

    evens(8)
    # prints
    #  2
    #  4
    #  6


def exercise11():
    # Write a function named `five_multiples_of` that accepts a number as an argument. The function should
    # print out the first five multiples of the given number. The function doesn't need to return any
    # value. It should just print to the terminal.
    def five_multiples_of(num):
        for i in range(1, 6):
            print(i * num)

    five_multiples_of(7)
    # prints
    #  7
    #  14
    #  21
    #  28
    #  35

    five_multiples_of(3)
    # prints
    #  3
    #  6
    #  9
    #  12
    #  15


def exercise12():
    # Write a function named `sum_up_to(max)` that accepts a max number as an argument. The function should
    # return the total sum of all whole numbers from 1 to the max, inclusive.
    #
    # For example, sum_up_to(4) should return 10 because 1 + 2 + 3 + 4 = 10.
    def sum_up_to(max):
        total = 0
        for i in range(1, max + 1):
            total += i
        return total

    print(sum_up_to(4))  # 10
    print(sum_up_to(5))  # 15
    print(sum_up_to(2))  # 3


def exercise13():
    # Write a function named `no_ohs` that accepts a string as an argument. The functions should print the
    # characters of the string one by one except the character 'o'. The function doesn't need to return
    # any value. It should just print to the terminal.
    def no_ohs(string):
        for i in string:
            if i != "o":
                print(i)

    no_ohs("code")
    # prints
    #  c
    #  d
    #  e

    no_ohs("school")
    # prints
    #  s
    #  c
    #  h
    #  l


def exercise14():
    # Write a function named `odd_sum(max)` that accepts a max number as an argument. The function should
    # return the total sum of all odd numbers from 1 to the max, inclusive.
    #
    # For example, odd_sum(10) should return 25 because 1 + 3 + 5 + 7 + 9 = 25
    def odd_sum(max):
        total = 0
        for i in range(1, max + 1, 2):
            total += i
        return total

    print(odd_sum(10))  # 25
    print(odd_sum(5))  # 9


def exercise15():
    # Write a function named `string_repeater(str, num)` that accepts a string and a number as arguments.
    # The function should return a new string consisting of the `str` repeated `num` number of times.
    def string_repeater(string, num):
        return string * num

    print(string_repeater("q", 4))  # 'qqqq'
    print(string_repeater("go", 2))  # 'gogo'
    print(string_repeater("tac", 3))  # 'tactactac'


def exercise16():
    # Write a function named `product_up_to(max)` that accepts a max number as an argument. The function
    # should return the total product of all whole numbers from 1 to the max, inclusive. A product is a
    # number obtained from multiplying numbers together.
    #
    # For example, product_up_to(4) should return 24 because 1 * 2 * 3 * 4 = 24
    def product_up_to(max):
        total = 1
        for i in range(1, max + 1):
            total *= i
        return total

    print(product_up_to(4))  # 24
    print(product_up_to(5))  # 120
    print(product_up_to(7))  # 5040


def exercise17():
    # Write a function named `div_by_either(num1, num2, max)` that accepts three numbers as arguments.
    # The function should print out all positive numbers less than max that are divisible by num1 or num2.
    # The function doesn't need to return any value. It should just print to the terminal.
    def div_by_either(num1, num2, max):
        for i in range(1, max):
            if i % num1 == 0 or i % num2 == 0:
                print(i)

    div_by_either(4, 3, 16)
    # prints
    #  3
    #  4
    #  6
    #  8
    #  9
    #  12
    #  15

    div_by_either(7, 5, 20)
    # prints
    #  5
    #  7
    #  10
    #  14
    #  15


def exercise18():
    # Write a function `divisible_range(min, max, num)` that accepts three numbers as arguments. The
    # function should print all numbers between `min` and `max` (exclusive) that are also divisible by
    # num.
    def divisible_range(min, max, num):
        for i in range(min + 1, max):
            if i % num == 0:
                print(i)

    divisible_range(17, 40, 9)
    # prints
    #  18
    #  27
    #  36

    divisible_range(10, 24, 4)
    # prints
    #  12
    #  16
    #  20


def exercise19():
    # Write a function `reverse_iterate` that accepts a string as an argument. The function should print
    # the characters of the string one by one, in reverse order. The function doesn't need to return any
    # value. It should just print to the terminal.
    def reverse_iterate(string):
        for i in range(len(string) - 1, -1, -1):
            print(string[i], i)

    reverse_iterate("carrot")
    # prints
    #  t
    #  o
    #  r
    #  r
    #  a
    #  c

    reverse_iterate("box")
    # prints
    #  x
    #  o
    #  b


def exercise20():
    # Write a function `remove_capitals` that accepts a string as an argument. The function should return a
    # new version of the string with all capital letters removed.
    def remove_capitals(string):
        new_string = ""
        for i in string:
            if i == i.lower():
                new_string += i

        return new_string

    print(remove_capitals("fOrEver"))  # 'frver'
    print(remove_capitals("raiNCoat"))  # 'raioat'
    print(remove_capitals("cElLAr Door"))  # 'clr oor'


def exercise21():
    # Write a function `raise_power(base, exponent)` that accepts two numbers, `base` and `exponent`. The
    # function should return `base` raised to the `exponent` power.
    #
    # For example, raise_power(2, 5) should return 32 because 2 * 2 * 2 * 2 * 2 = 32
    # For example, raise_power(4, 3) should return 64 because 4 * 4 * 4 = 64
    def raise_power(base, exponent):
        total = 1
        for i in range(1, exponent + 1):
            total *= base
        return total

    print(raise_power(2, 5))  # 32
    print(raise_power(4, 3))  # 64
    print(raise_power(10, 4))  # 10000
    print(raise_power(7, 2))  # 49


def exercise22():
    # Write a function `censor_e` that accepts a string as an argument. The function should return the a new
    # version of string where all characters that are 'e's are replaced with '*'s.
    def censor_e(string):
        new_string = ""
        for i in string:
            if i == "e":
                new_string += "*"
            else:
                new_string += i
        return new_string

    print(censor_e("speedy"))  # 'sp**dy'
    print(censor_e("pending"))  # 'p*nding'
    print(censor_e("scene"))  # 'sc*n*'
    print(censor_e("heat"))  # 'h*at'


def exercise23():
    # Write a function `fizz_buzz` that accepts a max number as an argument. The function should
    # print all numbers less than or equal to max that are divisible by either 3 or 5 but not both 3
    # and 5. The function doesn't need to return any value. It should just print to the terminal.
    def fizz_buzz(max):
        for i in range(1, max + 1):
            if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
                print(i)

    fizz_buzz(18)
    # prints
    #  3
    #  5
    #  6
    #  9
    #  10
    #  12
    #  18

    fizz_buzz(33)
    # prints
    #  3
    #  5
    #  6
    #  9
    #  10
    #  12
    #  18
    #  20
    #  21
    #  24
    #  25
    #  27
    #  33


main()
