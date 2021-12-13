#Name- Alexander Koschnitzki
#CSS- 225
# In this module, I was able to make this my main game
# so it would be the start and run all the modules. It
# also uses some functions to run the game.
import sys
import time
# This is the function that prints the words slower.
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
# This is the intro to the game and it displays the title.
print("*" * 50)
print()
slowprint("The Hollow File")
print()
print("*" * 50)
# This is the action that you input the name of the user.
slowprint("A Game by Alexander Koschnitzki")
if __name__ == "__Main__":
	main()
x = input("Input User Name :")
print()
import ChapteR1

