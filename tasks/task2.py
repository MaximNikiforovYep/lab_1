#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Расставьте знаки операций "плюс", "минус", "умножение" и скобки
# между числами "1 2 3 4 5" так, что бы получилось число "25".
#
# Использовать нужно только указанные знаки операций, но не обязательно все перечесленные.
# Порядок чисел нужно сохранить.

# Пример для чисел "1 2 3" и "9"
# result = (1 + 2) * 3
# print(result)

# TODO написать формулу для 1 2 3 4 5 и вывести значение на консоль
numbers = [1, 2, 3, 4, 5]
target = 25

operators = ['+', '-', '*']


def calculate_expression(numbers, ops):
    if ops[0] == '+':
        result = numbers[0] + numbers[1]
    elif ops[0] == '-':
        result = numbers[0] - numbers[1]
    elif ops[0] == '*':
        result = numbers[0] * numbers[1]

    if ops[1] == '+':
        result += numbers[2]
    elif ops[1] == '-':
        result -= numbers[2]
    elif ops[1] == '*':
        result *= numbers[2]

    if ops[2] == '+':
        result += numbers[3]
    elif ops[2] == '-':
        result -= numbers[3]
    elif ops[2] == '*':
        result *= numbers[3]

    if ops[3] == '+':
        result += numbers[4]
    elif ops[3] == '-':
        result -= numbers[4]
    elif ops[3] == '*':
        result *= numbers[4]

    expression = f"{numbers[0]} {ops[0]} {numbers[1]} {ops[1]} {numbers[2]} {ops[2]} {numbers[3]} {ops[3]} {numbers[4]}"

    return result, expression


found = False
for op1 in operators:
    for op2 in operators:
        for op3 in operators:
            for op4 in operators:
                ops = [op1, op2, op3, op4]
                result, expression = calculate_expression(numbers, ops)
                if result == target:
                    print(f"{expression} = {target}")
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        break

if not found:
    print("Решение не найдено.")