import random
from os import system, name 

#player credit is £1 at the start
player_credit = 1

#possible rolls
posibilities = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]

#function to clear the screen
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#untill the player looses all the money
while player_credit > 0:
	#clear the screen
	player_input = input("Would you like to roll again? (y/n)")
	

	if player_input == "y":

		#lower case for case insensitive
		player_input = player_input.lower()

		#get the random rolls
		r1 = random.choice(posibilities)
		r2 = random.choice(posibilities)
		r3 = random.choice(posibilities)

		#check if all 3 are same
		if r1 == r2 and r1 == r3:

			#check the winnings
			if r1 == "Skull":
				player_credit = -1

			elif r1 == "Bell":
				player_credit = player_credit + 5

			else:
				player_credit = player_credit + 1

		elif r1 == r2 or r2 == r3 or r1 == r3:
			a = [r1, r2 ,r3]

			if a.count("Skull") == 2:
				player_credit = player_credit -1

			else:
				player_credit = player_credit + 0.5


		print(r1)
		print(r2)
		print(r3)
		print("Your credit is: £" + str(player_credit))
	elif player_input == "n":
		break

	else:
		print("Not a valid input")







