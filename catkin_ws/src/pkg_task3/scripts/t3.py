#! /usr/bin/env python

import rospy                                #importing ROS-python main module
import sys                                  #importing system services module
import copy                                 #importing copy module
import moveit_commander                     #importing moveit_commander module
import moveit_msgs.msg                      #importing moveit messages
import geometry_msgs.msg                    #importing geometry messages
import actionlib                            #importing actionlib module
import math                                 #importing math module


from pkg_vb_sim.srv import vacuumGripper    #importing topic to which request will be send to control vacuum-gripper


class Ur5Moveit:

    # Constructor
    def __init__(self):

        rospy.init_node('node_t3_ur5_1_pick_place_3', anonymous=True)

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
        

        rospy.loginfo(
            '\033[94m' + "Planning Group: {}".format(self._planning_frame) + '\033[0m')
        rospy.loginfo(
            '\033[94m' + "End Effector Link: {}".format(self._eef_link) + '\033[0m')
        rospy.loginfo(
            '\033[94m' + "Group Names: {}".format(self._group_names) + '\033[0m')

        rospy.loginfo('\033[94m' + " >>> Ur5Moveit init done." + '\033[0m')