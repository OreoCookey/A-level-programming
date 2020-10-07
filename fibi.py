import sys
import time

def fib(n):
	if n == 1:
		return 1
	elif n == 0:
		return 1
	else:
		return fib(n-1) + fib(n-2)



u = int(sys.argv[1])
u2 = int(sys.argv[2])
#u = int(input(": "))
#u2 = int(input(": "))

for i in range(u, u2+1):

	start = time.time()
	a = str(fib(i))
	t =str(time.time()-start)

	print(t)

