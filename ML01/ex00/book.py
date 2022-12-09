import datetime
from recipe import Recipe


class Book:
    def __init__(self, name='Cookbook'):
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.recipe_list = {'starter': [], 'lunch': [], 'dessert': []}

    def get_recipe_by_name(self, name):
        for recipe in self.recipe_list:
            for item in self.recipe_list[recipe]:
                if item.name == name:
                    print(item)
                    return item
        print('Error: recipe does not exist\n')
        return

    def get_recipes_by_types(self, recipe_type):
        if recipe_type not in self.recipe_list:
            print('Error: recipe type does not exist')
            return
        list_to_return = []
        for recipe in self.recipe_list[recipe_type]:
            list_to_return.append(recipe.name)
        if len(list_to_return) == 0:
            print('No recipes of this type')
            return
        return list_to_return

    def add_recipe(self, recipe):
        try:
            if not isinstance(recipe, Recipe):
                raise TypeError(f'Error {recipe} is not a valid recipe')
            else:
                self.recipe_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.datetime.now()
        except TypeError as e:
            print(type(e).__name__ + ': ' + str(e))
            return
