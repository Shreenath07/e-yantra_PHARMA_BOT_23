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
from zmqRemoteApi import RemoteAPIClient
import traceback
import zmq
import numpy as np
import cv2
from pyzbar.pyzbar import decode

def read_qr_code(sim):
	"""
	Purpose:
	---
	This function detects the QR code present in the CoppeliaSim vision sensor's 
	field of view and returns the message encoded into it.

	Input Arguments:
	---
	`sim`    :   [ object ]
		ZeroMQ RemoteAPI object

	Returns:
	---
	`qr_message`   :    [ string ]
		QR message retrieved from reading QR code

	Example call:
	---
	control_logic(sim)
	"""
	qr_message = None
	visionSensor = sim.getObjectHandle('vision_sensor')
	buff,res=sim.getVisionSensorImg(visionSensor)

	image = np.asarray(bytearray(buff), dtype="uint8").reshape(512,512,3)
	img = cv2.flip(image,0)

	QR = decode(img)
	qr_message = QR[0].data.decode()
	return qr_message


def setup_server(host, port):

	"""
	Purpose:
	---
	This function creates a new socket server and then binds it 
	to a host and port specified by user.

	Input Arguments:
	---
	`host` :	[ string ]
			host name or ip address for the server

	`port` : [ int ]
			integer value specifying port number
	Returns:

	`server` : [ socket object ]
	---

	
	Example call:
	---
	server = setup_server(host, port)
	""" 
	server = None
	server = socket.socket()
	server.bind((host,port))
	return server

def setup_connection(server):
	"""
	Purpose:
	---
	This function listens for an incoming socket client and
	accepts the connection request

	Input Arguments:
	---
	`server` :	[ socket object ]
			socket object created by setupServer() function
	Returns:
	---
	`connection` : [ socket object ]
	        socket connection object

	`address` : [ tuple ]
	        address of socket connection
	
	Example call:
	---
	connection, address = setup_connection(server)
	"""
	connection = None
	address = None
	server.listen()
	connection , address = server.accept()

	return connection, address

def receive_message_via_socket(connection):
	"""
	Purpose:
	---
	This function listens for a message from the specified
	socket connection and returns the message when received.

	Input Arguments:
	---
	`connection` :	[ connection object ]
			connection object created by setupConnection() function
	Returns:
	---
	`message` : [ string ]
			message received through socket communication
	
	Example call:
	---
	message = receive_message_via_socket(connection)
	"""

	message = None
	message = connection.recv(1024).decode()
	return message

def send_message_via_socket(connection, message):
	"""
	Purpose:
	---
	This function sends a message over the specified socket connection

	Input Arguments:
	---
	`connection` :	[ connection object ]
			connection object created by setupConnection() function

	`message` : [ string ]
			message sent through socket communication

	Returns:
	---
	None
	
	Example call:
	---
	send_message_via_socket(connection, message)
	"""
	connection.send(message.encode())

if __name__ == "__main__":
	
	host = ''
	port = 5050

	try:
		server = setup_server(host, port)


	except socket.error as error:
		print("Error in setting up server")
		print(error)
		sys.exit()


	try:
		print("\nPlease run PB_task3d_socket.exe program and choose Part 3")
		connection_1, address_1 = setup_connection(server)
		print("Connected to: " + address_1[0] + ":" + str(address_1[1]))

	except KeyboardInterrupt:
		sys.exit()

	try:
		print("\nPlease run socket_client_rgb.py program")
		connection_2, address_2 = setup_connection(server)
		print("Connected to: " + address_2[0] + ":" + str(address_2[1]))

	except KeyboardInterrupt:
		sys.exit()

	send_message_via_socket(connection_1, "START")
	send_message_via_socket(connection_2, "START")

	time.sleep(5)

	client = RemoteAPIClient()
	sim = client.getObject('sim')

	while True:

		message = receive_message_via_socket(connection_1)

		if message == "READ_QR":
			color = read_qr_code(sim)
			print("QR details read: ", color)
			send_message_via_socket(connection_2, color)
			send_message_via_socket(connection_1, color)
			pass


		elif message == "STOP":

			send_message_via_socket(connection_2, "STOP")

			connection_1.close()
			connection_2.close()
			server.close()
			print("\nSocket Connections closed !!")
			print("Task 3D Part 3 execution stopped !!")
			break
		else:
			pass

