#!/usr/bin/python

import math
# We need to compare the amounts of each ingredient we have
# vs
# amount of each ingredient needed and
# increase the batch count by 1
# until incredients = 0

# recipe calls for 4 eggs, 5 cups of sugar
# we have 12 eggs, 14 cups of sugar
# recipe/stock = batches
# 12 eggs / 4 eggs = 3
# 14 cups of sugar / 5 cups of sugar = 2 with 4 cups left over NOTE: limiting ingredient
# the total batches you can make is = the ingredient with lowest number of batches


def recipe_batches(recipe, ingredients):

    max_batches = 0
    global limiting_ingredient
    limiting_ingredient = []

    for ingredient in recipe.keys():  # for milk in recipe
        # batches = amount_here/amount_needed
        batches = ingredients[ingredient]//recipe[ingredient]
        if batches <= 0:  # if amount i have is less than what is needed return 0
            return 0
        # update max batches after each iteration if batches < max_batches
        elif max_batches == 0 or batches < max_batches:
            max_batches = batches
            limiting_ingredient.append([ingredient])
    return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 1320, 'butter': 480, 'flour': 510}
    print("\n\033[93m{batches} batches\033[37m can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
print(
    "The limiting ingredient is: \033[31m" + str(limiting_ingredient[-1]) + "\n")
