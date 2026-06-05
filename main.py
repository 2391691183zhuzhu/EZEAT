from features.promotions import show_promotions
from features.recipes import suggest_recipes, get_ingredients
from features.cart import add_to_cart, show_cart

# 1. 显示促销
show_promotions()

# 2. 推荐菜谱
suggest_recipes("Tomaten")

# 3. 自动添加食材到购物车
print("\n=== 自动添加 'Ei met tomaat' 所需食材 ===")
ingredients = get_ingredients("Ei met tomaat")
for item in ingredients:
    add_to_cart(item)

# 4. 显示购物车和总价
show_cart()
