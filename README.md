**# e-yantra_PHARMA_BOT_23**

Task 1A

Image Processing

This task’s goal is to use Python’s OpenCV package to create various functions with the following goals:

* Detect multiple shapes in a given image

* Detect the color of shapes

* Detect lines present in an image

**Problem Statement**

Each image in the test_images folder of Task1A contains a 6x6 grid containing 36 cells.

A sample image can be found below for reference:

 Figure 1: Grid numbering
**2.1 Image Description**
 Figure 2: Sample Image
The cells numbered 1 through 6 in the arena correspond to the 6 medical shops that are located there. These shops stock medicine packages that can be differentiated by their shapes and colors.
Only three of the six companies in any test image will have packages that need to be delivered. Each shop is numbered as Shop_n where n varies from 1 to 6. Figure 2 shows Shop_4.
Packages of each shop are differentiated by their shapes and colors as shown in Figure 2:
Shapes of packages can be -
Square (S)
Triangular (T)
Circular (C)
Colours can be -
Sky Blue (SB)
Pink (P)
Orange (O)
Green (G)
A shop can have any number of packages from 1 to 4. A shop deals with only SAME SHAPED packages i.e a cell will not have multiple shapes. All packages in a company will have UNIQUE COLORED packages i.e no two packages in a cell will have the same color.
The black grid lines represent roads. The horizontal black lines are referred to as horizontal roads and vertical lines are vertical roads. The lines that are missing are roads under construction.
The horizontal missing lines are called horizontal roads under construction and vertical missing lines are called vertical roads under construction.
The intersections of the grid lines (roads) are called NODES and are represented with blue squares. Each node is represented by a combination of a letter and a number where the letter is a reference to the column (A-G) and number refers to the row (1-7).
Some of these nodes have Traffic Signals represented by Red Squares.
The green square is the Start Node.
2.2 Problem Description
The task is to find the following details from each image:

Detect all the nodes at which traffic signals are present.
Example: In Figure 2, there is a traffic signal present at node 'C3'
Detect all the horizontal roads under construction
Example - In Figure 2, the horizontal road from 'B3-C3' is missing.
Detect all the vertical roads under construction
Example - In Figure 2, the horizontal road from 'C2-C3' is missing.
Detect all the medicine packages present
Here 4 parameters have to be identified for each package. These are
The shop number in which the package is present(Shop_n)
Colour of the package
Shape of the package
Centroid co-ordinates
Example - In Figure 2,
[['Shop_2', 'Green', 'Square', [270, 170]], ['Shop_2', 'Orange', 'Square', [230, 170]], ['Shop_2', 'Pink', 'Square', [230, 130]], ['Shop_2', 'Skyblue', 'Square', [270, 130]] represents the packages present in Shop_2.
Please note that the nested list should be sorted according to the ASCENDING ORDER of the shop number (Shop_n) and the packages in a shop are sorted according to the ASCENDING ORDER of Colour.

For example, the list should first have the packages of Shop_1 listed. For the Shop_1 packages, the packages should be sorted in alphabetical order of color ie Green, Orange, Pink, and Skyblue.

All the detected arena parameters should be returned as a dictionary
Example - The output for Figure 2 will be,
