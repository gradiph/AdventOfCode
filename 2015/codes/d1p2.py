# Day 1 Part 2
# Now, given the same instructions, find the position of the first character
# that causes him to enter the basement (floor -1). The first character in the
# instructions has position 1, the second character has position 2, and so on.

# For example:

# ) causes him to enter the basement at character position 1.
# ()()) causes him to enter the basement at character position 5.
# What is the position of the character that causes Santa to first enter the
# basement?

with open('../inputs/d1.txt', 'r') as file:
    input = file.read()
    position = 0
    i = 0

    for data in input:
        i += 1
        if data == '(':
            position += 1
        elif data == ')':
            position -= 1
        if position == -1:
            break

    print('first index to enter basement: %d' % i)
