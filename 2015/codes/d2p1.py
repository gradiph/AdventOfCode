# DAY 2 PART 1

# The elves are running low on wrapping paper, and so they need to submit an
# order for more. They have a list of the dimensions (length l, width w, and
# height h) of each present, and only want to order exactly as much as they
# need.

# Fortunately, every present is a box (a perfect right rectangular prism),
# which makes calculating the required wrapping paper for each gift a little
# easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The
# elves also need a little extra paper for each present: the area of the
# smallest side.

# For example:

# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of
# wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
# A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet
# of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
# All numbers in the elves' list are in feet. How many total square feet of
# wrapping paper should they order?

from commons.Cuboid import Cuboid

with open('2015/inputs/d2.txt', 'r') as file:
    totalArea = 0
    i = 1
    for line in file:
        dimension = line.strip().split('x')
        length = int(dimension[0])
        width = int(dimension[1])
        height = int(dimension[2])

        tCuboid = Cuboid(length, width, height)

        # footArea = length * width
        # frontArea = width * height
        # sideArea = height * length
        # surfaceArea = 2 * footArea + 2 * frontArea + 2 * sideArea
        lastTotalArea = totalArea
        totalArea += tCuboid.getSurfaceArea() + tCuboid.getFootArea()

        print('totalArea[{0}]: {1} + ({2} + {3}) = {4}'.format(i,
              lastTotalArea, tCuboid.getSurfaceArea(), tCuboid.getFootArea(),
              totalArea))

        i += 1

    print('Total area: {0}'.format(totalArea))
