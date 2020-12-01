class Menue():
	def __init__ (self):
		self.items = []

	def show_menu():
		print("Here is the menu for today:\n")
		print("****** STARTER DISHES ******")

		for i in items:
			if i.menu_type == "starter":
				print("<>", i.name, "-------", "£"+str(i.cost))
				print("    ", i.desc)
				print("Ingredients:\n", i.ingr)

			elif i.menu_type == "main":
				print("<>", i.name, "-------", "£"+str(i.cost))
				print("    ", i.desc)
				print("Ingredients:\n", i.ingr)


			elif i.menu_type == "desert":
				print("<>", i.name, "-------", "£"+str(i.cost))
				print("    ", i.desc)
				print("Ingredients:\n", i.ingr)


			elif i.menu_type == "drink":
				print("<>", i.name, "-------", "£"+ str(i.cost))
				print("    ", i.desc)
				print("Ingredients:\n", i.ingr)


	def add_item(i):
		self.items.append(i)




