<a name="br1"></a> 

12/1/22, 9:38 PM

PB Task 3A - Instructions - Pharma Bot (PB) / Task 3 - e-Yantra

[**PB**](https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062)[** ](https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062)[Task**](https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062)[** ](https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062)[3A**](https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062)[** ](https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062)[-**](https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062)[** ](https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062)[Instructions**](https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062)

[**shyama**](https://discuss.e-yantra.org/u/shyama)[** ](https://discuss.e-yantra.org/u/shyama)[e-Yantra**](https://discuss.e-yantra.org/g/eyantra_staff)[** ](https://discuss.e-yantra.org/g/eyantra_staff)[Staff**](https://discuss.e-yantra.org/g/eyantra_staff)

[**9d**](https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062?u=niranjangunaseelan)

Task 3A

Path Planning

**1. Introduction to Path Planning**

**1.1 What is path planning ?**

Motion planning or path planning (also known as the navigation problem or the piano mover's

problem) is a computational problem to find a sequence of valid configurations that moves the

object from the source to destination. The term is used in computational geometry, computer

animation, robotics and computer games.

For example, consider navigating a mobile robot inside a building to a distant waypoint. It

should execute this task while avoiding walls and not falling down stairs. A motion planning

algorithm would take a description of these tasks as input, and produce the speed and turning

commands sent to the robot’s wheels. Motion planning algorithms might address robots with a

larger number of joints (e.g., industrial manipulators), more complex tasks (e.g. manipulation

of objects), different constraints (e.g., a car that can only drive forward), and uncertainty (e.g.

imperfect models of the environment or robot).

Motion planning has several robotics applications, such as autonomy, automation, and robot

design in CAD software, as well as applications in other fields, such as animating digital

characters, video games, architectural design, robotic surgery, and the study of biological

molecules.

**1.2 Tree search algorithms**

Once a space is represented as a graph, there are classic shortest-path graph algorithms that

can guarantee the shortest path is found, if given unlimited computation time and resources.

**Dijkstra’s algorithm**

**Skip to main content**

https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062

1/9



<a name="br2"></a> 

12/1/22, 9:38 PM

PB Task 3A - Instructions - Pharma Bot (PB) / Task 3 - e-Yantra

Dijkstra's algorithm creates a set of “visited” and “unvisited” nodes. An initial starting node is

assigned a distance of zero and all other node’s distance values are set to infinity (from the

start node). Then, each neighbor is visited and its distance from the current node is

determined, if the distance is less than the previously defined distance value, then the value is

updated. Once all neighboring values are updated, the algorithm moves the current node to

the “visited” set and repeats the process of the next neighboring node with the shortest

distance value. The algorithm continues until all nodes have been moved from “unvisited” to

“visited”.

**A\* algorithm**

A\* is another path-finding algorithm that extends Dijkstra’s algorithm by adding heuristics to

stop certain unnecessary nodes from being searched. This is done by weighting the cost

values of each node distance by their euclidean distance from the desired endpoint.

Therefore, only paths that are headed generally in the correct direction will be evaluated.

**Various other algorithms like D\*, RRT, RRT\*, etc exist too.**

Here, Robots follow a line on the floor with smooth PID control - more control theory, but

closely related to real-time path planning.

Video:

**2. Problem Statement**

**2.1 Task 3A Folder Layout**

**Skip to main content**

Download and extract the following Task 3A folder based on your OS

https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062

2/9



<a name="br3"></a> 

12/1/22, 9:38 PM

PB Task 3A - Instructions - Pharma Bot (PB) / Task 3 - e-Yantra

**1. PB Task 3A Ubuntu**

**2. PB Task 3A Windows**

Task 3A folder has the following layout

***Task3A*** folder

task\_3a.py

***test\_images*** folder

**maze\_000.png** to **maze\_009.png**

**test\_task\_3a.exe** (for windows) or **test\_task\_3a** (for ubuntu)

**2.2 Problem Statement**

Each image in the ***test\_images*** folder of Task 3A contains **a 5x5 grid containing 25 cells**.

A sample image can be found below for reference:

**Figure 1: Sample maze image**

The horizontal missing lines are called **horizontal roads under construction** and

vertical missing lines are called **vertical roads under construction**.

The intersections of the grid lines (roads) are called **NODES** and are represented with

**blue squares**. Each node is represented by a combination of a letter and a number

where the letter is a reference to the column (A-F) and number refers to the row (1-6).

Some of these nodes have **Traffic Signals** represented by **Red Squares**.

**Skip to main content e** is the **Start Node**.

The **purple square** is the **End Node**.

https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062

3/9



<a name="br4"></a> 

12/1/22, 9:38 PM

PB Task 3A - Instructions - Pharma Bot (PB) / Task 3 - e-Yantra

**2.3 Problem Description**

The aim of this task is to find the shortest path from the **start node (green node)** to the **end**

**node (purple node)** using all the functions given below:

1\. **Detect all types of nodes** which are present in the image like traffic\_signals (all nodes

which are traffic signals), start\_node and end\_node.

Example: In above figure, there is a traffic signal present at node 'C5', start\_node at

'E6'and end node at 'A4'

2\. **Detect all the nodes neighbouring to a particular node**.

Eg. : { "D3":{"C3", "E3", "D2", "D4" }, "D5":{"C5", "D4", "D6", "E5" }

}

3\. **Detect all arena parameters**, this will call and store all arena parameters in dictionary

format.

4\. Do the **Path Planning** for the shortest path using the graph

**Note:** You can use any path planning algorithm for this but need to produce the path

in the form of list as shown here

['E6', 'D6', 'D5', 'D4', 'C4', 'B4', 'A4']

5\. Now convert the **paths to moves** that the robot needs to take

Eg. : ['LEFT', 'RIGHT', 'STRAIGHT', 'LEFT', 'STRAIGHT', 'WAIT\_5',

'STRAIGHT']

**NOTE : The possible moves are [ 'LEFT', 'RIGHT', 'STRAIGHT', 'WAIT\_5',**

**'REVERSE' ]**

**Moves**

**STRAIGHT**

**RIGHT**

**Action by the bot**

Move 1 unit of black road from a node to neighbor node

Turn 90 degrees clockwise and move straight by 1 unit of black road

Turn 90 degrees anti-clockwise and move straight by 1 unit of black road

Wait for 5 second at the traffic signal node (red node)

**LEFT**

**WAIT\_5**

**REVERSE**

Turn 180 degree and move straight by 1 unit of black road

Example - The output for the above figure is,

**Figure 2: Example Output for Figure 1 maze image**

**Skip to main content**

**3. Task Instructions**

https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062

4/9



<a name="br5"></a> 

12/1/22, 9:38 PM

PB Task 3A - Instructions - Pharma Bot (PB) / Task 3 - e-Yantra

For this part of the task we have provided a **“snippet”** of outline code in the task\_3a.pyfile:

Teams are NOT allowed to import any other library/module, other than the ones already

imported in the task\_3a.py

Teams are NOT allowed to edit the **main()** function.

Teams should modify the following functions for completing the code and implementing

this task

The following 5 functions are to be completed in the given task\_3a.pyscript

**3.1 detect\_all\_nodes()**

**Function**

**detect\_all\_nodes()**

**name**

This function takes the image as an argument and returns a list of nodes in

which traffic signals, start\_node and end\_node are present in the image

**Purpose**

**Input**

**maze\_image : [ NumPy array ]**

**Argument**

numpy array of image returned by cv2 library

**traffic\_signals, start\_node, end\_node : [ list ], str, str**

**Returns**

list containing nodes in which traffic signals are present, start and end node too

**Example**

**Call**

**traffic\_signals, start\_node, end\_node =**

**detect\_all\_nodes(maze\_image)**

**3.2 detect\_paths\_to\_graph()**

**Function**

**name**

**detect\_paths\_to\_graph()**

This function takes the image as an argument and returns a dictionary of the

connect path from a node to other nodes and will be used for path planning

**Purpose**

**Input**

**maze\_image : [ NumPy array ]**

**Argument**

numpy array of image returned by cv2 library

**paths: { dictionary }**

**Returns**

Every node’s connection to other node

**Example**

**Call**

**paths = detect\_paths\_to\_graph(maze\_image)**

**3.3 detect\_arena\_parameters()**

**Function**

**detect\_arena\_parameters()**

**name**

This function takes the image as an argument and returns a dictionary

taining the details of the different arena parameters in that image

**Purpose**

**Skip to main content**

https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062

5/9



<a name="br6"></a> 

12/1/22, 9:38 PM

PB Task 3A - Instructions - Pharma Bot (PB) / Task 3 - e-Yantra

**Function**

**detect\_arena\_parameters()**

**name**

**Input**

**maze\_image : [ NumPy array ]**

**Argument**

numpy array of image returned by cv2 library

**arena\_parameters : { dictionary }**

**Returns**

dictionary containing details of the arena parameters

**Example**

**Call**

**arena\_parameters = detect\_arena\_parameters(maze\_image)**

**3.4 path\_planning()**

**Function**

**name**

**path\_planning()**

This function takes the graph(dict), start and end node for planning the

shortest path

**Purpose**

**Input**

**graph, start, end : [ numpy array ], str, str**

**Argument**

numpy array of image returned by cv2 library

**backtrace\_path : [ list of nodes ]**

**Returns**

list of nodes, produced using path planning algorithm

**Example Call**

**arena\_parameters = detect\_arena\_parameters(maze\_image)**

**Note: You can use any path planning algorithm for this but need to produce the**

**path in the form of list given below**

**3.5 paths\_to\_moves()**

**Function**

**paths\_to\_moves()**

**name**

This function takes the list of all nodes produces from the path planning

algorithm and connecting both start and end nodes

**Purpose**

**paths : [ list of all nodes]**

list of all nodes connecting both start and end nodes (SHORTEST PATH)

**traffic\_signals : [list of traffic signals]**

**Input**

**Argument**

list of all traffic signals in the graph

**moves : [ list of moves from start to end nodes ]**

**Returns**

list containing moves for the bot to move from start to end

**Example**

**Call**

**moves = paths\_to\_moves(paths, traffic\_signals)**

**4. Running your Solution**

**Skip to main content**

To test and run your solution, do the following:

https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062

6/9



<a name="br7"></a> 

12/1/22, 9:38 PM

PB Task 3A - Instructions - Pharma Bot (PB) / Task 3 - e-Yantra

Open Anaconda Prompt and navigate to the Task 3A directory/folder on your system.

Activate the Conda environment you created in task 0 using the command conda

activate PB\_<team-id>

Run the command: python task\_3a.pyto execute your solution.

When you run the task\_3a.py, as a default, the **main()** function will feed the file path

of the **maze\_000.png** to **maze\_009.png** files which is present in the ***test\_images***

folder.

It will print the output of the function i.e. the **2 lists** returned.

The final output of task\_3a.pyshould resemble Figure 4.

Figure 4: Overall output

Once your code runs successfully, you can do manual verification of the output to ensure

you are getting proper output.

***NOTE: Your solution will be tested against blind test cases. Ensure your solution is***

***robust and considers all the corner cases.***

**5. Testing your Solution**

Please do the following in order to test your solution:

This executable will require your modified **task\_3a.py**file to be present in the same

directory

Open your **terminal / Anaconda Prompt** and navigate to the Task 3A folder.

Activate your Conda environment

Type the following command and press **Enter**

For Windows: **test\_task\_3a.exe**

For Ubuntu: **./test\_task\_3a**

The code will start to execute. You will be required to enter your team id first.

While your solution gets tested, data will be sent to our servers. Hence ensure that there

**net connection** while running the executable file.

**Skip to main content**

https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062

7/9



<a name="br8"></a> 

12/1/22, 9:38 PM

PB Task 3A - Instructions - Pharma Bot (PB) / Task 3 - e-Yantra

The execution will be considered **successful only if the required data is received** at

our end.

On successful execution, **task3a\_output.txt** will be generated in the same directory.

**Figure 5: Testing for Task 3A**

**6. Submission Instructions**

For **Task 3A** submission you have to upload a **.zip file**. To create the appropriate file please

follow the instructions given below:

Create a new folder named **PB\_<Team-ID>\_Task3A**.

For example: if your team ID is 9999 then you need to create a folder named

**PB\_9999\_Task3A**.

Now copy and paste the following files into this folder:

**task\_3a.py**(modified file)

**task3a\_output.txt**(generated from executable)

Compress this folder into a **PB\_<Team-ID>\_Task3A.zip**

Now go to the eYRC Portal .Select the radio button as Task 1A and follow the

instructions to upload this **.zip** file for **Task 1A** as shown in Figure 7.

**Skip to main content**

https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062

8/9



<a name="br9"></a> 

12/1/22, 9:38 PM

PB Task 3A - Instructions - Pharma Bot (PB) / Task 3 - e-Yantra

**Figure 6: Submission of Task 3A**

7\. Resources

Motion Planning Algorithms - A\* vs Dijkstra’s (**Motion Planning Algorithms - A\* vs**

**Dijkstra's - YouTube** )

Robotic Path Planning ([**Robotic**](https://fab.cba.mit.edu/classes/865.21/topics/path_planning/robotic.html)[** ](https://fab.cba.mit.edu/classes/865.21/topics/path_planning/robotic.html)[Path**](https://fab.cba.mit.edu/classes/865.21/topics/path_planning/robotic.html)[** ](https://fab.cba.mit.edu/classes/865.21/topics/path_planning/robotic.html)[Planning**](https://fab.cba.mit.edu/classes/865.21/topics/path_planning/robotic.html)[** ](https://fab.cba.mit.edu/classes/865.21/topics/path_planning/robotic.html)[-**](https://fab.cba.mit.edu/classes/865.21/topics/path_planning/robotic.html)[** ](https://fab.cba.mit.edu/classes/865.21/topics/path_planning/robotic.html)[Path**](https://fab.cba.mit.edu/classes/865.21/topics/path_planning/robotic.html)[** ](https://fab.cba.mit.edu/classes/865.21/topics/path_planning/robotic.html)[Planning**](https://fab.cba.mit.edu/classes/865.21/topics/path_planning/robotic.html)[** ](https://fab.cba.mit.edu/classes/865.21/topics/path_planning/robotic.html))

[**PB**](https://discuss.e-yantra.org/t/pb-task-3-instructions-and-resources/22759)[** ](https://discuss.e-yantra.org/t/pb-task-3-instructions-and-resources/22759)[Task**](https://discuss.e-yantra.org/t/pb-task-3-instructions-and-resources/22759)[** ](https://discuss.e-yantra.org/t/pb-task-3-instructions-and-resources/22759)[3**](https://discuss.e-yantra.org/t/pb-task-3-instructions-and-resources/22759)[** ](https://discuss.e-yantra.org/t/pb-task-3-instructions-and-resources/22759)[-**](https://discuss.e-yantra.org/t/pb-task-3-instructions-and-resources/22759)[** ](https://discuss.e-yantra.org/t/pb-task-3-instructions-and-resources/22759)[Instructions**](https://discuss.e-yantra.org/t/pb-task-3-instructions-and-resources/22759)[** ](https://discuss.e-yantra.org/t/pb-task-3-instructions-and-resources/22759)[and**](https://discuss.e-yantra.org/t/pb-task-3-instructions-and-resources/22759)[** ](https://discuss.e-yantra.org/t/pb-task-3-instructions-and-resources/22759)[Resources**](https://discuss.e-yantra.org/t/pb-task-3-instructions-and-resources/22759)

**UNLISTED 1 DAY AGO**

**LISTED 1 DAY AGO**

**UNLISTED 33 MINS AGO**

**CLOSED 33 MINS AGO**

**1. Introduction to Path**

**Planning**

**1.1 What is path planning ?**

**1.2 Tree search algorithms**

**2. Problem Statement**

**3. Task Instructions**

**4. Running your Solution**

**5. Testing your Solution**

**6. Submission Instructions**

**7. Resources**

https://discuss.e-yantra.org/t/pb-task-3a-instructions/23062

9/9

