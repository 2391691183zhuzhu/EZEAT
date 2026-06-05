RECIPES = {
    "Tomato soup": {
        "nl": "Tomaten soep",
        "ingredients": ["Tomaten", "Uien"]
    },
    "Spaghetti bolognese": {
        "nl": "Spaghetti bolognese",
        "ingredients": ["Spaghetti", "Gehakt 500g", "Tomaten", "Uien"]
    },
    "Egg with tomato": {
        "nl": "Ei met tomaat",
        "ingredients": ["Eieren 12 stuks", "Tomaten"]
    },
    "Chicken curry": {
        "nl": "Kip curry",
        "ingredients": ["Kipfilet 500g", "Uien"]
    },
}

def suggest_recipes(product_name):
    found = False
    for recipe, data in RECIPES.items():
        if product_name in data["ingredients"]:
            found = True
    return found

def get_ingredients(recipe_name):
    for recipe, data in RECIPES.items():
        if recipe == recipe_name or data["nl"] == recipe_name:
            return data["ingredients"]
    return []
