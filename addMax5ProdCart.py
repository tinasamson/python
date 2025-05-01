# This only works in python >= 3.6

ItemsInCart = 0
def add_to_cart(items_to_add):
    global ItemsInCart
    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")
    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")
    ItemsInCart += items_to_add
    print(f"{items_to_add} items added. ")
    print(f"Total in cart: {items_to_add}")
try:
    add_to_cart(2)
    add_to_cart(-1)
except Exception as e:
    print (e)