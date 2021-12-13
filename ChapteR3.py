#Name- Alexander Koschnitzki
#CSS- 225
# In this chapter, I was able to use more functions
# to talk to more people and to be able to go over the
# clues that were founded earlier in the game.
import sys
import time
# This function is able to slow down the input of the words.
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
# This is the intro to this chapter.
print("*" * 100)
slowprint("Chapter 3 ")
print("*" * 100)
slowprint("A long car ride back to the station, a lot of thoughts flooded my mind")
slowprint("The player walks into the police station.")
slowprint("You decide on what action to do.")
# This is the function that goes to the certain function when you
# choose that number.
def action():
	choose_action()
	e = input("Choose one of the numbers :")
	while e:
		if e == '1':
			detective()
		elif e == '2':
			clues()
		elif e == '3':
			suspect()
		else:
			slowprint("Invalid option.")
			action()
# This is the function that displays the options that
# you can be able to choose.
def choose_action():
    print('*'*100)
    print("You can choose one of the following actions\n")
    print("1. Talk to the detectives.")
    print("2. Examine the clues.")
    print("3. Go to the first suspect.")
    print('*' * 100)
# This function is able to run the action of talking to
# the detectives.
def detective():
	while True:
		import random

		def police():
			global detectiveName
			global response
			global detectiveanswers

			response = ["Did you search for clues?", "Was there a lot of clues?", "Are the clues helpful?", ]
			detectiveNameChoice = ["Detective Cole", "Detective Taylor", "Officer Stevens"]
			detectiveanswers = ["That is interesting", "Hopefully they were"]

			random.shuffle(detectiveNameChoice)
			detectiveName = detectiveNameChoice[0]

			print(detectiveName, ":] Hello, I am ", detectiveName, ", would you like to talk to me?")
			random.shuffle(response)
			answer = input("Press y to talk to the officer")

			random.shuffle(detectiveanswers)
			detectiveanswers = detectiveanswers[0]
			if answer == "y":
				print(detectiveName, ":] ", response[0])
				input("Y or N :")
				print(detectiveanswers)

			elif answer == "n":
				print(detectiveName, ":] Goodbye")

		police()
		x = input("Do you still want to ask more questions? :")
		if x == "n":
			break
	action()
# This function is able to run the action of the clues and
# to go over the clues that you have found.
def clues():
	while True:
		import random

		def house2():
			global response
			global evidenceName

			response = ["Good Idea", "Good thinking", "Hopefully the right choice", "Maybe", "That is a good choice"]
			evidenceName = ["Wallet", "Money", "ID", "random hair", "finger print", "glass"]

			print("Would you like to examine the clues?")
			random.shuffle(evidenceName)
			answer = input("Press y to examine clues y/n:")

			random.shuffle(response)
			response = response[0]
			if answer == "y":
				print("Evidence is:", evidenceName[0])
				input("Y or N if it will be useful to find the murder:")
				print(response)

			elif answer == "n":
				print("Maybe a different evidence")

		house2()
		x = input("Do you still want to examine more evidence? :")
		if x == "n":
			break
	action()
# This function is to end the chapter and to go on to the
# next chapter.
def suspect():
	w = input("Would you like to go to the first suspect? y/n :")
	if w == "n":
		action()
	else:
		print("*" * 100)
		slowprint("End of Chapter 3")
		print("*" * 100)
		import ChapteR4
action()