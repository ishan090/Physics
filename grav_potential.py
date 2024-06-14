# In physics, there exists a gravitational potential for
# an object r distance away from a center of gravity

# This is expressed in the formula:
# -> gravitational potential = -GM/r
# gravitational potential, abbreviated as Vg is the
# potential energy upon the mass of the object whose Vg is being
# computed.

def Vg(r, M=None, G=6.67e-11):
    return -G*M/r
