class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width * self.height

class Triangle(Rectangle):
    def area2(self):
        return super().area() /2
        # return (self.width * self.height)/2
