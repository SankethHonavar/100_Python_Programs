class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width
    
length=float(input("Enter length of the rectangle: "))
width=float(input("Enter width of the rectangle: "))
rect=Rectangle(length,width)
print("Area of the rectangle: ", rect.area())