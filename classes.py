class person:
	def __init__(self, name, sname, age):
		self.name = name
		self.surname = sname
		self.age = age

	def greeting(self):
		print("Hi my name is " + self.name + " " + self.surname + ". Nice to meet you!")

	def saybye(self):
		print("Good Bye")


