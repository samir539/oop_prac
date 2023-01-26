import math
import numpy
class Point():
    """
    Model a point in 2d
    """
    def __init__(self,x=0,y=0):
        self.move(x,y)

    def move(self,x,y):
        """
        move the point object to a position x,y
        @params
        ------
        :x: the x position
        :y: the y position
        """
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)

    def calc_dist(self,p2):
        """
        calculate the distance between two points
        @param
        ------
        :p2: the point we want to find the distance to 

        @return
        ------
        :dist: the euclidan distance between the two points
    
        """
        dist = math.sqrt((p2.x-self.x)**2 + (p2.y - self.y)**2)
        return dist

    
p1 = Point(10,10)
p2 = Point(7,12)
p3 = Point()
