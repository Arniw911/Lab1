class Shape: 
  def __init__(self): 
    self.areaVal = 0
  
  def area(self):
    print(self.areaVal)

class Square(Shape):
  def __init__(self, lengthVal): 
    super().__init__()
    self.length = lengthVal
    self.areaVal = lengthVal * lengthVal

i = Square(12)
i.area()

    