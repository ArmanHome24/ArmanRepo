import turtle
from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def str(self):
        print(self.x, self.y)

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

    def calc_distance(self, otherpoint):
        return ((self.x - otherpoint.x) ** 2 +
                (self.y - otherpoint.y) ** 2) ** 0.5


class GuiPoint(Point):
    def draw(self, canvas, size=9, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()

        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()

        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


point1 = Point(randint(0, 400), randint(0, 400))
point2 = Point(randint(10, 400), randint(10, 400))
my_turtle = turtle.Turtle()

point3 = GuiPoint(float(input("Guess X:")),
                  float(input("Guess Y:")))
r1 = GuiRectangle(point1, point2)

print(f"Rectangle: {r1.point1.x},{r1.point1.y} \
 and {r1.point2.x},{r1.point2.y}")
print("point is in rRectangle:",
      point3.falls_in_rectangle(r1))
gussarea = float(input('Rectangle area:'))
print("Your area was off by:", r1.area() - gussarea)
r1.draw(my_turtle)
point3.draw(my_turtle)
turtle.done()
