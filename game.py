#!/usr/bin/env python3
import numpy as np
from ant import ant as ant
from world import world, gameObject


if __name__ == "__main__":
    import random
    #create world
    w = world((8, 8))

    #add random rock
    w.place(gameObject("rock"), [1,7])

    #create ant and place it
    a = ant("bobo")
    w.place(a, [6,2])

    #navigate towards rock
    print(w)
    print(a.status())
    count = 0
    while "rock" not in a.status():
        count += 1
        random.choice([
            a.turnLeft,
            a.turnRight,
            a.move
            ])()
    print(w)
    print(a.status())
    print("found rock after {} random commands".format(count))
