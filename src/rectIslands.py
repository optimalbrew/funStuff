"""
Given a 2D array with binary 0/1 elements, find all "islands of 0's" with rectangular shape
Single 0's are fine. Boundary (of array) can be treated as 1. Islands cannot "touch" each other
Even corner point touches are not allowed. This is my own interpretation and varies from source (Greg's example). 

input = [
        [1,1,1,1,0,1],
        [0,0,0,1,1,1],
        [0,0,0,1,1,1],
        [0,0,0,1,0,0],
        [1,1,1,1,0,0]
        ]
"""

#padding the input array with 1's on all sides, so the boundary is not treated any differently than points in the interior
def padInput(inputArray):   
    numRows = len(input)
    numCols = len(input[0])
    padRow = []
    i=0
    while i<=numCols+1: 
        padRow.append(1)
        i+=1
    paddedInput = []
    #pad top boundary
    paddedInput.append(padRow)
    #pad left and right boundaries
    i = 0
    while i<numRows:
        paddedInput.append([1]+input[i]+[1])
        i+=1    
    #pad bottom boundary
    paddedInput.append(padRow)
    return paddedInput


#visualizing the matrix (only for small input, upto 16 rows and cols)
def prettyInput(paddedInput):
    print('\n')
    if len(paddedInput)<=16 and len(paddedInput[1])<=16:
        for i in paddedInput:
            print(i)
    else:
        print('More than 16 rows or cols, skip printing')

# Find an initial 0 starting from some point (scan right moving down to next row as necessary)
def findInitZero(paddedInput, currRow, currCol):
    totRows = len(paddedInput)
    totCols = len(paddedInput[1])
    #make sure the starting point is within bounds
    if currCol == totCols or currRow == totRows:
        print(currCol,currRow,totCols,totRows)
        print('col index too large during recursive call')
        return [None,None]
    #Check if starting point is 0 (immediate match)
    if paddedInput[currRow][currCol] == 0: #immediate match
        return [currRow, currCol]
    else:
        #print('moving right')
        currCol+=1 #move right till we find a first 0.
        #print(currCol)
        if currCol >= totCols-1: #reached the end of row
            currRow += 1 #go to next row
            if currRow == totRows-1: #reached last row (all 1's)
                return [None,None]
            else:
                currCol = 1 #reset to col 0 (or to 1 because of padding)
                return findInitZero(paddedInput,currRow,currCol)
        else:
            #print(currCol)
            return findInitZero(paddedInput,currRow,currCol)

# From any 0 scan right for adjacent 0's
def scanRight(paddedInput, currTL):
    [currRow, currCol] = currTL
    totCols = len(paddedInput[1])
    while paddedInput[currRow][currCol] == 0 and currCol < totCols-1:
        currCol +=1 #this will update even the first time it fails, hence below 
    return [currRow,currCol-1] 

# * Then scan down for adjacent 0's
def scanDown(paddedInput, currTL):
    [currRow, currCol] = currTL
    totRows = len(paddedInput)
    while paddedInput[currRow][currCol] == 0 and currRow < totRows-1:
        currRow +=1 #this will update even the first time it fails, hence below 
    return [currRow-1,currCol] 

# * Test if island conditions are met
def isRect(arr, currRect): #top left is (0,0)
    if currRect == []:
        print('invalid current rect (None)')
        return False    
    row0,col0,row1,col1 = currRect[0][0],currRect[0][1],currRect[1][0],currRect[1][1]
    #check row above and below for any 0's (with extra offsets for corner points)
    i = col0-1
    while i <= col1+1:
        if arr[row0-1][i] == 0: #row above
            print('row above violation, check corner')
            return False
        elif arr[row1+1][i] == 0: #row below
            print('row below violation, check corner')
            return False
        i+=1    
    #check col on left and right for all 1's
    i = row0
    while i<=row1:
        if arr[i][col0-1] == 0: #col to left
            print('left col violation')
            return False
        elif arr[i][col1+1] == 0: #col to right
            print('right col violation')
            return False
        i+=1  
    #check for all 0's inside
    i,j = row0,col0
    while i<=row1 and j<=col1:
        if arr[i][j] == 1:
            print('non 0 interior element violation')
            return False
        i+=1
        j+=1   
    #things check out
    return True


#Main


input =  [
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 0]
        ]



paddedInput = padInput(input)

#check size
totRows = len(paddedInput)
totCols = len(paddedInput[1])

prettyInput(paddedInput)


# Start search from row2,col2 (that is topleft corner of orig array)
[currRow, currCol] = [1,1] #because of boundary padding (0,0) has moved to (1,1)
#initialize list of identified islands
rectList = []
while currRow <totRows and currCol <= totCols: #termination condition for searching islands
    #print('InitStart', [currRow, currCol])
    currTL = findInitZero(paddedInput, currRow, currCol) #current top left corner of potential rect
    #print('TL',currTL)
    if currTL == [None,None]:
        print('Reached end, current node is None')
        break
    currTR = scanRight(paddedInput, currTL)        #current top right
    currBL = scanDown(paddedInput, currTL) #current bottom left corner
    #Finally, the potential bottom right corner point
    currBR = []
    if paddedInput[currBL[0]][currTR[1]] == 0: #jump to the implied point first
        #then check the paths along edges
        if scanDown(paddedInput,currTR) == scanRight(paddedInput,currBL):
            currBR = [currBL[0], currTR[1]]
        else:
            currBR = [None,None]
    else:
        currBR = [None,None]
    #if all edges match up as rect
    currRect = [] 
    if currBR != [None,None]:
        currRect = [currTL,currBR] #boundaries (adjacent cells) and interior to be tested.
    #Test validity
    #prettyInput(paddedInput)
    #currRect
    if isRect(paddedInput,currRect):
        # If valid, add rect to list
        rectList.append(currRect)
        #change values so next search does not consider any 0's in previously identified rectangle
        [r,c] = currTL
        while r <= currBR[0]:
            while c <= currBR[1]:
                paddedInput[r][c] = 2
                c+=1
            r+=1 
    [currRow,currCol] = [currTR[0],currTR[1]+1]
    #print([currRow,currCol]) #


#change back to original coordinates (reduce by 1)
rects = []
for rList in rectList: 
    prow0 = rList[0][0]-1 #point row 0
    pcol0 = rList[0][1]-1
    prow1 = rList[1][0]-1
    pcol1 = rList[1][1]-1
    rects.append([[prow0,pcol0],[prow1,pcol1]]) 

print('\nFound', len(rectList), ' rectangular islands' )
print(rects)
prettyInput(input)
prettyInput(paddedInput)
#To do
# Optimization *
# * If currRow, currCol already within an identified island, should move out of that
# * one way to do that is to convert all 0's in verified rectangles to something else, so the search won't explore those. 
