from data.products import PRODUCTS

cart = []

def add_to_cart(product_name):
    for p in PRODUCTS:
        if p["name"] == product_name:
            cart.append(p)
            price = p["promo_price"] if p["promo_price"] else p["price"]
            print(f"✓ {p['name']} toegevoegd (€{price:.2f})")
            return
    print(f"Product niet gevonden: {product_name}")

def show_cart():
    print("\n=== Winkelwagen ===")
    total = 0
    for p in cart:
        price = p["promo_price"] if p["promo_price"] else p["price"]
        total += price
        print(f"  {p['name']}: €{price:.2f}")
    print(f"Totaal: €{total:.2f}")
