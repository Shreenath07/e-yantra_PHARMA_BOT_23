  <div align="center">
    <h1>  e-yantra_PHARMA_BOT_23  </h1>
    <h2>  Task 1A </h2>
  </div>                                                  

  <h2>Image Processing</h2>

    This task’s goal is to use Python’s OpenCV package to create various functions with the following goals:

                 * Detect multiple shapes in a given image

                 * Detect the color of shapes

                 * Detect lines present in an image

<h2>Problem Statement</h2>

      Each image in the test_images folder of Task1A contains a 6x6 grid containing 36 cells.

      A sample image can be found below for reference:
 <div align="center">
  <img src="Task 1/Images/Image1.png" alt="Image 1" style="width: 500px; height: 500px;">
</div>

 <div align="center">
    <h4> Figure 1: Grid numbering</h4> 
  </div>        

<h3>Image Description </h3> 
<div align="center">
  <img src="./Images/Imgae1.png" alt="Image 1" style="width: 500px; height: 500px;">
  <h4>Figure 2: Sample Image</h4>
</div>

<ul style="list-style-type: none; padding-left: 50px;">
    <li>The cells numbered 1 through 6 in the arena correspond to the 6 medical shops that are located there. These shops stock medicine packages that can be differentiated by their shapes and colors.</li>
    <li>Only three of the six companies in any test image will have packages that need to be delivered. Each shop is numbered as Shop_n where n varies from 1 to 6. Figure 2 shows Shop_4</li>
    <li>Packages of each shop are differentiated by their shapes and colors as shown in Figure 2</li>
    <li>Shapes of packages can be -</li>
       <ul style="list-style-type: none; padding-left: 30px;">
             <li>Square (S)</li>        
             <li>Triangular (T)</li>
             <li>Circular (C)</li>
         </ul>
     <li> Colours can be -</li>
         <ul style="list-style-type: none; padding-left: 30px;">
              <li> Sky Blue (SB)</li>
             <li> Pink (P)</li>
             <li>Orange (O)</li>
             <li>Green (G)</li>
         </ul>
      <li>A shop can have any number of packages from 1 to 4. A shop deals with only SAME SHAPED packages i.e a cell will not have multiple shapes. All packages in a company will have    
          UNIQUE COLORED packages i.e no two packages in a cell will have the same color.</li>
      <li>The black grid lines represent roads. The horizontal black lines are referred to as horizontal roads and vertical lines are vertical roads. The lines that are missing are roads 
          under construction.</li>
      <li>The horizontal missing lines are called horizontal roads under construction and vertical missing lines are called vertical roads under construction.</li>
      <li>The intersections of the grid lines (roads) are called NODES and are represented with blue squares. Each node is represented by a combination of a letter and a number where the 
          letter is a reference to the column (A-G) and number refers to the row (1-7).</li>
      <li>Some of these nodes have Traffic Signals represented by Red Squares.</li>
      <li>The green square is the Start Node.</li>
</ul> 
             
 <h2>Problem Description</h2>            
 <h3>The task is to find the following details from each image:</h3>
  <ol style="list-style-type: none; padding-left: 50px;">
    <li>Detect all the nodes at which traffic signals are present.<p>Example: In Figure 2, there is a traffic signal present at node 'C3'</p></li>
    <li>Detect all the horizontal roads under construction<p1>Example - In Figure 2, the horizontal road from 'B3-C3' is missing.</p1></li>
    <li>Detect all the vertical roads under construction<p>Example - In Figure 2, the horizontal road from 'C2-C3' is missing.</p></li>
    <li>Detect all the medicine packages present<p></p></li>
    <ul style="list-style-type: none; padding-left: 30px;">
         <p> Here 4 parameters have to be identified for each package. These are </p>
         <li>The shop number in which the package is present(Shop_n)</li>
         <li>Colour of the package</li>
         <li>Shape of the package</li>
         <li>Centroid co-ordinates</li>
</ol>           



Example - In Figure 2,
[['Shop_2', 'Green', 'Square', [270, 170]], ['Shop_2', 'Orange', 'Square', [230, 170]], ['Shop_2', 'Pink', 'Square', [230, 130]], ['Shop_2', 'Skyblue', 'Square', [270, 130]] represents the packages present in Shop_2.

All the detected arena parameters should be returned as a dictionary
Example - The output for Figure 2 will be,
<div align="center">
  <img src="Task 1/Images/Image3.png" alt="Image 3" style="width: 1000px; height: 100px;">
  <h4>Figure 3: Sample Output Image</h4>
</div>

