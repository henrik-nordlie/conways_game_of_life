#!/usr/bin/env python


import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from map import Map
import time
import matplotlib.pyplot as plt

class Simulation:
    def __init__(self):
        """
        self.map_list = [0,0,0,0,0,
                         0,0,0,0,0,
                         0,1,1,1,0,
                         0,0,0,0,0,
                         0,0,0,0,0]
        """
        #Repeating pattern example
        self.map_list= "0000000000000000000000000000000000000011100011100000000000000000000000100001010000100001000010100001000010000101000010000001110001110000000000000000000000000111000111000000100001010000100001000010100001000010000101000010000000000000000000000011100011100000000000000000000000000000000000000"

        self.map = Map(self.map_list)
        
    def update_sim(self):
        self.map.update()
        plt.clf()  # Clear the previous plot
        plt.imshow(self.map.plot_map, cmap='binary')
        plt.show(block=False)
        plt.pause(0.5)
        
def main():
    sim = Simulation()
    for i in range(100):
        sim.update_sim() 
        
if __name__ == "__main__":
    main()
