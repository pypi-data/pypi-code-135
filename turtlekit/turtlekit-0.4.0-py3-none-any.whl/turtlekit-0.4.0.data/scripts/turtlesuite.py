from turtle import Turtle, Screen

def get_screen():
    """
    Returns a screen object.

    Takes no arguments.
    """
    return Screen()


def draw_square(sidelength:int, start_angle:int, start_at:tuple, color, infill=True, pensize = 5):
    """
    Draws a square to an existing screen. Always draws from bottom left of shape.

    #### Parameters

    `sidelength` : How long the sides of the square should be, in integer format.

    `start_angle` : What angle to tilt the square. Always rotates left.

    `start_at` : A tuple containing x/y coordinates, in that order, of where to begin drawing the square.

    `color` : A string with a color name or hex value of the color the square should be.

    `infill` : Optional boolean parameter that decides if the square will be filled in. Defaults to True.

    `pensize` : Optional parameter that decides how large the pensize of the the turtle should be. Defaults to 5.
    """
    # defining turtle characteristics
    turt = Turtle()
    turt.hideturtle()
    turt.speed(0)
    turt.pensize(pensize)
    turt.color(color)
    turt.penup()
    turt.goto(start_at)
    turt.left(start_angle)
    turt.pendown()
    # drawing shape, filling if needed
    if infill is True:
        turt.fillcolor(color)
        turt.begin_fill()
        for i in range(4):
            turt.forward(sidelength)
            turt.left(90)
        turt.end_fill()
    else:
        for i in range(4):
            turt.forward(sidelength)
            turt.left(90)
    del turt


def draw_octagon(sidelength:int, start_angle:int, start_at:tuple, color, infill=True, pensize = 5):
    """
    Draws a square to an existing screen. Always draws from bottom left of shape.

    #### Parameters

    `sidelength` : How long the sides of the octagon should be, in integer format.

    `start_angle` : What angle to tilt the octagon. Always rotates left.

    `start_at` : A tuple containing x/y coordinates, in that order, of where to begin drawing the octagon.

    `color` : A string with a color name or hex value of the color the octagon should be.

    `infill` : Optional boolean parameter that decides if the octagon will be filled in. Defaults to True.

    `pensize` : Optional parameter that decides how large the pensize of the the turtle should be. Defaults to 5.
    """
    # defining turtle characteristics
    turt = Turtle()
    turt.hideturtle()
    turt.speed(0)
    turt.pensize(pensize)
    turt.color(color)
    turt.penup()
    turt.goto(start_at)
    turt.left(start_angle)
    turt.pendown()
    # drawing shape, filling if needed
    if infill is True:
        turt.fillcolor(color)
        turt.begin_fill()
        for i in range(8):
            turt.forward(sidelength)
            turt.left(45)
        turt.end_fill()
    else:
        for i in range(8):
            turt.forward(sidelength)
            turt.left(45)
    del turt


def draw_octagon(sidelength:int, start_angle:int, start_at:tuple, color, infill=True, pensize = 5):
    """
    Draws an octagon to an existing screen. Always draws from bottom left of shape.

    #### Parameters

    `sidelength` : How long the sides of the octagon should be, in integer format.

    `start_angle` : What angle to tilt the octagon. Always rotates left.

    `start_at` : A tuple containing x/y coordinates, in that order, of where to begin drawing the octagon.

    `color` : A string with a color name or hex value of the color the octagon should be.

    `infill` : Optional boolean parameter that decides if the octagon will be filled in. Defaults to True.

    `pensize` : Optional parameter that decides how large the pensize of the the turtle should be. Defaults to 5.
    """
    # defining turtle characteristics
    turt = Turtle()
    turt.hideturtle()
    turt.speed(0)
    turt.pensize(pensize)
    turt.color(color)
    turt.penup()
    turt.goto(start_at)
    turt.left(start_angle)
    turt.pendown()
    # drawing shape, filling if needed
    if infill is True:
        turt.fillcolor(color)
        turt.begin_fill()
        for i in range(8):
            turt.forward(sidelength)
            turt.left(45)
        turt.end_fill()
    else:
        for i in range(8):
            turt.forward(sidelength)
            turt.left(45)
    del turt


def draw_hexagon(sidelength:int, start_angle:int, start_at:tuple, color, infill=True, pensize = 5):
    """
    Draws a hexagon to an existing screen. Always draws from bottom left of shape.

    #### Parameters

    `sidelength` : How long the sides of the hexagon should be, in integer format.

    `start_angle` : What angle to tilt the hexagon. Always rotates left.

    `start_at` : A tuple containing x/y coordinates, in that order, of where to begin drawing the hexagon.

    `color` : A string with a color name or hex value of the color the hexagon should be.

    `infill` : Optional boolean parameter that decides if the hexagon will be filled in. Defaults to True.

    `pensize` : Optional parameter that decides how large the pensize of the the turtle should be. Defaults to 5.
    """
    # defining turtle characteristics
    turt = Turtle()
    turt.hideturtle()
    turt.speed(0)
    turt.pensize(pensize)
    turt.color(color)
    turt.penup()
    turt.goto(start_at)
    turt.left(start_angle)
    turt.pendown()
    # drawing shape, filling if needed
    if infill is True:
        turt.fillcolor(color)
        turt.begin_fill()
        for i in range(6):
            turt.forward(sidelength)
            turt.left(60)
        turt.end_fill()
    else:
        for i in range(6):
            turt.forward(sidelength)
            turt.left(60)
    del turt


def draw_equilateral_triangle(sidelength:int, start_angle:int, start_at:tuple, color, infill=True, pensize = 5):
    """
    Draws an equilateral triangle to an existing screen. Always draws from bottom left of shape.

    #### Parameters

    `sidelength` : How long the sides of the triangle should be, in integer format.

    `start_angle` : What angle to tilt the triangle. Always rotates left.

    `start_at` : A tuple containing x/y coordinates, in that order, of where to begin drawing the triangle.

    `color` : A string with a color name or hex value of the color the triangle should be.

    `infill` : Optional boolean parameter that decides if the triangle will be filled in. Defaults to True.

    `pensize` : Optional parameter that decides how large the pensize of the the turtle should be. Defaults to 5.
    """
    # defining turtle characteristics
    turt = Turtle()
    turt.hideturtle()
    turt.speed(0)
    turt.pensize(pensize)
    turt.color(color)
    turt.penup()
    turt.goto(start_at)
    turt.left(start_angle)
    turt.pendown()
    # drawing shape, filling if needed
    if infill is True:
        turt.fillcolor(color)
        turt.begin_fill()
        for i in range(3):
            turt.forward(sidelength)
            turt.left(120)
        turt.end_fill()
    else:
        for i in range(3):
            turt.forward(sidelength)
            turt.left(120)
    del turt


def draw_n_side_shape(num_sides:int, sidelength:int, start_angle:int, start_at:tuple, color, infill=True, pensize = 5):
    """
    Draws a shape with n amount of sides to an existing screen. Always draws from bottom left of shape.

    #### Parameters

    `num_side`: The number of sides the shape should have, as an integer. Values above 360 are allowed, although they tend to draw very slow circles.

    `sidelength` : How long the sides of the shape should be, in integer format.

    `start_angle` : What angle to tilt the shape. Always rotates left.

    `start_at` : A tuple containing x/y coordinates, in that order, of where to begin drawing the shape.

    `color` : A string with a color name or hex value of the color the shape should be.

    `infill` : Optional boolean parameter that decides if the shape will be filled in. Defaults to True.

    `pensize` : Optional parameter that decides how large the pensize of the the turtle should be. Defaults to 5.
    """
    # calculating the angles needed for the shape 
    angle = (360/num_sides)
    # defining turtle characteristics
    turt = Turtle()
    turt.hideturtle()
    turt.speed(0)
    turt.pensize(pensize)
    turt.color(color)
    turt.penup()
    turt.goto(start_at)
    turt.left(start_angle)
    turt.pendown()
    # drawing shape, filling if needed
    if infill is True:
        turt.fillcolor(color)
        turt.begin_fill()
        for i in range(num_sides):
            turt.forward(sidelength)
            turt.left(angle)
        turt.end_fill()
    else:
        for i in range(num_sides):
            turt.forward(sidelength)
            turt.left(angle)
    del turt