import math
import numpy
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self,x,y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)

    def calc_dist(self,p2):
        dist = math.sqrt((p2.x-self.x)**2 + (p2.y - self.y)**2)
        return dist

    



p1 = Point(10,10)
p2 = Point(7,12)

# p1.move(5,5)
# p2.move(10,10)
# print(p1.calc_dist(p2))
# p1.reset()
# print(p1.x,p1.y)
