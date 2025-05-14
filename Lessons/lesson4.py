

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __gt__(self, other):
        return self.x > other.x


    def __str__(self):
        return "Я магический метод"


test = Vector(12, 33)
test2 = Vector(9, 33)

print(test > test2)
print(test)