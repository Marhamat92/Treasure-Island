print('''

          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
''')
print("Welcome to tresure Island!")
print("Your mission is to find treasure to be millionaire!")
question1=input('You\'are in the middle of island.Do you want to go "left" or "right" ?\n').lower()

if question1=="left":
 question2=input('Do\'you want to "swim" or "wait" for the boat ?\n').lower()
 if question2=="wait":
  question3=input('There\' are 3 doors,which door you wish to choose? "yellow","red" or "blue" \n').lower()

  if question3=="yellow":
    print("YOU WİN")
  elif question3=="red":
     print("Burned by fire.GAME OVER")
  elif question3=="blue":
     print("Eaten by beasts.GAME OVER")
  else:
    print("You chose a door that doesn't exist")

 else:
   print("You have been attacked by angry trout.Game Over!")
else:
  print("you fell into a hole.GAME OVER")




