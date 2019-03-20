import numpy as np
import json
from world import gameObject

directions = [
    "north",
    "east",
    "south",
    "west"
]

class ant(gameObject):
    def __init__(self, name):
        super().__init__(name)
        self.facing = 0

    def ahead(self):
        if self.facing == 0:
            return self.position - [0,1]
        if self.facing == 1:
            return self.position + [1,0]
        if self.facing == 2:
            return self.position + [0,1]
        if self.facing == 3:
            return self.position - [1,0]

    def move(self):
        newpos = self.ahead()
        if self.world.getPos(newpos) == None:
            self.position = newpos
            print("moved forwards")

    def turnLeft(self):
        self.facing -= 1
        if self.facing < 0:
            self.facing = 3
        print("turned left")

    def turnRight(self):
        self.facing += 1
        if self.facing > 3:
            self.facing = 0
        print("turned right")

    def status(self):
        return json.dumps({
            "facing":directions[self.facing],
            "ahead":str(self.world.getPos(self.ahead()))
            })
