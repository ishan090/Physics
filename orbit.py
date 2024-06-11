# A simple program that returns either the radius required or velocity of
# an object's orbit given the other

import math
import sys


args = sys.argv


def orbit(r=None, t=None, M=5.9722e24):
    """
    :param r: radius of the orbit, in meters
    :param t: period of the orbit, in seconds
    :param M: constant, mass of the object being orbitted
    """
    assert r or t, "Either one of the params (r or t) must not be None"
    # Defining the constants
    G = 6.67430e-11

    if r is None:
        # The objective is to find r,
        return ((G*M) * t*t / (4 * math.pi*math.pi))**(1/3)
    else: # otherwise, if r is known:
        return ((r*r*r*4*math.pi*math.pi)/(G*M))**(1/2)


if len(args) > 1:
    r, t = args[1:]
if r == "0":
    r = None
    t = int(t)
elif t == "0":
    t = None
    r = int(r)
print(orbit(r, t))
