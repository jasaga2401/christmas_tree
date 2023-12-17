
import turtle

def draw_branch(turtle, branch_length):
    """Draws a single branch of the tree."""
    turtle.forward(branch_length)
    turtle.left(150)
    turtle.forward(branch_length / 2.0)
    turtle.right(150)
    turtle.forward(branch_length / 2.0)
    turtle.left(150)
    turtle.forward(branch_length / 2.0)
    turtle.right(150)
    turtle.forward(branch_length / 2.0)
    turtle.left(150)
    turtle.forward(branch_length / 2.0)
    turtle.right(150)
    turtle.forward(branch_length / 2.0)
    turtle.left(150)
    turtle.forward(branch_length)
    turtle.right(150)

def draw_tree(turtle, branch_length, shorten_by, angle):
    """Draws a Christmas tree with multiple branches."""
    if branch_length > 10:
        turtle.forward(branch_length)
        turtle.left(angle)
        draw_tree(turtle, branch_length - shorten_by, shorten_by, angle)
        turtle.right(angle * 2)
        draw_tree(turtle, branch_length - shorten_by, shorten_by, angle)
        turtle.left(angle)
        turtle.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen_width = 800  # width in pixels
    screen_height = 850  # height in pixels
    screen.setup(screen_width, screen_height)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("forest green")
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.speed("fastest")

    draw_tree(t, 100, 10, 30)

    # Draw the trunk
    t.color("saddle brown")
    t.up()
    t.goto(0, -100)
    t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.end_fill()

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
