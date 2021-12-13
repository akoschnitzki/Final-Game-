#Name- Alexander Koschnitzki
#CSS- 225
# In this chapter, I was able to use different functions
# to help the game. I was able to use them for searching for clues
# to help make the game.
import sys
import time
# This function is able to print the certain sentences slower
# to the speed that I choose.
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
# This is the intro to the chapter.
print("*" * 100)
slowprint("Chapter 2 ")
print("*" * 100)
slowprint("The blinding lights of camara flashes and sounds of detectives talking.")
slowprint("The player walked into the house where they saw the body of the one who was murdered. ")
slowprint("You decide on what action to do.")
# This is the function that goes to the certain function when you choose
# that certain number.
def action1():
	choose_action()
	e = input("Choose one of the numbers :")
	while e:
		if e == '1':
			house()
		elif e == '2':
			body()
		elif e == '3':
			home()
		else:
			slowprint("Invalid option.")
			action()
# This function is the one where it displays the
# choices you can choose from.
def choose_action():
    print('*'*100)
    print("You can choose one of the following actions\n")
    print("1. Search the house for clues.")
    print("2. Search the body for clues.")
    print("3. Leave house")
    print('*' * 100)
# This function is the one where you search the house
# for clues.
def house():
	while True:
		import random

		def house2():
			global floorNameChoice
			global response
			global evidenceName

			response = ["Good Idea", "Good thinking"]
			floorNameChoice = ["upstairs", "downstairs", "basement", "attic"]
			evidenceName = ["fingerprint", "broken glass"]

			random.shuffle(floorNameChoice)
			floorname = floorNameChoice[0]

			print("Would you like to search the", floorname, ":")
			random.shuffle(evidenceName)
			answer = input("Press y to search the floor :")

			random.shuffle(response)
			response = response[0]
			if answer == "y":
				print(floorname, ":", evidenceName[0])
				input("Y or N to keep it as evidence :")
				print(response)

			elif answer == "n":
				print("Maybe a different floor")

		house2()
		x = input("Do you still want to search for more clues? :")
		if x == "n":
			break
	action1()
# This function is the one where you search the body
# for clues.
def body():
	while True:
		import random

		def house2():
			global floorNameChoice
			global response
			global evidenceName

			response = ["Good Idea", "Good thinking", "Hopefully the right choice"]
			evidenceName = ["Wallet", "Money", "ID", "random hair"]

			print("Would you like to search the body")
			random.shuffle(evidenceName)
			answer = input("Press y to search the body y/n:")

			random.shuffle(response)
			response = response[0]
			if answer == "y":
				print("You found:", evidenceName[0])
				input("Y or N to keep it as evidence :")
				print(response)

			elif answer == "n":
				print("Maybe to keep searching")

		house2()
		x = input("Do you still want to search for more clues from the body? :")
		if x == "n":
			break
	action1()
# This function is the one that ends the chapter if you
# choose yes.
def home():
	w = input("Would you like to leave the house y/n :")
	if w == "n":
		action1()
	else:
		print("*" * 100)
		slowprint("End of Chapter 2")
		print("*" * 100)
		import ChapteR3
action1()