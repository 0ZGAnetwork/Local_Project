import math as m
class Rectangle:
    def __init__(self, width: int | float, height: int | float) -> None:
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            raise ValueError("Width must be more than 0")
    @height.setter
    def height(self, new_height):
        if new_height >= 1:
            self._height = new_height
        else:
            raise ValueError("Height must be more than 0")
    
    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_diagonal(self):
        return m.hypot(self.width, self.height)         
    
    def get_picture(self):
        
        if self.height > 50 or self.width > 50:
            return "Too big for picture."

        return ''.join('*' * self.width + "\n" for _ in range(self.height))

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    

class Square(Rectangle):
    def __init__(self, side: int | float) -> None:
        super().__init__(side, side)
        self.side = side

    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width
        self.side = new_width

    def set_height(self, new_height):
        self.set_width(new_height)

    def set_side(self, new_side):
        self.set_width(new_side)

    def __str__(self):
        return f"Square(side={self.side})"

# Test
try:
    # rectangle = Rectangle(3,3)
    # square = Square(2)
    # print(rectangle.get_picture())
    # print(square.get_picture())
    # print(rectangle.get_amount_inside(square))

    # square.set_width(3)
    # print(square.width)
    # print(square.height)
    # square.set_height(4)
    # print(square.width)
    # print(square.height)
    # square.set_side(6)
    # print(square.width)
    # print(square.height)
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(5)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))

except ValueError as e:
    print("Error: ",e)



