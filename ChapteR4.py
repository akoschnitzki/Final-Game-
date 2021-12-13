#Name- Alexander Koschnitzki
#CSS- 225
# In this chapter, I was able to use functions to
# help talk to more people and to be able to search for more
# clues. This chapter is able to help understand more about
# what is going to happen in the last chapter.
import sys
import time
# This function is able to print slower and easier to read.
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
# This is the intro to the chapter 4.
print("*" * 100)
slowprint("Chapter 4 ")
print("*" * 100)
slowprint("As we come closer to the suspect home, all I can hear are questions I can ask")
slowprint("The player approaches the home with two other detectives.")
slowprint("You decide on what action to do.")
# This function is able to display the function that you choose
# from the certain numbers that you choose.
def action():
	choose_action()
	e = input("Choose one of the numbers :")
	while e:
		if e == '1':
			clues()
		elif e == '2':
			witness()
		elif e == '3':
			home()
		else:
			slowprint("Invalid option.")
			action()
# This function is able to display the choices that you can be able to
# choose from.
def choose_action():
    print('*'*100)
    print("You can choose one of the following actions\n")
    print("1. Search outside the home.")
    print("2. Knock on the door.")
    print("3. Leave the area.")
    print('*' * 100)
# This function is able to search outside the home to find
# more clues.
def clues():
	while True:
		import random

		def house2():
			global floorNameChoice
			global response
			global evidenceName

			response = ["Good Idea", "Good thinking", "Hopefully the right choice"]
			evidenceName = ["shovel", "Quarter", "broken glass", "A fresh dug hole in the backyard"]

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
# This function is able to talk to the witness and to be able
# to find out more.
def witness():
	while True:
		import random

		def house2():
			global floorNameChoice
			global response
			global evidenceName

			response = ["Yes", "No", "Maybe"]
			questionName = ["Do you know the victim?", "Have you ever been to this house?", "Did you dig that hole?"]

			print("Would you like to talk to the suspect?")
			random.shuffle(questionName)
			answer = input("Press y to ask questions y/n:")

			random.shuffle(response)
			response = response[0]
			if answer == "y":
				print(questionName[0])
				print("Suspect 1 ;", response)

			elif answer == "n":
				print("Maybe ask another")

		house2()
		x = input("Do you still want to ask more questions? y/n:")
		if x == "n":
			break
	slowprint("As you walk away, you hear him tell you that he knows who might of done it")
	action()
# This function is able to end the chapter and to go onto the
# next and last chapter.
def home():
	w = input("Would you like to go to the second suspect? y/n :")
	if w == "n":
		action()
	else:
		print("*" * 100)
		slowprint("End of Chapter 4")
		print("*" * 100)
		import ChapteR5
action()

