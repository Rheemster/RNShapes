def sqrt(n):
    return n**(0.5)
class Pyramid(object):
    def __init__(self,l,w,h):
        self.l = l
        self.w = w
        self.h = h
    def getVolume(self):
        volume = (self.l*self.w*self.h)/3
        return volume
    def getSurfaceArea(self):
        l,w,h = self.l,self.w,self.h
        surfaceArea = (l*w)+(l*(sqrt(((w/2)**2)+(h**2)))+w*sqrt(((l/2)**2)+(h**2)))
        return surfaceArea