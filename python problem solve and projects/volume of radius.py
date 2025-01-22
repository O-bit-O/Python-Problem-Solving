import math

def vol(r):
    return 4/3*math.pi*r**3

radius=int(input("enter radius: "))
print(vol(radius))