#Name- Alexander Koschnitzki
#CSS- 225
# In this chapter, I was able to use different functions to
# help with talking to certain people and asking questions
# for the game to run the way it is suppose to run.
import sys
import time
# This is able to print the words slower to be able to
# read it easier.
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
print("*" * 100)
slowprint("Chapter 1 ")
print("*" * 100)
slowprint("It was a cold rainy night, the sirens of police cars filled the air")
slowprint("The young detective just arrived in there police car to the scene.")
slowprint("You decide on what action to do.")

# This is the function that brings you to a different
# function when you choose one of the numbers.
def action():
	choose_action()
	e = input("Choose one of the numbers :")
	while e:
		if e == '1':
			witness()
		elif e == '2':
			detective()
		elif e == '3':
			home()
		else:
			slowprint("Invalid option.")
			action()

# This function is one of the main ones where you talk
# to a witness.

def witness():
	while True:
		import random

		def people():
			global witnessName
			global response
			global witnessanswers

			response = ["Do you know who did it?", "Can you talk about what happened?", "Is everything ok?", "Did anyone get hurt"]
			witnessNameChoice = ["Ron", "Bobby", "Sam"]
			witnessanswers = ["That is interesting", "Hopefully you find the person"]

			random.shuffle(witnessNameChoice)
			witnessName = witnessNameChoice[0]

			print(witnessName, ":] Hello, I am ", witnessName, ", would you like to talk to me? :")
			random.shuffle(response)
			answer = input("Press y to talk to the witness :")

			random.shuffle(witnessanswers)
			witnessanswers = witnessanswers[0]
			if answer == "y":
				print(witnessName, ":] ", response[0])
				input("Y or N :")
				print(witnessanswers)

			elif answer == "n":
				print(witnessName, ":] Goodbye")

		people()
		x = input("Do you still want to ask more questions? :")
		if x == "n":
			break
	action()
# This function is another main one since you talk to the
# other detectives within the game.
def detective():
	while True:
		import random

		def police():
			global detectiveName
			global response
			global detectiveanswers

			response = ["Did you search for clues?", "Did you talk to any of the witnesses?"]
			detectiveNameChoice = ["Officer Gary", "Detective Stone"]
			detectiveanswers = ["That is interesting", "Hopefully you did"]

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
# This is the last option which is the one that ends the
# chapter when you choose yes.
def home():
	w = input("Would you like to go inside y/n")
	if w == "n":
		action()
	else:
		print("*" * 100)
		slowprint("End of Chapter 1")
		print("*" * 100)
		import ChapteR2
# This is the function that displays the options to be able
# to choose from.
def choose_action():
    print('*'*100)
    print("You can choose one of the following actions\n")
    print("1. Talk to witnesses.")
    print("2. Talk to detectives.")
    print("3. Go Inside home")
    print('*' * 100)
action()