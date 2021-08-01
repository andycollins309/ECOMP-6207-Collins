import turtle
shelly = turtle.Turtle()
#draw sky
turtle.bgcolor('skyBlue')
#move to draw grass
shelly.penup()
shelly.right(90)
shelly.forward(200)
shelly.right(90)
shelly.forward(420)
shelly.right(180)
#draw grass
shelly.begin_fill() 
shelly.color('green') 
for i in range (2):
    shelly.forward(880)
    shelly.right(90)
    shelly.forward(200)
    shelly.right(90)
shelly.end_fill() 
shelly.penup()
#move to draw trunk
shelly.forward(400)
shelly.left(90)
#draw trunk
shelly.pendown()
shelly.begin_fill()
shelly.color('#835C3B') 
for i in range (2):
    shelly.forward(300)
    shelly.right(90)
    shelly.forward(50)
    shelly.right(90)
shelly.end_fill()
#move to draw tree top
shelly.penup()
shelly.forward(300)
shelly.right(90)
shelly.forward(25)
#draw tree
shelly.pendown()
shelly.color('darkgreen')
#draw tree
for n in range(36):
# repeat 6 times - move forward and turn
    shelly.begin_fill()
    for i in range(6) :
        shelly.forward(50)
        shelly.left(60)
    shelly.right(10)
    shelly.end_fill()
#move to draw sun
shelly.penup()
shelly.left(90)
shelly.forward(400)
shelly.left(90)
shelly.forward(400)
#draw sun
shelly.begin_fill()
shelly.color('yellow')
shelly.circle(150)
shelly.end_fill()

