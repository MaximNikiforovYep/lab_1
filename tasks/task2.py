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



def generate_expressions(numbers, ops):
    if len(numbers) == 1:
        yield str(numbers[0])
    else:
        for i in range(1, len(numbers)):
            left_numbers = numbers[:i]
            right_numbers = numbers[i:]
            for left_expr in generate_expressions(left_numbers, ops):
                for right_expr in generate_expressions(right_numbers, ops):
                    for op in ops:
                        yield f"({left_expr} {op} {right_expr})"


def find_expression(numbers, target):
    operators = ['+', '-', '*']

    for expr in generate_expressions(numbers, operators):
        try:
            if eval(expr) == target:
                return expr
        except Exception:
            continue
    return None


def exp_find_main(numbers, target):
    # Получаем числа и цель от пользователя


    # Ищем выражение, которое дает целевой результат
    result = find_expression(numbers, target)

    if result:
        print(f"Результат: {result} = {target}")
    else:
        print("Невозможно получить заданное число с помощью указанных операций.")

