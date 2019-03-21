#!/usr/bin/env python3
import numpy as np
from ant import ant as ant
from world import world, gameObject
import threading
import time
class game():

    def __init__(self, world):
        self.running = False
        self.tickRate = 1/3
        self.w = world

    def runMainLoop(self):
        self.running = True
        threading.Timer(self.tickRate, self.mainLoop).start()

    def stop(self):
        self.running = False

    def mainLoop(self):
        startTime = time.time()
        threads = []
        for obj in self.w.objects:
            if getattr(obj, "tick", False):
                print(o.status())
                t = threading.Thread(target=obj.tick())
                threads.append(t)
                t.start()
        for t in threads:
            t.join()
        if self.running:
            nextTick = startTime-time.time()+self.tickRate
            threading.Timer(nextTick, self.mainLoop).start()
            if nextTick < 0:
                print("tickRate too high! ({} ms behind)".format(-nextTick*1000))

if __name__ == "__main__":
    import random
    #create world
    w = world((20, 20))

    counts = 10
    for n in range(counts):
        print("generating {} objects {}%\r".format(counts, 100*n/counts),end='')
        #add random rock
        w.place(gameObject("rock"), [random.randint(0,w.size[0]-1),random.randint(0,w.size[1]-1)])

        #create ant and place it
        a = ant("bobo{}".format(n))
        w.place(a, [random.randint(0,w.size[0]-1),random.randint(0,w.size[1]-1)])

        for x in range(10):
            a.do(random.choice([
                a.turnLeft,
                a.turnRight,
                a.move
                ]))
    print("\nready!")

    g = game(w)
    g.runMainLoop()
    for n in range(10):
        print(w)
        time.sleep(1/3)
    g.running = False
