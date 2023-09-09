'''
*****************************************************************************************
*
*        =================================================
*             Pharma Bot Theme (eYRC 2022-23)
*        =================================================
*
*  This script is intended for implementation of Task 4A
*  of Pharma Bot (PB) Theme (eYRC 2022-23).
*
*  Filename:			task_4a.py
*  Created:            		02/01/2023
*  Author:			e-Yantra Team
*****************************************************************************************
'''

import numpy as np
import cv2
from zmqRemoteApi import RemoteAPIClient
import zmq
import os
import time

def transform_coord(x,y):
    a = (x * 1.825)/700  + (-0.9125)
    b = (y * 1.825)/700 + (-0.9125)
    return a,-b

def find_coord(barricade):
    x1,y1 = get_coord(barricade[:2])
    x2,y2 = get_coord(barricade[3:])

    x = (x1+x2)/2
    y = (y1+y2)/2

    return x,y

def get_coord(Node):
    x = 0.89125 - 0.3575 * (ord(Node[0]) - 65)
    y = 0.89125 - 0.3575 * (int(Node[1]) -1)
    return -x,y

def place_packages(medicine_package_details, sim, all_models):
    """
	Purpose:
	---
	This function takes details (colour, shape and shop) of the packages present in 
    the arena (using "detect_arena_parameters" function from task_1a.py) and places
    them on the virtual arena. The packages should be inserted only into the 
    designated areas in each shop as mentioned in the Task document.

    Functions from Regular API References should be used to set the position of the 
    packages.

	Input Arguments:
	---
	`medicine_package_details` :	[ list ]
                                nested list containing details of the medicine packages present.
                                Each element of this list will contain 
                                - Shop number as Shop_n
                                - Color of the package as a string
                                - Shape of the package as a string
                                - Centroid co-ordinates of the package			

    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	Returns:


    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	
	Example call:
	---
	all_models = place_packages(medicine_package_details, sim, all_models)
	"""
    models_directory = os.getcwd()
    packages_models_directory = os.path.join(models_directory, "package_models")
    arena = sim.getObject('/Arena')    
    _2d_to_3d = {
                'Square' : 'cube',
                'Circle' : 'cylinder',
                'Triangle' : 'cone'
    }
    handles = {}
    x = [-1 for i in range(5)]
    for i in range(len(medicine_package_details)):
        package = medicine_package_details[i]
        s_n = int(package[0][-1])
        handles[i] = sim.loadModel(packages_models_directory+'/'+package[1]+'_'+_2d_to_3d[package[2]]+'.ttm')
        x[s_n-1] += 1
        sim.setObjectAlias(handles[i],package[1]+'_'+_2d_to_3d[package[2]])
        sim.setObjectPosition(handles[i],arena,[-0.830 + x[s_n -1]*0.0785 + (s_n-1)* 0.3575,0.687,0.0150])
        sim.setObjectParent(handles[i],arena,True)
        all_models.append(handles[i])    


    return all_models

def place_traffic_signals(traffic_signals, sim, all_models):
    """
	Purpose:
	---
	This function takes position of the traffic signals present in 
    the arena (using "detect_arena_parameters" function from task_1a.py) and places
    them on the virtual arena. The signal should be inserted at a particular node.

    Functions from Regular API References should be used to set the position of the 
    signals.

	Input Arguments:
	---
	`traffic_signals` : [ list ]
			list containing nodes in which traffic signals are present

    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	Returns:

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	None
	
	Example call:
	---
	all_models = place_traffic_signals(traffic_signals, sim, all_models)
	"""
    models_directory = os.getcwd()
    traffic_sig_model = os.path.join(models_directory, "signals", "traffic_signal.ttm" )
    arena = sim.getObject('/Arena')   
    handle = {}
    for i in range(len(traffic_signals)):
        handle[i] = sim.loadModel(traffic_sig_model)
        x,y=get_coord(traffic_signals[i])
        sim.setObjectAlias(handle[i],"Signal_"+traffic_signals[i])
        sim.setObjectPosition(handle[i],arena,[x,y,0.1528])
        sim.setObjectParent(handle[i],arena,True)
        all_models.append(handle[i])

    return all_models

def place_start_end_nodes(start_node, end_node, sim, all_models):
    """
	Purpose:
	---
	This function takes position of start and end nodes present in 
    the arena and places them on the virtual arena. 
    The models should be inserted at a particular node.

    Functions from Regular API References should be used to set the position of the 
    start and end nodes.

	Input Arguments:
	---
	`start_node` : [ string ]
    `end_node` : [ string ]
					

    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	Returns:

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	---
	None
	
	Example call:
	---
	all_models = place_start_end_nodes(start_node, end_node, sim, all_models)
	"""
    models_directory = os.getcwd()
    start_node_model = os.path.join(models_directory, "signals", "start_node.ttm" )
    end_node_model = os.path.join(models_directory, "signals", "end_node.ttm" )
    arena = sim.getObject('/Arena')   

    handle_s = sim.loadModel(start_node_model)
    x,y = get_coord(start_node)
    sim.setObjectAlias(handle_s,'Start_Node')
    sim.setObjectPosition(handle_s,arena,[x,y,0.1528])
    sim.setObjectParent(handle_s,arena,True)
    all_models.append(handle_s)

    handle_e = sim.loadModel(end_node_model)
    x,y = get_coord(end_node)
    sim.setObjectAlias(handle_e,'End_Node')
    sim.setObjectPosition(handle_e,arena,[x,y,0.1528])
    sim.setObjectParent(handle_e,arena,True)
    all_models.append(handle_e)
    return all_models

def place_horizontal_barricade(horizontal_roads_under_construction, sim, all_models):
    """
	Purpose:
	---
	This function takes the list of missing horizontal roads present in 
    the arena (using "detect_arena_parameters" function from task_1a.py) and places
    horizontal barricades on virtual arena. The barricade should be inserted 
    between two nodes as shown in Task document.

    Functions from Regular API References should be used to set the position of the 
    horizontal barricades.

	Input Arguments:
	---
	`horizontal_roads_under_construction` : [ list ]
			list containing missing horizontal links		

    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	Returns:

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	---
	None
	
	Example call:
	---
	all_models = place_horizontal_barricade(horizontal_roads_under_construction, sim, all_models)
	"""
    models_directory = os.getcwd()
    horiz_barricade_model = os.path.join(models_directory, "barricades", "horizontal_barricade.ttm" )
    arena = sim.getObject('/Arena')  

    handle = {}
    for i in range(len(horizontal_roads_under_construction)):
        barricade = horizontal_roads_under_construction[i]
        handle[i] = sim.loadModel(horiz_barricade_model)
        x,y = find_coord(barricade)
        sim.setObjectAlias(handle[i],'Horizontal_missing_road_'+barricade.replace('-','_'))
        sim.setObjectPosition(handle[i],arena,[x,y,0.0150])
        sim.setObjectParent(handle[i],arena,True)
        all_models.append(handle[i])
    return all_models


def place_vertical_barricade(vertical_roads_under_construction, sim, all_models):
    """
	Purpose:
	---
	This function takes the list of missing vertical roads present in 
    the arena (using "detect_arena_parameters" function from task_1a.py) and places
    vertical barricades on virtual arena. The barricade should be inserted 
    between two nodes as shown in Task document.

    Functions from Regular API References should be used to set the position of the 
    vertical barricades.

	Input Arguments:
	---
	`vertical_roads_under_construction` : [ list ]
			list containing missing vertical links		

    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	Returns:

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	---
	None
	
	Example call:
	---
	all_models = place_vertical_barricade(vertical_roads_under_construction, sim, all_models)
	"""
    models_directory = os.getcwd()
    vert_barricade_model = os.path.join(models_directory, "barricades", "vertical_barricade.ttm" )
    arena = sim.getObject('/Arena') 
    handle = {}
    for i in range(len(vertical_roads_under_construction)):
        barricade = vertical_roads_under_construction[i]
        handle[i] = sim.loadModel(vert_barricade_model)
        x,y = find_coord(barricade)
        sim.setObjectAlias(handle[i],'Vertical_missing_road_'+barricade.replace('-','_'))
        sim.setObjectPosition(handle[i],arena,[x,y,0.0150])
        sim.setObjectParent(handle[i],arena,True)
        all_models.append(handle[i])
    return all_models

if __name__ == "__main__":
    client = RemoteAPIClient()
    sim = client.getObject('sim')
    img_dir = os.getcwd() + "\\test_imgs\\"

    i = 0
    config_img = cv2.imread(img_dir + 'maze_' + str(i) + '.png')

    print('\n============================================')
    print('\nFor maze_0.png')
  
    all_models = []

    task_1 = __import__('task_1a')
    detected_arena_parameters = task_1.detect_arena_parameters(config_img)

    medicine_package_details = detected_arena_parameters['medicine_packages']
    traffic_signals = detected_arena_parameters['traffic_signals']
    start_node = detected_arena_parameters['start_node']
    end_node = detected_arena_parameters['end_node']
    horizontal_roads_under_construction = detected_arena_parameters['horizontal_roads_under_construction']
    vertical_roads_under_construction = detected_arena_parameters['vertical_roads_under_construction'] 

    print("[1] Setting up the scene in CoppeliaSim")
    all_models = place_packages(medicine_package_details, sim, all_models)
    all_models = place_traffic_signals(traffic_signals, sim, all_models)
    all_models = place_horizontal_barricade(horizontal_roads_under_construction, sim, all_models)
    all_models = place_vertical_barricade(vertical_roads_under_construction, sim, all_models)
    all_models = place_start_end_nodes(start_node, end_node, sim, all_models)
    print("[2] Completed setting up the scene in CoppeliaSim")

    time.sleep(10)
    print("[3] Removing models for maze_0.png")

    for i in all_models:
        sim.removeModel(i)

   
    choice = input('\nDo you want to run your script on all test images ? => "y" or "n": ')
    
    if choice == 'y':
        for i in range(1,5):

            print('\n============================================')
            print('\nFor maze_' + str(i) +'.png')
            config_img = cv2.imread(img_dir + 'maze_' + str(i) + '.png')

            all_models = []
            task_1 = __import__('task_1a')
            detected_arena_parameters = task_1.detect_arena_parameters(config_img)

            medicine_package_details = detected_arena_parameters["medicine_packages"]
            traffic_signals = detected_arena_parameters['traffic_signals']
            start_node = detected_arena_parameters['start_node']
            end_node = detected_arena_parameters['end_node']
            horizontal_roads_under_construction = detected_arena_parameters['horizontal_roads_under_construction']
            vertical_roads_under_construction = detected_arena_parameters['vertical_roads_under_construction'] 

            print("[1] Setting up the scene in CoppeliaSim")
            place_packages(medicine_package_details, sim, all_models)
            place_traffic_signals(traffic_signals, sim, all_models)
            place_horizontal_barricade(horizontal_roads_under_construction, sim, all_models)
            place_vertical_barricade(vertical_roads_under_construction, sim, all_models)
            place_start_end_nodes(start_node, end_node, sim, all_models)
            print("[2] Completed setting up the scene in CoppeliaSim")

            time.sleep(10)
            print("[3] Removing models for maze_" + str(i) + '.png')
            for i in all_models:
                sim.removeModel(i)
            
