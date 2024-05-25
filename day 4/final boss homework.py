import turtle
pen = turtle.Turtle()
pen.speed(100)
pen.pensize(2)

# Function to draw a rectangle
def draw_rectangle(t, width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Function to draw a triangle
def draw_triangle(t, length):
    for _ in range(3):
        t.forward(length)
        t.left(120)

# Function to draw the main palace structure
def draw_palace():
    # Main building
    pen.penup()
    pen.goto(-150, -100)
    pen.pendown()
    pen.color("black")
    draw_rectangle(pen, 300, 200)
    
    # Middle top structure
    pen.penup()
    pen.goto(-50, 100)
    pen.pendown()
    draw_triangle(pen, 100)
    
    # Left top structure
    pen.penup()
    pen.goto(-100, 100)
    pen.pendown()
    draw_triangle(pen, 50)
    
    # Right top structure
    pen.penup()
    pen.goto(50, 100)
    pen.pendown()
    draw_triangle(pen, 50)
    
    # Door
    pen.penup()
    pen.goto(-40, -100)
    pen.pendown()
    draw_rectangle(pen, 80, 100)
    pen.penup()
    pen.goto(-40, -100)
    pen.pendown()
    pen.goto(40, 0)
    pen.goto(40, -100)

    # Door bars
    for i in range(-30, 40, 15):
        pen.penup()
        pen.goto(i, -100)
        pen.pendown()
        pen.goto(i, 0)

    # Windows on the main building
    for i in [-100, -20, 60]:
        pen.penup()
        pen.goto(i, 0)
        pen.pendown()
        draw_rectangle(pen, 40, 80)
    
    # Left tower
    pen.penup()
    pen.goto(-200, -100)
    pen.pendown()
    draw_rectangle(pen, 50, 200)
    
    pen.penup()
    pen.goto(-200, 100)
    pen.pendown()
    draw_triangle(pen, 50)
    
    pen.penup()
    pen.goto(-200, 50)
    pen.pendown()
    draw_rectangle(pen, 30, 40)
    
    # Right tower
    pen.penup()
    pen.goto(150, -100)
    pen.pendown()
    draw_rectangle(pen, 50, 200)
    
    pen.penup()
    pen.goto(150, 100)
    pen.pendown()
    draw_triangle(pen, 50)
    
    pen.penup()
    pen.goto(150, 50)
    pen.pendown()
    draw_rectangle(pen, 30, 40)

# The flag
def draw_flag():
    pen.penup()
    pen.goto(-25, 150)
    pen.pendown()
    pen.left(90)
    pen.forward(80)
    pen.right(90)
    
    pen.penup()
    pen.goto(-25, 230)
    pen.pendown()
    pen.fillcolor("black")
    pen.begin_fill()
    draw_rectangle(pen, 120, 60)
    pen.end_fill()
    
    pen.penup()
    pen.goto(-20, 235)
    pen.pendown()
    pen.color("green")
    pen.write("GOA", font=("Arial", 28, "normal"))
# Mountains in the background
def draw_mountains():
    pen.penup()
    pen.goto(-300, 100)
    pen.pendown()
    pen.color("black")
    pen.goto(0, 300)
    pen.goto(300, 100)
    pen.penup()
    pen.goto(-150, 200)
    pen.pendown()
    pen.goto(0, 350)
    pen.goto(150, 200)

# End of the code
draw_mountains()
draw_palace()
draw_flag()


pen.hideturtle()
turtle.done()
