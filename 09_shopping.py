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

# Итерируем по каждому магазину
for shop, products in shops.items():
    # Итерируем по каждому продукту в магазине
    for product in products:
        name = product['name']  # Название товара
        price = product['price']  # Цена товара

        # Если товар еще не добавлен в sweets, инициализируем его
        if name not in sweets:
            sweets[name] = []

        # Добавляем информацию о магазине и цене в список товара
        sweets[name].append({shop: {'название магазина': shop, 'price': price}})

# Приводим к нужному формату
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