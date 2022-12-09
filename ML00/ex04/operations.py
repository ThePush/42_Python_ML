import sys


def main():
    if len(sys.argv) != 3:
        exit('Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3')
    try:
        if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
            raise AssertionError('only integers')
    except Exception as e:
        print(type(e).__name__ + ': ' + str(e))
        exit()

    print('Sum:       ', int(sys.argv[1])+int(sys.argv[2]))
    print('Difference:', int(sys.argv[1])-int(sys.argv[2]))
    print('Product:   ', int(sys.argv[1])*int(sys.argv[2]))
    print('ERROR (division by zero)') if int(sys.argv[2]) == 0 else print(
        'Quotient:  ', float((f'{int(sys.argv[1])/int(sys.argv[2]):.4f}')))
    print('ERROR (modulo by zero)') if int(sys.argv[2]) == 0 else print(
        'Remainder: ', int(sys.argv[1]) % int(sys.argv[2]))


if __name__ == "__main__":
    main()
