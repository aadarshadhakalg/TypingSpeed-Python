#This script requires python installed in the system.
#This script requires 'datetime' module to run properly without errors.
#This script is written by Aadarsha Dhakal (@aadarshadhakalg)

import datetime

print("This is a typing speed checker python script.")
print("Note: User are requested to type as soon as you are requested for input")


#Takes user decision, to start the test.
ustate=input("Are you ready for Typing Speed test? y = Yes and n = no : ")
if ustate=="y":
	#This block records the start time in seconds and print the start time.
	x=datetime.datetime.now()
	isec=x.strftime("%S")
	imin=x.strftime("%M")
	total_it=int(imin)*60+int(isec)
	print("Typing start time: ", x)
	
	#This block creates a temporary file to store typed text.
	
	file=open("temp.txt","w")
	sample=("Namaste! Nepal is a beautiful country situated in South Asia. (Heaven is myth, Nepal is real)")
	print(sample)
	text=input("Please type above text here: ")
	
	#This block records the end time in seconds and prints end time. 
	
	y=datetime.datetime.now()
	fsec=y.strftime("%S")
	fmin=y.strftime("%M")
	total_ft=int(fmin)*60+int(fsec)
	print("Typing end time: ", y)
	
	#This block writes user input to the temporary file and calculate typing speed.
	
	chars=file.write(text)
	tdiff=float(total_ft)-float(total_it)
	print("Your taken time: ", tdiff)
	total_char=len(text)
	tspeed=float(total_char/tdiff)
	print("Your typing speed is: ", tspeed, "charecters per second")
	
	#Error Calculation
	
	if len(sample)<=len(text):
		counter=0
		error=0
		while counter < len(sample):
			if sample[counter]==text[counter]:
				error=error+0
			else:
				error=error+1
			counter=counter+1
	elif len(text)<=len(sample):
		counter=0
		error=0
		while counter < len(text):
			if sample[counter]==text[counter]:
				error=error+0
			else:
				error=error+1
				counter=counter+1
	print("Errors: ", error,"characters")

elif ustate=="n":
	print("Thank You!")
else:
	print("Invalid Input!")


#Funny experience: I got error 28 times while writing this simple script. 
#still noob
#Thank You
