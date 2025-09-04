def main():
    print("Arrays")
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
    exercise18()


def exercise1():
    # Write a function `total` that accepts an array of numbers as an argument. The function should return
    # the total sum of all elements of the array.
    def total(array):
        total = 0
        for i in array:
            total += i
        return total

    print(total([3, 2, 8]))  # 13
    print(total([-5, 7, 4, 6]))  # 12
    print(total([7]))  # 7
    print(total([]))  # 0


def exercise2():
    # Write a function `stay_positive` that accepts an array of numbers as an argument. The function should
    # return an array containing only the positive numbers.
    def stay_positive(array):
        new_array = []

        for i in array:
            if i > 0:
                new_array.append(i)
        return new_array

    print(stay_positive([10, -4, 3, 6]))  # [10, 3, 6]
    print(stay_positive([-5, 11, -40, 30.3, -2]))  # [11, 30.3]
    print(stay_positive([-11, -30]))  # []


def exercise3():
    # Write a function `bleep_vowels` that accepts a string as an argument. The function should return
    # a new string where all vowels are replaced with `*`s. Vowels are the letters a, e, i, o, u.
    def bleep_vowels(string):
        new_string = ""
        for i in string:
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                new_string += "*"
            else:
                new_string += i
        return new_string

    print(bleep_vowels("skateboard"))  # 'sk*t*b**rd'
    print(bleep_vowels("slipper"))  # 'sl*pp*r'
    print(bleep_vowels("range"))  # 'r*ng*'
    print(bleep_vowels("brisk morning"))  # 'br*sk m*rn*ng'


def exercise4():
    # Write a function `filter_long_words` that accepts an array of strings as an argument. The function
    # should return a new array containing only the strings that are less than 5 characters long.
    def filter_long_words(array):
        new_array = []
        for i in array:
            if len(i) < 5:
                new_array.append(i)
        return new_array

    print(filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]))
    # ['kale', 'cat', 'axe']

    print(filter_long_words(["disrupt", "pour", "trade", "pic"]))
    # ['pour', 'pic']


def exercise5():
    # Write a function `num_odds` that accepts an array of numbers as an argument. The function should
    # return a number representing the count of odd elements in the array.
    def num_odds(numbers_array):
        total_odds = 0
        for i in range(0, len(numbers_array)):
            if numbers_array[i] % 2 != 0:
                total_odds += 1
        return total_odds

    print(num_odds([4, 7, 2, 5, 9]))  # 3
    print(num_odds([11, 31, 58, 99, 21, 60]))  # 4
    print(num_odds([100, 40, 4]))  # 0


def exercise6():
    # Write a function `string_to_lengths` that accepts an array of strings as an argument. The function
    # should return a new array containing the lengths of the elements of the original array.
    def string_to_lengths(strings_array):
        new_array = []
        for i in range(0, len(strings_array)):
            new_array.append(len(strings_array[i]))
        return new_array

    print(string_to_lengths(["belly", "echo", "irony", "pickled"]))
    # [5, 4, 5, 7]

    print(string_to_lengths(["on", "off", "handmade"]))
    # [2, 3, 8]


def exercise7():
    # Write a function `divisors` that accepts a number as an argument. The function should return an
    # array containing all positive numbers that can divide into the argument.
    def divisors(number):
        new_array = []
        for i in range(number + 1):
            if i > 0 and number % i == 0:
                new_array.append(i)
        return new_array

    print(divisors(15))  # [1, 3, 5, 15]
    print(divisors(7))  # [1, 7]
    print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]


def exercise8():
    # Write a function `make_acronym` that accepts a sentence string as an argument. The function should
    # return a string containing the first character of each word in the sentence.
    def make_acronym(string):
        string_array = string.split(" ")
        new_string = ""
        for i in string_array:
            new_string += i[0].upper()
        return new_string

    print(make_acronym("New York"))  # NY
    print(make_acronym("same stuff different day"))  # SSDD
    print(make_acronym("Laugh out loud"))  # LOL
    print(make_acronym("don't over think stuff"))  # DOTS


def exercise9():
    # Write a function `reverse_array` that accepts an array as an argument. The function should return a
    # array containing the elements of the original array in reverse order.
    def reverse_array(array):
        new_array = []
        for i in range(len(array) - 1, -1, -1):
            new_array.append(array[i])
        return new_array

    print(
        reverse_array(["zero", "one", "two", "three"])
    )  # ['three', 'two', 'one', 'zero']
    print(reverse_array([7, 1, 8]))  # [8, 1, 7]


def exercise10():
    # Write a function `your_average_function` that accepts an array of numbers as an argument. The
    # function should return the average of all elements of the array. If the input array is empty,
    # then the function should return None.
    def your_average_function(array):
        if len(array) == 0:
            return None
        total = 0
        for i in array:
            total += i
        return total / len(array)

    print(your_average_function([5, 2, 7, 24]))  # 9.5
    print(your_average_function([100, 6]))  # 53
    print(your_average_function([31, 32, 40, 12, 33]))  # 29.6
    print(your_average_function([]))  # None


def exercise11():
    # Write a function `choose_divisibles(numbers, target)` that accepts an array of numbers and a
    # target number as arguments. The function should return an array containing elements of the original
    # array that are divisible by the target.
    def choose_divisibles(numbers, target):
        new_array = []
        for i in numbers:
            if i % target == 0:
                new_array.append(i)
        return new_array

    print(choose_divisibles([40, 7, 22, 20, 24], 4))  # [40, 20, 24]
    print(choose_divisibles([9, 33, 8, 17], 3))  # [9, 33]
    print(choose_divisibles([4, 25, 1000], 10))  # [1000]


def exercise12():
    # Write a function `maximum` that accepts an array of numbers as an argument. The function should
    # return the largest number of the array. If the array is empty, then the function should return None.
    def maximum(numbers):
        if len(numbers) == 0:
            return None
        max_num = numbers[0]
        for i in numbers:
            if i > max_num:
                max_num = i
        return max_num

    print(maximum([5, 6, 3, 7]))  # 7
    print(maximum([17, 15, 19, 11, 2]))  # 19
    print(maximum([]))  # None


def exercise13():
    # Write a function `word_count(sentence, target_words)` that accepts a sentence string and an array of
    # `target_words`. The function should return a count of the number of words of the sentence that are
    # in `target_words`.
    def word_count(sentence, target_words):
        count = 0
        sentence_words = sentence.split(" ")
        for i in range(0, len(sentence_words)):
            for y in range(0, len(target_words)):
                if sentence_words[i] == target_words[y]:
                    count += 1
        return count

    print(word_count("open the window please", ["please", "open", "sorry"]))  # 2
    print(word_count("drive to the cinema", ["the", "driver"]))  # 1
    print(word_count("can I have that can", ["can", "I"]))  # 3


def exercise14():
    # Write a function `lenghiest_word` that accepts a sentence string as an argument. The function should
    # return the longest word of the sentence. If there is a tie, return the word that appears later
    # in the sentence.
    def lenghiest_word(string):
        string_array = string.split(" ")
        larger_string = string_array[0]
        for i in range(1, len(string_array)):
            if len(larger_string) <= len(string_array[i]):
                larger_string = string_array[i]
        return larger_string

    print(lenghiest_word("I am pretty hungry"))  # 'hungry'
    print(lenghiest_word("we should think outside of the box"))  # 'outside'
    print(lenghiest_word("down the rabbit hole"))  # 'rabbit'
    print(lenghiest_word("simmer down"))  # 'simmer'


def exercise15():
    # Write a function `alternating_caps` that accepts a sentence string as an argument. The function should
    # return the sentence where words alternate between lowercase and uppercase.
    def alternating_caps(string):
        string_array = string.split(" ")
        new_string = string_array[0]
        for i in range(1, len(string_array)):
            if i % 2 == 0:
                new_string += f" {string_array[i].lower()}"
            else:
                new_string += f" {string_array[i].upper()}"
        return new_string

    print(alternating_caps("take them to school"))  # 'take THEM to SCHOOL'
    print(alternating_caps("What did ThEy EAT before?"))  # 'what DID they EAT before?'


def exercise16():
    # Write a function `number_range(min, max, step)` that accepts three numbers as arguments, `min`,
    # `max`, and `step`. The function should return all numbers between `min` and `max` at `step` intervals.
    # `min` and `max` are inclusive.
    def number_range(min, max, step):
        numbers = []
        for i in range(min, max + 1, step):
            numbers.append(i)
        return numbers

    print(number_range(10, 40, 5))  # [10, 15, 20, 25, 30, 35, 40]
    print(number_range(14, 24, 3))  # [14, 17, 20, 23]
    print(number_range(8, 35, 6))  # [8, 14, 20, 26, 32]


def exercise17():
    # Write a function `remove_short_words` that accepts a sentence string as an argument. The function
    # should return a new sentence where all of the words shorter than 4 characters are removed.
    def remove_short_words(string):
        string_array = string.split(" ")
        new_string = ""
        for i in range(0, len(string_array)):
            if len(string_array[i]) >= 4:
                new_string += (
                    string_array[i] if len(new_string) == 0 else f" {string_array[i]}"
                )
        return new_string

    print(remove_short_words("knock on the door will you"))  # 'knock door will'
    print(remove_short_words("a terrible plan"))  # 'terrible plan'
    print(remove_short_words("run faster that way"))  # 'faster that'


def exercise18():
    # Write a function `common_elements` that accepts two arrays as arguments. The function should return
    # a new array containing the elements that are found in both of the input arrays. The order of
    # the elements in the output array doesn't matter as long as the function returns the correct elements.
    def common_elements(array1, array2):
        new_array = []
        for i in array1:
            for y in array2:
                if i == y:
                    new_array.append(i)

        return new_array

    arr1 = ["a", "c", "d", "b"]
    arr2 = ["b", "a", "y"]
    print(common_elements(arr1, arr2))  # ['a', 'b']

    arr3 = [4, 7]
    arr4 = [32, 7, 1, 4]
    print(common_elements(arr3, arr4))  # [4, 7]


if __name__ == "__main__":
    main()
