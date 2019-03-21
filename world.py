import numpy as np
import threading

class gameObject():
    def __init__(self, name = "generic object"):
        self.name = name
        self.position = None
        self.world = None

    def __str__(self):
        return self.name

    __repr__ = __str__

class world():
    def __init__(self, size = (5, 5)):
        self.size = np.array(size)
        self.objects = []
        self.actionLock = threading.Lock()

    #add object to world and set its position
    def place(self, obj, position):
        if obj not in self.objects:
            self.objects.append(obj)
        obj.position = np.array(position)
        obj.world = self
   
    #properly remove object from world
    def remove(self, obj):
        self.objects.remove(obj)
        obj.position = None
        obj.world = None

    #get object from given position
    def getPos(self, position):
        for o in self.objects:
            if np.array_equal(o.position, position):
                return o
        x, y = position
        if x > 0 and x < self.size[0] and y > 0 and y < self.size[1]:
            return None
        return False

    def __str__(self):
        m = np.full(self.size, ".")
        for o in self.objects:
            x, y = o.position
            try:
                m[x][y] = o.name
            except:
                print(o.position)
                break
       
        Map = " "
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                #get object name
                Map += str(m[x][y]) + " "
            Map += "\n"
        return Map
