from flask import Flask, render_template, jsonify
from features.recipes import RECIPES, get_ingredients
from data.products import PRODUCTS

app = Flask(__name__)

PRODUCT_NAMES = {
    "Tomaten":        {"en": "Tomatoes",      "zh": "西红柿"},
    "Eieren 12 stuks":{"en": "Eggs (12)",     "zh": "鸡蛋12个"},
    "Kipfilet 500g":  {"en": "Chicken 500g",  "zh": "鸡胸肉500g"},
    "Spaghetti":      {"en": "Spaghetti",     "zh": "意大利面"},
    "Kaas 500g":      {"en": "Cheese 500g",   "zh": "奶酪500g"},
    "Uien":           {"en": "Onions",        "zh": "洋葱"},
    "Gehakt 500g":    {"en": "Minced meat 500g", "zh": "碎肉500g"},
}

@app.route('/')
def home():
    promos = [p for p in PRODUCTS if p["promo_price"]]
    return render_template('index.html', promos=promos, names=PRODUCT_NAMES)

@app.route('/recipes/<product_name>')
def recipes(product_name):
    result = []
    for en_name, data in RECIPES.items():
        if product_name in data["ingredients"]:
            result.append({"en": en_name, "nl": data["nl"], "zh": data["zh"]})
    return jsonify(result)

@app.route('/ingredients/<recipe_name>')
def ingredients(recipe_name):
    items = get_ingredients(recipe_name)
    total = 0
    details = []
    for name in items:
        for p in PRODUCTS:
            if p["name"] == name:
                price = p["promo_price"] if p["promo_price"] else p["price"]
                total += price
                details.append({
                    "name": name,
                    "en": PRODUCT_NAMES.get(name, {}).get("en", name),
                    "zh": PRODUCT_NAMES.get(name, {}).get("zh", name),
                    "price": price
                })
    return jsonify({"ingredients": details, "total": round(total, 2)})

if __name__ == '__main__':
    app.run(debug=True)
