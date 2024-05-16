import math

class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def display_name(self):
        print(f"Shape: {self.name}")


class Triangle(Shape):
    def __init__(self, side_length):
        super().__init__("Triangle")
        self.side_length = side_length

    def calculate_area(self):
        return (math.sqrt(3) / 4) * self.side_length ** 2

    def calculate_perimeter(self):
        return 3 * self.side_length


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


def main():
    triangle = Triangle(5)
    rectangle = Rectangle(4, 6)
    circle = Circle(3)

    triangle.display_name()
    rectangle.display_name()
    circle.display_name()

    print(f"Pole trójkąta: {triangle.calculate_area()}, obwód: {triangle.calculate_perimeter()}")
    print(f"Pole prostokąta: {rectangle.calculate_area()}, Obwód: {rectangle.calculate_perimeter()}")
    print(f"Pole kola: {circle.calculate_area()}, Obwód: {circle.calculate_perimeter()}")


if __name__ == "__main__":
    main()