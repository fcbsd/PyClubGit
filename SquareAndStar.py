import turtle 
t=turtle.Pen()

def square():
  for A in range(4):
    t.forward(100)
    t.left(90)

def star():
  for A in range(5):
    t.forward(75)
    t.left(36)
    
star()