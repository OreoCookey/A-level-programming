import time
import sys


def fib(n):
	count = 1
	n0 = 1
	n1 = 1
	a = 0

	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		while True:
			count = count + 1
			a = n0 + n1

			n0 = n1
			n1 = a

			if count == n:
				break


		return a

r = int(sys.argv[1])
r2 = int(sys.argv[2])
r3 = int(sys.argv[3])

for i in range(int(r), int(r2+1), int(r3)):
	start = time.time()
	a = fib(i)


	t = time.time()-start
	print(t)