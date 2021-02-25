import turtle
t=turtle.Pen()
t.shape("turtle")

def square():
  t.fillcolor("LightSkyBlue")
  t.begin_fill()
  for A in range(4):
    t.forward(100)
    t.left(90)
  t.end_fill()

t.goto(-100,0)
square()
t.penup()
t.forward(110)
t.pendown()
square()

t.penup()
t.right(90)
t.forward(10)
t.pendown()
square()

t.penup()
t.left(270)
t.forward(10)
t.pendown()

square()

t.up()
t.forward(120)
t.left(90)
t.forward(130)
t.left(90)
t.down()
t.forward(260)
t.left(90)
t.forward(270)
t.left(90)
t.forward(270)
t.left(90)
t.forward(270)
t.left(90)
t.forward(10)

t.up()
t.goto(60,30)
t.down()
t.fillcolor("yellow")
t.begin_fill()
t.circle(30)
t.end_fill()
t.up()
t.fillcolor("green")
t.left(45)
t.goto(-140,-157)
t.shape("turtle")
A=1 
while A <7:
  t.shapesize(A)
  A=A+1
t.stamp()


t.hideturtle()