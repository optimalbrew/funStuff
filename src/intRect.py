"""
Find the rectangle formed by intersection of two other rects (assuming they are axes aligned)
If a rect is not axes aligned, then we would need 3 corners to define it uniquely. Then use a trig (to simulate a rotation) of the axes, and then
use the same process as below.
"""


# No intersection

# 0A            I -------------- I      2 ways for no intersection
#    I-----I                      
#
# 0B     I -------------- I      
#                             I-----I  # In either case, max(minX) > min(maxX), overlap is negative
#  
# If intersection, then, 3 possibilities (but not guararanteed, need to check Y)
# 1:               I -------------- I   
#        I-------------I             Overlap = min(maxX) - max(minX)       
#
# # 2:               I ----------------- I
#                       I-------------I      overlap  =  min(maxX) - max(minX)              
#
# # 3:               I -------------- I
#                                I-------------I    overlap =  min(maxX) - max(minX)                    


class rectangle:
    def __init__(self, x):
        self.minX = min(x[0],x[2])
        self.maxX = max(x[0],x[2])
        self.minY = min(x[1],x[3])
        self.maxY = max(x[1],x[3])

    def lenX(self):
        return (self.maxX-self.minX)
    
    def lenY(self):
        return (self.maxY-self.minY)
    
    def area(self):
        lenX =(self.maxX-self.minX)
        lenY = (self.maxY-self.minY) 
        return lenX * lenY

r1 = rectangle([0,0,2,4])
r2 = rectangle([-1,-2,1,2])

r1.lenX()
r2.lenY()
r1.area()
r2.area()


# overlap along X
minMaxX = min(r1.maxX, r2.maxX)
maxMinX = max(r1.minX, r2.minX)
overlapX = minMaxX - maxMinX

#similarly along Y
minMaxY = min(r1.maxY, r2.maxY)
maxMinY = max(r1.minY, r2.minY)
overlapY = minMaxY - maxMinY

if overlapX>=0 and overlapY>=0:
    print('Intersection area is '+ str(overlapX * overlapY))
else:
    print('No intersection')