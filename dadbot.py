#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Chat Bot: Dad's Version
'''
import random 

def getInput(questionPrompt, whoName="", errorMessage = 'Nothing was typed...'):
  if whoName != "":
    questiontext = whoName + " what's your favourite " + questionPrompt
  else:
    questiontext = "What's your favourite " + questionPrompt
  while True:
        value = input(questiontext)
        Reply = value.strip() 
        if Reply:
            return Reply
        else:
            print(errorMessage)

myName = ['Dad', 'Daddy', 'Fred', 'Nic', 'Mummy','Mum']

favQuestions = [
             "animal? ",
             "drink? ",
             "food? ",
             "sport? ",
             "teddy bear? ",
             "movie? ",
            ]

favAnswers = ["frogs", "juice", "pineapple", "bmx", "politoed", "frozen"]

orderList = [ 0, 1, 2, 3, 4, 5 ]

number = random.randrange(6)
random.shuffle(orderList)

print("Hello, I'm ", myName[number])
if myName[number] == "Mum" or myName[number] == "Mummy":
  print("Hold on! That's not my name I'm " + myName[random.randrange(5)] +"!")

yourName = input("What's your name? ")

print("Good to meet you " + yourName)
if yourName == 'Ally':
    print("I know a really clever girl called " + yourName)

score = 0 

for thisitem in orderList:
    answer = getInput(favQuestions[thisitem], yourName)
    if answer.lower() == favAnswers[thisitem]:
        print("Wow " + answer + " is also my favourite!")
        score += 1
    else:
        print(answer + ", that's interesting mine is " + favAnswers[thisitem])

if score < 2:
    print("we don't have much in common yet")
if score == 3:
    print("we like lots of the same things!")
if score >= 4:
    print("wow, we must be twins (OoO) <3")

print("Bye for now,",yourName,"see you later!")
#line 67 exists!