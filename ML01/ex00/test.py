from book import Book
from recipe import Recipe


def main():
    r1 = Recipe('Salad caesar', 1, 20, [
                'Caesar sauce', 'parmesan', 'tomatoes'], 'Incredible salad caesar', 'starter')
    r2 = Recipe('Sandwich', 1, 3, [
                'bread', 'cheese'], 'A triangle sandwich', 'lunch')
    r3 = Recipe('Chocolate cake', 2, 60, [
                'chocolate', 'flour', 'sugar'], 'A random cake', 'dessert')
    r4 = Recipe('Chocolate cake2', 2, 60, [
                'chocolate', 'flour', 'sugar'], 'A random cake', 'dessert')
    r5 = Recipe('Chocolate cake3', 2, 60, [
                'chocolate', 'flour', 'sugar'], 'A random cake', 'dessert')

    b1 = Book('My cookbook')
    b1.add_recipe((r1))
    b1.add_recipe(r2)
    b1.add_recipe(r3)
    b1.add_recipe(r4)
    b1.add_recipe(r5)
    print('Testing get_recipe_by_name:')
    b1.get_recipe_by_name('Sandwich')
    print('\nTesting get_recipes_by_types:')
    print(b1.get_recipes_by_types('dessert'))

    print('\nError testing:')
    r6 = Recipe('Constructor test', 2, 60, 6667, 'A random cake', 'dessert')
    r7 = 'This a string not a recipe'
    b1.add_recipe(r7)
    b1.get_recipes_by_types('Type that does not exist')
    b1.get_recipe_by_name('Recipe that does not exist')

    del b1, r1, r2, r3, r4, r5


if __name__ == '__main__':
    main()
