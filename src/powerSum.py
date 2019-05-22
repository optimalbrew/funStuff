"""
Find number of ways that an integer X can be expressed as the sum of the 'n'-th power of unique natural numbers
Example: X = 13, n=2 :  2^2 + 3^2 = 13
         X = 100, n=2; {10}, {6,8}, {1,3,4,5,7} sum of squares of these elements = 100

From Justin: this tree based exploration does not track the paths (so the combinations or sets are not returned)
"""

def numWays(X,n):
    return count_ways(X,n,1)

def count_ways(X,n,i):
    val = X - i**n
    if val == 0: #exact hit for X (of residual in general intermediate step)
        return 1
    if val < 0: #overshot
        return 0
    #or keep exploring other ints using the residual (assumes i is part of some solution) or unchanged
    return count_ways(X, n, i+1) + count_ways(val,n,i+1)