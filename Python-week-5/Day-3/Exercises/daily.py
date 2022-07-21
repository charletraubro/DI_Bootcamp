# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
# english_words = ["Hello", "Goodbye", "Welcome", "See you soon"]
# result = zip(french_words, english_words)
# print(dict(result))

import turtle

class Circle:
    def _init_(self, radius: int):
        self.radius = radius
        self.diameter = radius * 2
    
    @classmethod
    def from_diameter(cls, diameter):
        new_circle = Circle(diameter/2)
        return new_circle

    def area(self):
        return 3.14 * self.radius ** 2

    def print_circle(self):
        output = turtle.circle(self.area())
        return output

    def _add_(self, circle):
        return Circle(self.radius + circle.radius)
    
    def _le_(self, circle):
        return self.area() <= circle.area()

    def _eq_(self, circle):
        return self.area() == circle.area()

    
circle1 = Circle(2)
print(f"cirlce 1: r-{circle1.radius} d-{circle1.diameter}")

circle2 = Circle.from_diameter(7)
print(f"cirlce 2: r-{circle2.radius} d-{circle2.diameter}")
circle2.print_circle()

circle3 = circle1 + circle2
print(f'Circle 3: r-{circle3.radius} d-{circle3.diameter}')