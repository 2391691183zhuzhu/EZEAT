from flask import Flask, render_template, jsonify, request
from features.recipes import RECIPES, get_ingredients
from data.products import PRODUCTS

app = Flask(__name__)

@app.route('/')
def home():
    promos = [p for p in PRODUCTS if p["promo_price"]]
    return render_template('index.html', promos=promos)

@app.route('/recipes/<product_name>')
def recipes(product_name):
    result = []
    for en_name, data in RECIPES.items():
        if product_name in data["ingredients"]:
            result.append({"en": en_name, "nl": data["nl"]})
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
                details.append({"name": name, "price": price})
    return jsonify({"ingredients": details, "total": round(total, 2)})

if __name__ == '__main__':
    app.run(debug=True)
