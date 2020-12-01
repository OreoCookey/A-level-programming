class Person():
	def __init__ (self, name, surname):
		self.name = name
		self.surname = name

	def introduce(self):
		print(self.name, self.surname)



class Student(Person):
	pass