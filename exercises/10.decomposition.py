def main():
    print("decomposition")
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
    exercise14()


def exercise1():
    # snippet 1
    def flim():
        print("leak")
        flam()
        print("geek")

    def flam():
        print("beak")
        print("sneak")

    flim()
    # leak
    # beak
    # sneak
    # geek


def exercise2():
    def alice(n):
        for i in range(0, n + 1, 1):
            bob(i)

    def bob(n):
        if n % 2 == 0:
            print("good")
        else:
            print("bad")

    alice(4)
    # good
    # bad
    # good
    # bad
    # good


def exercise3():
    # snippet 3
    def foo():
        for i in range(0, 5):
            print("i =", i)
            bar()

    def bar():
        for j in range(0, 5):
            print("  j =", j)

    foo()
    # i = 0
    #   j = 0
    #   j = 1
    #   j = 2
    #   j = 3
    #   j = 4
    # i = 1
    #   j = 0
    #   j = 1
    #   j = 2
    #   j = 3
    #   j = 4
    # i = 2
    #   j = 0
    #   j = 1
    #   j = 2
    #   j = 3
    #   j = 4
    # i = 3
    #   j = 0
    #   j = 1
    #   j = 2
    #   j = 3
    #   j = 4
    # i = 4
    #   j = 0
    #   j = 1
    #   j = 2
    #   j = 3
    #   j = 4


def exercise4():
    # Write a function `double_vowel` that accepts a string as an argument. The function should return
    # the string where every occurrence of a vowel in the original string is repeated twice consecutively.
    # Vowels are the letters a, e, i, o, u.

    print(double_vowel("runner"))  # 'ruunneer'
    print(double_vowel("stoplight"))  # 'stoopliight'
    print(double_vowel("gardener"))  # 'gaardeeneer'


def double_vowel(string):
    new_string = ""
    for i in string:
        if i in vowels():
            new_string += i
        new_string += i
    return new_string


def exercise5():
    # Write a function `funny_phrase` that accepts a sentence string as an argument. The function should
    # return the sentence where every other word has its vowels repeated twice consecutively.
    # Vowels are the letters a, e, i, o, u.

    def funny_phrase(string):
        string_array = string.split(" ")
        new_array = []
        for i in range(0, len(string_array)):
            if i % 2 != 0:
                new_array.append(double_vowel(string_array[i]))
            else:
                new_array.append(string_array[i])

        return " ".join(new_array)

    print(
        funny_phrase("she dreamed of being a runner")
    )  # 'she dreeaameed of beeiing a ruunneer'
    print(funny_phrase("park near the stoplight"))  # 'park neeaar the stoopliight'
    print(funny_phrase("we need many gardeners"))  # 'we neeeed many gaardeeneers'


def exercise6():
    # Write a function `is_prime` that accepts a number as an argument. The function should return a
    # boolean indicating whether or not the given number is prime. A prime number is a number that is
    # only divisible by 1 and itself. The smallest prime number is 1.
    #
    # For example, 11 is a prime because it is only divisible by 1 and 11.
    # For example, 8 is not a prime because it is divisible by 1, 2, 4, and 8

    print(is_prime(11))  # True
    print(is_prime(8))  # False
    print(is_prime(7))  # True
    print(is_prime(21))  # False
    print(is_prime(2))  # True
    print(is_prime(15))  # False
    print(is_prime(1))  # False


def is_prime(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    return True if count == 2 else False


def exercise7():
    # Write a function `pick_primes` that accepts an array of numbers as an argument. The function should
    # return an array containing only the prime numbers. A prime number is a number that is
    # only divisible by 1 and itself. The smallest prime number is 1.

    def pick_primes(numbers_array):
        new_array = []
        for i in numbers_array:
            if is_prime(i):
                new_array.append(i)
        return new_array

    print(pick_primes([12, 3, 7, 18, 11]))  # [3, 7, 11]
    print(pick_primes([17, 23, 9, 42]))  # [17, 23]
    print(pick_primes([4, 2048, 100, 55]))  # []


def exercise8():
    # Write a function `remove_last_vowel` that accepts a string as argument. The function should return
    # the string with its last vowel removed. Vowels are the letters a, e, i, o, u

    print(remove_last_vowel("speaker"))  # 'speakr'
    print(remove_last_vowel("trading"))  # 'tradng'
    print(remove_last_vowel("thunder"))  # 'thundr'
    print(remove_last_vowel("myth"))  # 'myth'


def remove_last_vowel(string):
    inverted_string = invert_string(string)

    new_string = ""
    counter = 0
    for i in inverted_string:
        if i in vowels() and counter == 0:
            counter += 1
            continue
        new_string += i
    return invert_string(new_string)


def invert_string(string):
    new_string = ""
    for i in range(len(string) - 1, -1, -1):
        new_string += string[i]
    return new_string


def exercise9():
    # Write a function `pick_prefix(strings, prefix)` that accepts an array of strings and a prefix string
    # as an argument. The function should return the an array of words that begin with the prefix.
    def pick_prefix(strings, prefix):
        oah = cut_array(strings, len(prefix))
        new_array = []
        for i in range(0, len(oah)):
            if oah[i] == prefix:
                new_array.append(strings[i])
        return new_array

    def cut_array(strings, size):
        new_array = []
        for i in strings:
            new_array.append(i[:size])
        return new_array

    print(pick_prefix(["connect", "company", "concert", "cram"], "con"))
    # ['connect', 'concert']

    print(pick_prefix(["miner", "mistake", "misspeak", "moose", "mission"], "mis"))
    # [''mistake', 'misspeak', 'mission']


def exercise10():
    # Write a function `trendy_text` that accepts a sentence string as an argument. The function should
    # return the sentence where the last vowel of every word is removed.
    def trendy_text(string):
        new_string_array = []
        string_array = string.split(" ")
        for i in string_array:
            new_string_array.append(remove_last_vowel(i))
        return " ".join(new_string_array)

    print(trendy_text("the concert will be epic"))  # 'th concrt wll be epc'
    print(trendy_text("breakfast food is wonderful"))  # 'breakfst fod s wonderfl'
    print(
        trendy_text("the weather will improve hopefully")
    )  # 'th weathr wll improv hopeflly'


def exercise11():
    # Write a function `most_letter_word` that accepts a sentence string and a character as arguments.
    # The function should return the word of the sentence that contains the character the most number
    # of times. You can assume that the sentence contains at least one word. If there is a tie, return
    # the word that appears earlier in the sentence.
    def most_letter_word(sentence, string):
        string_array = sentence.split(" ")
        numbers_array = count_word(string_array, string)
        bigger = 0
        for z in numbers_array:
            if z > bigger:
                bigger = z
        return string_array[numbers_array.index(bigger)]

    def count_word(array, word):
        numbers_array = []
        for i in range(0, len(array)):
            count = 0
            for y in range(0, len(array[i])):
                if array[i][y] == word:
                    count += 1
            numbers_array.append(count)
        return numbers_array

    print(
        most_letter_word("she received an award for excellence in science", "e")
    )  # 'excellence'
    print(
        most_letter_word("she received an award for excellence in science", "a")
    )  # 'award'
    print(most_letter_word("I hope sophomore year comes soon", "o"))  # 'sophomore'
    print(most_letter_word("I hope sophomore year comes soon", "s"))  # 'sophomore'


def exercise12():
    # Write a function `lala_language` that accepts a sentence string as an argument. The function should
    # return a new sentence where words longer that 3 characters are modified. Modified words should have
    # each vowel followed by 'l' and the same vowel repeated again. See the examples.
    def lala_language(sentence):
        string_array = sentence.split(" ")
        new_sentence_array = []
        for word in string_array:
            new_word = ""
            for y in range(0, len(word)):
                if len(word) > 3 and word[y] in vowels():
                    new_word += word[y]
                    new_word += "l"
                    new_word += word[y]
                else:
                    new_word += word[y]
            new_sentence_array.append(new_word)
        return new_sentence_array

    print(lala_language("this is pretty strange"))  # 'thilis is preletty stralangele'
    print(
        lala_language("can you speak our language")
    )  # 'can you spelealak our lalangulualagele'


def exercise13():
    # Write a function `pick_perfect_squares` that accepts an array of numbers as an argument. The function
    # should return an array containing only the elements that are perfect squares. A perfect square
    # is a number that can result from multiplying some number by itself.
    #
    # For example, 4 is a perfect square because 2 * 2 = 4
    # For example, 81 is a perfect square because 9 * 9 = 81
    def pick_perfect_squares(numbers_array):
        new_array = []
        for i in range(0, len(numbers_array)):
            for y in range(0, numbers_array[i]):
                if numbers_array[i] == y * y:
                    new_array.append(numbers_array[i])
        return new_array

    print(pick_perfect_squares([6, 4, 81, 21, 36]))  # [4, 81, 36]
    print(pick_perfect_squares([100, 24, 144]))  # [100, 144]
    print(pick_perfect_squares([30, 25]))  # [25]


def exercise14():
    # Write a function `censor_sentence(sentence, target_words)` that accepts a sentence string and an array
    # of target words as arguments. The function should return a new sentence where any target words
    # have all of their characters replaced with '*'s.
    def censor_sentence(sentence, target_words):
        sentence_array = sentence.split(" ")
        new_sentence_array = []
        for i in sentence_array:
            word = i
            for y in target_words:
                if i == y:
                    word = len(i) * "*"
            new_sentence_array.append(word)
        return " ".join(new_sentence_array)

    print(censor_sentence("where the heck is my celery", ["heck", "celery"]))
    # 'where the **** is my ******'

    print(censor_sentence("why you little sweetheart", ["sweetheart", "salad"]))
    # 'why you little **********'


def vowels():
    return ["a", "e", "i", "o", "u"]


if __name__ == "__main__":
    main()
