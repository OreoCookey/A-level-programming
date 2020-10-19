import socket
import time
import pickle

#The main network class
class Network():
	def __init__(self, host, port):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host = host
		self.port = port
		self.addr = (self.host, self.port)
		self.connected = False
		self.id = self.connect()
		print(self.id)


	#method used to establish the initial connection
	def connect(self):
		try:
			#connect and recieve the reply from the server
			self.client.connect(self.addr)
			return pickle.loads(self.client.recv(2048))
		except Exception as e:
			print("Couldn't establish a connection to the server")
			print(e)


	#method used to send data to the server
	def send(self, data):
		try:
			#sends data to the server and returns server reply
			self.client.send(pickle.dumps(data))
			return pickle.loads(self.client.recv(2048))
		except Exception as e:
			print(e)


n = Network("127.0.0.1", 3000)

print(n.send("Hello"))
time.sleep(3)
print(n.send("This is a test"))



		


