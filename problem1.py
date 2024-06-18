#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side

assert hypotenuse(3,4,True) == 5
(2 points)
"""
import math

def hypotenuse(a, b, c=True):
    if c == True:
        hypotenuses = math.sqrt(float(a**2) + float(b**2))
        return hypotenuses
    elif c==False:
        hypotenusess = float(a**2) - float(b**2)
        o = math.sqrt(hypotenusess)
        return o


if __name__ == "__main__":
    assert hypotenuse(3, 4, True) == 5
    assert hypotenuse(5, 12, True) == 13
    assert hypotenuse(5, 3, False) == 4
    assert hypotenuse(13, 12, False) == 5


    