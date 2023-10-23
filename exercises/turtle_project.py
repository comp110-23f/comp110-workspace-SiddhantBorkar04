"""TO DO: Describe your scene program."""
 
__author__ = "730652641"
 
from turtle import Turtle, done
import random

# TO DO: Define the procedures for other components in your scene here.


def draw_tree(a_turtle: Turtle, x: float, y: float, height: float) -> None:
    """Draws trees in given locations at given height, using helper functions. (Points attempted: Drawing Function, Above and Beyond: Breaks up complex function, )."""
    draw_trunk(a_turtle, x, y, height)
    draw_branches(a_turtle, x, y, height)
    a_turtle.penup()


def draw_branches(a_turt: Turtle, x: float, y: float, height: float) -> None:
    """Function to make the green triangle part of tree. (Points attempted: Drawing Function, Fill Color, Marker Color)."""
    width_of_base = height * 1.5
    side_len = 2 * width_of_base

    # position the bottom left of branch
    a_turt.goto(x - (height * .25), y) 

    # draw and color the tree
    a_turt.pendown()
    a_turt.color("green")
    a_turt.begin_fill()
    a_turt.forward(width_of_base)
    a_turt.left(105)
    a_turt.forward(side_len)
    a_turt.left(150)
    a_turt.forward(side_len)
    a_turt.end_fill()
    a_turt.penup()
    a_turt.left(105)


def draw_trunk(a_turt: Turtle, x: float, y: float, height: float) -> None:
    """Function to make brown bottom part of tree. (Points attempted: Drawing Function, Loop Usage, Fill Color, Marker Color)."""
    base = height
    # position the base
    a_turt.goto(x, y)

    # draw and color the base
    a_turt.pendown()
    a_turt.color("brown")
    a_turt.begin_fill()
    n = 0
    while n < 4:
        a_turt.forward(base)
        a_turt.right(90)
        n += 1
    a_turt.end_fill()
    a_turt.penup()


def draw_background(turt: Turtle, x_pos: float, y_pos: float, base_size: float, height_size: float, color: str) -> None:
    """Sets large square/rectangular blocks to a certain color. (Points attempted: Drawing Function, Loop Usage, Fill Color)."""
    turt.goto(x_pos, y_pos)
    turt.pendown()
    turt.color(color)
    turt.begin_fill()
    n = 0
    while n < 2:
        turt.forward(base_size)
        turt.left(90)
        turt.forward(height_size)
        turt.left(90)
        n += 1
    turt.end_fill()
    turt.penup()


def draw_apple(turt: Turtle, x_pos: float, y_pos: float) -> None:
    """Draws red squares (apples) that have fallen from the trees in specified locations. (Points attempted: Drawing Function, Loop Usage, Fill Color, Marker Color)."""
    base: int = 10
    turt.goto(x_pos, y_pos)
    turt.color("red")
    turt.pendown()
    turt.begin_fill()
    n = 0
    while n < 4:
        turt.forward(base)
        turt.left(90)
        n += 1
    turt.end_fill()
    turt.penup()


def draw_mountain(a_turt: Turtle, x_pos: float, y_pos: float, base_size: float, color: str) -> None:
    """Draws mountains in the background of the scene. (Points attempted: Drawing Function, Fill Color)."""
    side_len = 2 * base_size
    # position the bottom left of branch
    a_turt.goto(x_pos, y_pos) 
    # draw and color the tree
    a_turt.pendown()
    a_turt.color(color)
    a_turt.begin_fill()
    a_turt.forward(base_size)
    a_turt.left(105)
    a_turt.forward(side_len)
    a_turt.left(150)
    a_turt.forward(side_len)
    a_turt.end_fill()
    a_turt.penup()
    a_turt.left(105)


def main() -> None:
    """The entrypoint of my scene. (Points attempted: Main, Draw Something Twice, Loop Usage, Above and Beyond: try something fun (random function))."""
    turt: Turtle = Turtle()
    # turt.speed(MAX_SPEED)
    # TO DO: Call the procedures you define and pass your Turtle(s) as an argument.
    # Draws the Sky
    draw_background(turt, -300, -300, 600, 600, "blue")

    # Draws plains/ground
    draw_background(turt, -300, -300, 600, 300, "yellow")

    # Draws Mountains
    draw_mountain(turt, -300, 0, 150, "purple")
    draw_mountain(turt, -150, 0, 150, "purple")
    draw_mountain(turt, 0, 0, 150, "purple")
    draw_mountain(turt, 150, 0, 150, "purple")

    # Draws multiple trees in random locations (complex point for random locations)
    for i in range(5):
        rand_x_pos1: int = random.randint(-290, 290)
        rand_y_pos1: int = random.randint(-300, 0)
        draw_tree(turt, rand_x_pos1, rand_y_pos1, 15)

    # Draws multiple apples in random locations (complex point for random locations)
    for n in range(15):
        rand_x_pos2: int = random.randint(-290, 290)
        rand_y_pos2: int = random.randint(-300, 0)
        draw_apple(turt, rand_x_pos2, rand_y_pos2)

    done()
 
 
# TO DO: Use the __name__ is "__main__" idiom shown in class
if __name__ == "__main__":
    main()