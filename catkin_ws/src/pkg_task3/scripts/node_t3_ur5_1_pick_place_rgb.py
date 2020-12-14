#!/usr/bin/python

import rospy                                    # importing ROS-python main library
import sys                                      # importing system-specific parameters and functions
import copy                                     # importing copy module
import moveit_commander                         # importing moveit_commander module

import actionlib                                # importing actionlib module
import math                                     # importing python-math module

import moveit_msgs.msg                          # importing messages from moveit
import geometry_msgs.msg                        # importing messages of type geometry


from pkg_vb_sim.srv import vacuumGripper        # importing the service for vacuum-gripper
from pkg_vb_sim.srv import conveyorBeltPowerMsg # importing the service for conveyor-belt

from pkg_vb_sim.msg import LogicalCameraImage   # importing messages of type LogicalCameraImage

red_flag = 0        # red_flag = 1; when '/eyrc/vb/logical_camera_2' identifies red-box at y=0
green_flag = 0      # green_flag = 1; when '/eyrc/vb/logical_camera_2' identifies green-box at y=0
blue_flag = 0       # blue_flag = 1; when '/eyrc/vb/logical_camera_2' identifies blue-box at y=0
flag1 = 0           # flag to control unnecessary looping of "callback_topic_subscription()" into "if" loop1
flag2 = 0           # flag to control unnecessary looping of "callback_topic_subscription()" into "if" loop2
flag3 = 0           # flag to control unnecessary looping of "callback_topic_subscription()" into "if" loop3

# defining dimensions

box_length = 0.15
vacuum_gripper_width = 0.115
delta = vacuum_gripper_width + box_length / 2

# defining empty box name variable

box_info = ''

# defining variable ur5_pose_box which get updated in callback_topic_subscription of '/eyrc/vb/logical_camera_2'

ur5_pose_box = geometry_msgs.msg.Pose()
ur5_pose_box.position.x = 0.0
ur5_pose_box.position.y = 0.0
ur5_pose_box.position.z = 0.0
ur5_pose_box.orientation.x = -0.5
ur5_pose_box.orientation.y = -0.5
ur5_pose_box.orientation.z = 0.5
ur5_pose_box.orientation.w = 0.5

# defining home-pose

lst_joint_angles_home = [0.13685723861509302,
						-2.4187425237720737,
						-0.9814488113660955,
						-1.3126940302415715,
						1.570201522236509,
						0.1377829842690499]

# defining the pose of red bin

lst_joint_angles_red_bin = [-1.572184973613136,
							-2.0994949938510876,
							-0.5254250205227358,
							-2.086538285094317,
							1.5699339831843382,
							-1.5724046515014916]

# defining the pose of green bin

lst_joint_angles_green_bin = [-0.10595895571085823,
								-0.857728977300714,
								1.1972589199929713,
								-1.9105803216062958,
								-1.5699827701952476,
								 3.0347509373039987]

# defining the pose of blue bin

lst_joint_angles_blue_bin = [1.8006901509669113,
								-2.0743284534279427,
								-1.5773086584286702,
								-1.0598575186767052,
								1.570639394818273,
								1.79996415235194]


class Ur5Moveit:

    # Constructor

    def __init__(self):

        rospy.init_node('node_t3_ur5_1_pick_place_rgb', anonymous=True)

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

    def set_joint_angles(self, arg_list_joint_angles):

        self._group.set_joint_value_target(arg_list_joint_angles)
        self._group.plan()
        flag_plan = self._group.go(wait=True)

        if (flag_plan == True):
            rospy.loginfo(
                '\033[94m' + "^^^^^^^^^^^Home Pose Success^^^^^^^^^^^^" + '\033[0m')
        else:
            rospy.logerr(
                '\033[94m' + "^^^^^^^^^^^Home Pose Failed^^^^^^^^^^^^" + '\033[0m')

        return flag_plan

    def pick_place(
        self,
        arg_pose_box,
        arg_list_joint_angles_bin,
        box_name,
        ):

        # creating service objects

        vg_req = \
            rospy.ServiceProxy('/eyrc/vb/ur5_1/activate_vacuum_gripper'
                               , vacuumGripper)

        cb_req = rospy.ServiceProxy('/eyrc/vb/conveyor/set_power',
                                    conveyorBeltPowerMsg)

        # extracting the pose at which box gets spawned in rviz

        box_pose_rviz = geometry_msgs.msg.PoseStamped()
        box_pose_rviz.pose.position.x = arg_pose_box.position.x
        box_pose_rviz.pose.position.y = arg_pose_box.position.y
        box_pose_rviz.pose.position.z = arg_pose_box.position.z - 0.193  # offset for no collision
        box_pose_rviz.header.frame_id = 'world'

        # going to box pose

        self._group.set_pose_target(arg_pose_box)
        flag_plan_box = self._group.go(wait=True)

        if flag_plan_box == True:
            rospy.loginfo('\033[94m' + '>>> go to box^^^^^^^^^' + box_name
                          + '^^^^^^^^^^^Pose Success' + '\033[0m')
        else:
            rospy.logerr('\033[94m' + '>>>  Solution for box^^^^^^^^^^^^'
                         + box_name + '^^^^^^^^^^^Pose not Found.' + '\033[0m')

        # activating vacuum gripper

        vg_req(True)

        # adding box in rviz

        self._scene.add_box(box_name, box_pose_rviz, size=(0.15, 0.15,
                            0.15))

        self._scene.attach_box(self._eef_link, box_name)

        # activating conveyor belt

        cb_req(22)

        # going to bin pose

        self._group.set_joint_value_target(arg_list_joint_angles_bin)
        self._group.plan()
        flag_plan_bin = self._group.go(wait=True)

        if (flag_plan_bin == True):
            rospy.loginfo(
                '\033[94m' + "^^^^^^^^^^^Bin Pose Success^^^^^^^^^^^^" + '\033[0m')
        else:
            rospy.logerr(
                '\033[94m' + "^^^^^^^^^^^Bin Pose Failed^^^^^^^^^^^^" + '\033[0m')

        # deactivating vacuum gripper

        vg_req(False)

        # remove box from End-Effector

        self._scene.remove_attached_object(self._eef_link,
                name=box_name)

        # removing box from rviz

        self._scene.remove_world_object(box_name)

        return flag_plan_box and flag_plan_bin

    def callback_topic_subscription(self, x_msg):

        # creating service object for conveyor belt

        cb_req = rospy.ServiceProxy('/eyrc/vb/conveyor/set_power',
                                    conveyorBeltPowerMsg)

        global flag1
        global flag2
        global flag3

        global red_flag
        global green_flag
        global blue_flag

        global ur5_pose_box
        global box_info
        global delta

        # getting the length of 'callback message' list

        number_models = len(x_msg.models)

        # searching for models of required type

        for i in range(0, number_models):

            name_model = x_msg.models[i].type
            pos = x_msg.models[i].pose

            # if 'packagen1' is found and is near specified pose range in y-axis of logical camera

            if name_model == 'packagen1' and pos.position.y >= -0.05 \
                and pos.position.y < 0.05 and flag1 == 0:

                # stopping conveyor belt

                cb_req(0)

                # assigning 'current pose' to 'goal'

                ur5_pose_box.position.x = pos.position.z - 0.8
                ur5_pose_box.position.y = pos.position.y
                ur5_pose_box.position.z = pos.position.x + delta
                box_info = name_model
                flag1 = 1
                red_flag = 1

            elif name_model == 'packagen2' and pos.position.y >= -0.05 \
                and pos.position.y < 0.05 and flag2 == 0:

            # if 'packagen2' is found and is near specified pose range in y-axis of logical camera

                # stopping conveyor belt

                cb_req(0)

                # assigning 'current pose' to 'goal'

                ur5_pose_box.position.x = pos.position.z - 0.8
                ur5_pose_box.position.y = pos.position.y
                ur5_pose_box.position.z = pos.position.x + delta
                box_info = name_model
                flag2 = 1
                green_flag = 1

            elif name_model == 'packagen3' and pos.position.y >= -0.05 \
                and pos.position.y < 0.05 and flag3 == 0:

            # if 'packagen3' is found and is near specified pose range in y-axis of logical camera

                # stopping conveyor belt

                cb_req(0)

                # assigning 'current pose' to 'goal'

                ur5_pose_box.position.x = pos.position.z - 0.8
                ur5_pose_box.position.y = pos.position.y
                ur5_pose_box.position.z = pos.position.x + delta
                box_info = name_model
                flag3 = 1
                blue_flag = 1

    # Destructor

    def __del__(self):
        moveit_commander.roscpp_shutdown()
        rospy.loginfo('\033[94m' + 'Object of class Ur5Moveit Deleted.'
                      + '\033[0m')


def main():

    # initialize the object of class Ur5Moveit()

    ur5 = Ur5Moveit()

    # subscribing to logical camera topic

    rospy.Subscriber('/eyrc/vb/logical_camera_2', LogicalCameraImage,
                     ur5.callback_topic_subscription)

    # creating service object for conveyor belt

    cb_req = rospy.ServiceProxy('/eyrc/vb/conveyor/set_power',
                                conveyorBeltPowerMsg)

    # let other threads get CPU time

    rospy.sleep(4) # also controls execution time of task

    # got to home pose

    ur5.set_joint_angles(lst_joint_angles_home)

    # let other threads get CPU time

    rospy.sleep(4) # also controls execution time of task

    # starting the conveyor belt

    cb_req(70)

    # wait for feedback from callback topic subscription

    while red_flag == 0:
        {}

    # pick red box and place in red bin

    ur5.pick_place(ur5_pose_box, lst_joint_angles_red_bin, box_info)

    # comeback to home pose

    ur5.set_joint_angles(lst_joint_angles_home)

    # wait for feedback from callback topic subscription

    while green_flag == 0:
        {}

    # pick green box and place in green bin

    ur5.pick_place(ur5_pose_box, lst_joint_angles_green_bin, box_info)

    # comeback to home pose

    #ur5.go_to_pose(home_pose)

    # wait for feedback from callback topic subscription

    while blue_flag == 0:
        {}

    # pick blue box and place in blue bin

    ur5.pick_place(ur5_pose_box, lst_joint_angles_blue_bin, box_info)

    # comeback to home pose

    ur5.set_joint_angles(lst_joint_angles_home)

    # end executing this script

    del ur5


if __name__ == '__main__':
    main()