#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Cell:
    def __init__(self, alive):
        if alive == 1 or alive == "1" or alive == "1":
            self.alive = True
        else:
            self.alive = False
        self.num_neighbours = 0

