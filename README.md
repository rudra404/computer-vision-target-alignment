# Semi-Autonomous Robot with Vision-Based Target Alignment
## Project at The Hong Kong Polytechnic University

I designed and developed this robot from scratch with 2 of my classmates from PolyU. The project was originally undertaken to compete in the ASME Student Design Competition, organized by the 'American Society of Mechanical Engineers'. The main objective of the competition was to design a pick-n-place robot that can pick several balls of various sizes, and deposit them inside the drop-zone in the shortest time possible. The rules-sheet of the competition provides more clarity on the competition objectives. We built an r/c robot with mecanum wheels and a universal gripper and won the 2nd-runner-up prize at this competition.<br />

We then decided to further develop the robot and introduce a certain level of automation to it using vision-sensors, to use it for garbage-collection, as an example. This would also be our Capstone Project at PolyU.

## Software: files uploaded here
#### Python + OpenCV

- Functions and Algorithms for Image processing & Object Detection including:<br />

    - Thresholding + Masking (HSV)<br />

    - Morphological transformations<br />

    - Using moments to find centre of detected contour<br />

    - Harris Corner Detection<br />

#### Arduino Code for wireless motor control + circuitry<br />

## Quick Look
[Watch the Robot in action](https://youtu.be/HGe3ylRFrF8) <br />
Top-Left window is the Robot’s POV and Bottom-Left window shows output commands for Left-Right Alignment, Distance from Target, and Angular Alignment.

For understanding the project in more detail, you can look at the [Final Presentation file](https://drive.google.com/file/d/1_rxxEy8RX1OQHu4WSANbJCBW798E2nNd/view) for our Capstone Project (which includes code snippets); Or if you would like to deep-dive into the details of this project, you can also read our Final Report uploaded here.
