class Item():
	def __init__ (self, name, desc, cost, ingr):
		self.name = name
		self.description = desc
		self.cost = cost
		self.ingr = ingr


class Drinks(Item):
	def __init__(self, name, desc, cost, ingr, drink_type):
		super().__init__(name, desc, cost, ingr)
		self.menu_type = drink_type
		self.size = 500

class Dishes(Item):
	def __init__(self, name, desc, cost, ingr, course_type):
		super().__init__(name, desc, cost, ingr)
		self.menu_type = course_type









