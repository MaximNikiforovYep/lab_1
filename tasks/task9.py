#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_best_shops(shops):
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

    return min_price_sweets


