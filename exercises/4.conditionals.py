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
    exercise12()


def exercise1():
    if True:
        print("foo")  # foo

    if False:
        print("bar")


def exercise2():
    if False or False:
        print("boop")

    if True or False:
        print("beep")  # beep


def exercise3():
    num = 40

    if num > 0:
        print("zip")  # zip

    if num % 2 == 0:
        print("zoop")  # zoop


def exercise4():
    word = "jeep"

    if word[0] == "d":
        print("yer")
    else:
        print("nah")  # nah


def exercise5():
    sentence = "roger that"

    if sentence[-1] == "t":
        print("ends in t")  # ends in t
    else:
        print("does not end in t")

    if len(sentence) <= 4:
        print("short")
    else:
        print("long")  # long


def exercise6():
    qty = 38

    if qty > 30 and qty % 5 == 4:
        print("swish")
    else:
        print("swoosh")  # swoosh

    if qty > 0:
        print("pos")  # pos


def exercise7():
    alpha = "celery"
    beta = "SQUASH"

    if alpha == alpha.upper():
        print("alpha")

    if beta == beta.upper():
        print("beta")  # beta


def exercise8():
    number = 9

    if number > 4:
        print("ding")  # ding
    elif number % 3 == 0:
        print("dong")


def exercise9():
    z = 12

    if z > 10:
        print("vroom")  # vroom

    if z % 3 == 0:
        print("skrrt")  # skrrt


def exercise10():
    nonsense = "blog trust fund tattooed williamsburg poke roof party"
    has_ok = "ok" in nonsense

    if has_ok:
        print("yeet")  # yeet
    elif len(nonsense) > 10:
        print("yo")
    else:
        print("no")

    has_zoo = "zoo" in nonsense
    has_fun = "fun" in nonsense

    if has_zoo and has_ok:
        print("cool")
    elif has_ok:
        print("rad")  # rad
    elif has_fun:
        print("dope")
    else:
        print("nope")


def exercise11():
    q = 25
    if q % 3 == 0 and q % 5 == 0:
        print("both")
    elif q % 3 == 0 or q % 5 == 0:
        print("either")  # either
    else:
        print("neither")

    r = 9
    if r % 3 == 0 and r % 5 == 0:
        print("both")
    elif r % 3 == 0 or r % 5 == 0:
        print("either")  # either
    else:
        print("neither")

    s = 15
    if s % 3 == 0 and s % 5 == 0:
        print("both")  # both
    elif s % 3 == 0 or s % 5 == 0:
        print("either")
    else:
        print("neither")


def exercise12():

    string = "AIICXAIBAAKBgQCuw0YyucjI9bf7yRhIkyg4Ru6kYU7O6fIn2JoFDzCZNkzDdsuXFGh6BXNvbu8uZUT289ERzYP1QjryMEKWzcbtsioyQApL7AgOZyFc3JJ7wvupHhIj2sqxJNtpAh7HQFG08rYh2Pb3HwOm83rbTomM6LnnjooGcoDeuWkuPqXsRlwIDAQABAoGAeQkbPBR5n9y2QLaEjcDGv7dVpFiMGHMaZZVDX34rZPy1EkZNZqlQU0jopLVvLyLESMh9A7gKhqoyMAbgZPpdb0CvniTJPpKYk24mLBeym8rBMW3XBmKk1xIOcJPGXMxeJW61jxPg6doah0aCIjf8n0Z8t8B81kLFojpECQQDzlCp0Nzka3AVZVPdBuuPg0fzeV8ugpiPEp6wQLjIMDFqYtGoAOEy4JpkmkK7zwsQsHZ8jbOtqIFdRLPrvAkEAruU321Ie1CnYCHX4Q79vLcDeWOUpdzEHp2uzDIfzP1gv7RIktGgSZWKhrnNWdeH4Y0CFb9lu6TQYJwNJvug2QJBANX0m3Uds9P9pLbQlI9WWmAtYqIZrsBElcAjOgAik0uOfawholNiw5B3ADvIYqPkLW4dGk1dO6zxW8ZF83MdMCQHGfhxLuFgsOBSfF7Bj4UX6T9FGhUGSXiqUsd06E2mMRLAjWUUUw82DLwucxMrSsV4z1aN57asC8YuQ9FkCQGirlVCt4ccXeGLCHcCsI8AYQJFRzbMs381M16jEpnaKUGrtdbMW018gWJ0EoD4tS2YZpr1hEbtiOkPJaaTKQ"
    code = "coDe"

    if code in string:
        print("FOUND")  # FOUND
    else:
        print("NOT FOUND")


if __name__ == "__main__":

    main()
