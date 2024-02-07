class Shape: 
  def __init__(self): 
    self.areaVal = 0
  
  def area(self):
    print(self.areaVal)

class Square(Shape):
  def __init__(self, length): 
    super().__init__()
    self.length = length
    self.areaVal = length * length

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length 
        self.width = width
        self.areaVal = length * width
        

i = Rectangle(5, 6)
i.area()
