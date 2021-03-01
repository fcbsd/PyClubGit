import turtle
t = turtle.Pen()

sides = int(input("How many sides do you want? "))

colour = input("What colour would you like your shape's outline to be? ")

fill = input("What colour do you want your shape to be? ")

t.fillcolor(fill)
t.begin_fill()
for A in range(sides):
	t.pencolor(colour)
	t.forward(50)
	t.right(30)
t.end_fill()
