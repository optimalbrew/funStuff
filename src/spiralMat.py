"""
Read the elements of a 2D matrix as a 'spiral' (clockwise)

Idea: 
* recursion based on reading the edges of a rectangle
* 4 segments to read (if n,m>1)
* if either of row or col = 1, just read that segment.
"""
n,m = 5,5 #default
# print('\nEnter num rows')
# n = int(input())
# print('\nEnter num cols')
# m = int(input())

#create an input matrix
data = []
c = 0
for r in range(n):
    l=[]
    for c in range(m):
        l.append((m)*r+c)
    data.append(l)

#reset row and col of upper left corner
r,c = 0,0
l = [] #for result

def readSpiral(r,c,n,m):
    if n > 1 and m > 1: #read all 4 borders
        for i in range(c,c+(m-1)): #read right
            l.append(data[r][i])
        for i in range(r,r+(n-1)): #read down
            l.append(data[i][c+ (m-1)])
        for i in reversed(range(c+1,c+ (m-1)+1)): #read left
            l.append(data[r+(n-1)][i])
        for i in reversed(range(r+1,r+(n-1)+1)): #read up
            l.append(data[i][c])
        #update values + recursion
        r += 1
        c += 1
        n -= 2
        m -= 2
        readSpiral(r,c,n,m)
    elif n == 1 and m >= 1: #read right # includes case with just 1 element
        for i in range(c,c+(m-1)+1): #read right ALL
            l.append(data[r][i])
    elif n > 1 and m == 1: #read down
        for i in range(r,r+(n-1)+1): #read down ALL
            l.append(data[i][c+ (m-1)])


readSpiral(r,c,n,m)

for d in data:
    print(d)

print('\n')
print(l)