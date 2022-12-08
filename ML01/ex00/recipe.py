class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description='Food', recipe_type=None):
        if not isinstance(name, str) or len(name) == 0:
            raise TypeError('name must be a non-empty string')
        else:
            self.name = name

        if not isinstance(cooking_lvl, int) or int(cooking_lvl) not in range(0, 6):
            raise Exception('cooking_lvl must be an integer between 1 and 5')
        else:
            self.cooking_lvl = cooking_lvl

        if not isinstance(cooking_time, int) or cooking_time < 0:
            raise Exception('cooking_time must be a postive integer')
        else:
            self.cooking_time = cooking_time

        if not isinstance(ingredients, list) or len(ingredients) == 0:
            raise TypeError('ingredients must be a non-empty list')
        else:
            self.ingredients = ingredients

        self.description = description

        if not isinstance(recipe_type, str) or len(recipe_type) == 0 or recipe_type not in ['starter', 'lunch', 'dessert']:
            raise Exception(
                'recipe_type must be a non-empty string and be either starter, lunch or dessert')
        else:
            self.recipe_type = recipe_type

    def __str__(self):
        return str(f'{self.name}:\n\tlvl: {self.cooking_lvl},\n\t{self.cooking_time}mn of prep time,\n\t{self.ingredients},\n\t{self.description},\n\tSuitable as a {self.recipe_type}')


# https://www.w3schools.com/python/python_classes.asp
