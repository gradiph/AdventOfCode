class NiceString:
    def __init__(self,
                 word,
                 vowels=['a', 'i', 'u', 'e', 'o'],
                 forbiddens=['ab', 'cd', 'pq', 'xy']):
        self.word = word
        self.vowels = vowels
        self.forbiddens = forbiddens

    def validate(self):
        try:
            self.validateVowels()
            self.validateTwiceInARow()
            self.validateForbidden()
        except Exception as e:
            raise e

    def validate2(self):
        try:
            self.validateTwoLetterTwice()
            self.validateBetweenRepeat()
        except Exception as e:
            raise e

    def validateVowels(self):
        nVowels = 0

        for char in self.word:
            if char in self.vowels:
                nVowels += 1

        if nVowels < 3:
            raise Exception('ERROR Rule 1: It contains less than 3 vowels.')

    def validateTwiceInARow(self):
        lastChar = ''
        isValidated = False

        for char in self.word:
            if char == lastChar:
                isValidated = True

            lastChar = char

        if not isValidated:
            raise Exception('ERROR Rule 2: It doesn\'t contains at least one '
                            'letter that appears twice in a row.')

    def validateForbidden(self):
        for forbiddenWord in self.forbiddens:
            if (forbiddenWord in self.word):
                raise Exception('ERROR Rule 3: It contains the forbidden '
                                'strings.')

    def validateTwoLetterTwice(self):
        firstChar = ''
        secondChar = ''
        letterPairs = list()

        i = 0
        for char in self.word:
            if firstChar == '':
                firstChar = char
            else:
                secondChar = char
                letterPairs.append(firstChar + secondChar)
                firstChar = secondChar
            i += 1

        isTwoLetterTwice = False
        for pair in letterPairs:
            searchIndex = letterPairs.index(pair)
            searchingPairs = letterPairs.copy()
            searchingPairs.pop(searchIndex)
            try:
                resultIndex = searchingPairs.index(pair)
                # check for same value because of the first one is popped, so
                # if it overlaps, then the index would be same.
                if resultIndex != searchIndex:
                    isTwoLetterTwice = True
                    break
            except Exception:
                pass

        if (not isTwoLetterTwice):
            raise Exception('ERROR: It doesn\'t contain at least a pair of any'
                            ' two letters that appears twice.')

    def validateBetweenRepeat(self):
        isBetweenRepeat = False
        i = 0

        for char in self.word:
            try:
                secondChar = self.word[i + 2]
                if char == secondChar:
                    isBetweenRepeat = True
                    break
                i += 1
            except Exception:
                break

        if (not isBetweenRepeat):
            raise Exception('ERROR: It doesn\'t contain at least one letter '
                            'which repeats with exactly one letter between '
                            'them.')
