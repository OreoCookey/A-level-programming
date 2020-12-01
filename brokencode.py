print("Welcome to the zoop!")


class animal():
	'''This is an animal class'''

	def __init__(self,
	             threat=0,
	             diet="unknown",
	             skin_colour="unknown",
	             mammal=True,
	             can_attack=True):
		self.threat = threat
		self.diet = diet
		self.skin_colour = skin_colour
		self.mammal = mammal
		self.can_attack = can_attack

	def Set_Threat(self):
		self.threat = int(input("Enter the animal's threat level:  "))

	def Set_Diet(self):
		self.diet = input("Enter the animal's diet :  ")

	def Set_Skin(self):
		self.skin_colour = input("Enter the animal's skin colour :  ")

	def Set_mammal(self):
		self.mammal = input("Mammal? True or False :  ")

	def Set_attack(self):
		self.can_attack = input("Can it attack? :  ")


print("First we will create the lions")


class lion(animal):
	'''This is a lion class'''

	def __init__(self, mane, pride_size, name):
		super().__init__()
		self.mane = mane
		self.pride = pride_size
		self.name = name
		self.Set_Threat()
		self.Set_Diet()
		self.Set_Skin()
		self.Set_mammal()
		self.Set_attack()


pride_size = int(input("How big is the lion pride?"))
lions = []
for i in range(0, pride_size):
	tempName = input("What is this lion's name?   ")
	tempMane = input("Does the lion have a mane?   ")
	if tempMane == "yes":
		tempMane2 = True
	else:
		tempMane2 = False
	tempLion = lion(tempMane2, pride_size, tempName)
	lions.append(tempLion)
for l in lions:
	print(l.name, "has been created")

print("Now we will create the giraffes")


class giraffe(animal):
	'''This is a giraffe class'''

	def __init__(self, neck_length, name):
		super().__init__()
		self.neck_length = neck_length
		self.name = name
		self.Set_Threat()
		self.Set_Diet()
		self.Set_Skin()
		self.Set_mammal()
		self.Set_attack()


tower_size = int(input("How big is the giraffe tower?"))
giraffes = []
for i in range(0, tower_size):
	tempName = input("What is this giraffe's name?   ")
	tempNeck = input("How long is the giraffe's neck?   ")
	tempGiraffe = giraffe(tempNeck, tempName)
	giraffes.append(tempGiraffe)
for l in giraffes:
	print(l.name, "has been created")
'''
def Attack(self):
  print (lion.name)
'''

Ans = input(
    "You have finished! Which animal enclousure would you like to view?  ")
if Ans == "lions" or "lion":
	print("This animal  has a threat level of ", lions[0].threat)
	print("It lives on a diet of", lion.diet)
	print("It has", a_lion.skin_colour, "skin")
	print("It's mammal status is", lion.mammal)
	if lion.can_attack == "yes" or "Yes":
		canAttack = "can"
	else:
		canAttack = "can't"
	if lion.mane == True:
		hasMane = "does"
	else:
		hasMane = "doesn't"
	print('The lion ', hasMane, "have a mane")
	willAttack = input("the lion ", canAttack, "attack, would you like it to?")
	if willAttack == "yes" or "Yes":
		Attack(self)
elif Ans == "giraffes" or "giraffe":
	print("This animal  has a threat level of ", giraffe.threat)
	print("It lives on a diet of", giraffe.diet)
	print("It has", giraffe.skin_colour, "skin")
	print("It's mammal status is", giraffe.mammal)
