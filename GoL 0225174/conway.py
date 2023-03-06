"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from datetime import datetime
from tabulate import tabulate       #pip install tabulate

#Impot class and other sources
from patternsConfig import *

#Calss conway is all operations for the GoL
class Conway:
    def __init__(self, fileName, args):
        self.fileName = fileName
        self.args = args
        self.cells_allive = list()
        self.actual_gen = 0
        self.out = outputFile 

        #Counters
        self.totalCounter = 0
        self.blockCounter = 0
        self.beehiveCounter = 0
        self.loafCounter = 0
        self.boatCounter = 0
        self.tubCounter = 0
        self.blinkCounter = 0
        self.toadCounter = 0
        self.beaconCounter = 0
        self.gliderCounter = 0
        self.spaceshipCounter = 0
        

    # Configurates values from file as reader
    def readData(self):
        with open(self.fileName) as file:
            if (self.args):
                self.N = int(self.args[0])

                file.readline().split()
            else:
                s = file.readline().split()
                #Read widht
                self.N = int(s[0])

            #First lines for the output
            fp.write(f"Simulation at {date}\n")
            fp.write(f"Universe size {self.N} x {self.N}\n\n")

            self.grid = np.zeros(self.N * self.N, dtype=np.int32).reshape(self.N, self.N)

            #Set custom generations or default generations
            self.gens = int(file.readline()[0:3])
            print("HOW MANY GENERATIONS DO YOU WANT TO RUN? (If you set 0, default is 200)")
            generations = int(input())
            if generations>0:
                self.gens = generations

            #Get and Set coordinates for the grid  
            for line in file:
                s = line.split()
                i, j = int(s[0]), int(s[1])
                self.grid[i, j] = ON
    
    """
    RULES
    • Any live cell with two or three neighbors survives.
    • Any dead cell with three live neighbors becomes a live cell.
    • All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    """
    def rules(self):
        if (self.actual_gen < self.gens):
            self.actual_gen += 1
            print(f'Generation #{self.actual_gen}')
            gen=str(self.actual_gen)
            plt.title("Generation:"+gen)
            new_grid = self.grid.copy()
            
            for i in range(self.N):
                for j in range(self.N):
                    ns = neighbourSum(i, j, self.grid, self.N)
                    if (self.grid[i, j] == 0):
                        if (ns == 3):
                            new_grid[i, j] = 255
                    else:
                        if (ns < 2 or ns > 3):
                            new_grid[i, j] = 0
            
            self.counters()

            self.write_to_file()
            
            self.grid[:] = new_grid[:]


    #Counter each Blocks, Beehives, Loafs, Boats, Tubs, Blinkers, Toads, Beacons, Gliders and Light-weight spaceships on the grid
    def counters(self):
        for i in range(self.N):
            for j in range(self.N):
                #Use a equal_nan operation for ocmpare 2 np arrays.
                #STILL LIFES
                #BLOCK
                if(np.array_equal(self.grid[i:i+4, j:j+4] , block, equal_nan=True) ):
                    self.blockCounter+=1
                    self.totalCounter+=1
                    
                #BEEHIVE
                if(np.array_equal(self.grid[i:i+5, j:j+6] , beehive, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+5] , np.rot90(beehive), equal_nan=True)):
                    self.beehiveCounter+=1
                    self.totalCounter+=1
                    
                #LOAF
                if(np.array_equal(self.grid[i:i+6, j:j+6] , loaf, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(loaf), equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(loaf, 2), equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(loaf, 3), equal_nan=True)):
                    self.loafCounter+=1
                    self.totalCounter+=1
                    
                #BOAT
                if(np.array_equal(self.grid[i:i+5, j:j+5] , boat, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(boat), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(boat, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(boat, 3), equal_nan=True)):
                    self.boatCounter+=1
                    self.totalCounter+=1
                    
                #TUB
                if(np.array_equal(self.grid[i:i+5, j:j+5] , tub, equal_nan=True) ):
                    self.tubCounter+=1
                    self.totalCounter+=1
                    
                #OSCILATORS
                #BLINKER
                if(np.array_equal(self.grid[i:i+5, j:j+3] , blinker1, equal_nan=True) or np.array_equal(self.grid[i:i+3, j:j+5] , blinker2, equal_nan=True)):
                    self.blinkCounter+=1
                    self.totalCounter+=1
                
                #TOAD
                if(np.array_equal(self.grid[i:i+6, j:j+6] , toad1, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(toad1), equal_nan=True)):
                    self.toadCounter+=1
                    self.totalCounter+=1
                    
                if(np.array_equal(self.grid[i:i+4, j:j+6] , toad2, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+4] , np.rot90(toad2), equal_nan=True)):
                    self.toadCounter+=1
                    self.totalCounter+=1
                
                #BEACON
                if(np.array_equal(self.grid[i:i+6, j:j+6] , beacon1, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(beacon1), equal_nan=True)):
                    self.beaconCounter+=1
                    self.totalCounter+=1
                    
                if(np.array_equal(self.grid[i:i+6, j:j+6] , beacon2, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(beacon2), equal_nan=True)):
                    self.beaconCounter+=1
                    self.totalCounter+=1
                    

                #SPACESHIPS
                #GLIDERS
                if(np.array_equal(self.grid[i:i+5, j:j+5] , glider1, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider1), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider1, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider1, 3), equal_nan=True)):
                    self.gliderCounter+=1
                    self.totalCounter+=1
                    
                if(np.array_equal(self.grid[i:i+5, j:j+5] , glider2, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider2, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider2, 3), equal_nan=True)):
                    self.gliderCounter+=1
                    self.totalCounter+=1
                    
                if(np.array_equal(self.grid[i:i+5, j:j+5] , glider3, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider3), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider3, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider3, 3), equal_nan=True)):
                    self.gliderCounter+=1
                    self.totalCounter+=1
                    
                if(np.array_equal(self.grid[i:i+5, j:j+5] , glider4, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider4), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider4, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider4, 3), equal_nan=True)):
                    self.gliderCounter+=1
                    self.totalCounter+=1
                    
                #LIGHT WEIGHT SPACESHIPS
                if(np.array_equal(self.grid[i:i+6, j:j+7] , l_ws1, equal_nan=True) or np.array_equal(self.grid[i:i+7, j:j+6] , np.rot90(l_ws1), equal_nan=True) or np.array_equal( self.grid[i:i+6, j:j+7] , np.rot90(l_ws1, 2), equal_nan=True) or np.array_equal( self.grid[i:i+7, j:j+6] , np.rot90(l_ws1, 3), equal_nan=True)):
                    self.spaceshipCounter +=1
                    self.totalCounter+=1
                    
                if(np.array_equal(self.grid[i:i+6, j:j+7] , l_ws2, equal_nan=True) or np.array_equal(self.grid[i:i+7, j:j+6] , np.rot90(l_ws2), equal_nan=True) or np.array_equal( self.grid[i:i+6, j:j+7] , np.rot90(l_ws2, 2), equal_nan=True) or np.array_equal( self.grid[i:i+7, j:j+6] , np.rot90(l_ws2, 3), equal_nan=True)):
                    self.spaceshipCounter +=1
                    self.totalCounter+=1
                    
                if(np.array_equal(self.grid[i:i+6, j:j+7] , l_ws3, equal_nan=True) or np.array_equal(self.grid[i:i+7, j:j+6] , np.rot90(l_ws3), equal_nan=True) or np.array_equal( self.grid[i:i+6, j:j+7] , np.rot90(l_ws3, 2), equal_nan=True) or np.array_equal( self.grid[i:i+7, j:j+6] , np.rot90(l_ws3, 3), equal_nan=True)):
                    self.spaceshipCounter +=1
                    self.totalCounter+=1
                    
                if(np.array_equal(self.grid[i:i+6, j:j+7] , l_ws4, equal_nan=True) or np.array_equal(self.grid[i:i+7, j:j+6] , np.rot90(l_ws4), equal_nan=True) or np.array_equal( self.grid[i:i+6, j:j+7] , np.rot90(l_ws4, 2), equal_nan=True) or np.array_equal( self.grid[i:i+7, j:j+6] , np.rot90(l_ws4, 3), equal_nan=True)):
                    self.spaceshipCounter +=1
                    self.totalCounter+=1
                    

    #Tabulate data
    def write_to_file(self):
        fp.write(f'Iteration: {self.actual_gen}\n')
        if(self.totalCounter!=0):
            fp.write(tabulate([['Block', self.blockCounter, self.blockCounter*100/self.totalCounter], ['Beehive', self.beehiveCounter, self.beehiveCounter*100/self.totalCounter], ['Loaf', self.loafCounter, self.loafCounter*100/self.totalCounter], ['Boat', self.boatCounter, self.boatCounter*100/self.totalCounter], ['Tub', self.tubCounter, self.tubCounter*100/self.totalCounter], ['Blinker', self.blinkCounter, self.blinkCounter*100/self.totalCounter], ['Toad', self.toadCounter, self.toadCounter*100/self.totalCounter], ['Beacon', self.beaconCounter, self.beaconCounter*100/self.totalCounter], ['Glider', self.gliderCounter, self.gliderCounter*100/self.totalCounter], ['L-G spaceship', self.spaceshipCounter, self.spaceshipCounter*100/self.totalCounter], ['TOTAL',self.totalCounter]], headers=[' ','Count', 'Percent'], tablefmt="outline"))
        else:
            fp.write(tabulate([['Block', self.blockCounter, 0], ['Beehive', self.beehiveCounter, 0], ['Loaf', self.loafCounter, 0], ['Boat', self.boatCounter, 0], ['Tub', self.tubCounter, 0], ['Blinker', self.blinkCounter, 0], ['Toad', self.toadCounter, 0], ['Beacon', self.beaconCounter, 0], ['Glider', self.gliderCounter, 0], ['L-G spaceship', self.spaceshipCounter, 0], ['TOTAL',0]], headers=[' ','Count', 'Percent'], tablefmt='orgtbl'))
        fp.write('\n\n')


ON = 255
OFF = 0
vals = [ON, OFF]


print("SELECT THE ID FOR THE CASE TO GAME (2 DIGITS):")
id = input()
if len(id)<2:
    id = "0"+id
#relative url for the txt HERE CHANGES DE NAME FILE
inputFile = 'Cases\input'+id+'.txt' 
outputFile = 'Results\output'+id+'.txt'
date = datetime.today().strftime('%Y-%m-%d, %H:%M:%S')


#Check neigbours and sum their values, returns 0 or 1
def neighbourSum(i, j, grid, N):
    total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + #horizontal
                 grid[(i-1)%N, j] + grid[(i+1)%N, j] + #vertical
                 grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + #corners up
                 grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/ON) #corners down
    return total


def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)


def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255], 
                       [255,  0, 255], 
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider


def update(frameNum, img, cw):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    cw.rules()
    newGrid = cw.grid.copy()
    # TODO: Implement the rules of Conway's Game of Life

    # update data
    img.set_data(newGrid)
    cw.grid[:] = newGrid[:]
    return img,


# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
 
    args_buff = None
    if(len(sys.argv) > 1):
        args_buff = sys.argv[1:]

    cw = Conway(inputFile, args_buff)
    global fp
    fp = open(cw.out, "w")
    cw.readData()

    # set animation update interval
    updateInterval = 50
    # declare grid
    #grid = np.array([])
    # populate grid with random on/off - more off than on
    #grid = randomGrid(N)
    # Uncomment lines to see the "glider" demo
    #grid = np.zeros(N*N).reshape(N, N)
    #addGlider(1, 1, grid)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(cw.grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, cw),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)
    
    plt.title("Game of Life - 0225174")
    plt.show()
    fp.close()


# call main
if __name__ == '__main__':
    main()


#REFERENCES
#https://www.w3schools.com/python/numpy/default.asp
#https://www.w3schools.com/python/matplotlib_intro.asp
#https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
#https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html
#https://www.programiz.com/python-programming/datetime/strftime
#https://pypi.org/project/tabulate/
