# tello_control
a tello_control algorithm using motive tracker.

run the following command to active the drone.

1.roslaunch kobuki_node minimal.launch --screen
# focus on this terminal to control the ground robot.
2.roslaunch kobuki_keyop keyop.launch --screen
3.roslaunch optitrack optitrack_pipeline.launch
4.roslaunch tello_controller controller.launch 
