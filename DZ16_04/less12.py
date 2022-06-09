
class Dog:

    __slots__ = ["name", "breed", "weight"]
    counter = 0

    @classmethod
    def increase_count(cls):
        cls.counter += 1
        # method for count all created dogs

    @staticmethod
    def bark():
        print("Guf-guf!")

    def __init__(self, name, breed, weight):
        self.name = name
        self.breed = breed
        self.weight = weight

        self.increase_count()

    def __add__(self, other):
        # add weight dogs
        return self.weight + other.weight


Dog.bark()
