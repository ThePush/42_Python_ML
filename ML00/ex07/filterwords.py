import sys
import string


def main():
    if len(sys.argv) != 3:
        exit('ERROR')
    if not sys.argv[2].isdigit():
        exit('ERROR')
    print([x.strip(string.punctuation)
          for x in sys.argv[1].split() if len(x) > int(sys.argv[2])])


if __name__ == '__main__':
    main()

# https://blog.finxter.com/python-split-string-by-comma-and-whitespace/
# https://blog.finxter.com/list-comprehension/
