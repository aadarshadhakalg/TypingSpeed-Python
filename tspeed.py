#This script requires python installed in the system.
#This script requires 'datetime' module to run properly without errors.
#This script is written by Aadarsha Dhakal (@aadarshadhakalg)

import datetime
import time
import os


def choice(char):
	if char =="y":
		return True
	elif char == "n":
		return False
	else:
		raise Exception("Invalid")

def check(sample, text):
	# Error Calculation

	if len(sample) <= len(text):
		counter = 0
		error = 0
		while counter < len(sample):
			if sample[counter] == text[counter]:
				error = error + 0
			else:
				error = error + 1
			counter = counter + 1
	elif len(text) <= len(sample):
		counter = 0
		error = 0
		while counter < len(text):
			if sample[counter] == text[counter]:
				error = error + 0
			else:
				error = error + 1
				counter = counter + 1
	print("Errors: ", error, "characters")

def main():
	os.system('clear||cls')
	print()

	print("This is a typing speed checker python script.")
	print("Note: User are requested to type as soon as you are requested for input")


	#Takes user decision, to start the test.
	ustate=input("Are you ready for Typing Speed test? y = Yes and n = no : ")
	try:
		choice(ustate)
		if choice(ustate):
			#This block records the start time in seconds and print the start time.
			x = datetime.datetime.now()
			print("Typing start time: %s:%s:%s" % (x.hour, x.minute, x.second))

			#This block creates a temporary file to store typed text.

			sample=("Namaste! Nepal is a beautiful country situated in South Asia. (Heaven is myth, Nepal is real)")
			print(len(sample))
			t1 = time.perf_counter()

			text=input("Please type above text here: ")
			t2=time.perf_counter()


			#This block records the end time in seconds and prints end time.
			y = datetime.datetime.now()
			check(sample, text)
			print("-"*80)
			print("RESULT")

			print("Typing end time: %s:%s:%s" % (y.hour, y.minute, y.second))

			#This block writes user input to the temporary file and calculate typing speed.

			tdiff = t2 - t1
			print("Your taken time: ", tdiff)
			total_char=len(text)
			tspeed=float(total_char/tdiff)
			print("Your typing speed is: ", tspeed, "charecters per second")

		else:
			print("Thank You!")
	except:
		print("Invalid Input!")
		main()

#Funny experience: I got error 28 times while writing this simple script.
#still noob
#Thank You


if __name__ == '__main__':
    main()



