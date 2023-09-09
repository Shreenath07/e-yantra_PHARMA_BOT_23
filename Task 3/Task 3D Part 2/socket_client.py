'''
*****************************************************************************************
*
*        		===============================================
*           		Pharma Bot (PB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script is to implement Task 3D of Pharma Bot (PB) Theme (eYRC 2022-23).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

import socket
import time
import os, sys

def setup_client(host, port):

	"""
	Purpose:
	---
	This function creates a new socket client and then tries
    to connect to a socket server.

	Input Arguments:
	---
	`host` :	[ string ]
			host name or ip address for the server

	`port` : [ string ]
			integer value specifying port name
	Returns:

	`client` : [ socket object ]
	           a new client socket object
	---

	
	Example call:
	---
	client = setup_client(host, port)
	""" 

	client = None

	client =  socket.socket()
	client.connect((host,port	))
	return client

def receive_message_via_socket(client):
	"""
	Purpose:
	---
	This function listens for a message from the specified
	socket client and returns the message when received.

	Input Arguments:
	---
	`client` :	[ socket object ]
			socket client object created by setup_client() function
	Returns:
	---
	`message` : [ string ]
			message received through socket communication
	
	Example call:
	---
	message = receive_message_via_socket(connection)
	"""

	message = None

	message = client.recv(1024).decode()

	return message

def send_message_via_socket(client, message):
	"""
	Purpose:
	---
	This function sends a message over the specified socket client

	Input Arguments:
	---
	`client` :	[ socket object ]
			client socket object created by setup_client() function

	`message` : [ string ]
			message sent through socket communication

	Returns:
	---
	None
	
	Example call:
	---
	send_message_via_socket(connection, message)
	"""

	client.send(message.encode())


if __name__ == "__main__":

		host = "192.168.128.170"
		port = 5050

		try:
			client = setup_client(host, port)

		except socket.error as error:
			print("Error in setting up client")
			print(error)
			sys.exit()

		print("\nSTART command sent to PB Task 3D socket server\n")
		send_message_via_socket(client, "START")

		while True:
			
			message = receive_message_via_socket(client)
			if message == "SHUFFLE":
				break
			else:
				print("Received message from server: " + message)

		print("\nWaiting for shuffled phrase \n")

		while True:
			message = receive_message_via_socket(client)
			send_message_via_socket(client, message)
			if message == "KILL":
				print("\nSocket connection closed by server")
				break
			else:
				print("Received message from server: " + message)

