# Project Euler 11
#
# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

'''Answer = 70600674'''

input_grid = []
input_grid.append([8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8])
input_grid.append([49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,04,56,62,0])
input_grid.append([81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65])
input_grid.append([52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91])
input_grid.append([22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80])
input_grid.append([24,47,32,60,99,3,45,02,44,75,33,53,78,36,84,20,35,17,12,50])
input_grid.append([32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70])
input_grid.append([67,26,20,68,02,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21])
input_grid.append([24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72])
input_grid.append([21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95])
input_grid.append([78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92])
input_grid.append([16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57])
input_grid.append([86,56,0,48,35,71,89,07,5,44,44,37,44,60,21,58,51,54,17,58])
input_grid.append([19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,04,89,55,40])
input_grid.append([4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66])
input_grid.append([88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69])
input_grid.append([4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36])
input_grid.append([20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16])
input_grid.append([20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54])
input_grid.append([1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48])

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same 
# direction (up, down, left, right, or diagonally) in the 20×20 grid?
def bin_factor(input_list):
    f = 1
    for n in input_list:
        f = f*n
    return f

horz = 0
for y in range(0,20):
    for x in range(0,20-4):
        horz = max(bin_factor(input_grid[y][x:x+4]), horz)
print "Horizontal:", horz        
        
vert = 0
for x in range(0,20):
    for y in range(0,20-4):
        vert_list = []        
        for y_b in range(y,y+4): 
            vert_list.append(input_grid[y_b][x])
        vert = max(bin_factor(vert_list), vert)
print "Vertical:", vert

LU_diag = 0
for x in range(0,20):
    for y in range(0,20):
        diag_list = []
        x_b = x
        y_b = y        
        for i in range(-1,3):
            x_b -= 1
            y_b += 1
            if x_b>=0 and y_b>=0 and x_b<20 and y_b<20:
                diag_list.append(input_grid[y_b][x_b])
            if len(diag_list)==4:
                LU_diag = max(bin_factor(diag_list), LU_diag)
print "Left Up Diagonal:", LU_diag

LD_diag = 0
for x in range(0,20):
    for y in range(0,20):
        diag_list = []
        x_b = x
        y_b = y        
        for i in range(-1,3):
            x_b -= 1
            y_b -= 1
            if x_b>=0 and y_b>=0 and x_b<20 and y_b<20:
                diag_list.append(input_grid[y_b][x_b])
            if len(diag_list)==4:
                LD_diag = max(bin_factor(diag_list), LD_diag)
print "Left Down Diagonal:", LD_diag

RU_diag = 0
for x in range(0,20):
    for y in range(0,20):
        diag_list = []
        x_b = x
        y_b = y        
        for i in range(-1,3):
            x_b += 1
            y_b += 1
            if x_b>=0 and y_b>=0 and x_b<20 and y_b<20:
                diag_list.append(input_grid[y_b][x_b])
            if len(diag_list)==4:                
                RU_diag = max(bin_factor(diag_list), RU_diag)
print "Right Up Diagonal:", RU_diag

RD_diag = 0
for x in range(0,20):
    for y in range(0,20):
        diag_list = []
        x_b = x
        y_b = y        
        for i in range(-1,3):
            x_b += 1
            y_b -= 1
            if x_b>=0 and y_b>=0 and x_b<20 and y_b<20:
                diag_list.append(input_grid[y_b][x_b])
            if len(diag_list)==4:
                RD_diag = max(bin_factor(diag_list), RD_diag)
print "Right Down Diagonal:", RD_diag

print "Largest Product:", max(horz, vert, LU_diag, LD_diag, RD_diag, RU_diag)




