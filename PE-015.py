# ProjectEuler 15

''''
Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

from itertools import permutations

grid_size_x = 20
grid_size_y = 20

steps = list('x'*grid_size_x + 'y'*grid_size_y)

p = list(permutations(steps))