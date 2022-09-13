'''
Write a Python program to calculate surface volume and area of a cylinder. Go to the editor

Note: A cylinder is one of the most basic curvilinear geometric shapes, the surface formed by the points at a fixed distance from a given straight line, the axis of the cylinder.

Test Data:

volume: Height (4), Radius (6)

Expected Output:

Volume is: 452.57142857142856

Surface Area is: 377.1428571428571
'''

import math
def main():
    height = int(input('Height: '))
    radius = int(input('Radius: '))
    volume = math.pi * radius ** 2 * height
    surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
    print('Volume is: {}'.format(volume))
    print('Surface Area is: {}'.format(surface_area))
if __name__ == '__main__':
    main()

    