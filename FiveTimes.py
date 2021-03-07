print("what times table would you like to know?")
number=input()
number=int(number)
num=0
for A in range(1,13):
  num+=1
  print(num,"times",number," =",(num*number))
