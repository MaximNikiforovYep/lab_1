#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
#my_family = []


# список списков приблизителного роста членов вашей семьи
#my_family_height = [
    # ['имя', рост],
#    [],
#]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

def get_family_member_height(my_family, member):
    flag = False
    family_member_height = -1
    for family_member in my_family:
        if family_member[0] == member:
            flag = True
            family_member_height = family_member[1]
    if flag:
        return family_member_height
    else:
        return "Error"


def get_total_height(my_family):
    total = 0
    for family_member in my_family:
        total += family_member[1]
    return total


#my_family = ['мама', 'папа', 'бабушка']

#my_family_height = [
#    ['мама', 165],
#    ['папа', 180],
#    ['бабушка', 155],
#]

#print("Рост отца - " + str(my_family_height[1][1]) + "см")

#total_height = 0

#for member in my_family_height:
#    total_height += member[1]

#print("Общий рост семьи:", total_height)