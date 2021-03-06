#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle
t=turtle.Pen()
t.fillcolor("LightPink")
t.begin_fill()
t.pencolor("black")
t.pensize(1)
t.up()
t.setposition(0,-50)
t.down()
t.circle(100)
t.end_fill()
t.up()

def eye(x,y):
  t.setpos(x,y)
  t.pensize(10)
  t.pencolor("black")
  t.shape("circle")
  t.shapesize(3.5,1.5,1)
  t.fillcolor("black")
  t.stamp()
  t.up()
  t.setpos(x,y+12)
  t.shapesize(1)
  t.circle(10)
  t.fillcolor("white")
  t.stamp()
  t.shape("classic")

def semic(x,y,size):
  t.setpos(x,y)
  t.pencolor("black")
  t.pensize(1)
  t.fillcolor("blue")
  t.begin_fill()
  t.up()
  t.right(90)
  t.down()
  t.circle(size,180)
  t.left(90)
  t.forward(size*2)
  t.end_fill()
  #t.stamp()
  #t.shape("classic")
  t.up()

def arm(x,y,mycolour):
  t.setpos(x,y)
  t.fillcolor(mycolour)
  t.down()
  t.begin_fill()
  t.circle(30,200)
  t.end_fill()
  t.up()
  
def feet(x,y,mycolour):
  t.setpos(x,y)
  t.shape("circle")
  t.shapesize(4,3,2)
  t.fillcolor(mycolour)
  t.stamp()
  t.shape("classic")

def cheek(x,y,tilt,mycolour):
  t.setpos(x,y)
  t.tilt(tilt)
  t.shape("circle")
  t.shapesize(2,1.1,1)
  t.fillcolor(mycolour)
  t.stamp()
  t.shape("classic")


eyesize=10
eye(25,65)
eye(-25,65)
semic(15,40,eyesize)
t.left(180)
semic(-34,40,eyesize)

t.pencolor("black")
t.pensize(1)
t.left(180)
t.forward(132)
t.position()
 
arm(98,40,"LightPink")
arm(-98,50,"LightPink")
feet(40,-40,"red")
feet(-40,-40,"red")
cheek(60,30,45,"HotPink")
cheek(-60,30,0,"HotPink")

t.pencolor("black")
t.pensize(3)
t.goto(-20,10)
t.right(90)
t.down()
t.circle(30,100)
t.up()

t.pencolor("HotPink")
t.goto(0,-130)
t.write("Kirby", align='Center', font=('Courier',20))

t.hideturtle()