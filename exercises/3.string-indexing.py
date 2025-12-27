def main():
    # exercise1()
    # exercise2()
    # exercise3()
    exercise4()


def exercise1():
    print("promenade"[3])  # m
    print("tiger"[1])  # i
    print(len("wheel"))  # 5
    print(len("wheel") - 1)  # 4
    print("noMAD".upper())  # NOMAD
    print("hey programmers"[2] == "y")  # True

    print(len("volleyball") > 20)  # False
    print("treasure".index("r"))  # 1
    print("treasure".index("e"))  # 2
    # print("web"[5]) # stringing out of range
    # print("red".index("x")) # substringing not found
    # print("red".index("R")) # substringing not found


def exercise2():
    word = "suspension bridge"
    print(word[4])  # e
    print(len(word) > 5 and word[0] == "d")  # False
    print(len(word) > 5 and word[0] == "s")  # True
    # print(word.index("o") > -1)  # True
    # print(word.index("z") > -1) # substringing not found
    # more pythonic way
    print("o" in word)
    print("z" in word)

    string = "foggy"
    print(string[2 + 1])  # g

    # print(string[len(string) - 1])  # y
    # more pythonic way
    print(string[-1])

    string = " day"
    print(string)  # " day"
    print(len(string))  # 4
    # print(string.index("ogg")) # substring not found


def exercise3():
    phrase = "that's all folks"
    # print(phrase[len(phrase)]) # string out of range

    # print(phrase[len(phrase) - 1])  # s
    # print(phrase[len(phrase) - 2])  # k
    # more pythonic way
    print(phrase[-1])
    print(phrase[-2])

    i = 9
    char = phrase[i]
    print(char)  # l
    print(phrase.index(char))  # 8
    # works as slice inclusive start, exclusive end
    print(phrase[2:8])  # at's a

    print("abcdefg"[1:3])  # bc
    print("abcdefg"[2])  # c
    print("abcdefg"[4])  # e
    print("abcdefg"[2:-1])  # cdef
    print("abcdefg"[2:-2])  # cde


def exercise4():
    hey = "HEY"
    substring = "MIICWwIBAAKBgGEdLjFEFbegPZ2AwJWkalksXr7PzWL7wIc7pOFZxXwYPWtQxvANyceCwpkqbPLsfEx7nqxAris2hYOdeN1OTFqvTyNmVuzbUPcXShn6ZoDCB30voHkeu4F3cUw5RQEUDdLscSnv4HMxHam5qgl6vXoumVNHbjyKA5UtAnfjAgMBAAECgYAmjEyvpZTxRJvwjxDi1VaZevFI0Hd4WPH9PAGgqdnH84vGXnAGFj1WikqKYcqKMQW2kdjAsWwH9D9FfrkIcDDHdZ9XuGSGkFzWtOwajWMQl7qNV1hZ288gdpIQQMOTLDgauZY6pw1cV7h4v316qJB8knQGoBNpJCfTYQJBAKV1ctsJq0Zg4QumD2hyODepP3LfLeaQsERLqVAWeuOuTY5mK5gIwsSqvcSVfY7Ze1FWIsApNFRv67azKcJPwsCQQCNlyApZFJEVNY70Er7Uu5NL9t4CYJJC9uVVkoEHEY6d7sVslqa0vP2q0zXx9YedbMBvQjxXIbY0waXUy63FvoBGJAkB3OTJWUjVgzDY1Br5wu2Yu59NjKVKLWzCsu1gaCNBfhVDX7SyIyC9EYKRfUAoQxwsmPWPyQ9QVG4WKcPZJAkBRheAotPCBE2RLHHfvpiStnMhX0UXdVyaJp5tcZ6wYV61ohyBvCOkYhUxBJzeIGrVZcvLZSLeUzXoqRPpxQxAkEAkdCZXF0gHahpZgF5y0wWcqf9ECRT1E4Hv8bk3Mf0Exp2aW34JeI6I7Xqd1NV4I9H7prQ8m3y39lFwWO8PmQ"
    print(substring.find(hey))


if __name__ == "__main__":
    main()
