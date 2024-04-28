from turtle import *


# we wanna paint a house

#step 1: draw a square 
speed(30)
width(8)
color("gray")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()

#end of square

#drawing a door
forward(70)
left(90)
color("brown")
begin_fill()
forward(100) #height of the door
right(90)
forward(50)
right(90)
forward(100)
end_fill()
#start of the roof

penup()
goto(200, 200)
pendown()
color("maroon")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
left(120)
forward(200)
end_fill()

#end of the roof

#start of the left window
penup()
goto(0, 170)
pendown()
color("blue")
begin_fill()
forward(70)
right(90)
forward(40)
right(90)
forward(70)
right(90)
forward(40)
end_fill()

#end of the left window

#start of the right window
penup()
goto(200, 170)
pendown()
begin_fill()
left(90)
forward(70)
left(90)
forward(40)
left(90)
forward(70)
left(90)
forward(40)
end_fill()
     
#left window detailing
penup()
goto(35, 170)
color("gray")
back(40)
pendown()
forward(40)
penup()
goto(70, 150)
left(90)
pendown()
forward(70)

#right window detailing
penup()
goto(200,150)
color("gray")
pendown()
forward(70)
penup()
goto(165, 170)
right(90)
back(40)
pendown()
forward(40)





exitonclick()