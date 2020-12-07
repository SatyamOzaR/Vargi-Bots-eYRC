#!/usr/bin/python

import rospy                                    # importing ROS-python main library
import sys                                      # importing system-specific parameters and functions
import copy                                     # importing copy module
import moveit_commander                         # importing moveit_commander module
import moveit_msgs.msg                          # importing messages from moveit
import geometry_msgs.msg                        # importing messages of type geometry
import actionlib                                # importing actionlib module
import math                                     # importing python-math module

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

home_pose = geometry_msgs.msg.Pose()
home_pose.position.x = -0.8
home_pose.position.y = 0.0
home_pose.position.z = 1.22
home_pose.orientation.x = -0.5
home_pose.orientation.y = -0.5
home_pose.orientation.z = 0.5
home_pose.orientation.w = 0.5

# defining the pose of red bin

pose_red_bin = geometry_msgs.msg.Pose()
pose_red_bin.position.x = 0.11
pose_red_bin.position.y = 0.65
pose_red_bin.position.z = 1.3 + delta
pose_red_bin.orientation.x = -0.5
pose_red_bin.orientation.y = -0.5
pose_red_bin.orientation.z = 0.5
pose_red_bin.orientation.w = 0.5

# defining the pose pf green bin

pose_green_bin = geometry_msgs.msg.Pose()
pose_green_bin.position.x = 0.75
pose_green_bin.position.y = 0.03
pose_green_bin.position.z = 1.2 + delta
pose_green_bin.orientation.x = -0.5
pose_green_bin.orientation.y = -0.5
pose_green_bin.orientation.z = 0.5
pose_green_bin.orientation.w = 0.5

# defining the pose of blue bin

pose_blue_bin = geometry_msgs.msg.Pose()
pose_blue_bin.position.x = 0.04
pose_blue_bin.position.y = -0.65
pose_blue_bin.position.z = 1 + delta
pose_blue_bin.orientation.x = -0.5
pose_blue_bin.orientation.y = -0.5
pose_blue_bin.orientation.z = 0.5
pose_blue_bin.orientation.w = 0.5


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

    def go_to_pose(self, arg_pose):

        self._group.set_pose_target(arg_pose)
        flag_plan = self._group.go(wait=True)

        return flag_plan

    def ee_cartesian_translation(self, trans_x, trans_y, trans_z):
        # Create a empty list to hold waypoints
        waypoints = []

        # Add Current Pose to the list of waypoints
        waypoints.append(self._group.get_current_pose().pose)

        # Create a New waypoint
        wpose = geometry_msgs.msg.Pose()
        wpose.position.x = waypoints[0].position.x + (trans_x)  
        wpose.position.y = waypoints[0].position.y + (trans_y)  
        wpose.position.z = waypoints[0].position.z + (trans_z)
        # This to keep EE parallel to Ground Plane
        wpose.orientation.x = -0.5
        wpose.orientation.y = -0.5
        wpose.orientation.z = 0.5
        wpose.orientation.w = 0.5

        waypoints.append(copy.deepcopy(wpose))

        (plan, fraction) = self._group.compute_cartesian_path(
            waypoints,
            0.01,  
            0.0)
        rospy.loginfo("Path computed successfully. Moving the arm.")

        num_pts = len(plan.joint_trajectory.points)
        if (num_pts >= 3):
            del plan.joint_trajectory.points[0]
            del plan.joint_trajectory.points[1]

        self._group.execute(plan)

    def add_box(self, arg_pose_box, box_name):

        # extracting the pose at which box gets spawned in rviz

        box_pose_rviz = geometry_msgs.msg.PoseStamped()
        box_pose_rviz.pose.position.x = arg_pose_box.position.x
        box_pose_rviz.pose.position.y = arg_pose_box.position.y
        box_pose_rviz.pose.position.z = arg_pose_box.position.z - 0.192  # offset for no collision
        box_pose_rviz.header.frame_id = 'world'

        # adding box in rviz

        self._scene.add_box(box_name, box_pose_rviz, size=(0.15, 0.15,
                            0.15))

        self._scene.attach_box(self._eef_link, box_name)

    def remove_box(self, box_name):
        # remove box from End-Effector

        self._scene.remove_attached_object(self._eef_link,
                name=box_name)

        # removing box from rviz

        self._scene.remove_world_object(box_name)

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

            if name_model == 'packagen1' and pos.position.y >= -0.03 \
                and pos.position.y < 0.03 and flag1 == 0:

                # stopping conveyor belt

                cb_req(0)

                # assigning 'current pose' to 'goal'

                ur5_pose_box.position.x = pos.position.z - 0.8
                ur5_pose_box.position.y = pos.position.y
                ur5_pose_box.position.z = pos.position.x + delta
                box_info = name_model
                flag1 = 1
                red_flag = 1

            elif name_model == 'packagen2' and pos.position.y >= -0.03 \
                and pos.position.y < 0.03 and flag2 == 0:

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

            elif name_model == 'packagen3' and pos.position.y >= -0.03 \
                and pos.position.y < 0.03 and flag3 == 0:

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

    # creating service objects
    vg_req = rospy.ServiceProxy('/eyrc/vb/ur5_1/activate_vacuum_gripper'
                               , vacuumGripper)

    # creating service object for conveyor belt

    cb_req = rospy.ServiceProxy('/eyrc/vb/conveyor/set_power',
                                conveyorBeltPowerMsg)

    # starting the conveyor belt

    cb_req(35)

    # got to home pose

    ur5.go_to_pose(home_pose)

    # wait for feedback from callback topic subscription

    while red_flag == 0:
        {}

    pose_red_box = geometry_msgs.msg.Pose()
    pose_red_box.position.x = ur5_pose_box.position.x
    pose_red_box.position.y = ur5_pose_box.position.y
    pose_red_box.position.z = ur5_pose_box.position.z
    pose_red_box.orientation.x = ur5_pose_box.orientation.x
    pose_red_box.orientation.y = ur5_pose_box.orientation.y
    pose_red_box.orientation.z = ur5_pose_box.orientation.z
    pose_red_box.orientation.w = ur5_pose_box.orientation.w

    name = box_info

    # going to red box pose

    ur5.ee_cartesian_translation(pose_red_box.position.x - home_pose.position.x,
                                 pose_red_box.position.y - home_pose.position.y,
                                 pose_red_box.position.z - home_pose.position.z)
    # add box

    ur5.add_box(pose_red_box, name)

    # activating vacuum gripper

    vg_req(True)

    # activating conveyor belt

    cb_req(25)

    # go to pose red bin

    ur5.ee_cartesian_translation(pose_red_bin.position.x - pose_red_box.position.x,
                                 pose_red_bin.position.y - pose_red_box.position.y,
                                 pose_red_bin.position.z - pose_red_box.position.z)

    # deactivating vacuum gripper

    vg_req(False)

    # remove box

    ur5.remove_box(name)

    # comeback to home pose

    ur5.ee_cartesian_translation(home_pose.position.x - pose_red_bin.position.x,
                                 home_pose.position.y - pose_red_bin.position.y,
                                 home_pose.position.z - pose_red_bin.position.z)

    # wait for feedback from callback topic subscription

    while green_flag == 0:
        {}

    pose_green_box = geometry_msgs.msg.Pose()
    pose_green_box.position.x = ur5_pose_box.position.x
    pose_green_box.position.y = ur5_pose_box.position.y
    pose_green_box.position.z = ur5_pose_box.position.z
    pose_green_box.orientation.x = ur5_pose_box.orientation.x
    pose_green_box.orientation.y = ur5_pose_box.orientation.y
    pose_green_box.orientation.z = ur5_pose_box.orientation.z
    pose_green_box.orientation.w = ur5_pose_box.orientation.w

    name = box_info

    # going to green box pose

    ur5.ee_cartesian_translation(pose_green_box.position.x - home_pose.position.x,
                                 pose_green_box.position.y - home_pose.position.y,
                                 pose_green_box.position.z - home_pose.position.z)
    # add box

    ur5.add_box(pose_green_box, name)

    # activating vacuum gripper

    vg_req(True)

    # activating conveyor belt

    cb_req(20)

    # go to pose green bin

    ur5.go_to_pose(pose_green_bin)

    # deactivating vacuum gripper

    vg_req(False)

    # remove box

    ur5.remove_box(name)

    # comeback to home pose

    ur5.go_to_pose(home_pose)

    # wait for feedback from callback topic subscription

    while blue_flag == 0:
        {}

    pose_blue_box = geometry_msgs.msg.Pose()
    pose_blue_box.position.x = ur5_pose_box.position.x
    pose_blue_box.position.y = ur5_pose_box.position.y
    pose_blue_box.position.z = ur5_pose_box.position.z
    pose_blue_box.orientation.x = ur5_pose_box.orientation.x
    pose_blue_box.orientation.y = ur5_pose_box.orientation.y
    pose_blue_box.orientation.z = ur5_pose_box.orientation.z
    pose_blue_box.orientation.w = ur5_pose_box.orientation.w

    name = box_info

    # going to green box pose

    ur5.ee_cartesian_translation(pose_blue_box.position.x - home_pose.position.x,
                                 pose_blue_box.position.y - home_pose.position.y,
                                 pose_blue_box.position.z - home_pose.position.z)
    # add box

    ur5.add_box(pose_blue_box, name)

    # activating vacuum gripper

    vg_req(True)

    # activating conveyor belt

    cb_req(20)

    ur5.ee_cartesian_translation(pose_blue_bin.position.x - pose_blue_box.position.x,
                                 pose_blue_bin.position.y - pose_blue_box.position.y,
                                 pose_blue_bin.position.z - pose_blue_box.position.z)

    # deactivating vacuum gripper

    vg_req(False)

    # remove box

    ur5.remove_box(name)
    
    # comeback to home pose

    ur5.ee_cartesian_translation(home_pose.position.x - pose_blue_bin.position.x,
                                 home_pose.position.y - pose_blue_bin.position.y,
                                 home_pose.position.z - pose_blue_bin.position.z)

    # end executing this script

    del ur5


if __name__ == '__main__':
    main()
	