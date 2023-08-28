#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cell import Cell
import numpy as np

class Map:
    def __init__(self, map_string):
        self.make_map(map_string)

    def make_map(self, map_string):
        self.map_size = int(np.sqrt(len(map_string)))
        self.map = np.empty((self.map_size, self.map_size), dtype=object)
        for i in range(self.map_size):
            for j in range(self.map_size):
                self.map[i, j] = Cell(map_string[i * self.map_size + j])
        self.plot_map = np.zeros((self.map_size, self.map_size),dtype=int)



    def count_neighbours(self, cell):
        neighbours = [[cell[0]-1, cell[1]],
                      [cell[0]+1, cell[1]],
                      [cell[0], cell[1]-1],
                      [cell[0], cell[1]+1],
                      [cell[0]-1, cell[1]-1],
                      [cell[0]-1, cell[1]+1],
                      [cell[0]+1, cell[1]-1],
                      [cell[0]+1, cell[1]+1]]

        valid_neighbours = []
        for neighbour in neighbours:
            if 0 <= neighbour[0] < self.map_size and 0 <= neighbour[1] < self.map_size:
                valid_neighbours.append(neighbour)
        neighbours = valid_neighbours
        for neighbour in neighbours:
            if self.map[neighbour[0], neighbour[1]].alive:
                self.map[cell[0], cell[1]].num_neighbours +=1

    
    def update(self):
        self.plot_map = np.zeros((self.map_size, self.map_size),dtype=int)
        for col in range(self.map_size): 
            for row in range(self.map_size): 
                self.map[col,row].num_neighbours = 0
                self.count_neighbours([col,row])
        for col in range(self.map_size): 
            for row in range(self.map_size): 
                if self.map[col,row].alive:
                    if self.map[col,row].num_neighbours < 2:
                        self.map[col,row].alive = False
                    elif self.map[col,row].num_neighbours > 3:
                        self.map[col,row].alive = False
                    else:
                        self.map[col,row].alive = True 
                    self.plot_map[col,row] = 1
                else:
                    if self.map[col,row].num_neighbours == 3:
                        self.map[col,row].alive = True

                    











