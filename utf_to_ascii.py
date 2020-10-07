done = False

n = int(input("How many characters would you like to convert: "))
a = ""
for i in range(n):
	user_input = input("Unicode: ")
	a = a + chr(user_input)

print(a)