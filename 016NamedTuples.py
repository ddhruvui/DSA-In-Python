from collections import namedtuple

class Point_Old:
    def __init__(self,x,y):
        self.x = x
        self.y = y

p1 = Point_Old(1,2)
p2 = Point_Old(1,2)

print(p1 == p2)

Point_New  = namedtuple("Point_New", ["x","y"])
p1 = Point_New(1,2)
p2 = Point_New(1,2)
print(p1 == p2)