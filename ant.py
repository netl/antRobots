import numpy as np
import queue
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
        self.commands = queue.Queue(10)
        self.info = {
            "name":self.name,
            "facing":directions[self.facing],
            "ahead":str(self.world.getPos(self.ahead())),
            "status":"idle"
            }

    def ahead(self):
        if self.facing == 0:
            return self.position - [0,1]
        if self.facing == 1:
            return self.position + [1,0]
        if self.facing == 2:
            return self.position + [0,1]
        if self.facing == 3:
            return self.position - [1,0]

    def do(self, command):
        try:
            self.commands.put(command, False)
        except queue.Full:
            pass

    def tick(self):
        try:
            self.commands.get(False)()
        except queue.Empty:
            self.setStatus("idle")
        self.info["ahead"]:str(self.world.getPos(self.ahead())),

    def setStatus(self, state):
        self.info["status"] = state

    def move(self):
        self.setStatus("moving")
        with self.world.actionLock:
            newpos = self.ahead()
            if self.world.getPos(newpos) == None:
                self.position = newpos

    def turnLeft(self):
        self.setStatus("turning Left")
        self.facing -= 1
        if self.facing < 0:
            self.facing = 3
        self.info["facing"] = directions[self.facing]

    def turnRight(self):
        self.setStatus("turning Right")
        self.facing += 1
        if self.facing > 3:
            self.facing = 0
        self.info["facing"] = directions[self.facing]
