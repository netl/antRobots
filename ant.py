import numpy as np
import json
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
        self.active = True

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
            #print(self.name+": queue full")
            pass

    def tick(self):
        try:
            self.commands.get(False)()
        except queue.Empty:
            #print(self.name+": idle")
            pass

    def move(self):
        with self.world.actionLock:
            newpos = self.ahead()
            if self.world.getPos(newpos) == None:
                self.position = newpos
            return
        #print(self.name+": failed to move {}:{}".format(newpos, self.world.getPos(newpos)))

    def turnLeft(self):
        self.facing -= 1
        if self.facing < 0:
            self.facing = 3
        #print(self.name+": turned left")

    def turnRight(self):
        self.facing += 1
        if self.facing > 3:
            self.facing = 0
        #print(self.name+": turned right")

    def status(self):
        return json.dumps({
            "facing":directions[self.facing],
            "ahead":str(self.world.getPos(self.ahead()))
            "commands":self.queue.qsize()
            })
