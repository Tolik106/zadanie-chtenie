
from pprint import pprint

with open('file.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        quantities = int(file.readline())
        ingredients = []
        for ingridient in range(quantities):
            ingr = file.readline()
            ingredient_name, quantity, measure = ingr.strip().split(' | ')
            book = {
                'ingredient_name': ingredient_name,
                "quantity": quantity,
                'measure': measure,

                }
            
            ingredients.append(book)

        file.readline()
        cook_book[dish] = ingredients

    pprint(cook_book, sort_dicts=False)
