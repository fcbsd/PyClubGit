import turtle 
t=turtle.Pen()

def nextshape():
  t.up()
  t.forward(20)
  t.down()
  
def nextrow():
  t.up()
  t.right(90)
  t.forward(20)
  t.right(90)
  t.forward(200)
  t.left(90)
  t.forward(5)
  t.left(90)
  t.down()

def square():
  for A in range(4):
    t.forward(10)
    t.left(90)

def squares():
  for A in range(10):
    square()
    nextshape()

t.up()
t.goto(-210,0)
t.down()
squares()
nextrow()
squares()
t.hideturtle()
