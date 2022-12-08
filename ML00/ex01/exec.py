# exec.py
import sys


def main():
    '''main function'''
    # sys.argv[1:][::-1] goes from the last argument to the first excluding the first one
    print(' '.join([arg[::-1].swapcase() for arg in sys.argv[1:][::-1]]))


if __name__ == "__main__":
    main()

# [::-1] https://www.w3schools.com/python/python_howto_reverse_string.asp
# __main__ https://realpython.com/python-main-function/
# nested loop (not used here) https://pynative.com/python-nested-loops/
# swapcase() https://www.w3schools.com/python/ref_string_swapcase.asp
