<a name="br1"></a> 

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



<a name="br2"></a> 

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

