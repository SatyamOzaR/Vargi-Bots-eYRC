#!/usr/bin/python

import rospy  						# importing ROS-python main library
import sys  						# importing system-specific parameters and functions
import copy 						# importing copy module
import moveit_commander 			# importing moveit_commander module
import moveit_msgs.msg  			# importing messages from moveit
import geometry_msgs.msg  			# importing messages of type geometry
import actionlib  					# importing actionlib module
import math  						# importing python-math module

from pkg_vb_sim.srv import vacuumGripper  			# importing the service for vacuum-gripper
from pkg_vb_sim.srv import conveyorBeltPowerMsg  	# importing the service for conveyor-belt
from pkg_vb_sim.msg import LogicalCameraImage  		# importing messages of type LogicalCameraImage

red_flag = 0  		# red_flag = 1; when '/eyrc/vb/logical_camera_2' identifies red-box at y=0
green_flag = 0  	# green_flag = 1; when '/eyrc/vb/logical_camera_2' identifies green-box at y=0
blue_flag = 0  		# blue_flag = 1; when '/eyrc/vb/logical_camera_2' identifies blue-box at y=0
flag1 = 0  			# flag to control unnecessary looping of "callback_topic_subscription()" into "if" loop1
flag2 = 0  			# flag to control unnecessary looping of "callback_topic_subscription()" into "if" loop2
flag3 = 0  			# flag to control unnecessary looping of "callback_topic_subscription()" into "if" loop3


class Ur5Moveit:

    # Constructor

    def __init__(self):

        rospy.init_node('node_t3_ur5_1_pick_place_rgb.py',
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

        # Current State of the Robot is needed to add box to planning scene

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

    def set_joint_angles(self, arg_list_joint_angles):

        list_joint_values = self._group.get_current_joint_values()
        rospy.loginfo('\033[94m' + '>>> Current Joint Values:'
                      + '\033[0m')
        rospy.loginfo(list_joint_values)

        self._group.set_joint_value_target(arg_list_joint_angles)
        self._group.plan()
        flag_plan = self._group.go(wait=True)

        list_joint_values = self._group.get_current_joint_values()
        rospy.loginfo('\033[94m' + '>>> Final Joint Values:' + '\033[0m'
                      )
        rospy.loginfo(list_joint_values)

        pose_values = self._group.get_current_pose().pose
        rospy.loginfo('\033[94m' + '>>> Final Pose:' + '\033[0m')
        rospy.loginfo(pose_values)

        if flag_plan == True:
            rospy.loginfo('\033[94m' + '>>> set_joint_angles() Success'
                          + '\033[0m')
        else:
            rospy.logerr('\033[94m' + '>>> set_joint_angles() Failed.'
                         + '\033[0m')

        return flag_plan

    def add_box(self, pose1, name):

        self._pose = pose1
        self._box_name = name
        self.scene = moveit_commander.PlanningSceneInterface()
        self.scene.add_box(self._box_name, self._pose, size=(0.15,
                           0.15, 0.15))

        self.group_name = 'ur5_1_planning_group'
        self.group = \
            moveit_commander.MoveGroupCommander(self.group_name)

        self.eef_link = self.group.get_end_effector_link()
        self.scene.attach_box(self.eef_link, self._box_name)

    def remove_box(self, object_name):

        self.box_name = object_name

        self.scene = moveit_commander.PlanningSceneInterface()
        self.eef_link = self.group.get_end_effector_link()

        self.scene.remove_attached_object(self.eef_link,
                name=self.box_name)

        self.scene.remove_world_object(self.box_name)

    def callback_topic_subscription(self, x_msg):

        global red_flag
        global green_flag
        global blue_flag
        global flag1
        global flag2
        global flag3

        number_models = len(x_msg.models)

        for i in range(0, number_models):

            name_model = x_msg.models[i].type
            pos = x_msg.models[i].pose

            if name_model == 'packagen1' and pos.position.y >= -0.01 \
                and pos.position.y < 0.01 and flag1 == 0:

                print 'ready to pick red box'
                flag1 == 1
                red_flag = 1
            elif name_model == 'packagen2' and pos.position.y >= -0.01 \
                and pos.position.y < 0.01 and flag2 == 0:

                print 'ready to pick green box'
                flag2 == 1
                green_flag = 1
            elif name_model == 'packagen3' and pos.position.y >= -0.01 \
                and pos.position.y < 0.01 and flag3 == 0:

                print 'ready to pick blue box'
                flag3 = 1
                blue_flag = 1

    # Destructor

    def __del__(self):
        moveit_commander.roscpp_shutdown()
        rospy.loginfo('\033[94m' + 'Object of class Ur5Moveit Deleted.'
                      + '\033[0m')


def main():

    # creating the object of class Ur5Moveit()

    ur5 = Ur5Moveit()

    # creating client object for conveyor-power server

    cb_req = rospy.ServiceProxy('/eyrc/vb/conveyor/set_power',
                                conveyorBeltPowerMsg)

    # creating client object for vacuum-gripper server

    vg_req = rospy.ServiceProxy('/eyrc/vb/ur5_1/activate_vacuum_gripper'
                                , vacuumGripper)

    # subscribing to the topic '/eyrc/vb/logical_camera_2' and to get feedback in terms of package-name and positions

    rospy.Subscriber('/eyrc/vb/logical_camera_2', LogicalCameraImage,
                     ur5.callback_topic_subscription)

    # defining joint-poses of boxes and bins

    lst_joint_red_box = [
        0.136738174176239,
        -2.4433723314322577,
        -1.015493231203589,
        -1.2527420976789383,
        1.5701598096829272,
        0.13745811570573352,
        ]

    lst_joint_red_bin = [
        -1.572095163914824,
        -2.126789666427629,
        -1.5804880008405808,
        -1.0047835414082948,
        1.570448212469267,
        -1.5722516385510321,
        ]

    lst_joint_green_box = [
        0.16592096336899775,
        -2.129488982949546,
        -1.5759294868634353,
        -1.006705467061689,
        1.5700307146689507,
        0.1657972464914419,
        ]

    lst_joint_green_bin = [
        -0.10593894411957905,
        -0.8202531299890437,
        1.2400931742133245,
        -1.9898387564450184,
        -1.5700210689062253,
        3.035497458578803,
        ]
    lst_joint_blue_box = [
        0.12158735222169703,
        -2.8613667015769444,
        -0.1953767748745321,
        -1.6556216744224201,
        1.5700218863245965,
        0.12258242897469174,
        ]
    lst_joint_blue_bin = [
        1.8005952135366776,
        -2.5540825847368067,
        -0.805238265236035,
        1.7883759664740175,
        -1.5702815624673567,
        -1.3409121510993067,
        ]

    # defining the spawn-poses for boxes in rviz

    red_box_spawn_rviz = geometry_msgs.msg.PoseStamped()
    red_box_spawn_rviz.pose.position.x = -0.800328
    red_box_spawn_rviz.pose.position.y = 0.0
    red_box_spawn_rviz.pose.position.z = 0.998
    red_box_spawn_rviz.header.frame_id = 'world'

    green_box_spawn_rviz = geometry_msgs.msg.PoseStamped()
    green_box_spawn_rviz.pose.position.x = -0.660551
    green_box_spawn_rviz.pose.position.y = 0.0
    green_box_spawn_rviz.pose.position.z = 0.998
    green_box_spawn_rviz.header.frame_id = 'world'

    blue_box_spawn_rviz = geometry_msgs.msg.PoseStamped()
    blue_box_spawn_rviz.pose.position.x = -0.900551
    blue_box_spawn_rviz.pose.position.y = 0.0
    blue_box_spawn_rviz.pose.position.z = 0.998
    blue_box_spawn_rviz.header.frame_id = 'world'

    # requesting the conveyor-power server to activate for defined power

    power_req = 40
    r = cb_req(power_req)
    cb_req.wait_for_service()

    # make ur5 arm to head towards the red pox pose

    ur5.set_joint_angles(lst_joint_red_box)

    # waiting for logical-camera feedback

    while red_flag == 0:
        {}

    # stopping conveyor-belt

    power_req = 0
    r = cb_req(power_req)
    cb_req.wait_for_service()

    # activating vacuum-gripper by requesting vacuum-gripper server

    req = True
    q = vg_req(req)
    vg_req.wait_for_service()

    # adding box in rviz and attaching it to the end-effector

    name1 = 'packagen1'
    ur5.add_box(red_box_spawn_rviz, name1)
    

    # make ur5 arm to head towards the red bin pose

    ur5.set_joint_angles(lst_joint_red_bin)

    # deactivating vacuum-gripper

    req = False
    q = vg_req(req)
    vg_req.wait_for_service()

    # removing box from end-effector and from rviz

    ur5.remove_box(name1)

    # activating conveyor-belt

    power_req = 30
    r = cb_req(power_req)
    cb_req.wait_for_service()

    # make ur5 arm to head towards the green box pose

    ur5.set_joint_angles(lst_joint_green_box)

    # waiting for logical-camera feedback

    while green_flag == 0:
        {}

    # stop conveyor-belt

    power_req = 0
    r = cb_req(power_req)
    cb_req.wait_for_service()

    # activating vacuum-gripper

    req = True
    q = vg_req(req)
    vg_req.wait_for_service()

    # adding box to rviz and attaching it to the end-effector

    name1 = 'packagen2'
    ur5.add_box(green_box_spawn_rviz, name1)
    

    # make ur5 arm to head towards the green bin pose

    ur5.set_joint_angles(lst_joint_green_bin)

    # deactivating vacuum-gripper

    req = False
    q = vg_req(req)
    vg_req.wait_for_service()

    # removing box from end-effector and rviz

    ur5.remove_box(name1)

    # activating conveyor-belt

    power_req = 25
    r = cb_req(power_req)
    cb_req.wait_for_service()

    # make ur5 arm to head towards the blue box pose

    ur5.set_joint_angles(lst_joint_blue_box)

    # wait for logical-camera feedback

    while blue_flag == 0:
        {}

    # deactivating conveyor-belt

    power_req = 0
    r = cb_req(power_req)
    cb_req.wait_for_service()

    # activating vacuum-gripper

    req = True
    q = vg_req(req)
    vg_req.wait_for_service()

    # adding box to rviz and attaching it to the end-effector

    name1 = 'packagen3'
    ur5.add_box(blue_box_spawn_rviz, name1)
    

    # make ur5 arm to head towards the blue pin pose

    ur5.set_joint_angles(lst_joint_blue_bin)

    # deactivating vacuum-gripper

    req = False
    q = vg_req(req)
    vg_req.wait_for_service()

    # removing box from end-effector and rviz

    ur5.remove_box(name1)

    # make ur5 arm to go to rest pose

    ur5.set_joint_angles(lst_joint_red_box)

    # deleting the object of class Ur5Moveit()

    del ur5


if __name__ == '__main__':
    main()