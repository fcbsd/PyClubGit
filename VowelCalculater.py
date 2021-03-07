YourSentence=str(input("Type a sentence and the vowel calculator will tell you how many vowels there are\n"))

yourvowel=str(input("What would you like the vowel calculator to calculate-you can type 'all the vowels'. "))

if yourvowel=="e":
  numberE=0
  for letter in YourSentence:
    if letter=="e" or letter=="E":
      numberE+=1
  print("The number of e's in the sentence is:",numberE)
  
if yourvowel=="a":
  numberE=0
  for letter in YourSentence:
    if letter=="a" or letter=="A":
      numberE+=1
  print("The number of a's in the sentence is:",numberE)
  
if yourvowel=="i":
  numberE=0
  for letter in YourSentence:
    if letter=="i" or letter=="I":
      numberE+=1
  print("The number of i's in the sentence is:",numberE)

if yourvowel=="u":
  numberE=0
  for letter in YourSentence:
    if letter=="u" or letter=="U":
      numberE+=1
  print("The number of u's in the sentence is:",numberE)

if yourvowel=="o":
  numberE=0
  for letter in YourSentence:
    if letter=="o" or letter=="O":
      numberE+=1
  print("The number of o's in the sentence is:",numberE)

if yourvowel=="all the vowels":
  numberE=0
  allvowels = ['a','A','e','E','i','I','o','O','u','U']
  for letter in YourSentence:
    if letter in allvowels:
      numberE+=1
  print("The number of vowels in the sentence is:",numberE)