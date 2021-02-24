#! /usr/bin/env python3
# -*- coding: utf-8 -*-
score=0
print("Task 1\n")

my_name=input("Welcome to the hardest maths quiz you've ever taken!\nNow before we start I was wandering what's your name? ")
print("Well",my_name,"I'll give you an easy beginning, What is 63 / 7? ")
answer=input()
answer=int(answer)
if answer==9:
  print("great job, but don't get confident yet! The next question will be harder")
  score=score+1
else:
  print("The answer was 9, hopefully you'll get the next one right")
  score=score-1
print("Your current score is",score)

print("Here comes a harder question",my_name+",So what is 123 x 52")
answer=input()
anwser=int(answer)
if anwser==123*52:
  print("Ok,ok didn't think you'd get that one but the hardest questions are still left to come! ")
  score=score+1
else:
  print("The answer was",123*52,"but that one was hard so don't be down in the dumps!")
  score=score-1

print("Your current score is",score)

print("Time for question 3, did you know that 3 is my lucky number? Here comes the question, what is 0.69 x 7? ")
answer=input()
answer=float(answer)
if answer==0.69*7:
  print("Woohoo, that one was REALLY hard, you're amazing at maths!")
  score=score+2 
else:
  print("The answer was",0.69*7, "although that one was REALLY hard so I'm not surprised you didn't get it")
  score=score-1
print("Your current score is",score)
print("Qqqqqqqquestion 4 is what is 4 / 8?, bet you won't get this one",my_name+"!")
answer=input()
answer=float(answer)
if answer==4/8:
  print("Well done, no really REALLY well done!")
  score=score+2
else:
  print("The answer was",4/8,"better luck next time")
  score=score-1
print("Your current score is",score)

answer=input("Oh woah we're halfway there, the question for number 5 what is 34 x 8.9? ")
answer=float(answer)
if answer==34*8.9:
  print("Ok, I may have lied this was the penultimate question so are you ready for the final question!")
  score=score+2 
else:
  print("The answer was",34*8.9,"Ok, I may have lied this was the penultimate question so are you ready for the final question!")
  score=score-1
  
print("so",my_name,"are you ready for the fffffffinal question because it's coming your way what is 937 x 9? ")
answer=input()
answer=int(answer)

if answer==937*9:
  print("Wow, did you really just get that right I thought this one was impossible!")
  score=score+3 
else:
  print("I mean that was the hardest question in the word so I'm not surprised, maybe you'll do better next time!")
  score=score-1
  
print("That was so much fun",my_name,"I hope we get to do this again some other time, you want to know your overall score don't you, well to that I say your score is",score)

if score>=11:
  print("You are truly the master of maths! you got the highest score possible!")
elif score>=6:
  print("You got a pretty good score for the hardest maths quiz in the world")

elif score>=2:
  print("You didn't do that well in this quiz better luck next time")

elif score<=2:
  print("You did quite badly in this quiz, I hope it's helped you improve a little though")