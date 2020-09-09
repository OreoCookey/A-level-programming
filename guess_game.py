import random
import sys

#check if the number is prime
def isprime(number):
	if number < 2:
		return False

	else:
		for i in range(2, (number-1)):
			if number % i == 0:
				return False

		return True


#run on user quit
def quit_screen(total_score):
	print("Thanks for playing the game")
	print("Your overall balance is £" + str(total_score))
	sys.exit(0)

#min guesse number
max_g = 30
#max guesse number
min_g = 0

#cost
cost = 1

#overall score
total_score = 0


#main loop
while True:

	#score multiplier
	mult = 1

	#validating the input
	while True:

		#get user inout
		user_input = input("What number would you like to bet? or type 'quit'")
	
		#if its a number check it s with in the correct range and check if its an interger
		try: 
			user_input = int(user_input)
			if user_input <= max_g and user_input >= min_g and user_input >= 0:
				break
			else:
				print("The input is outside of the guesse boundary")
		except:
			#if not an interger check if its a quit command
			if user_input == "quit" or user_input == "q":
				quit_screen(total_score)
				break
			else:
				print("Not a valid input")


	#asking to input the money
	while True:
		try:
			#original user balance
			balance = int(input("How much money would you like to bet?: "))
			break
		except:
			print("Not a valid input")





	#quit programm if user wants to quit
	if user_input == "quit" or user_input == "q":
		quit_screen(total_score)
		break

	#calculate game logic
	else:
		#generate the random number
		random_number = random.randint(min_g, max_g) 

		#calculate the multiplier
		if user_input % 2 == 0:
			mult = mult * 2
		if user_input % 10 == 0:
			mult = mult * 3
		if isprime(user_input):
			mult = mult * 5
		if user_input < 5:
			mult = mult * 2


		if user_input == random_number:
			print("Congrats! You won £" + str(balance*mult) + "!")
			total_score = total_score + (balance*mult)


		else:
			print("Tooo bad")
			print("Your betted on number " + str(user_input))
			print("The actual number was:" + str(random_number))

			total_score = total_score - (balance*mult)

			print("Your overall balance is £" + str(total_score))


