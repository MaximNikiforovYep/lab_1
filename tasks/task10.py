#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def find_cost_for_goods(goods, store):
    for item, code in goods.items():
        total_quantity = 0
        total_cost = 0

        if code in store:
            for stock in store[code]:
                quantity = stock['quantity']
                price = stock['price']
                total_quantity += quantity
                total_cost += quantity * price

        print(f"{item} - {total_quantity} шт, стоимость {total_cost} руб")