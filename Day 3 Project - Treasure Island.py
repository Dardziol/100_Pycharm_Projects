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
 _________|___________| ;`-.o`"=._; ." ` '`."'` . "-._ /_______________|_______
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

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
print("*******************************************************************************")
print("After hours of traveling through the jungle, you've finally found an entrance to the temple.\n"
      "You can feel a soft breeze from the left side but unfortunately,\n"
      "There's absolutely no source of light as you go further.\n"
      "The only thing that can help you see through the darkness is your lighter.\n"
      "It won't last long and there are 2 tunnels ahead of you.\n"
      "You have only one chance!")
print("*******************************************************************************")
choice = input("Would you like to go left or right?\n").lower()
if choice == "left":
    print("*******************************************************************************")
    print("You've made a right choice as just when you reached the end of a tunnel your lighter went out.\n"
          "After a long walk you've reached a lake and felt very tired.\n"
          "The water is clean and it looks safe to swim.")
    print("*******************************************************************************")
    choice1 = input("Would you like to swim or wait?\n").lower()
    if choice1 == "wait":
        print("*******************************************************************************")
        print("You've decided to wait and rest.\n"
              "You woke up by the sound of a raft that landed on a shore.\n"
              "You decided to use it to swam across the lake but you reached the temple again.\n"
              "You could swear that you're on the same place that you've first saw it but this time,\n"
              "There are mysterious doors in various colors.\nThey have to lead to a treasure!\n"
              "You sense some danger.\n"
              "You have to act fast.")
        print("*******************************************************************************")
        choice2 = input("What color will you choose? Yellow, Red or Blue?\n").lower()
        print("*******************************************************************************")
        if choice2 == "yellow":
            print("CONGRATULATIONS! YOU'VE FOUND A TREASURE!")
        elif choice2 == "red":
            print("You took 5 steps and stepped on a floor button that triggered a trap.\n"
                  "The whole corridor went up in flames.\n"
                  "Burned by fire.\n"
                  "GAME OVER!")
        elif choice2 == "blue":
            print("Just when you opened the blue door you heard a strange noise.\n"
                  "What might that be?\n"
                  "Noises started to become louder and grew in numbers when suddenly,\n"
                  "You noticed one small creature that you've never saw before draw your attention.\n"
                  "You've decided to take a closer look but then you noticed\n"
                  "That there's swarm of larger creatures right above it starting at you.\n"
                  "Slowly you started to step back but the creatures jumped at you.\n"
                  "You were eaten by beasts.\n"
                  "GAME OVER!")
        else:
            print("GAME OVER!")
    else:
        print("You were attacked by a trout.\n"
              "You tried to swim back to the shore but lost stamina too quickly.\n"
              "You drowned.\n"
              "GAME OVER!")
else:
    print("'Damn, that tunnel is so long' you said to yourself.\n"
          "You feel like it's been hours since you've entered it and your lighter died out at least 15 minutes ago.\n"
          "You decided to go further by sticking to the walls as you couldn't see anything.\n"
          "Unfortunately, you reached a very slippery place and fell into a hole.\n"
          "GAME OVER!")
