cookbook = {'Sandwich': (['ham', 'bread', 'cheese'], 'lunch', 10),
            'Cake': (['flour', 'sugar', 'egg'], 'dessert', 60),
            'Salad': (['avocado', 'arugula', 'tomatoes', 'spinach'], 'lunch', 15)}


def add_recipe():
    recipe_name = None
    while recipe_name is None:
        recipe_name = input('\n>>> Enter a name:\n')

    ingredients = []
    print('>>> Enter ingredients:')
    while True:
        to_add = input()
        if to_add:
            ingredients.append(to_add)
        elif not to_add and len(ingredients) > 0:
            break
        else:
            print('>>> Enter ingredients:')

    meal = None
    while not meal:
        meal = input('>>> Enter a meal type:\n')

    while True:
        prep_time = input('>>> Enter a preparation time:\n')
        if prep_time.isdigit() and int(prep_time) >= 0:
            break

    cookbook[recipe_name] = (ingredients, meal, prep_time)


def pop_recipe():
    recipe = input('\nPlease enter a recipe name to delete it:\n>> ')
    if not cookbook.pop(recipe, None):
        print('Sorry, recipe does not exist in cookbook')


def print_recipe():
    recipe = input('\nPlease enter a recipe name to get its details:\n>> ')
    if recipe in cookbook:
        print(f'\nRecipe for {recipe}:')
        print(f'Ingredients list: {cookbook[recipe][0]}')
        print(f'To be eaten for {cookbook[recipe][1]}.')
        print(f'Takes {cookbook[recipe][2]} minutes of cooking.')
    else:
        print('Sorry, recipe does not exist in cookbook')


def print_cookbook():
    if len(cookbook) > 0:
        print('\nHere are all the cookbook\'s recipes:\n')
        print(list(cookbook.keys()))
    else:
        print('\nCookbook empty !\n')


def close_cookbook():
    print('\nCookbook closed. Goodbye !')
    exit()


def print_usage():
    print('List of available option:\n'
          '1: Add a recipe\n'
          '2: Delete a recipe\n'
          '3: Print a recipe\n'
          '4: Print the cookbook\n'
          '5: Quit\n')


def select_option(user_input):
    switcher = {
        1: add_recipe,
        2: pop_recipe,
        3: print_recipe,
        4: print_cookbook,
        5: close_cookbook
    }
    return switcher.get(user_input, lambda: '\nSorry, this option does not exist.')


def main():
    print('Welcome to the Python Cookbook !')
    print_usage()
    user_input = None
    while True:
        while True:
            user_input = input('\nPlease select an option:\n>> ')
            if user_input:
                try:
                    assert (user_input.isdigit()) and (int(user_input) > 0 and int(
                        user_input) < 6), '\nSorry, this option does not exist.'
                    break
                except AssertionError as e:
                    print(e)
                    print_usage()
        select_option(int(user_input))()


if __name__ == "__main__":
    main()
