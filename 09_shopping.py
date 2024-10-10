#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

sweets = {}

for shop, products in shops.items():
    for product in products:
        name = product['name']
        price = product['price']

        if name not in sweets:
            sweets[name] = []

        sweets[name].append({shop: {'название магазина': shop, 'price': price}})

final_sweets = {}
for sweet, shop_list in sweets.items():
    final_sweets[sweet] = []
    for shop in shop_list:
        shop_name = list(shop.keys())[0]
        price = shop[shop_name]['price']
        final_sweets[sweet].append({shop_name: 'название магазина', 'price': price})

min_price_sweets = {}
for sweet, shops_list in final_sweets.items():
    sorted_shops = sorted(shops_list, key=lambda x: x['price'])
    min_price_sweets[sweet] = sorted_shops[:2]

print(min_price_sweets)