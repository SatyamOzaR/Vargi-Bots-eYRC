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

        rospy.init_node('node_t2_ur5_1_pick_place', anonymous=True)

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


    def add_box(self, pose1):

        self._pose = pose1
        self._box_name = "package$1"
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


    
    def go_to_predefined_pose(self, arg_pose_name):

        rospy.loginfo('\033[94m' + "Going to Pose: {}".format(arg_pose_name) + '\033[0m')

        self._group.set_named_target(arg_pose_name)

        plan = self._group.plan()
        goal = moveit_msgs.msg.ExecuteTrajectoryGoal()

        goal.trajectory = plan
        self._exectute_trajectory_client.send_goal(goal)
        self._exectute_trajectory_client.wait_for_result()

        rospy.loginfo('\033[94m' + "Now at Pose: {}".format(arg_pose_name) + '\033[0m')        


    # Destructor
    def __del__(self):

        moveit_commander.roscpp_shutdown()

        rospy.loginfo(
            '\033[94m' + "Object of class Ur5Moveit Deleted." + '\033[0m')


def main():

    ur5 = Ur5Moveit()

    #assigning the pose values to pick-box
    ur5_pose_pick = geometry_msgs.msg.Pose()
    ur5_pose_pick.position.x = 0.002621
    ur5_pose_pick.position.y = 0.250205
    ur5_pose_pick.position.z = 1.917898
    ur5_pose_pick.orientation.x = 0.000440
    ur5_pose_pick.orientation.y = 0.000447
    ur5_pose_pick.orientation.z = -0.000256
    ur5_pose_pick.orientation.w = 0.999999

    #assigning the pose values to drop-box
    ur5_pose_drop = geometry_msgs.msg.Pose()
    ur5_pose_drop.position.x = -0.648135
    ur5_pose_drop.position.y = -0.159417
    ur5_pose_drop.position.z = 0.921802
    ur5_pose_drop.orientation.x = -0.000228
    ur5_pose_drop.orientation.y = 9.168198e-05
    ur5_pose_drop.orientation.z = -0.000269
    ur5_pose_drop.orientation.w = 0.999999

    #pose at which the box is spawned in rviz
    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.pose.position.x = 0.0
    box_pose.pose.position.y = 0.455
    box_pose.pose.position.z = 1.917919
    box_pose.header.frame_id = "world"
   
    #heading towards pick pose
    ur5.go_to_pose(ur5_pose_pick)
    rospy.sleep(3)    

    #activating vacuum-gripper
    vg_req = rospy.ServiceProxy('/eyrc/vb/ur5_1/activate_vacuum_gripper', vacuumGripper)
    req = True
    q = vg_req(req)
    vg_req.wait_for_service()

    #adding box and attaching to end-effector
    ur5.add_box(box_pose)

    #going to drop box pose
    ur5.go_to_pose(ur5_pose_drop)
    rospy.sleep(2)

    #deactivating vacuum-gripper
    
    req = False
    q = vg_req(req)
    vg_req.wait_for_service()

    #removing the box from end-effector and from world
    box_name = "package$1"
    ur5.remove_box(box_name)

    #going to normal state
    ur5.go_to_predefined_pose("allZeros")
    rospy.sleep(2)

    #deleting Object of class Ur5Moveit
    del ur5


if __name__ == '__main__':
    main()