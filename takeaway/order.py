class Order():
	def __init__(self, n):
		self.order_number = n
		self.items = []
		self.total_cost = 0

	def add_to_order(self, item, quantity):
		for i in range(quantity):
			self.items.append(item)
			self.total_cost += item.cost


	def remove_from_order(self, item_name, quantity):
		for i in range(quantity):
			try:
				for i in self.items:
					if i.name == item_name:
						index_to_remove = self.items.index(i)
						break
				self.total_cost = cost -= self.items[index_to_remove].cost
				del self.items[index_to_remove]

			except ValueError:
				print("There is no such item in your menue")

	def show_order():
		print("Your order consists of the following items:")
		for i in self.items:
			print(i)

