import random
import sys


def generator(text, sep=' ', option=None):
    if not isinstance(text, str):
        print("ERROR")
        sys.exit(1)

    words = text.split(sep)

    if option == 'shuffle':
        for i in range(len(words)):
            j = random.randint(0, len(words) - 1)
            words[i], words[j] = words[j], words[i]
    elif option == 'unique':
        words = list(set(words))
    elif option == 'ordered':
        words.sort()
    elif option is not None:
        print("ERROR")
        sys.exit(1)

    for word in words:
        yield word


# https://www.w3schools.com/python/python_sets.asp
