import turtle 
t=turtle.Pen()

def square():
  for A in range(4):
    t.forward(50)
    t.left(90)


def star():
  angle=144
  for A in range(5):
    t.right(angle)
    t.forward(100)
    
def nextsquare():
  t.up()
  t.forward(75)
  t.down()

t.up()
t.goto(-100,100)
t.down()
star()
t.up()
t.goto(-100,-50)
t.down()

for A in range(4):
  square()
  nextsquare()

t.hideturtle()