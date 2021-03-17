print('''
*******************************************************************************
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
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You find yourself on the beach. Where do you want to go? Type "Forrst" or "Cave" \n').lower()
if choice1 == "forrest":
  choice2 = input('Now that your in the forrest, you have come to a fork! Type "Left" or "Right". \n').lower()
  if choice2 == "right":
    choice3 = input('You followed the right path which has lead you to the tempele of teasure! You now have 2 option. To enter through the front door or via the roof! Type "Door" or "Roof" \n').lower()
    if choice3 == "roof":
      print("You climb to the top of tempele, where you absaile down to find the hidden Treasure! YOU WIN!")
    else: 
      print("You took front door which was booby trapped. GAME OVER! ")
  else:
    print("You took the left turning which took you to the hidden tribe, who hold you hostage. GAME OVER!")


else:
  print("You fell into the cave and was trapped forever. GAME OVER!")