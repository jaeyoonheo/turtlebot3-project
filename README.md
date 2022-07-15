# Turtlebot3 project

### Description

Project related to turtlebot3 driving

CMakeList.txt file and package.xml file must be included. (manage dependency)



### Environment

These programs can execute on the Ubuntu 18.04 LTS, ROS1 and ROS2



### Moving coordinate (ROS1)

The program for turtlebot3 driving to certain point(x,y,z)

When a specific position is input, it drives to that position.

This program can also be confirmed by simulation results in gazebo.

 

### Auto driving with camera (ROS2)

The program for turtlebot3 do auto driving with pycamera

![image](https://user-images.githubusercontent.com/109254266/179161966-a4434ffc-0fa8-49cc-b72a-1b570ecdbe7e.png)

Turtlebot3 gets frame from pycamera video. In the frame, the image of the lane is visible, and the image is detected by edge detection to distinguish straight lines and curves. The sum of the inclinations of the straight lines displayed in the image determines the straight-line running direction.

![image](https://user-images.githubusercontent.com/109254266/179160474-08d13749-8703-4bba-8244-98b453aeb9f0.png)

In a curve, the slope of the curve is inferred based on a specific x value. Steering coefficient increases as the curve is positioned at the bottom of the image.

![image](https://user-images.githubusercontent.com/109254266/179161092-1f7d89e4-ee47-4d6a-9493-bd7fb04593d1.png)

