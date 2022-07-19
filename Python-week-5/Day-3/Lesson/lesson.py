# class Dog():
#     number_of_dogs = 0
#     dogs_king = "Bernie IV"

#     # Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)
#         self.name = name_of_the_dog
#         # Increment the number of dogs
#         Dog.number_of_dogs += 1

#     def bark(self):
#         print("{} barks ! WAF".format(self.name))

#     def walk(self, number_of_meters):
#         print("{} walked {} meters".format(self.name, number_of_meters))

#     def rename(self, new_name):
#         self.name = new_name

# my_dog = Dog("Rex")
# my_dog2 = Dog("Bernie V")
# print("Curently, there are {} dogs".format(Dog.number_of_dogs))

class Circle:
    color = "red"

    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        self.diameter = self.diameter * factor

    def get_color(self):
       return Circle.color

circle1 = Circle(2)
print(circle1.color)
print(Circle.color)
print(circle1.get_color())
circle1.grow(3)
print(circle1.diameter)
