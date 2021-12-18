# DAY 4 PART 2

# Now find one that starts with six zeroes.

import hashlib

with open('2015/inputs/d4.txt', 'r') as file:
    for input in file:
        hashed = ''
        i = 0
        while not hashed.startswith('000000'):
            i += 1
            plain = input.strip() + str(i)
            hashed = hashlib.md5(plain.encode('utf-8')).hexdigest()

        print('The answer is {} (plain: {}, hashed: {})'.format(i, plain,
                                                                hashed))
