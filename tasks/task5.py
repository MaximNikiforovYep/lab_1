#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Zoo:
    def __init__(self, zoo):
        self.zoo = zoo

    def insert(self, poss, animal):
        self.zoo.insert(poss, animal)

    def extend(self, sub_zoo):
        self.zoo.extend(sub_zoo)

    def remove(self, animal):
        self.zoo.remove(animal)

    def find_pos(self, animal):
        return self.zoo.index(animal) + 1

    def print(self):
        print(self.zoo)


