#version 1: not memory/space optimized (see https://stackoverflow.com/questions/18761766/mergesort-with-python)
def msort(x):
    if len(x) < 2: #this is not just for kicks, this is what terminates the recursive calls (reached a leaf node).
        return x #a leaf node
    result = []
    mid = int(len(x) / 2)
    y = msort(x[:mid]) #these recursive calls continue till len<2, i.e. a single element (leaf node) is returned
    print(y)
    z = msort(x[mid:]) #also why this implementation uses up a quite a bit of memory (new y,z's created @ each level)
    print(z)
    i,j = 0,0   #re initialized within each level to scan through left and right sub-lists
    while i < len(y) and j < len(z): #scan through both lists comparing elements (at least each element from the smaller list)
        if y[i] > z[j]: #starting with left[0] > right[0]
            result.append(z[j]) #add right[] to result
            j += 1 #move to compare next elem in right
        else:
            result.append(y[i]) #else add left to result
            i += 1 #move to next elem of left
    #on exiting while loop (i.e. at least one of left or right completely scanned), add the leftover from the other one
    result += y[i:] #append any residual left as is
    result += z[j:] #append any residual right as is
    return result

msort([21,4,12,3,7,8,5,4])
msort(['q','e','r','c', 'a','e','z','b'])


#alternative version 2: using pop https://stackoverflow.com/questions/18761766/mergesort-with-python
def msort2(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = msort2(x[:mid])
    z = msort2(x[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result


msort2([1,4,2,3,7,8,5,4])