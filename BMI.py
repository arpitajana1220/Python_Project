"""
It is important to keep track of a persons BMI, which is an important indicator of health 
this program helps you to analyse your BMI in 5 category severely underweight, underweight, severely overweight, overweight, Healthy
This simple program can be integrated in projects to add more value to client or can be used as self help calculator.
"""
#Taking inputs from user
Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))

#Calculating 
Height = Height/100
BMI=Weight/(Height*Height)

#Displaying BMI
print("your Body Mass Index is: ",BMI)

#Categorising BMI
if(BMI>0):
	if(BMI<=16):
		print("you are severely underweight")
	elif(BMI<=18.5):
		print("you are underweight")
	elif(BMI<=25):
		print("you are Healthy")
	elif(BMI<=30):
		print("you are overweight")
	else: print("you are severely overweight")
else:("enter valid details")
