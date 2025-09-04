# A way to express yourself in code "maybe do something IF something is true"
def main():
    print("Welcome")

    # num1 = int(input("What's num1? "))
    # num2 = int(input("What's num2? "))

    # print(compare(num1, num2))

    # print(equal(num1, num2))

    # print(score(num1))

    # if (is_even(num1)):
    #   print("Even")
    # else:
    #   print("Odd")

    flavor = int(input("Choose a flavor:\n1.Marguerita\n2.Pepperoni\n3.Portuguese\n"))
    print(pizza(flavor))


def compare(num1, num2):
    if num1 > num2:
        return "num1 is greater than num2"
    elif num1 < num2:
        return "num2 is greater than num1"
    else:
        return "num1 and num2 are equal"


def equal(num1, num2):
    # if num1 > num2 or num2 > num1: # using or
    if num1 != num2:
        return "num1 is not equal to num2"
    else:
        return "num1 and num2 are equal"


def score(num1):
    # if num1 >= 90 and num1 <= 100: # using and
    # if 90 <= num1 <= 100: # nested conditional
    if num1 >= 90:
        return "Grade: A"
    elif num1 >= 80:
        return "Grade: B"
    elif num1 >= 70:
        return "Grade: C"
    elif num1 >= 60:
        return "Grade: D"
    elif num1 >= 50:
        return "Grade: E"
    else:
        return "Grade: F"


def is_even(num1):  # even or odd
    return num1 % 2 == 0
    # return True if num1 % 2 == 0 else False


def pizza(flavor):
    match flavor:  # match is close to switch-case but without logic
        case 1:
            return "A Marguerita pizza is on the way"
        case 2:
            return "A Pepperoni pizza is on the way"
        case 3:
            return "A Portuguese pizza is on the way"
        case _:  # default _
            print("----------------------------")
            print("Choose a number from 1 to 3.")
            return main()


main()
