#!/usr/bin/env python
import rospy
from tello import Tello
from optitrack.msg import RigidBody, RigidBodyArray
import time
import threading

x = 0
y = 0
z = 0

def readData(data):
	global x
	global y
	global z
	global v
	global u
	x = data.bodies[0].pose.position.x
	y = data.bodies[0].pose.position.y
	z = data.bodies[0].pose.position.z
	u = data.bodies[1].pose.position.x
	v = data.bodies[1].pose.position.y
	w = data.bodies[1].pose.position.z
	x = x + 0.07 # for drift.

def p(drone):
	global x
	global y
	global z
	global v
	global u
	try:
		drone.send_command('command')
		drone.send_command('takeoff')
		while y < 2:
			if x > 0.7:
				drone.send_command('left 20')
			if x < 0.3:
				drone.send_command('right 20')
			drone.send_command('forward 50')
		while x > -0.5 :
			if y > 2.3:
				drone.send_command('back 20')
			if y < 1.7:
				drone.send_command('forward 20')
			drone.send_command('left 30')
		while y > 0:
			if x > -0.3:
				drone.send_command('left 20')
			if x < -0.7:
				drone.send_command('right 20')
			drone.send_command('back 40')
		while x < 0.5:
			if y > 0.3:
				drone.send_command('back 20')
			if y < -0.3:
				drone.send_command('forward 20')
			drone.send_command('right 30')
		land = True
		while land:
			if y < v :
			    drone.send_command('forward 20')
			if v < y :
				drone.send_command('back 20')
			if x > u :
				drone.send_command('left 20')
			if u > x:
				drone.send_command('right 20')
			if abs(y - v) < 0.06 and abs(x - u) < 0.06:
				land = False
		drone.send_command('land')
	except KeyboardInterrupt:
		drone.send_command('land')
	finally:
		drone.send_command('land')

tello = Tello()
threading.Thread(target=p, args=[tello]).start()
rospy.init_node('listener', anonymous=True)
rospy.Subscriber('/optitrack/rigid_bodies', RigidBodyArray,readData)
rospy.spin()