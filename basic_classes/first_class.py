class Point():
    def reset(self):
        self.x = 0
        self.y = 0

        

p1 = Point()
p2 = Point()

p1.x = 1
p1.y = 2
p2.x = 3
p2.y = 4

print(p1.x,p1.y,p2.x,p2.y)
p1.reset()
p2.reset()
print(p1.x,p1.y,p2.x,p2.y)
