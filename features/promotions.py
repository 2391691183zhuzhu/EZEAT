from data.products import PRODUCTS

def show_promotions(category=None):
    print("=== 本周促销 ===")
    for p in PRODUCTS:
        if p["promo_price"]:
            if category is None or p["category"] == category:
                besparing = p["price"] - p["promo_price"]
                print(f"[{p['supermarket']}] {p['name']}: €{p['price']} → €{p['promo_price']} (bespaar €{besparing:.2f})")
