# This program asks the user for a town
# it responds differently depending on where they are from

name = input("Hi there,\nI'm Mrs A, What is your name? ")
place = input("Nice to meet you "+name+" Where are you from? ")
if place == "Romsey" or place == "romsey":
    print("I LOVE Romsey")
elif place == "Southampton":
    print("Wow, Thats a busy City, I find that a bit intimidating!")
else:
    print("Oh, I have never been to "+place+" before.")
