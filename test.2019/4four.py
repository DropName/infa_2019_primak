def shoplist(products, money=0):
    """
    shows you what is possible 'products' to buy for your 'money'
    """
    cart = []
    for key in products:
        if products[key] < money:
            cart.append(key)
    return cart


print(shoplist({'banana': 10, 'apple': 5, 'steak': 100}, 50))
