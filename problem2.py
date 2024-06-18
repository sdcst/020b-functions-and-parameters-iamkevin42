#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math


def distance(x,y):
    x1, y1 = x
    x2, y2 = y

    xx = x2 - x1
    yy = y2 - y1

    dd = xx**2 + yy**2
    ddd= math.sqrt(dd)
    roundd= round(ddd,3)

    return roundd
        




if __name__ == "__main__":
    d = distance( (2,4) , (6,3) )
    assert round(d,3) == 4.123
    d = distance( (-3,2.2) , (1,2) )
    assert round(d,3) == 4.005  


