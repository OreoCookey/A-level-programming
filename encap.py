class ProtectedData():
	def __init__(self, initial_cash):
		self.__cash = initial_cash

	def show_balance(self):
		return self.__cash

	def add_money(self, m):
		self.__cash = self.__cash + m

	def remove_money(self, m):
		self.__cash = self.__cash + m


	balance = property(show_balance, add_money)  




class UnprotectedData():
	def __init__(self, initial_cash):
		self.cash = initial_cash

	def show_balance(self):
		print(str(self.cash))

	def add_money(self, m):
		self.cash = self.cash + m

	def remove_money(self, m):
		self.cash = self.cash + m



protected_account = ProtectedData(200)

print(protected_account.show_balance())

protected_account.balance = 400

print(protected_account.show_balance())



