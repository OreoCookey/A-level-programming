import random
from os import system, name 


#player credit is £1 at the start
player_credit = 1

#last credit
last_credit = 1

#highest ever credit
top_credit = 1

#rounds played
rounds_played = 0

#the round you had the top score
top_score_round = 0

#possible rolls
posibilities = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]

#run the machine once by default
player_input = "y"

#function to clear the screen
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


#function to run on game over
def gameover(last_credit, rounds_played, top_credit, top_score_round):
	while True:
		clear()
		print("I guess you lost all your money huh. Too bad")
		print("You played " + str(rounds_played) + " rounds")
		print("You could have had £" + str(last_credit) + " if you stoped last round")
		print("Your top credit was: £" + str(top_credit) + " in round " + str(top_score_round))
		u = input("Play again? (y/n)")
		u = u.lower()

		if u == "y":
			return True
		elif u == "n":
			return False
		else:
			pass

def user_quit(player_credit, rounds_played, top_credit, top_score_round):
	clear()
	print("You played " + str(rounds_played) + " rounds")
	print("You earned £" + str(player_credit))
	print("Your top credit was: £" + str(top_credit) + " in round " + str(top_score_round))
	print("Thank you for playing the game!")


#untill the player looses all the money
while True:
	
	if player_input == "y":
		#new credit will be calculated so asign current credit to last credit
		last_credit = player_credit

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

		print("You rolled:")
		print(r1)
		print(r2)
		print(r3)
		print("Your credit is: £" + str(player_credit))

		#update rounds played
		rounds_played = rounds_played + 1

		#check if its new highest score
		if player_credit > top_credit:
			top_credit = player_credit
			top_score_round  = rounds_played

		

	elif player_input == "n":
		#run the appropriate user quit screen
		user_quit(player_credit, rounds_played, top_credit, top_score_round)
		break

	else:
		print("Not a valid input")

	#check if players credit has run out
	if player_credit > 0:
		#player_input = "y"
		player_input = input("Would you like to roll again? (y/n)")
		clear()


	else:
		user_wants_to_restart = gameover(last_credit, rounds_played, top_credit, top_score_round)
		if user_wants_to_restart:
			#reset stats
			player_credit = 1
			last_credit = 1
			top_credit = 1
			rounds_played = 0
			top_score_round = 0
		else:
			break







