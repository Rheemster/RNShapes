import math
class Sphere(object):
    def __init__(self,l,w,h):
        self.l = l
        self.w = w
        self.h = h
    def getVolume(self):
        volume = (4/3)*math.pi*self.l*self.w*self.h
        return volume
    def getSurfaceArea(self):
        surfaceArea = math.pi*4*(((self.l*self.w)**1.6+(self.l*self.h)**1.6)+(self.h*self.w)**1.6)/3**1/1.6
        return surfaceArea