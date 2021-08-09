from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dic of default color for canvas
colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}
canvas_color = input("Enter canvas color (white or black): ")

# Create a convas with the user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw? Enter quit to quit. ")
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter width of rectangle: "))
        rec_height = int(input("Enter height of rectangle: "))
        rec_colors = input("Enter weight of Red,Blue,Green for the rectangle: ")
        rec_colors = rec_colors.split(',')

        rec = Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height,
                        color=(rec_colors[0], rec_colors[1], rec_colors[2]))
        rec.draw(canvas)

    if shape_type.lower() == "square":
        squ_x = int(input("Enter x of the square: "))
        squ_y = int(input("Enter y of the square: "))
        squ_side = int(input("Enter side of square: "))
        rec_colors = input("Enter weight of Red,Blue,Green for the square: ")
        rec_colors = rec_colors.split(',')

        squ = Square(x=squ_x, y=squ_y, side=squ_side,
                     color=(rec_colors[0], rec_colors[1], rec_colors[2]))
        squ.draw(canvas)

    if shape_type.lower() == "quit":
        break


canvas.make(imagepath="./resources/pic.png")


