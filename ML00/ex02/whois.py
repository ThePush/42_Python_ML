import sys


def main():
    try:
        assert len(sys.argv) > 1, "AssertionError: No argument provided"
        assert len(
            sys.argv) == 2, "AssertionError: more than one argument are provided"
        assert sys.argv[1].isdigit(
        ), "AssertionError: argument is not an integer"
    except AssertionError as e:
        exit(e)

    print("I'm Zero." if int(sys.argv[1]) == 0 else
          "I'm Odd." if int(sys.argv[1]) & 1 else
          "I'm Even.")


if __name__ == "__main__":
    main()

# ternary operator: https://www.geeksforgeeks.org/ternary-operator-in-python/
