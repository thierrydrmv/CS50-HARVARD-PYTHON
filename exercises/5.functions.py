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
    exercise24()
    exercise25()


def exercise1():
    def greet():
        print("hey")  # 3
        print("programmers")  # 4

    def whistle():
        print("doot")  # 7

    print("first")  # 1
    print("second")  # 2
    greet()
    print("third")  # 5
    print("fourth")  # 6
    whistle()


def exercise2():
    def howMany():
        return 42

    print(howMany)  # function
    print(howMany())  # 42

    def theAnswer():
        howMany()

    print(theAnswer)  # function

    def howMuch():
        5

    print(howMuch())  # None


def exercise3():
    def average(num1, num2):
        print("calculating...")
        return (num1 + num2) / 2

    print(average(5, 10))  # calculating... # 7.5
    print(average(20, 26))  # calculating... # 23.0
    print(average(50, 100) + 2)  # calculating... # 77.0

    a = 21 + 3
    b = 20
    n = average(a, b)  # calculating...
    print(average(n, 18))  # calculating # 20.0


def exercise4():
    def exclaim(string):
        capitalizing = string.upper()
        return capitalizing + "!!"

    result = exclaim("potato")
    print(result)  # POTATO!!
    print(len(result))  # 8
    print(result[0])  # P
    print(result[len(result) - 1])  # !


def exercise5():
    # Write a function `is_div_by_4` that accepts a number as an argument. The function should return a
    # boolean indicating whether or not the number is divisible by 4.
    def is_div_by_4(num):
        return num % 4 == 0

    print(is_div_by_4(8))  # True
    print(is_div_by_4(12))  # True
    print(is_div_by_4(24))  # True
    print(is_div_by_4(9))  # False
    print(is_div_by_4(10))  # False


def exercise6():
    # Write a function `keep_it_quiet` that accepts a string as an argument. The function should return the
    # lowercase version of the string with 3 periods added to the end of it.
    def keep_it_quiet(string):
        return string.lower() + "..."

    print(keep_it_quiet("HOORAY"))  # 'hooray...'
    print(keep_it_quiet("Doggo"))  # 'doggo...'
    print(keep_it_quiet("WHAT?!?!"))  # 'what?!?!...'


def exercise7():
    # Write a function `is_long` that accepts a string as an argument. The function should return a boolean
    # indicating whether or not the string is longer than 5 characters
    def is_long(string):
        return len(string) > 5

    print(is_long("pie"))  # False
    print(is_long("kite"))  # False
    print(is_long("kitty"))  # False
    print(is_long("telescope"))  # True
    print(is_long("thermometer"))  # True
    print(is_long("restaurant"))  # True


def exercise8():
    # Write a function `half` that accepts a number as an argument. The function should return half of the
    # number.
    def half(num):
        return num / 2

    print(half(8))  # 4
    print(half(15))  # 7.5
    print(half(90))  # 45


def exercise9():
    # Write a function `ends_with_t` that accepts a string as an argument. The function should return a
    # boolean indicating whether or not the string ends with the character 't'.
    def ends_with_t(string):
        return string[len(string) - 1] == "t"

    print(ends_with_t("smart"))  # True
    print(ends_with_t("racket"))  # True
    print(ends_with_t("taco"))  # False
    print(ends_with_t("boomerang"))  # False


def exercise10():
    # Write a function `average` that accepts three numbers as arguments. The function should return the
    # average of the three numbers.
    def average(num1, num2, num3):
        return (num1 + num2 + num3) / 3

    print(average(3, 10, 8))  # 7
    print(average(10, 5, 12))  # 9
    print(average(6, 20, 40))  # 22


def exercise11():
    # Write a function `starts_with_r` that accepts a string as an argument and returns a boolean indicating
    # whether or not the string starts with 'r' or 'R'.
    def starts_with_r(string):
        return string[0] == "R" or string[0] == "r"

    print(starts_with_r("roger that"))  # True
    print(starts_with_r("Row, row, row your boat"))  # True
    print(starts_with_r("slip"))  # False
    print(starts_with_r("Taxicab"))  # False


def exercise12():
    # Write a function `parity` that accepts a number as an argument. The function should return the
    # string 'even' if the number is even. It should return the string 'odd' if the number is odd.

    def parity(num):
        return "even" if num % 2 == 0 else "odd"

    print(parity(5))  # 'odd'
    print(parity(7))  # 'odd'
    print(parity(13))  # 'odd'
    print(parity(32))  # 'even'
    print(parity(10))  # 'even'
    print(parity(602348))  # 'even'


def exercise13():
    # Write a function `longer` that accepts two strings as arguments. The function should return the
    # string that is longer. If the strings have the same length, then return the first string.
    def longer(string1, string2):
        return string2 if len(string1) < len(string2) else string1

    print(longer("drum", "piranha"))  # 'piranha'
    print(longer("basket", "fork"))  # 'basket'
    print(longer("flannel", "sustainable"))  # 'sustainable'
    print(longer("disrupt", "ability"))  # 'disrupt'
    print(longer("bird", "shoe"))  # 'bird'


def exercise14():
    # Write a function `one_or_none` that accepts two booleans as arguments. The function should return True
    # if exactly one of the arguments is True. If BOTH arguments are True, then it should return False.
    def one_or_none(bool1, bool2):
        return bool1 != bool2 if True else False

    print(one_or_none(False, False))  # False
    print(one_or_none(True, False))  # True
    print(one_or_none(False, True))  # True
    print(one_or_none(True, True))  # False


def exercise15():
    # Write a function `ends_in_ly` that accepts a string as an argument and returns a boolean indicating
    # whether or not the string ends in the substring 'ly'.
    def ends_in_ly(string):
        return string[-2 : len(string)] == "ly"

    print(ends_in_ly("pretty"))  # False
    print(ends_in_ly("instant"))  # False
    print(ends_in_ly("analytic"))  # False
    print(ends_in_ly("timidly"))  # True
    print(ends_in_ly("fly"))  # True
    print(ends_in_ly("gallantly"))  # True


def exercise16():
    def funny_sound(string1, string2):
        return string1[0:3] + string2[0:3]

    # Write a function `funny_sound` that accepts two strings as arguments. The function should return a
    # new string containing the first three characters of both strings concatenated together.

    # You can assume that the arguments are both at least three characters long.

    print(funny_sound("tiger", "spoon"))  # 'tigspo'
    print(funny_sound("computer", "phone"))  # 'compho'
    print(funny_sound("skate", "bottle"))  # 'skabot'
    print(funny_sound("frog", "ashtray"))  # 'froash'


def exercise17():
    # Write a function `string_size` that accepts a string as an argument. The function should return the
    # string 'small' if the argument is shorter than 5 characters, 'medium' if it is exactly 5 characters, and
    # 'large' if it is longer than 5 characters.
    def string_size(string):
        return (
            "small" if len(string) < 5 else ("medium" if len(string) == 5 else "large")
        )

    print(string_size("cat"))  # 'small'
    print(string_size("bell"))  # 'small'
    print(string_size("ready"))  # 'medium'
    print(string_size("shirt"))  # 'medium'
    print(string_size("shallow"))  # 'large'
    print(string_size("intelligence"))  # 'large'


def exercise18():
    # Write a function `wacky_word` that accepts two strings as arguments. The function should return a new
    # string containing the first three characters of the first string concatenated with the last two
    # character of the second string.

    # You can assume that the first argument has a length of at least three and the second argument has a
    # length of at least two.
    def wacky_word(string1, string2):
        return string1[0:3] + string2[-2 : len(string2)]

    print(wacky_word("very", "kindly"))  # 'verly'
    print(wacky_word("forever", "sick"))  # 'forck'
    print(wacky_word("cellar", "door"))  # 'celor'
    print(wacky_word("bagel", "sweep"))  # 'bagep'


def exercise19():
    # Write a function `divisible(num1, num2)` that accepts two numbers as arguments. The function should
    # return a boolean indicating whether or not `num1` is divisible by `num2`.
    def divisible(num1, num2):
        return True if num1 % num2 == 0 else False

    print(divisible(12, 3))  # True
    print(divisible(12, 5))  # False
    print(divisible(60, 4))  # True
    print(divisible(60, 11))  # False
    print(divisible(21, 7))  # True
    print(divisible(21, 6))  # False


def exercise20():
    # Write a function `case_change` that accepts a string and a boolean as arguments. The function should
    # return the uppercase version of the string if the boolean is True. The function should return the
    # lowercase version of the string if the boolean is False.
    def case_change(string, bool1):
        return string.upper() if bool1 else string.lower()

    print(case_change("Super", True))  # 'SUPER'
    print(case_change("Super", False))  # 'super'
    print(case_change("tAmBourine", True))  # 'TAMBOURINE'
    print(case_change("tAmBourine", False))  # 'tambourine'


def exercise21():
    # Write a function `in_range(min, max, n)` that accepts three numbers as arguments. The function should
    # return a boolean indicating if `n` is between `min` and `max` inclusive.
    def in_range(min, max, n):
        return min <= n <= max

    print(in_range(5, 13, 8))  # True
    print(in_range(5, 13, 29))  # False
    print(in_range(100, 125, 100))  # True
    print(in_range(100, 125, 99))  # False
    print(in_range(40, 45, 44))  # True
    print(in_range(40, 45, 45))  # True
    print(in_range(40, 45, 46))  # False


def exercise22():
    # Write a function `average_of_four(num1, num2, num3, num4)` that accepts four numbers as arguments. The
    # function should return the average of all four numbers.
    def average_of_four(num1, num2, num3, num4):
        return (num1 + num2 + num3 + num4) / 4

    print(average_of_four(10, 4, 12, 3))  # 7.25
    print(average_of_four(-20, 50, 4, 21))  # 13.75
    print(average_of_four(10, 4, 12, 3))  # 7.25
    print(average_of_four(5, 5, 3, 7))  # 5


def exercise23():
    # Write a function `number_change` that accepts a number as an argument. The function should return
    # half the number if it is even. The function should return double the number if it is odd.
    def number_change(num):
        return num / 2 if num % 2 == 0 else num * 2

    print(number_change(6))  # 3
    print(number_change(7))  # 14
    print(number_change(16))  # 8
    print(number_change(21))  # 42


def exercise24():
    # Write a function `larger` that accepts two numbers as arguments. The function should return the
    # larger number.
    def larger(num1, num2):
        return num1 if num1 > num2 else num2

    print(larger(256, 400))  # 400
    print(larger(31, 4))  # 31
    print(larger(-6, 7))  # 7
    print(larger(11.3, 11.2))  # 11.3
    print(larger(-10, -3))  # -3


def exercise25():
    # Write a function `contains(str1, str2)` that accepts two strings as arguments. The function should
    # return a boolean indicating whether or not `str2` is contained within `str1`. The function should
    # ignore any differences in capitalization.
    def contains(str1, str2):
        return True if str2.lower() in str1.lower() else False

    print(contains("caterpillar", "pill"))  # True
    print(contains("lion's share", "on"))  # True
    print(contains("SORRY", "or"))  # True
    print(contains("tangent", "gem"))  # False
    print(contains("clock", "ok"))  # False


if __name__ == "__main__":
    main()
