#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

def find_total_play_time_of_songs_list(songs, songs_to_calc):
    total_duration = 0
    for song in songs:
        if song[0] in songs_to_calc:
            total_duration += song[1]
    return total_duration


def find_total_play_time_of_songs_dict(songs, songs_to_calc):
    total_duration = 0
    for song in songs_to_calc:
        total_duration += songs[song]
    return total_duration

# violator_songs_list = [
#     ['World in My Eyes', 4.86],
#     ['Sweetest Perfection', 4.43],
#     ['Personal Jesus', 4.56],
#     ['Halo', 4.9],
#     ['Waiting for the Night', 6.07],
#     ['Enjoy the Silence', 4.20],
#     ['Policy of Truth', 4.76],
#     ['Blue Dress', 4.29],
#     ['Clean', 5.83],
# ]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# time_halo = violator_songs_list[3][1]
# time_enjoy_the_silence = violator_songs_list[5][1]
# time_clean = violator_songs_list[8][1]
#
# total_time = time_halo + time_enjoy_the_silence + time_clean
# total_time_rounded = round(total_time, 2)
# print(f'Три песни звучат {total_time_rounded} минут')

# Есть словарь песен группы Depeche Mode
# violator_songs_dict = {
#     'World in My Eyes': 4.76,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.30,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.6,
#     'Policy of Truth': 4.88,
#     'Blue Dress': 4.18,
#     'Clean': 5.68,
# }

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# first_song = 'Sweetest Perfection'
# second_song = 'Policy of Truth'
# third_song = 'Blue Dress'
# time_sweetest_perfection = violator_songs_dict[first_song]
# time_policy_of_truth = violator_songs_dict[second_song]
# time_blue_dress = violator_songs_dict[third_song]
#
# total_time_dict = time_sweetest_perfection + time_policy_of_truth + time_blue_dress
#
# total_time_dict_rounded = round(total_time_dict, 2)
#
# print(f'А другие три песни звучат {total_time_dict_rounded} минут')