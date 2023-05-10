
from pprint import pprint

with open('file.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dishnes = line.strip()
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
        cook_book[dishnes] = ingredients

    pprint(cook_book, sort_dicts=False)

print()
print()
def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        recipe = cook_book[dish]
        for ingridient in recipe:
            key = ingridient['ingredient_name']
            if key not in result:
                new_dict = {
                    'measure' : ingridient['measure'],
                    'quantity' : int(ingridient['quantity']) * person_count

                }
                result[key] = new_dict
            else:
                result[key]['quantity'] += int(ingridient['quantity']) * person_count

    pprint(result, sort_dicts=False)

get_shop_list_by_dishes(['Запеченный картофель', 'Утка по-пекински', 'Фахитос'], 2)
    




