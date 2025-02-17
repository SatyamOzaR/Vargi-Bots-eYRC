#!/usr/bin/python

import rospy  						# importing ROS-python main library
import sys  						# importing system-specific parameters and functions
import copy 						# importing copy module
import moveit_commander 			# importing moveit_commander module
import moveit_msgs.msg  			# importing messages from moveit
import geometry_msgs.msg  			# importing messages of type geometry
import actionlib  					# importing actionlib module
import math  						# importing python-math module
import threading

from pkg_vb_sim.srv import vacuumGripper  			# importing the service for vacuum-gripper
from pkg_vb_sim.srv import conveyorBeltPowerMsg  	# importing the service for conveyor-belt
from pkg_vb_sim.msg import LogicalCameraImage  		# importing messages of type LogicalCameraImage

red_flag = 0
green_flag = 0
blue_flag =0
flag1 = 0  			# flag to control unnecessary looping of "callback_topic_subscription()" into "if" loop1
flag2 = 0  			# flag to control unnecessary looping of "callback_topic_subscription()" into "if" loop2
flag3 = 0  			# flag to control unnecessary looping of "callback_topic_subscription()" into "if" loop3
home_pose = geometry_msgs.msg.Pose()
home_pose.position.x = -0.8
home_pose.position.y = 0.0
home_pose.position.z = 1.22
home_pose.orientation.x = -0.5
home_pose.orientation.y = -0.5
home_pose.orientation.z = 0.5
home_pose.orientation.w = 0.5

ur5_pose_box = geometry_msgs.msg.Pose()
ur5_pose_box.position.x = 0.0
ur5_pose_box.position.y = 0.0
ur5_pose_box.position.z = 0.0
ur5_pose_box.orientation.x = -0.5
ur5_pose_box.orientation.y = -0.5
ur5_pose_box.orientation.z = 0.5
ur5_pose_box.orientation.w = 0.5
box_length = 0.15
vacuum_gripper_width = 0.115
delta = vacuum_gripper_width + box_length / 2

pose_red_bin = geometry_msgs.msg.Pose()
pose_red_bin.position.x = 0.11
pose_red_bin.position.y = 0.65
pose_red_bin.position.z = 1.3 + delta
pose_red_bin.orientation.x = -0.5
pose_red_bin.orientation.y = -0.5
pose_red_bin.orientation.z = 0.5
pose_red_bin.orientation.w = 0.5

pose_green_bin = geometry_msgs.msg.Pose()
pose_green_bin.position.x = 0.75
pose_green_bin.position.y = 0.03
pose_green_bin.position.z = 1.2+ delta
pose_green_bin.orientation.x = -0.5
pose_green_bin.orientation.y = -0.5
pose_green_bin.orientation.z = 0.5
pose_green_bin.orientation.w = 0.5

pose_blue_bin = geometry_msgs.msg.Pose()
pose_blue_bin.position.x = 0.04
pose_blue_bin.position.y = -0.65
pose_blue_bin.position.z = 1 + delta
pose_blue_bin.orientation.x = -0.5
pose_blue_bin.orientation.y = -0.5
pose_blue_bin.orientation.z = 0.5
pose_blue_bin.orientation.w = 0.5

box_info = ''

class Ur5Moveit:

	# Constructor

	def __init__(self):

		rospy.init_node('node_t3_ur5_1_pick_place_rgb',
						anonymous=True)

		self._planning_group = 'ur5_1_planning_group'
		self._commander = moveit_commander.roscpp_initialize(sys.argv)
		self._robot = moveit_commander.RobotCommander()
		self._scene = moveit_commander.PlanningSceneInterface()
		self._group = \
			moveit_commander.MoveGroupCommander(self._planning_group)
		self._display_trajectory_publisher = \
			rospy.Publisher('/move_group/display_planned_path',
							moveit_msgs.msg.DisplayTrajectory,
							queue_size=1)

		self._exectute_trajectory_client = \
			actionlib.SimpleActionClient('execute_trajectory',
				moveit_msgs.msg.ExecuteTrajectoryAction)
		self._exectute_trajectory_client.wait_for_server()

		self._planning_frame = self._group.get_planning_frame()
		self._eef_link = self._group.get_end_effector_link()
		self._group_names = self._robot.get_group_names()
		self._box_name = ''

		# Current State of the Robot is needed to add box to planning _scene

		self._curr_state = self._robot.get_current_state()

		rospy.loginfo('\033[94m'
					  + 'Planning Group: {}'.format(self._planning_frame)
					  + '\033[0m')
		rospy.loginfo('\033[94m'
					  + 'End Effector Link: {}'.format(self._eef_link)
					  + '\033[0m')
		rospy.loginfo('\033[94m'
					  + 'Group Names: {}'.format(self._group_names)
					  + '\033[0m')

		rospy.loginfo('\033[94m' + ' >>> Ur5Moveit init done.'
					  + '\033[0m')

	def go_to_pose(self, arg_pose):

		pose_values = self._group.get_current_pose().pose
		rospy.loginfo('\033[94m' + ">>> Current Pose:" + '\033[0m')
		rospy.loginfo(pose_values)

		self._group.set_pose_target(arg_pose)
		flag_plan = self._group.go(wait=True)  # wait=False for Async Move

		pose_values = self._group.get_current_pose().pose
		rospy.loginfo('\033[94m' + ">>> Final Pose:" + '\033[0m')
		rospy.loginfo(pose_values)

		list_joint_values = self._group.get_current_joint_values()
		rospy.loginfo('\033[94m' + ">>> Final Joint Values:" + '\033[0m')
		rospy.loginfo(list_joint_values)

		if (flag_plan == True):
			rospy.loginfo(
				'\033[94m' + ">>> go_to_pose() Success" + '\033[0m')
		else:
			rospy.logerr(
				'\033[94m' + ">>> go_to_pose() Failed. Solution for Pose not Found." + '\033[0m')

		return flag_plan

	def conveyor_power(self, power):

		# creating client object for conveyor-power server
		cb_req = rospy.ServiceProxy('/eyrc/vb/conveyor/set_power',
								conveyorBeltPowerMsg)

		# requesting the conveyor-power server to activate for defined power
		r = cb_req(power)


	def vacuum_gripper(self, req):

		# creating client object for vacuum-gripper server
		vg_req = rospy.ServiceProxy('/eyrc/vb/ur5_1/activate_vacuum_gripper'
								, vacuumGripper)

		# activating vacuum-gripper by requesting vacuum-gripper server
		q = vg_req(req)

	def pick_place(self, arg_pose_box, arg_pose_bin, box_name):

		box_pose_rviz = geometry_msgs.msg.PoseStamped()
		box_pose_rviz.pose.position.x = arg_pose_box.position.x
		box_pose_rviz.pose.position.y = arg_pose_box.position.y
		box_pose_rviz.pose.position.z = 0.998
		box_pose_rviz.header.frame_id = 'world'

		vg_req = rospy.ServiceProxy('/eyrc/vb/ur5_1/activate_vacuum_gripper'
								, vacuumGripper)

		cb_req = rospy.ServiceProxy('/eyrc/vb/conveyor/set_power',
								conveyorBeltPowerMsg)

		self._box_pose = box_pose_rviz
		self._box_name = box_name
		
		
		pose_values = self._group.get_current_pose().pose
		rospy.loginfo('\033[94m' + '>>> Current Pose:' + '\033[0m')
		rospy.loginfo(pose_values)

		self._group.set_pose_target(arg_pose_box)
		flag_plan_box = self._group.go(wait=True)  # wait=False for Async Move

		pose_values = self._group.get_current_pose().pose
		rospy.loginfo('\033[94m' + '>>> Final box Pose:' + '\033[0m')
		rospy.loginfo(pose_values)

		list_joint_values = self._group.get_current_joint_values()
		rospy.loginfo('\033[94m' + '>>> Final Joint Values at box pose:' + '\033[0m'
					  )
		rospy.loginfo(list_joint_values)

		if flag_plan_box == True:
			rospy.loginfo('\033[94m' + '>>> go to box pose Success'
						  + '\033[0m')
		else:
			rospy.logerr('\033[94m'
						 + '>>> go_to_pose() Failed. Solution for box Pose not Found.'
						  + '\033[0m')

		req = True
		q = vg_req(req)

		
		self._scene.add_box(self._box_name, self._box_pose, size=(0.15,
						   0.15, 0.15))

		
		
		self._scene.attach_box(self._eef_link, self._box_name)

		power_req = 13
		r = cb_req(power_req)

		pose_values = self._group.get_current_pose().pose
		rospy.loginfo('\033[94m' + '>>> Current Pose:' + '\033[0m')
		rospy.loginfo(pose_values)

		self._group.set_pose_target(arg_pose_bin)
		flag_plan_bin = self._group.go(wait=True)  # wait=False for Async Move


		pose_values = self._group.get_current_pose().pose
		rospy.loginfo('\033[94m' + '>>> Final bin Pose:' + '\033[0m')
		rospy.loginfo(pose_values)

		list_joint_values = self._group.get_current_joint_values()
		rospy.loginfo('\033[94m' + '>>> Final Joint Values at bin pose:' + '\033[0m'
					  )
		rospy.loginfo(list_joint_values)

		if flag_plan_bin == True:
			rospy.loginfo('\033[94m' + '>>> go to bin pose Success'
						  + '\033[0m')
		else:
			rospy.logerr('\033[94m'
						 + '>>> go_to_pose() Failed. Solution for bin Pose not Found.'
						  + '\033[0m')

		req = False
		q = vg_req(req)

		self._scene.remove_attached_object(self._eef_link,
				name=self._box_name)
		self._scene.remove_world_object(self._box_name)


		return (flag_plan_box and flag_plan_bin)

	def callback_topic_subscription(self, x_msg):

		cb_req = rospy.ServiceProxy('/eyrc/vb/conveyor/set_power',
								conveyorBeltPowerMsg)

		global flag1
		global flag2
		global flag3
		global ur5_pose_box
		global delta
		global box_info
		global red_flag
		global green_flag
		global blue_flag



		number_models = len(x_msg.models)

		for i in range(0, number_models):

			name_model = x_msg.models[i].type
			pos = x_msg.models[i].pose

			if name_model == 'packagen1' and pos.position.y >= -0.01 \
				and pos.position.y < 0.01 and flag1 == 0:
				power = 0
				r = cb_req(power)
				ur5_pose_box.position.x = pos.position.z-0.8
				ur5_pose_box.position.y = pos.position.y
				ur5_pose_box.position.z = pos.position.x+delta
				box_info = name_model
				flag1 = 1
				red_flag = 1
			elif name_model == 'packagen2' and pos.position.y >= -0.01 \
				and pos.position.y < 0.01 and flag2 == 0:
				power = 0
				r = cb_req(power)
				ur5_pose_box.position.x = pos.position.z-0.8
				ur5_pose_box.position.y = pos.position.y
				ur5_pose_box.position.z = pos.position.x+delta
				box_info = name_model
				flag2 = 1
				green_flag = 1
			elif name_model == 'packagen3' and pos.position.y >= -0.01 \
				and pos.position.y < 0.01 and flag3 == 0:
				power = 0
				r = cb_req(power)
				ur5_pose_box.position.x = pos.position.z-0.8
				ur5_pose_box.position.y = pos.position.y
				ur5_pose_box.position.z = pos.position.x+delta
				box_info = name_model
				flag3 = 1
				blue_flag = 1

	# Destructor

	def __del__(self):
		moveit_commander.roscpp_shutdown()
		rospy.loginfo('\033[94m' + 'Object of class Ur5Moveit Deleted.'
					  + '\033[0m')


def main():

	ur5 = Ur5Moveit()


	rospy.Subscriber('/eyrc/vb/logical_camera_2', LogicalCameraImage,
					 ur5.callback_topic_subscription)


	ur5.conveyor_power(25)

	ur5.go_to_pose(home_pose)


	while red_flag == 0:
		{}

	#ur5.conveyor_power(0)

	ur5.pick_place(ur5_pose_box, pose_red_bin, box_info)

	ur5.go_to_pose(home_pose)
	#t1 = threading.Thread(target=ur5.go_to_pose, args=(home_pose))
	#t1.start()

	while green_flag == 0:
		{}

	#t1.join()
	#ur5.conveyor_power(0)

	ur5.pick_place(ur5_pose_box, pose_green_bin, box_info)

	ur5.go_to_pose(home_pose)
	#t1 = threading.Thread(target=ur5.go_to_pose, args=(home_pose))
	#t1.start()

	while blue_flag == 0:	
		{}

	#t1.join()
	#ur5.conveyor_power(0)

	ur5.pick_place(ur5_pose_box, pose_blue_bin, box_info)

	ur5.go_to_pose(home_pose)

	del ur5

if __name__ == '__main__':
	main()


	