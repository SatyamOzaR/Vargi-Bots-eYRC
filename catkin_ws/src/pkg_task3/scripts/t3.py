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


class Ur5Moveit:

    # Constructor
    def __init__(self):

        rospy.init_node('node_eg3_set_joint_angles', anonymous=True)

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
        self._box_name = ''

        # Current State of the Robot is needed to add box to planning scene
        self._curr_state = self._robot.get_current_state()

        rospy.loginfo(
            '\033[94m' + "Planning Group: {}".format(self._planning_frame) + '\033[0m')
        rospy.loginfo(
            '\033[94m' + "End Effector Link: {}".format(self._eef_link) + '\033[0m')
        rospy.loginfo(
            '\033[94m' + "Group Names: {}".format(self._group_names) + '\033[0m')

        rospy.loginfo('\033[94m' + " >>> Ur5Moveit init done." + '\033[0m')

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

    def add_box(self, pose1, name):

        self._pose = pose1
        self._box_name = name
        self.scene = moveit_commander.PlanningSceneInterface()
        self.scene.add_box(self._box_name, self._pose, size=(0.15, 0.15, 0.15))

        self.group_name = "ur5_1_planning_group"
        self.group = moveit_commander.MoveGroupCommander(self.group_name)
        
        self.eef_link = self.group.get_end_effector_link()
        self.scene.attach_box(self.eef_link, self._box_name )

    # Destructor
    def __del__(self):
        moveit_commander.roscpp_shutdown()
        rospy.loginfo(
            '\033[94m' + "Object of class Ur5Moveit Deleted." + '\033[0m')


def main():

    ur5 = Ur5Moveit()

    ur5_pose_red_box = geometry_msgs.msg.Pose()
    ur5_pose_red_box.position.x = -0.800328
    ur5_pose_red_box.position.y = 0.0
    ur5_pose_red_box.position.z = 1.19
    ur5_pose_red_box.orientation.x = -0.5
    ur5_pose_red_box.orientation.y = -0.5
    ur5_pose_red_box.orientation.z = 0.5
    ur5_pose_red_box.orientation.w = 0.5

    ur5_pose_green_box = geometry_msgs.msg.Pose()
    ur5_pose_green_box.position.x = -0.660551
    ur5_pose_green_box.position.y = 0.0
    ur5_pose_green_box.position.z = 1.19
    ur5_pose_green_box.orientation.x = -0.5
    ur5_pose_green_box.orientation.y = -0.5
    ur5_pose_green_box.orientation.z = 0.5
    ur5_pose_green_box.orientation.w = 0.5

    ur5_pose_blue_box = geometry_msgs.msg.Pose()
    ur5_pose_blue_box.position.x = -0.900551
    ur5_pose_blue_box.position.y = 0.0
    ur5_pose_blue_box.position.z = 1.19
    ur5_pose_blue_box.orientation.x = -0.5
    ur5_pose_blue_box.orientation.y = -0.5
    ur5_pose_blue_box.orientation.z = 0.5
    ur5_pose_blue_box.orientation.w = 0.5

    ur5_pose_red_bin = geometry_msgs.msg.Pose()
    ur5_pose_red_bin.position.x = 0.11
    ur5_pose_red_bin.position.y = 0.65
    ur5_pose_red_bin.position.z = 1.19
    ur5_pose_red_bin.orientation.x = -0.5
    ur5_pose_red_bin.orientation.y = -0.5
    ur5_pose_red_bin.orientation.z = 0.5
    ur5_pose_red_bin.orientation.w = 0.5

    ur5_pose_green_bin = geometry_msgs.msg.Pose()
    ur5_pose_green_bin.position.x = 0.75
    ur5_pose_green_bin.position.y = 0.03
    ur5_pose_green_bin.position.z = 1.19
    ur5_pose_green_bin.orientation.x = -0.5
    ur5_pose_green_bin.orientation.y = -0.5
    ur5_pose_green_bin.orientation.z = 0.5
    ur5_pose_green_bin.orientation.w = 0.5

    ur5_pose_blue_bin = geometry_msgs.msg.Pose()
    ur5_pose_blue_bin.position.x = 0.04
    ur5_pose_blue_bin.position.y = -0.65
    ur5_pose_blue_bin.position.z = 1.19
    ur5_pose_blue_bin.orientation.x = -0.5
    ur5_pose_blue_bin.orientation.y = -0.5
    ur5_pose_blue_bin.orientation.z = 0.5
    ur5_pose_blue_bin.orientation.w = 0.5

    while not rospy.is_shutdown():

    	cb_req = rospy.ServiceProxy('/eyrc/vb/conveyor/set_power', conveyorBeltPowerMsg)
    	power_req = 11
    	r = cb_req(power_req)
    	cb_req.wait_for_service()

    	rospy.Subscriber('/eyrc/vb/logical_camera_2', LogicalCameraImage, ur5.callback_topic_subscription)
    	
        ur5.go_to_pose(ur5_pose_red_box)
        rospy.sleep(2)

        vg_req = rospy.ServiceProxy('/eyrc/vb/ur5_1/activate_vacuum_gripper', vacuumGripper)
    	req = True
    	q = vg_req(req)
    	vg_req.wait_for_service()

    	package_name = "packagen1"
    	ur5.add_box(box_pose, package_name)

        ur5.go_to_pose(ur5_pose_red_bin)
        rospy.sleep(2)
        ur5.go_to_pose(ur5_pose_green_box)
        rospy.sleep(2)
        ur5.go_to_pose(ur5_pose_green_bin)
        rospy.sleep(2)
        ur5.go_to_pose(ur5_pose_blue_box)
        rospy.sleep(2)
        ur5.go_to_pose(ur5_pose_blue_bin)
        rospy.sleep(2)

    del ur5


if __name__ == '__main__':
    main()