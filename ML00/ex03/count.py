import sys


def text_analyzer(string=None):
    '''\n\tThis function counts the number of upper characters, lower characters,
\tpunctuation and spaces in a given text.'''

    if string is None:
        while True:
            string = input('What is the text to analyze?\n>> ')
            if string:
                break

    try:
        if not isinstance(string, str):
            raise AssertionError('argument is not a string.')
    except Exception as e:
        print(type(e).__name__ + ': ' + str(e))
        return

    print("The text contains", len(string), "character(s):")
    upper_case, lower_case, punctuation, spaces = 0, 0, 0, 0
    for char in string:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
        elif char.isspace():
            spaces += 1
        elif not char.isdigit():
            punctuation += 1

    print("-", upper_case, "upper letter(s)")
    print("-", lower_case, "lower letter(s)")
    print("-", punctuation, "punctuation mark(s)")
    print("-", spaces, "space(s)")


def main():
    if len(sys.argv) != 2:
        exit("Usage: python count.py <string>")
    text_analyzer(sys.argv[1])


if __name__ == "__main__":
    main()

# string=None https://realpython.com/python-optional-arguments/#using-python-optional-arguments-with-default-values
