import random

#GRID
grid = random.randrange(0, 230, 1)
generations = 200
#cells
cells = random.randrange(grid, int((grid*grid)/3), 1)


fp = open('Cases\input06.txt' , "w")
fp.write(str(grid)+" #Width Height\n")
fp.write(str(generations)+" #Generations\n")
for i in range(cells):
    x = random.randrange(0, grid-1, 1)
    y = random.randrange(0, grid-1, 1)
    fp.write(str(x) +" "+str(y)+"\n")
