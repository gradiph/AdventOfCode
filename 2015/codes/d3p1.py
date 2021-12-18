# DAY 3 PART 1

# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and
# then an elf at the North Pole calls him via radio and tells him where to move
# next. Moves are always exactly one house to the north (^), south (v),
# east (>), or west (<). After each move, he delivers another present to the
# house at his new location.

# However, the elf back at the north pole has had a little too much eggnog,
# and so his directions are a little off, and Santa ends up visiting some
# houses more than once. How many houses receive at least one present?

# For example:

# > delivers presents to 2 houses: one at the starting location,
# and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice
# to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children
# at only 2 houses.

with open('2015/inputs/d3.txt', 'r') as file:
    inputs = file.read()
    x, y = 0, 0
    houses = {(x, y)}
    for input in inputs:
        if input == '^':
            y += 1
        elif input == '<':
            x -= 1
        elif input == '>':
            x += 1
        elif input == 'v':
            y -= 1
        houses.add((x, y))
    print('Total delivered presents: {0}'.format(len(houses)))
