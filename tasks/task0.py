#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distance = {}


def find_distance(cities):
    distances = {}
    for city1, (x1, y1) in cities.items():
        distances[city1] = {}
        for city2, (x2, y2) in cities.items():
            if city1 != city2:
                distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                distances[city1][city2] = distance
    return distances


#print(find_distance(sites))
