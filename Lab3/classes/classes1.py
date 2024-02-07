class String:
  def __init__(self):
    self.ourString = ""
  
  def getString(self):
    self.ourString = str(input())
  
  def printString(self):
    print(self.ourString.upper())

i = String()
i.getString()
i.printString()