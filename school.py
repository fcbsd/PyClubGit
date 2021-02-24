print("Task 2\n")

name=input("What is your name? ")
print("Hello",name,"how old are you? ")
age=input()
age=int(age)
if age>=18:
  print("You should be going to a university, collage or workplace")
elif age>=11:
  print("You should be going to secondary school")
elif age>4:
  print("You should be going to primary school")
elif age<=4:
  print("You should be going to nursery")
workplace_education=input("What is the name of where you get educated or work? ")

print("How many miles is",workplace_education,"from your house?")
miles=input()
miles=int(miles)
if age>=18:
  print("You should buy your own house or")
if age<=4:
  print("Your parents should take you to nursery or if your parents allow it")

if miles>=2:
  print("You should get a bus or a train")
elif miles==1:
  print("Why don't you cycle to school?")
elif miles<1:
  print("You should walk to school")

