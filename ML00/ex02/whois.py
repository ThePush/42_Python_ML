import sys


def main():
    try:
        if len(sys.argv) < 2:
            raise AssertionError('No argument provided.')
        if len(sys.argv) > 2:
            raise AssertionError('More than one argument provided')
        if not sys.argv[1].isdigit():
            raise AssertionError('Argument is not a number.')
    except Exception as e:
        print(type(e).__name__ + ': ' + str(e))
        return

    print("I'm Zero." if int(sys.argv[1]) == 0 else
          "I'm Odd." if int(sys.argv[1]) & 1 else
          "I'm Even.")


if __name__ == "__main__":
    main()

# ternary operator: https://www.geeksforgeeks.org/ternary-operator-in-python/
