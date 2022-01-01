class LightField:
    def __init__(self,
                 version=1,
                 length=1000,
                 width=1000):
        self.version = version
        self.length = length
        self.width = width
        self.field = [[0 for x in range(width)] for x in range(length)]

    def countLitLights(self):
        return sum(sum(x) for x in self.field)

    def sumLightBrightness(self):
        return self.countLitLights()

    def run(self, command):
        start, end = self.parseCommand(command)
        if command.startswith('turn on'):
            if self.version == 1:
                self.turnOn(start, end)
            elif self.version == 2:
                self.addBrightness(start, end, 1)
        elif command.startswith('turn off'):
            if self.version == 1:
                self.turnOff(start, end)
            elif self.version == 2:
                self.addBrightness(start, end, -1)
        else:
            if self.version == 1:
                self.toggle(start, end)
            elif self.version == 2:
                self.addBrightness(start, end, 2)

    def parseCommand(self, command):
        part = command.split(' ')
        position = [x for x in part if ',' in x]
        start = [int(x) for x in position[0].split(',')]
        end = [int(x) for x in position[1].split(',')]
        return start, end

    def turnOn(self, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                self.field[x][y] = 1

    def turnOff(self, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                self.field[x][y] = 0

    def toggle(self, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                self.field[x][y] = 1 if self.field[x][y] == 0 else 0

    def addBrightness(self, start, end, amount):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                self.field[x][y] += amount
                if self.field[x][y] < 0:
                    self.field[x][y] = 0
