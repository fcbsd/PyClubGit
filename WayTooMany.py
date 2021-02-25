import turtle

t=turtle.Pen()

t.goto(-100,0)
def square():
  for A in range(4):
    t.forward(100)
    t.left(90)
    
def nextshape():
  t.penup()
  t.forward(10)
  t.pendown()
     
square()
nextshape()
square()
nextshape()
square()
nextshape()
square()
nextshape()
square()
nextshape()
square()
nextshape()
square()
nextshape()
square()
nextshape()
square()
nextshape()
square()

i = 0
while i < 10:
  i += 1
  square()
  nextshape()