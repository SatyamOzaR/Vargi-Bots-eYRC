#! /usr/bin/env python

import rospy
import sys
import copy

import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import actionlib
import math


from pkg_vb_sim.srv import vacuumGripper
from pkg_vb_sim.srv import conveyorBeltPowerMsg
from pkg_vb_sim.msg import LogicalCameraImage


class CartesianPath:

	# Constructor
	def __init__(self):

		rospy.init_node('node_eg5_waypoints', anonymous=True)

		self._planning_group = "ur5_1_planning_group"
		self._commander = moveit_commander.roscpp_initialize(sys.argv)
		self._robot = moveit_commander.RobotCommander()
		self._scene = moveit_commander.PlanningSceneInterface()
		self._group = moveit_commander.MoveGroupCommander(self._planning_group)
		self._display_trajectory_publisher = rospy.Publisher(
			'/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

		self._exectute_trajectory_client = actionlib.SimpleActionClient(
			'execute_trajectory', moveit_msgs.msg.ExecuteTrajectoryAction)
		self._exectute_trajectory_client.wait_for_server()

		self._planning_frame = self._group.get_planning_frame()
		self._eef_link = self._group.get_end_effector_link()
		self._group_names = self._robot.get_group_names()

		rospy.loginfo('\033[94m' + " >>> Init done." + '\033[0m')

	def ee_cartesian_translation(self, trans_x, trans_y, trans_z):

		# 1. Create a empty list to hold waypoints
		waypoints = []

		# 2. Add Current Pose to the list of waypoints
		waypoints.append(self._group.get_current_pose().pose)

		# 3. Create a New waypoint
		wpose = geometry_msgs.msg.Pose()
		wpose.position.x = waypoints[0].position.x + (trans_x)  
		wpose.position.y = waypoints[0].position.y + (trans_y)  
		wpose.position.z = waypoints[0].position.z + (trans_z)
		# This to keep EE parallel to Ground Plane
		wpose.orientation.x = -0.5
		wpose.orientation.y = -0.5
		wpose.orientation.z = 0.5
		wpose.orientation.w = 0.5


		# 4. Add the new waypoint to the list of waypoints
		waypoints.append(copy.deepcopy(wpose))


		# 5. Compute Cartesian Path connecting the waypoints in the list of waypoints
		(plan, fraction) = self._group.compute_cartesian_path(
			waypoints,   # waypoints to follow
			0.01,        # Step Size, distance between two adjacent computed waypoints will be 1 cm
			0.0)         # Jump Threshold
		rospy.loginfo("Path computed successfully. Moving the arm.")

		# The reason for deleting the first two waypoints from the computed Cartisian Path can be found here,
		# https://answers.ros.org/question/253004/moveit-problem-error-trajectory-message-contains-waypoints-that-are-not-strictly-increasing-in-time/?answer=257488#post-id-257488
		num_pts = len(plan.joint_trajectory.points)
		if (num_pts >= 3):
			del plan.joint_trajectory.points[0]
			del plan.joint_trajectory.points[1]

		# 6. Make the arm follow the Computed Cartesian Path
		self._group.execute(plan)

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
			rospy.loginfo('\033[94m' + ">>> go_to_pose() Success" + '\033[0m')
		else:
			rospy.logerr(
				'\033[94m' + ">>> go_to_pose() Failed. Solution for Pose not Found." + '\033[0m')

		return flag_plan

	def add_box(self, pose1, name):

		self._pose = pose1
		self._box_name = name
		self.scene = moveit_commander.PlanningSceneInterface()
		self.scene.add_box(self._box_name, self._pose, size=(0.15, 0.15, 0.15))

		self.group_name = "ur5_1_planning_group"
		self.group = moveit_commander.MoveGroupCommander(self.group_name)
		
		self.eef_link = self.group.get_end_effector_link()
		self.scene.attach_box(self.eef_link, self._box_name )

	def remove_box(self, object_name):

		self.box_name = object_name

		self.scene = moveit_commander.PlanningSceneInterface()
		self.eef_link = self.group.get_end_effector_link()

		self.scene.remove_attached_object(self.eef_link, name=self.box_name)
		rospy.sleep(2)
		self.scene.remove_world_object(self.box_name)

	# Destructor
	def __del__(self):
		moveit_commander.roscpp_shutdown()
		rospy.loginfo(
			'\033[94m' + "Object of class CartesianPath Deleted." + '\033[0m')

def main():
	ur5 = CartesianPath()

	box_length = 0.15               # Length of the Package
	vacuum_gripper_width = 0.115    # Vacuum Gripper Width
	delta = vacuum_gripper_width + (box_length/2)  # 0.19

	ur5_pose_red_box = geometry_msgs.msg.Pose()
	ur5_pose_red_box.position.x = -0.800328
	ur5_pose_red_box.position.y = 0.0
	ur5_pose_red_box.position.z = 1+delta
	ur5_pose_red_box.orientation.x = -0.5
	ur5_pose_red_box.orientation.y = -0.5
	ur5_pose_red_box.orientation.z = 0.5
	ur5_pose_red_box.orientation.w = 0.5

	ur5_pose_green_box = geometry_msgs.msg.Pose()
	ur5_pose_green_box.position.x = -0.660551
	ur5_pose_green_box.position.y = 0.0
	ur5_pose_green_box.position.z = 1+delta
	ur5_pose_green_box.orientation.x = -0.5
	ur5_pose_green_box.orientation.y = -0.5
	ur5_pose_green_box.orientation.z = 0.5
	ur5_pose_green_box.orientation.w = 0.5

	ur5_pose_blue_box = geometry_msgs.msg.Pose()
	ur5_pose_blue_box.position.x = -0.900551
	ur5_pose_blue_box.position.y = 0.0
	ur5_pose_blue_box.position.z = 1+delta
	ur5_pose_blue_box.orientation.x = -0.5
	ur5_pose_blue_box.orientation.y = -0.5
	ur5_pose_blue_box.orientation.z = 0.5
	ur5_pose_blue_box.orientation.w = 0.5

	ur5_pose_red_bin = geometry_msgs.msg.Pose()
	ur5_pose_red_bin.position.x = 0.11
	ur5_pose_red_bin.position.y = 0.65
	ur5_pose_red_bin.position.z = 1+delta
	ur5_pose_red_bin.orientation.x = -0.5
	ur5_pose_red_bin.orientation.y = -0.5
	ur5_pose_red_bin.orientation.z = 0.5
	ur5_pose_red_bin.orientation.w = 0.5

	ur5_pose_green_bin = geometry_msgs.msg.Pose()
	ur5_pose_green_bin.position.x = 0.75
	ur5_pose_green_bin.position.y = 0.03
	ur5_pose_green_bin.position.z = 1+delta
	ur5_pose_green_bin.orientation.x = -0.5
	ur5_pose_green_bin.orientation.y = -0.5
	ur5_pose_green_bin.orientation.z = 0.5
	ur5_pose_green_bin.orientation.w = 0.5

	ur5_pose_blue_bin = geometry_msgs.msg.Pose()
	ur5_pose_blue_bin.position.x = 0.04
	ur5_pose_blue_bin.position.y = -0.65
	ur5_pose_blue_bin.position.z = 1+delta
	ur5_pose_blue_bin.orientation.x = -0.5
	ur5_pose_blue_bin.orientation.y = -0.5
	ur5_pose_blue_bin.orientation.z = 0.5
	ur5_pose_blue_bin.orientation.w = 0.5

	red_box_spawn_rviz = geometry_msgs.msg.PoseStamped()
	red_box_spawn_rviz.pose.position.x = -0.800328
	red_box_spawn_rviz.pose.position.y = 0.0
	red_box_spawn_rviz.pose.position.z = 1
	red_box_spawn_rviz.header.frame_id = "world"

	green_box_spawn_rviz = geometry_msgs.msg.PoseStamped()
	green_box_spawn_rviz.pose.position.x = -0.660551
	green_box_spawn_rviz.pose.position.y = 0.0
	green_box_spawn_rviz.pose.position.z = 1

	blue_box_spawn_rviz = geometry_msgs.msg.PoseStamped()
	blue_box_spawn_rviz.pose.position.x = -0.900551
	blue_box_spawn_rviz.pose.position.y = 0.0
	blue_box_spawn_rviz.pose.position.z = 1

	while not rospy.is_shutdown():
		
		ur5.go_to_pose(ur5_pose_red_box)
		rospy.sleep(2)
		

		
		
		ur5.ee_cartesian_translation(ur5_pose_red_bin.position.x-ur5_pose_red_box.position.x,
										ur5_pose_red_bin.position.y-ur5_pose_red_box.position.y,
										ur5_pose_red_bin.position.z-ur5_pose_red_box.position.z)
		rospy.sleep(4)
		
		
		
		
		ur5.ee_cartesian_translation(ur5_pose_green_box.position.x-ur5_pose_red_bin.position.x,
										ur5_pose_green_box.position.y-ur5_pose_red_bin.position.y,
										ur5_pose_green_box.position.z-ur5_pose_red_bin.position.z)
		rospy.sleep(4)



		ur5.ee_cartesian_translation(ur5_pose_green_bin.position.x-ur5_pose_green_box.position.x,
										ur5_pose_green_bin.position.y-ur5_pose_green_box.position.y,
										ur5_pose_green_bin.position.z-ur5_pose_green_box.position.z)
		rospy.sleep(4)

		ur5.ee_cartesian_translation(ur5_pose_blue_box.position.x-ur5_pose_green_bin.position.x,
										ur5_pose_blue_box.position.y-ur5_pose_green_bin.position.y,
										ur5_pose_blue_box.position.z-ur5_pose_green_bin.position.z)
		rospy.sleep(4)
		

		ur5.ee_cartesian_translation(ur5_pose_blue_bin.position.x-ur5_pose_blue_box.position.x,
										ur5_pose_blue_bin.position.y-ur5_pose_blue_box.position.y,
										ur5_pose_blue_bin.position.z-ur5_pose_blue_box.position.z)
		rospy.sleep(4)
		
	del ur5


if __name__ == '__main__':
	main()

	