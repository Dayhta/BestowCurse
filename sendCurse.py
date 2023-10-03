import socket
import sys


try:
	target_host = sys.argv[1]
	target_port = 0 
	
	#Create a socket object
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	#Connect the Client
	client.connect((target_host,target_port))
	
	#Send data
	client.send(f"GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n")
	
	#Receive some data
	response = client.recv(4096)
	
	print(response.decode())
	client.close()

except IndexError:
	print("[+] ERROR | Please provide a host. \n\n    'EX: python3 google.com'")
