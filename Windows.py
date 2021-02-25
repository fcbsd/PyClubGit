import turtle
t=turtle.Pen()

def square():
  t.fillcolor("LightSkyBlue")
  t.begin_fill()
  for A in range(4):
    t.forward(100)
    t.left(90)
  t.end_fill()

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
