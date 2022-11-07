inventory = ["tentacle sweeper", "cat", "cake", "gun"]
greeting_txt = """ """   # this is for large amounts of text, can go down multiple lines

words = "hello world"
numLs = int(0)

words2 = "python"

numbers = [2, 3, 5, 7, 66, 89, 134]
output = []

# activity 6
playerInventory = ["Flashlight"]

print("To see your inventory, type inventory.")
print("You are in a dark room, you can not see anything.")
option = input("").lower()

if option == "inventory":
    print(playerInventory)

else:
    print("You cannot see")

flashlight = input("What would you like to do? ").lower()
if flashlight == "use":
    print("You are in a kitchen.")
    print("There is a door to the left, it looks to be locked,")
    yes_no = input("Would you like to search the room?").lower()
    if yes_no == "yes":
        print("There is a box on the counter, it looks as though it was recently added.")
        yes_no2 = input("Would you like to open it?").lower()

        if yes_no2 == "yes":
            print("key")

        elif yes_no2 == "no":
            print("they key was in there, tough luck")

        else:
            print("I do not understand")

    elif yes_no == "no":
        print("Then what was the point?")

    else:
        print("I do not understand")

elif flashlight == "inventory":
    print(playerInventory)

else:
    print("I do not understand.")


# activity 5
attempts = 3

while attempts > 0:
    password = input("Please enter password: ")
    attempts -= 1

    if password == "password":
        print("Welcome")
        break
    else:
        print("wrong password ")
        print(attempts, " attempts remaining")

else:
    print("you lost")

# activity 4
numEntered = input("Please enter number: ")
numEntered = int(numEntered)

for i in numbers:
    if i < numEntered:
        output.append(i)
    print(output)

# activity 3
print("")
print(words2)
for letter in words2:
    if letter.lower() == "t":
        print(words2.replace("t", ""))

# activity 2
for letters in words:
    if letters.lower() == "l":
        numLs += 1

print("")
print(numLs)

# activity 1
print("")
openIn = input("Oh no...A tentacle monster...You should check your inventory to see if you have anything to fight it. ")

if openIn == "open inventory":
    print(inventory)
    fightMonster = input("What do you use to fight it? ").lower()  # .lower() allows it to be written in capitals too

    if fightMonster == inventory[0]:
        print("Yay you beat it.")

    elif fightMonster == inventory[1]:
        print("Why would you do that, the cat dies.")

    elif fightMonster == inventory[2]:
        print("It eats the cake and you die.")

    elif fightMonster == inventory[3]:
        print("You have one bullet, you go to shoot but the monster takes the gun and shoots you.")

    else:
        print("That wasn't an option.")
        exit()

else:
    print("That is wrong.")
    exit()
