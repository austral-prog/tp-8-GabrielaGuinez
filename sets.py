from sets_categories_data import (ALCOHOLS)

def clean_ingredients(dish_name, dish_ingredients):
    dish_ingredients_set = set(dish_ingredients)
    final_dish = dish_name, dish_ingredients_set
    return final_dish
print(clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro']))


def check_drinks(drink_name, drink_ingredients):
    for alcohol in ALCOHOLS:
        if alcohol in drink_ingredients:
            return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"
print(check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber']))
