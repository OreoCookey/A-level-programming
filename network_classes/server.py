import socket
from _thread import *
import sys
import pickle

server_ip = "127.0.0.1"
server_port = 3000

#create a server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#threaded function to hndle connections to the server
def threaded_client(conn):
	#initial server responce on connect
	conn.send(pickle.dumps("You are connected"))

	reply = ""

	#while the connection is active
	while True:
		try:
			#recieve data if there is any
			data = pickle.loads(conn.recv(2048))
			reply = "Server recieved the folowing data: " + str(data)


			#if there is no data disconnect
			if not data:
				break

			else:
				print("Recieved:", data)
				print("Replied with:", reply)
				conn.sendall(pickle.dumps(reply))
			
		except:
			break

	print("Connection is lost")
	conn.close()



#try to bind to an address
try:
	server.bind((server_ip, server_port))
except Exception as e:
	print(e)


#listen for connections
server.listen(2)
print("Server is running. Waiting for connections")



#accept and handle all incoming connections
while True:
	#accept the connection
	conn, addr = server.accept()
	print(addr, "Connected")

	#start new thread to handle each individual connection
	start_new_thread(threaded_client, (conn,))



	



