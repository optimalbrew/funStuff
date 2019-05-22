"""
Given a 2D n X m  matrix find the number of paths from top left to bottom right. 
If all routes are available, then we have [((n-1)+(m-1))!]/((n-1)!(m-1)!) paths. 

The interesting versions are those where some cells are blocking cells, say marked by *'s.
"""

# Idea: start from the end, i.e. row n and col m. Since that is the end, that cell is not blocked.
# * if we start from that cell, there is only 1 path till the end (to itself). 
# * If the top and left cells are open, then there is one path via each. 
# * each open corner (left,up) cell offers 2 ways to get to a cell. So accumulate those sums from corners
"""
Example:
input = [
        [0,0,0,*],
        [0,*,0,0],
        [0,0,0,0]
        ]
path accumulations: 3 paths: DDRRR,RRDDR, RRDRD 
input = [
        [3,2,2,*],
        [1,*,2,1],
        [1,1,1,1]
        ]
""" 

input = [
        [0,0,0,1],
        [0,1,0,0],
        [0,0,0,0]
        ]

#logic to fill a cell using corner neighbors (only if cell is not blocked)
def fillCell(input,r,c):
    if input[r][c] == 1: # the cell is blocked
        return 0
    n = len(input)
    m = len(input[0])
    if r<n-1 and c<m-1: #interior
        fill = input[r][c+1] + input[r+1][c]
    if r == n-1 and c == m-1: #bottom right corner ("starting" point for backward induction)
        fill = 1
    if r == n-1 and c < m-1:    #bottom row, not the right corner
        fill = input[r][c+1]
    if r < n-1 and c == m-1:    #right column, not the bottom corner
        fill = input[r+1][c]
    return fill

def numpaths(input):
    output = input    
    n = len(input)
    m = len(input[0])
    if n == 1: #just one row (including just one cell)
        if sum(input[0]) == 0:
            return 1 
        else:   #some cell is blocked 
            return 0
    if m == 1: #just one colum (including just one cell)
        if sum(input[1]) == 0:
            return 1
        else:   #some cell is blocked 
            return 0
    r = n-1
    while r >= 0: #for each row, starting from bottom
        c = m-1 #start from right column
        while c >= 0:
            output[r][c] = fillCell(input,r,c)
            c -= 1
        r -= 1
    return output

paths = numpaths(input)

for i in range(len(paths)):
    print(paths[i])