alive_students = []

def student_exists(s):
	for i in alive_students:
		if i.name == s:
			return True

	return False

def student_index(s, all_s):
	for i in all_s:
		if i.name == s:
			return all_s.index(i)


class Student():
	def __init__(self, name, studentID, tutor, year, strength, shield):
		self.name = name
		self.studentID = studentID
		self.tutor = tutor
		self.year = year
		self.strength = strength
		self.health = 100
		self.alive = True
		if shield <= 80:
			self.shield = shield
		else:
			self.shield = 0

	def fight(self, op_name):
		if student_exists(op_name):
			opp_student_index = student_index(op_name, alive_students)
			oponent = alive_students[opp_student_index]
			oponent.take_damage(self.strength)


		else:
			print("No such students or they are dead")


	def powerup(self):
		self.strength += 10

	def heal(self):
		self.health += 20

	def strengthboost(self):
		self.strength = self.strength*2
		self.shield = self.shield*(1/5)

	def shieldboost(self):
		self.strength = self.strength*(1/5)
		self.shield = self.shield*2



	def take_damage(self, damage):
		damage = (damage* ((100- self.shield)/100))
		self.health -= damage
		print(self.name + " : took "  + str(damage) + " damage")

		if self.health <= 0:
			self.alive = False
			print(self.name, "died")
			global alive_students
			del alive_students[student_index(self.name, alive_students)]

	def make_love(self, p):
		global alive_students
		if student_exists(p):
			partner_index = student_index(p, alive_students)
			partner = alive_students[partner_index]

			kid_name = self.name + "-" + partner.name
			kid_id = self.studentID
			kid_tutor = self.tutor
			kid_year = self.year
			kid_strength = (self.strength + partner.strength)/2
			kid_shield = (self.shield+partner.shield)/2

			kid = Student(kid_name, kid_id, kid_tutor, kid_year, kid_strength, kid_shield)
			alive_students.append(kid)

			print(self.name, "and",  partner.name, "made a baby")

		else:
			print("No such student exists or they are dead")



eugene = Student("Eugene", 123, "DVAD", "12", 20, 50)
trump = Student("Trump", 124, "None", "Boomer", 5, 10)

alive_students.append(eugene)
alive_students.append(trump)


