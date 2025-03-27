class abstractShape:
    def area(self):
        return 0
    def perimeter(self):
        return 0

class circle(abstractShape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius

class rectangle(abstractShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

class square(rectangle):
    def __init__(self, side):
        super().__init__(side, side)

def menu():
    while True:
        print("What is your shape? (1)circle (2)rectangle (3)square (4)exit")


        answer = input("enter shape number: ")

        if answer == "1":
            radius = input("enter radius: ")
            shape = circle(radius)
        elif answer == "2":
            width = input("enter width: ")
            height = input("enter height: ")
            shape = rectangle(width, height)
        elif answer == "3":
            side = input("enter side for square: ")
            shape = square(side)
        elif answer == "4":
            break
        else:
            print("invalid input, try again.")
            continue

        print("area:", shape.area())
        print("perimeter:", shape.perimeter())

menu()
