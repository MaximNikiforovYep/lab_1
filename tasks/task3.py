#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

comma_indexes = [-1]
for i in range(len(my_favorite_movies)):
    if my_favorite_movies[i] == ',':
        comma_indexes.append(i)

comma_indexes.append(len(my_favorite_movies))

first_movie = my_favorite_movies[comma_indexes[0]+1:comma_indexes[1]].strip()
last_movie = my_favorite_movies[comma_indexes[-2]+1:comma_indexes[-1]].strip()
second_movie = my_favorite_movies[comma_indexes[1]+1:comma_indexes[2]].strip()
second_to_last_movie = my_favorite_movies[comma_indexes[-3]+1:comma_indexes[-2]].strip()

print("Первый фильм:", first_movie)
print("Последний фильм:", last_movie)
print("Второй фильм:", second_movie)
print("Второй с конца фильм:", second_to_last_movie)