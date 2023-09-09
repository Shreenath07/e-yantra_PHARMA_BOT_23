'''
*****************************************************************************************
*
*        =================================================
*             Pharma Bot Theme (eYRC 2022-23)
*        =================================================
*                                                         
*  This script is intended for implementation of Task 2B   
*  of Pharma Bot (PB) Theme (eYRC 2022-23).
*
*  Filename:			task_2b.py
*  Created:				8/10/2022
*
*****************************************************************************************
'''

import  sys
import traceback
import time
import os
import math
from zmqRemoteApi import RemoteAPIClient
import zmq
import numpy as np
import cv2
import random



def control_logic(sim):
	"""
	Purpose:
	---
	This function should implement the control logic for the given problem statement
	You are required to make the robot follow the line to cover all the checkpoints
	and deliver packages at the correct locations.

	Input Arguments:
	---
	`sim`    :   [ object ]
		ZeroMQ RemoteAPI object

	Returns:
	---
	None

	Example call:
	---
	control_logic(sim)
	"""
	##############  ADD YOUR CODE HERE  ##############


	joint1=sim.getObjectHandle('left_joint')
	joint2=sim.getObjectHandle('right_joint')

	visionSensor = sim.getObjectHandle('vision_sensor')
	
	buff,res=sim.getVisionSensorImg(visionSensor)
	image = np.asarray(bytearray(buff), dtype="uint8").reshape(512,512,3)
	img = cv2.flip(image,0)

#	cv2.imshow('VisSen',image)
	cv2.imshow('VisSen2',img)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	ig = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	cv2.imshow('Gray',ig)
	ig2 = cv2.Canny(ig,245,255)
	
	cv2.imshow('Canny',ig2)
	
	contours, hierarchy = cv2.findContours(ig2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	blank = np.zeros(ig2.shape[:2],dtype='uint8')
	cv2.drawContours(blank,contours,-1,(255,0,0),1)
	cv2.imwrite('Contours.png',blank)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()


	for i in range(10):
		sim.setJointTargetVelocity(joint1,5)
		sim.setJointTargetVelocity(joint2,5)

	sim.setJointTargetVelocity(joint1,0)
	sim.setJointTargetVelocity(joint2,0)

	buff,res=sim.getVisionSensorImg(visionSensor)
	image = np.asarray(bytearray(buff), dtype="uint8").reshape(512,512,3)
	img = cv2.flip(image,0)

	cv2.imshow('VisSen',image)
	cv2.imshow('VisSen2',img)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	ig = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	cv2.imshow('Gray',ig)
	ig2 = cv2.Canny(ig,245,255)
	
	cv2.imshow('Canny',ig2)
	
	contours, hierarchy = cv2.findContours(ig2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cv2.imshow('Contours',ig2)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	for i in range(10):
		sim.setJointTargetVelocity(joint1,4)
		sim.setJointTargetVelocity(joint2,4)

	sim.setJointTargetVelocity(joint1,0)
	sim.setJointTargetVelocity(joint2,0)

	buff,res=sim.getVisionSensorImg(visionSensor)
	image = np.asarray(bytearray(buff), dtype="uint8").reshape(512,512,3)
	img = cv2.flip(image,0)

	cv2.imshow('VisSen',image)
	cv2.imshow('VisSen2',img)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	ig = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	cv2.imshow('Gray',ig)
	ig2 = cv2.Canny(ig,0,255)
	
	cv2.imshow('Canny',ig2)
	
	contours, hierarchy = cv2.findContours(ig2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cv2.imshow('Contours',ig2)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	


def read_qr_code(sim):
	"""
	Purpose:
	---
	This function detects the QR code present in the camera's field of view and
	returns the message encoded into it.

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
	return qr_message



if __name__ == "__main__":
	client = RemoteAPIClient()
	sim = client.getObject('sim')	

	try:

		try:
			return_code = sim.startSimulation()
			if sim.getSimulationState() != sim.simulation_stopped:
				print('\nSimulation started correctly in CoppeliaSim.')
			else:
				print('\nSimulation could not be started correctly in CoppeliaSim.')
				sys.exit()

		except Exception:
			print('\n[ERROR] Simulation could not be started !!')
			traceback.print_exc(file=sys.stdout)
			sys.exit()

		try:
			time.sleep(5)
			control_logic(sim)

		except Exception:
			print('\n[ERROR] Your control_logic function throwed an Exception, kindly debug your code!')
			print('Stop the CoppeliaSim simulation manually if required.\n')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()

		try:
			return_code = sim.stopSimulation()
			time.sleep(0.5)
			if sim.getSimulationState() == sim.simulation_stopped:
				print('\nSimulation stopped correctly in CoppeliaSim.')
			else:
				print('\nSimulation could not be stopped correctly in CoppeliaSim.')
				sys.exit()

		except Exception:
			print('\n[ERROR] Simulation could not be stopped !!')
			traceback.print_exc(file=sys.stdout)
			sys.exit()

	except KeyboardInterrupt:
		return_code = sim.stopSimulation()
		time.sleep(0.5)
		if sim.getSimulationState() == sim.simulation_stopped:
			print('\nSimulation interrupted by user in CoppeliaSim.')
		else:
			print('\nSimulation could not be interrupted. Stop the simulation manually .')
			sys.exit()
