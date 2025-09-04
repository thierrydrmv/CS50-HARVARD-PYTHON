# third part code that you can use for optimzing time use, don't
# create something that already exists (modules/libraries)

# import random -> brings every function from the module
# from random import choice -> brings only the choice function

# packages pypi.org
# pip -> package manage

import random
import statistics
import sys  # system functions
import cowsay
import requests
import json
import module


def main():
    # random_module()
    # statistics_module()
    # sys_module()
    # slicing_list()
    # say_cowsay_hi()
    # itunes_api()
    using_my_module()


def random_module():
    coin = random.choice(["heads", "tails"])

    d20 = random.randint(1, 20)

    cards = ["jack", "queen", "king"]
    random.shuffle(cards)  # randomize cards

    print(coin)
    print(d20)
    print(cards)


def statistics_module():
    print(statistics.mean([100, 22]))


def sys_module():
    # brings what you type after the doc
    # ex: python3 5-libraries.py Thierry
    # sys.argv[0] name of the program
    print(sys.argv[0])
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    print("hello, my name is", sys.argv[1])


def slicing_list():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    # this is the more optimized way of not using the first argument of an array
    for i in sys.argv[1:]:
        print("Hello, my name is", i)


def say_cowsay_hi():
    if len(sys.argv) == 2:
        cowsay.cow("hello, " + sys.argv[1])


def itunes_api():
    # aplication program interface ->
    # Mechanism that is used to access information in another server and integrate with yours
    if len(sys.argv) != 2:
        sys.exit()
    # pretend to be a browser:
    response = requests.get(
        "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
    )
    # dumps -> dump string, indent make pretty like my code :D
    # print(json.dumps(response.json(), indent=2))
    o = response.json()
    for result in o["results"]:
        print(result["trackName"])


def using_my_module():
    if len(sys.argv) == 2:
        module.hello(sys.argv[1])
        module.goodbye(sys.argv[1])


if __name__ == "__main__":
    main()
