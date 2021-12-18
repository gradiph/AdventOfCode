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
            self.validateRule1()
            self.validateRule2()
            self.validateRule3()
        except Exception as e:
            raise e

    def validateRule1(self):
        nVowels = 0

        for char in self.word:
            if char in self.vowels:
                nVowels += 1

        if nVowels < 3:
            raise Exception('ERROR Rule 1: It contains less than 3 vowels.')

    def validateRule2(self):
        lastChar = ''
        isValidated = False

        for char in self.word:
            if char == lastChar:
                isValidated = True

            lastChar = char

        if not isValidated:
            raise Exception('ERROR Rule 2: It doesn\'t contains at least one '
                            'letter that appears twice in a row.')

    def validateRule3(self):
        for forbiddenWord in self.forbiddens:
            if (forbiddenWord in self.word):
                raise Exception('ERROR Rule 3: It contains the forbidden '
                                'strings.')
