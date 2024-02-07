class Point:
    def __init__(self, x, y):
        self.xcoordinate = x
        self.ycoordinate = y
    def move(self, x, y):
        self.xcoordinate = x + self.xcoordinate
        self.ycoordinate = y + self.ycoordinate
    def show(self):
        print("The x coordinate is: " + str(self.xcoordinate))
        print("The y coordinate is: " + str(self.ycoordinate))
    def dist(self, point2x, point2y):
        self.distance = ((point2x - self.xcoordinate)**2 + (point2y - self.ycoordinate)**2)**0.5
        print("The distance is: " + str(self.distance))
a = Point(1, 2)
a.show()
a.move(2, 4)
a.show()
a.dist(0, 0)
        

    