class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return self.x, self.y, self.width, self.height

rec = Rectangle(5, 10, 50, 100)
print(rec.__str__())
