# DAY 3 PART 2

# The next year, to speed up the process, Santa creates a robot version of
# himself, Robo-Santa, to deliver presents with him.

# Santa and Robo-Santa start at the same location (delivering two presents to
# the same starting house), then take turns moving based on instructions from
# the elf, who is eggnoggedly reading from the same script as the previous
# year.

# This year, how many houses receive at least one present?

# For example:

# ^v delivers presents to 3 houses, because Santa goes north, and then
# Robo-Santa goes south.
# ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up
# back where they started.
# ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one
# direction and Robo-Santa going the other.

with open('2015/inputs/d3.txt', 'r') as file:
    inputs = file.read()
    x, y, x2, y2 = 0, 0, 0, 0
    houses = {(x, y)}
    isSantaTurn = True

    for input in inputs:
        if isSantaTurn:
            if input == '^':
                y += 1
            elif input == '<':
                x -= 1
            elif input == '>':
                x += 1
            elif input == 'v':
                y -= 1
            houses.add((x, y))
        else:
            if input == '^':
                y2 += 1
            elif input == '<':
                x2 -= 1
            elif input == '>':
                x2 += 1
            elif input == 'v':
                y2 -= 1
            houses.add((x2, y2))

        isSantaTurn = not isSantaTurn

    print('Total delivered presents: {0}'.format(len(houses)))
