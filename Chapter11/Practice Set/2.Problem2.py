class Animals:
    pass


class pets(Animals):
    pass



class Dog(pets):
    @staticmethod
    def bark():
        print("Woof Woof!")

d = Dog()
d.bark()