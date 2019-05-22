"""
Given a matrix, rotate it (say clockwise) like so
a b c      g d a
d e f      h e b
g h i      i f c

A clockwise rotation is simply  
* take the top row and make it the last col
* then take the 2nd row and make that the 2nd last col
* and so on.. last row becomes 1st col

"""

data = [
        ['a', 'b', 'c', 'd'],
        ['e', 'f', 'g', 'h'],
        ['i', 'j', 'k', 'l']
]

n = len(data)
m = len(data[0])

final=[]
for c in range(m):
    temp = []
    for r in reversed(range(n)): #start from bottom row
        temp.append(data[r][c]) #build a list from each col of data (bottom up)
    final.append(temp) #insert lists from cols into list of new rows 

print('\n**** Input ****\n')
for r in data:
    print(r)

print('\n\n**** Rotated ****\n')
for r in final:
    print(r)
