import random as r
number=r.randint(1,100)
guesscount=0
guess=int(input("Guess a number from 1-100\n OK, GO!! "))
while guess !=number:
  guesscount+=1
  if guess<number:
    print(guess,"is too low, try again: ")
    guess=int(input())
  else:
    print(guess,"is too high, try again: ")
    guess=int(input())
print("Great job, the anwser was",number,"and you got it in",guesscount,"guesses")

 