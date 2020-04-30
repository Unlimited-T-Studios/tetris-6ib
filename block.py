#parent class
class Block:
    
    def __init__(self, speed, position, color):
        self.speed = speed
        self.position = position
        self.color = color
    
#all block child classes
class LBlock(Block):

    def __init__(self, layout):
        #the layout / how the block looks
        self.layout = layout

class TBlock(Block):

    def __init__(self, layout):
        self.layout = layout

class SBlock(Block):

    def __init__(self, layout):
        self.layout = layout

class LongBlock(Block):

    def __init__(self, layout):
        self.layout = layout

class SquareBlock(Block):

    def __init__(self, layout):
        self.layout = layout

class Rotate:

    def rotateleft(self, layout):
        if len(layout) == 5:
            l = layout
            newl = []
            for i in range(5):
                newl.append([0, 0, 0, 0, 0])
            for x in range(len(layout)):
                #numbers level
                for y in range(len(layout[x])):
                    if layout[x][y] == 1:
                        newl[4-y][x] = 1
            return newl


    def rotateright(self, layout):
        if len(layout) == 5:
            l = layout
            newl = []
            for i in range(5):
                newl.append([0, 0, 0, 0, 0])
            for x in range(len(layout)):
                #numbers level
                for y in range(len(layout[x])):
                    if layout[x][y] == 1:
                        newl[y][4-x] = 1
            return newl