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
import time

from pkg_vb_sim.srv import vacuumGripper  			# importing the service for vacuum-gripper
from pkg_vb_sim.srv import conveyorBeltPowerMsg  	# importing the service for conveyor-belt
from pkg_vb_sim.msg import LogicalCameraImage  		# importing messages of type LogicalCameraImage

red_flag = 0  		# red_flag = 1; when '/eyrc/vb/logical_camera_2' identifies red-box at y=0
green_flag = 0  	# green_flag = 1; when '/eyrc/vb/logical_camera_2' identifies green-box at y=0
blue_flag = 0  		# blue_flag = 1; when '/eyrc/vb/logical_camera_2' identifies blue-box at y=0
flag1 = 0  			# flag to control unnecessary looping of "callback_topic_subscription()" into "if" loop1
flag2 = 0  			# flag to control unnecessary looping of "callback_topic_subscription()" into "if" loop2
flag3 = 0  			# flag to control unnecessary looping of "callback_topic_subscription()" into "if" loop3
success_flag = 0
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
pose_red_bin.position.z = 1.005 + delta
pose_red_bin.orientation.x = -0.5
pose_red_bin.orientation.y = -0.5
pose_red_bin.orientation.z = 0.5
pose_red_bin.orientation.w = 0.5

pose_green_bin = geometry_msgs.msg.Pose()
pose_green_bin.position.x = 0.75
pose_green_bin.position.y = 0.03
pose_green_bin.position.z = 1.005 + delta
pose_green_bin.orientation.x = -0.5
pose_green_bin.orientation.y = -0.5
pose_green_bin.orientation.z = 0.5
pose_green_bin.orientation.w = 0.5

pose_blue_bin = geometry_msgs.msg.Pose()
pose_blue_bin.position.x = 0.04
pose_blue_bin.position.y = -0.65
pose_blue_bin.position.z = 1.005 + delta
pose_blue_bin.orientation.x = -0.5
pose_blue_bin.orientation.y = -0.5
pose_blue_bin.orientation.z = 0.5
pose_blue_bin.orientation.w = 0.5

box_info = ''


class Ur5Moveit:

    # Constructor

    def __init__(self):

        rospy.init_node('node_t_ur5_1_pick',
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

    def add_box(self, pose1, name):
        box_pose_rviz = geometry_msgs.msg.PoseStamped()
        box_pose_rviz.pose.position.x = pose1.position.x
        box_pose_rviz.pose.position.y = pose1.position.y
        box_pose_rviz.pose.position.z = 0.998
        box_pose_rviz.header.frame_id = 'world'
        self._pose = box_pose_rviz
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



    def conveyor_power(self, power):

        # creating client object for conveyor-power server
        cb_req = rospy.ServiceProxy('/eyrc/vb/conveyor/set_power',
                                conveyorBeltPowerMsg)

        # requesting the conveyor-power server to activate for defined power
        r = cb_req(power)
        cb_req.wait_for_service()


    def vacuum_gripper(self, req):

        # creating client object for vacuum-gripper server

        vg_req = rospy.ServiceProxy('/eyrc/vb/ur5_1/activate_vacuum_gripper'
                                , vacuumGripper)

        # activating vacuum-gripper by requesting vacuum-gripper server
        q = vg_req(req)
        vg_req.wait_for_service()

    def callback_topic_subscription(self, x_msg):

        global red_flag
        global green_flag
        global blue_flag
        global flag1
        global flag2
        global flag3
        global ur5_pose_box
        global delta


        number_models = len(x_msg.models)

        for i in range(0, number_models):

            name_model = x_msg.models[i].type
            pos = x_msg.models[i].pose

            if name_model == 'packagen1' and pos.position.y >= -0.01 \
                and pos.position.y < 0.01 and flag1 == 0:
                ur5_pose_box.position.x = pos.position.z-0.8
                ur5_pose_box.position.y = pos.position.y
                ur5_pose_box.position.z = pos.position.x+delta
                flag1 == 1
                red_flag = 1
            elif name_model == 'packagen2' and pos.position.y >= -0.01 \
                and pos.position.y < 0.01 and flag2 == 0:
                ur5_pose_box.position.x = pos.position.z-0.8
                ur5_pose_box.position.y = pos.position.y
                ur5_pose_box.position.z = pos.position.x+delta
                flag2 == 1
                green_flag = 1
            elif name_model == 'packagen3' and pos.position.y >= -0.01 \
                and pos.position.y < 0.01 and flag3 == 0:
                ur5_pose_box.position.x = pos.position.z-0.8
                ur5_pose_box.position.y = pos.position.y
                ur5_pose_box.position.z = pos.position.x+delta

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

    # subscribing to the topic '/eyrc/vb/logical_camera_2' and to get feedback in terms of package-name and positions

    rospy.Subscriber('/eyrc/vb/logical_camera_2', LogicalCameraImage,
                     ur5.callback_topic_subscription)

    ur5.conveyor_power(25)

    while red_flag == 0:
        {}


    box = 'packagen1'
            
    ur5.conveyor_power(0)

    ur5.go_to_pose(ur5_pose_box)

    ur5.vacuum_gripper(True)

    ur5.add_box(ur5_pose_box, box)

    #ur5.go_to_pose(pose_red_bin)

    ur5.ee_cartesian_translation(pose_red_bin.position.x-ur5_pose_box.position.x,
                                        pose_red_bin.position.y-ur5_pose_box.position.y,
                                        pose_red_bin.position.z-ur5_pose_box.position.z)

    
    ur5.conveyor_power(15)

    ur5.vacuum_gripper(False)

    ur5.remove_box(box)



    while green_flag == 0:
        {}

    box = 'packagen2'

    ur5.conveyor_power(0)

    #ur5.go_to_pose(ur5_pose_box)

    ur5.ee_cartesian_translation(ur5_pose_box.position.x-pose_red_bin.position.x,
                                ur5_pose_box.position.y-pose_red_bin.position.y,
                                ur5_pose_box.position.z-pose_red_bin.position.z)

    ur5.vacuum_gripper(True)

    ur5.add_box(ur5_pose_box, box)

    ur5.conveyor_power(11)

    ur5.go_to_pose(pose_green_bin)

    ur5.conveyor_power(11)

    ur5.vacuum_gripper(False)

    ur5.remove_box(box)



    while blue_flag == 0:
        {}

    box3 = 'packagen3'


    ur5.conveyor_power(0)

    ur5.go_to_pose(ur5_pose_box)

    ur5.vacuum_gripper(True)

    ur5.add_box(ur5_pose_box, box3)

    ur5.conveyor_power(11)

    #ur5.go_to_pose(pose_blue_bin)

    ur5.ee_cartesian_translation(pose_blue_bin.position.x-ur5_pose_box.position.x,
                                pose_blue_bin.position.y-ur5_pose_box.position.y,
                                pose_blue_bin.position.z-ur5_pose_box.position.z)
    ur5.conveyor_power(11)

    ur5.vacuum_gripper(False)

    ur5.remove_box(box3)

    del ur5

if __name__ == '__main__':
    main()





