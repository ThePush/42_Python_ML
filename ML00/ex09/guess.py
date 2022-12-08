import random


def main():
    print('This is an interactive guessing game!\n'
          'You have to enter a number between 1 and 99 to find out the secret number.\n'
          'Type \'exit\' to end the game.\n'
          'Good luck!\n')
    int_to_guess = random.randint(1, 99)
    count = 0
    while True:
        user_input = input('What\'s your guess between 1 and 99?\n>> ')
        if user_input == 'exit':
            exit('Goodbye!')
        count += 1
        if not user_input.isdigit():
            print('That\'s not a number.\n')
        else:
            print('Too high!' if int(user_input) > int_to_guess else
                'Too low!'if int(user_input) < int_to_guess else
                'Congratulations, you\'ve got it!')
            if int(user_input) == int_to_guess:
                if int_to_guess is 42:
                    print(
                        'The answer to the ultimate question of life, the universe and everything is 42.')
                print(f'You won in {count} attempts!\n' if count is not 1 else
                    'Congratulations! You got it on your first try!\n')


if __name__ == '__main__':
    main()
