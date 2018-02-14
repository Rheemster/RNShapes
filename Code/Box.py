class Box(object):
    def __init__(self,w,l,h):
        self.w = w
        self.l = l
        self.h = h
    def getVolume(self):
        volume = self.w*self.l*self.h
        return volume
    def getSurfaceArea(self):
        surfaceArea = (2*self.l*self.h)+(2*self.h*self.w)+(2*self.w*self.l)
        return surfaceArea
