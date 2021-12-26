class LightField:
    def __init__(self,
                 length=1000,
                 width=1000):
        self.length = length
        self.width = width
        self.field = [[0 for x in range(width)] for x in range(length)]

    def countLitLights(self):
        return sum(sum(x) for x in self.field)

    def run(self, command):
        start, end = self.parseCommand(command)
        if command.startswith('turn on'):
            self.turnOn(start, end)
        elif command.startswith('turn off'):
            self.turnOff(start, end)
        else:
            self.toggle(start, end)

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
