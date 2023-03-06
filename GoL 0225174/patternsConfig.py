import numpy as np

#STIL LIFES
block = np.array([[0,  0,   0,   0],
                  [0, 255, 255,  0], 
                  [0, 255, 255,  0], 
                  [0,  0,   0,   0]])

beehive = np.array([[0,  0,  0,  0,  0,   0],
                    [0, 255, 0,  0, 255,  0],
                    [0,  0, 255, 0, 255,  0],
                    [0,  0,  0, 255, 0,   0],
                    [0,  0,  0,  0,  0,   0]])

loaf = np.array([[0,  0,  0,   0,  0,   0],
                 [0,  0, 255, 255, 0,   0],
                 [0, 255, 0,   0, 255,  0],
                 [0,  0, 255,  0, 255,  0],
                 [0,  0,  0,  255, 0,   0],
                 [0,  0,  0,   0,  0,   0]])


boat = np.array([[0,  0,   0,  0,  0],
                 [0, 255, 255, 0,  0], 
                 [0, 255,  0, 255, 0], 
                 [0,  0,  255, 0,  0],
                 [0,  0,   0,  0,  0]])

tub = np.array([[0,  0,  0,  0,  0],
                [0,  0, 255, 0,  0], 
                [0, 255, 0, 255, 0], 
                [0,  0, 255, 0,  0],
                [0,  0,  0,  0,  0]])


#OSCILATORS 
            #Blinker
blinker1 = np.array([[0,  0,  0],
                     [0, 255, 0], 
                     [0, 255, 0], 
                     [0, 255, 0],
                     [0,  0,  0]])
        
blinker2 = np.array([[0,  0,   0,   0,  0],
                     [0, 255, 255, 255, 0],
                     [0,  0,    0,  0,  0]])

            #Toad
toad1 = np.array([[0,  0,  0,  0,  0,   0],
                  [0,  0,  0, 255, 0,   0],
                  [0, 255, 0,  0, 255,  0],
                  [0, 255, 0,  0, 255,  0],
                  [0,  0, 255, 0,  0,   0],
                  [0,  0,  0,  0,  0,   0]])
        
toad2 = np.array([[0,  0,   0,   0,   0,   0],
                  [0,  0,  255, 255, 255,  0],
                  [0, 255, 255, 255,  0,   0],
                  [0,  0,   0,   0,   0,   0]])
        
            #Beacon
beacon1 = np.array([[0,  0,   0,  0,   0,   0],
                    [0, 255, 255, 0,   0,   0],
                    [0, 255, 255, 0,   0,   0],
                    [0,  0,   0, 255, 255,  0],
                    [0,  0,   0, 255, 255,  0],
                    [0,  0,   0,  0,   0,   0]])

beacon2 = np.array([[0,  0,   0,  0,   0,   0],
                    [0, 255, 255, 0,   0,   0],
                    [0, 255,  0,  0,   0,   0],
                    [0,  0,   0,  0,  255,  0],
                    [0,  0,   0, 255, 255,  0],
                    [0,  0,   0,  0,   0,   0]])


#SPACESHIPS
            #Glider
glider1 = np.array([[0,  0,   0,   0,  0],
                    [0,  0,  255,  0,  0], 
                    [0,  0,   0,  255, 0], 
                    [0, 255, 255, 255, 0],
                    [0,  0,   0,   0,  0]])

glider2 = np.array([[0,  0,  0,   0,  0],
                    [0, 255, 0,  255, 0], 
                    [0,  0, 255, 255, 0], 
                    [0,  0, 255,  0,  0],
                    [0,  0,  0,   0,  0]])
        
glider3 = np.array([[0,  0,  0,   0,  0],
                    [0,  0,  0,  255, 0], 
                    [0, 255, 0,  255, 0], 
                    [0,  0, 255, 255, 0],
                    [0,  0,  0,   0,  0]])
        
glider4 = np.array([[0,  0,   0,   0,  0],
                    [0, 255,  0,   0,  0], 
                    [0,  0,  255, 255, 0], 
                    [0, 255, 255,  0,  0],
                    [0,  0,   0,   0,  0]])

    #LIGHT-WEIGHT SPACESHIP
l_ws1 = np.array([[0,  0,  0,   0,   0,   0,   0],
                  [0, 255, 0,   0,  255,  0,   0], 
                  [0,  0,  0,   0,   0,  255,  0], 
                  [0, 255, 0,   0,   0,  255,  0],
                  [0,  0, 255, 255, 255, 255,  0],
                  [0,  0,  0,   0,   0,   0,   0]])
        
l_ws2 = np.array([[0,  0,   0,   0,   0,   0,   0],
                  [0,  0,   0,  255, 255,  0,   0], 
                  [0, 255, 255,  0,  255, 255,  0], 
                  [0, 255, 255, 255, 255,  0,   0],
                  [0,  0,  255, 255,  0,   0,   0],
                  [0,  0,   0,   0,   0,   0,   0]])
        
l_ws3 = np.array([[0,  0,  0,   0,   0,   0,   0],
                  [0,  0, 255, 255, 255, 255,  0], 
                  [0, 255, 0,   0,   0,  255,  0], 
                  [0,  0,  0,   0,   0,  255,  0],
                  [0, 255, 0,   0,  255,  0,   0],
                  [0,  0,  0,   0,   0,   0,   0]])
        
l_ws4 = np.array([[0,  0,   0,   0,   0,   0,   0],
                  [0,  0,  255, 255,  0,   0,   0], 
                  [0, 255, 255, 255, 255,  0,   0], 
                  [0, 255, 255,  0,  255, 255,  0],
                  [0,  0,   0,  255, 255,  0,   0],
                  [0,  0,   0,   0,   0,   0,   0]])