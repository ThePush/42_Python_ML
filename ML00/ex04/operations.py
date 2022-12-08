import sys


def main():
    if len(sys.argv) != 3:
        exit('Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3')
    try:
        assert sys.argv[1].isdigit(
        ), "AssertionError: only integers"
        assert sys.argv[2].isdigit(
        ), "AssertionError: only integers"
    except AssertionError as e:
        exit(e)

    print('Sum:       ', int(sys.argv[1])+int(sys.argv[2]))
    print('Difference:', int(sys.argv[1])-int(sys.argv[2]))
    print('Product:   ', int(sys.argv[1])*int(sys.argv[2]))
    print('ERROR (division by zero)') if int(sys.argv[2]) == 0 else print(
        'Quotient:  ', float((f'{int(sys.argv[1])/int(sys.argv[2]):.4f}')))
    print('ERROR (modulo by zero)') if int(sys.argv[2]) == 0 else print(
        'Remainder: ', int(sys.argv[1]) % int(sys.argv[2]))


if __name__ == "__main__":
    main()
