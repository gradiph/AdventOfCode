class Cuboid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def getFootArea(self):
        areaList = [self.getBottomArea(), self.getSideArea(),
                    self.getFrontArea()]
        return min(areaList)

    def getSurfaceArea(self):
        return (2 * self.getBottomArea() + 2 * self.getSideArea()
                + 2 * self.getFrontArea())

    def getBottomArea(self):
        return self.length * self.width

    def getSideArea(self):
        return self.width * self.height

    def getFrontArea(self):
        return self.height * self.length
