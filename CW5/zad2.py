class Turtle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.__x = 0  # Prywatne pole

    def say_name(self):
        print(f"Nazywam się {self.name} i moja prędkość to {self.speed}")

    def move(self, distance):
        self.__x += distance

    def get_position(self):
        return self.__x