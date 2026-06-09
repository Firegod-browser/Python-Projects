import turtle
turtle.colormode(255)

turtle.speed(0)
for x in range(0,255,20):
    for y in range (0,255,20):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.color(x,y,int((x+y)/2))
        turtle.circle(10)
turtle.done()
