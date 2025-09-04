# type hints
# mypy is library that checks if the type hints have been followed
# python is dynamic type
def meow(n: int) -> str:
    # docstrings -> documenting your code directly
    """
    Meow in times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number: int = int(input("Number: "))

print(meow(number), end="")

# mypy cat.py
# could see if the type hints are followed
