"""
Kash found this somewhere:

In cartesian space, is it possible to move from (a,b) -> (c,d) using the following operations only
* (a,b) -> (a, a+b)
* (a,b) -> (a+b, b)
* null op (stay where you are, i.e. when (c,d) is the same as (a,b))
"""

"""
This is the easy version which assumes (a,b,c,d) >= (0,0,0,0). Obviously this also works if all are negative, with a trivial change.
In general case: starting from [-1,1] can get everywhere, except origin.
# Continuing with simple case:
Idea is to work backwards. Given a point (c,d), there is only one way it could have been reached:
The only way to reach (47,52) is from (47,5) or (-5,52). If the starting point is (1,2), then we can never reach (-5,52), thus
that can be ruled out.
"""

def isPossible(a,b,c,d):
    #trivial case where the points are the same
    if [a,b] == [c,d]:
        print('Possible')
        return True
    else:
        #more trivial cases where both points are on x axis
        if a == 0:
            if c!=0:
                print('Not Possible')
                return False
            else:
                if b == 0:
                    print('Not Possible')
                    return False
                else:
                    if d%b != 0:
                        print('Not Possible')
                        return False
                    else:
                        print('Possible')
                        return True
        #more trivial cases both points on y axis
        if b == 0:
            if d!=0:
                print('Not Possible')
                return False
            else:
                if a == 0:
                    print('Not Possible')
                    return False
                else:
                    if c%a != 0:
                        print('Not Possible')
                        return False
                    else:
                        print('Possible')
                        return True
        #non trivial cases, work backwards from (c,d) see if (a,b) is reachable
        prev1 = [c,d-c]
        prev2 = [c-d,d]
        #print([prev1, prev2])
        if min(prev1) < 0:
            prev1 = None
        if min(prev2) < 0:
            prev2 = None
        if prev1 == None and prev2 == None:
            print('Not possible')
            return False
        elif prev1 != None:
            if [a,b] == [prev1[0],prev1[1]]:
                #print([prev1])
                print('Possible')
                return True
            else:
                print(prev1)
                isPossible(a,b,prev1[0],prev1[1])
        elif prev2 != None:
            if [a,b] == [prev2[0],prev2[1]]:
                #print([prev2])
                print('Possible')
                return True
            else:
                print(prev2)
                isPossible(a,b,prev2[0],prev2[1])
        