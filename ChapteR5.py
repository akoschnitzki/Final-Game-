#Name- Alexander Koschnitzki
#CSS- 225
# In this chapter, I was able to use functions to be
# able to end the game. There is two different ways the game
# can be able to end by the different choice that you
# can be able to make.
import sys
import time
# This function is able to print slower to be able to make it
# easier to read and you can change how fast it prints.
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
# This is the intro to the last chapter.
print("*" * 100)
slowprint("Chapter 5 ")
print("*" * 100)
slowprint("The car ride to the next one felt weird, I had a bad feeling something is going to happen")
slowprint("As you get to the house you get a bad feeling.")
slowprint("You decide on what action to do.")
# This is the function that displays the function when you choose the
# certain number that you pick.
def action():
	choose_action()
	e = input("Choose one of the numbers :")
	while e:
		if e == '1':
			house()
		elif e == '2':
			witness2()
		else:
			slowprint("Invalid option.")
			action()
# This function is able to display the options that you
# can be able to choose from.
def choose_action():
    print('*'*100)
    print("You can choose one of the following actions\n")
    print("1. Search outside the home.")
    print("2. Knock on the door.")
    print('*' * 100)
# This function is where you search outside for more clues
# and try to get more evidence.
def house():
	while True:
		import random

		def house2():
			global floorNameChoice
			global response
			global evidenceName

			response = ["Good Idea", "Good thinking", "Hopefully the right choice"]
			evidenceName = ["broken windows", "junk everywhere", "broken glass", "shovel with red liquid on it"]

			random.shuffle(evidenceName)
			answer = input("Would you like to search outside the home? y/n:")

			random.shuffle(response)
			response = response[0]
			if answer == "y":
				print("You found:", evidenceName[0])
				input("Y or N to keep it as evidence :")
				print(response)

			elif answer == "n":
				print("Maybe to keep searching")

		house2()
		x = input("Do you still want to search for more clues? y/n:")
		if x == "n":
			break
	action()
# This function is where you question the witness questions to
# find out more.
def witness2():
	while True:
		import random

		def house2():
			global floorNameChoice
			global response
			global evidenceName

			response = ["Yes", "No", "Maybe"]
			questionName = ["Do you know the victim?", "Have you ever been to this house?", "Is that your shovel in the yard?"]

			print("Would you like to talk to the suspect?")
			random.shuffle(questionName)
			answer = input("Press y to ask questions y/n:")

			random.shuffle(response)
			response = response[0]
			if answer == "y":
				print(questionName[0])
				print("Suspect 2 :", response)

			elif answer == "n":
				print("Maybe ask another")

		house2()
		x = input("Do you still want to ask more questions? y/n:")
		if x == "n":
			break
	slowprint("Suspect ask for me to go inside to find out more")
	z = input("Do you want to go inside? y/n: ")
	if z == "n":
		action3()
	else:
		part()
# This functions is where you get a choice to make and it decides how the
# game ends.
def part():
	slowprint("Suspect pulls a gun on you.")
	z = input("Do you want to pull your gun? y/n:")
	if z == "y":
		slowprint("Suspect shoots you")
		print("*" * 100)
		slowprint("You Died")
		slowprint("End of Game")
		slowprint("THANK YOU FOR PLAYING")
		print("*" * 100)
		exit()
	else:
		slowprint("You talk the suspect to drop the gun")
		slowprint("You are able to arrest him")
		print("*" * 100)
		slowprint("End of Game")
		slowprint("THANK YOU FOR PLAYING")
		print("*" * 100)
		exit()
# This function is another way that the game ends.
def action3():
	slowprint("You did not find the murderer")
	slowprint("You did not get your big arrest")
	print("*" * 100)
	slowprint("End of Game")
	slowprint("THANK YOU FOR PLAYING")
	print("*" * 100)
	exit()

action()