#!/usr/bin/env python

# ROS Node - IoT Action Client - Turtle

import rospy
import actionlib
import time

from pkg_task1.msg import msgTurtleAction               # Message Class that is used by ROS Actions internally
from pkg_task1.msg import msgTurtleGoal                 # Message Class that is used for Goal messages

from pkg_ros_iot_bridge.msg import msgRosIotAction      # Message Class that is used by ROS Actions internally
from pkg_ros_iot_bridge.msg import msgRosIotGoal        # Message Class that is used for Goal Messages
from pkg_ros_iot_bridge.msg import msgRosIotResult      # Message Class that is used for Result Messages

from pkg_iot_ros_bridge.msg import msgMqttSub           # Message Class for MQTT Subscription Messages  


flag1=0
flag2=0


class IotActionClientTurtle:
   
    # Constructor
    def __init__(self):
        self._ac = actionlib.SimpleActionClient('/action_turtle',
                                                msgTurtleAction)
        self.turtle_client=send_pos_to_bridge()
        self._ac.wait_for_server()
        rospy.loginfo("Action server is up, we can send new goals!")

    # Function to send Goals to Action Servers
    def send_goal(self, arg_dis, arg_angle):
        global flag1
        # Create Goal message for Simple Action Server
        goal = msgTurtleGoal(distance=arg_dis, angle=arg_angle)
        
        '''
            * done_cb is set to the function pointer of the function which should be called once 
                the Goal is processed by the Simple Action Server.
            * feedback_cb is set to the function pointer of the function which should be called while
                the goal is being processed by the Simple Action Server.
        ''' 
       
        self._ac.send_goal(goal, done_cb=self.done_callback,
                           feedback_cb=self.feedback_callback)
            
        flag1=flag1+1

        rospy.loginfo("Goal " + str(flag1)+ " has been sent.")

    # Function print result on Goal completion
    def done_callback(self, status, result):
        global flag2

        store=[]
        
        rospy.loginfo("Result is : " + str(result))
        store.append(result.final_x)
        store.append(result.final_y)
        store.append(result.final_theta)
        rospy.loginfo(store)
        self.turtle_client.send_bridge_goal("mqtt","pub","eyrc/EyrcSaka/ros_to_iot",str(store))

    # Function to print feedback while Goal is being processed
    def feedback_callback(self, feedback):
        rospy.loginfo(feedback)
        


class send_pos_to_bridge:
    
    #Constructor 
    def __init__(self):
        
        self._ac2=actionlib.ActionClient('/action_ros_iot',msgRosIotAction)
        self._goal_handles={}  #Dictionary to Store all the goal handels

        param_config_pyiot=rospy.get_param('config_pyiot')
        self._config_mqtt_pub_topic=param_config_pyiot['mqtt']['topic_pub']
        self._ac2.wait_for_server()

        rospy.loginfo("Ros-IoT Bridge server is ready...")

    def send_bridge_goal(self,arg_protocol,arg_mode,arg_topic,arg_message):
        bridge_goal=msgRosIotGoal()

        bridge_goal.protocol=arg_protocol
        bridge_goal.mode=arg_mode
        bridge_goal.topic=arg_topic
        bridge_goal.message=arg_message

        goal_handle=self._ac2.send_goal(bridge_goal,None,None)

        return goal_handle



def bridge_callback(bridgeMsg):
    global flag2
    if bridgeMsg.topic == 'eyrc/EyrcSaka/iot_to_ros' and bridgeMsg.message=='start':
        flag2=1



# Main Function
def main():

    # 1. Initialize ROS Node
    rospy.init_node('node_simple_action_client_turtle')
    rospy.Subscriber('/ros_iot_bridge/mqtt/sub',msgMqttSub , bridge_callback)
    while flag2 == 0:
       {}
    rospy.loginfo(flag2)


    # 2. Create a object for Simple Action Client.
    obj_client = IotActionClientTurtle()

    # 3. Send Goals to Draw a Square
    obj_client.send_goal(2, 0)
    rospy.sleep(10)
   
    obj_client.send_goal(2, 60)
    rospy.sleep(10)

    obj_client.send_goal(2, 60)
    rospy.sleep(10)

    obj_client.send_goal(2, 60)
    rospy.sleep(10)

    obj_client.send_goal(2, 60)
    rospy.sleep(10)

    obj_client.send_goal(2, 60)
    rospy.sleep(10)


    # 4. Loop forever
    rospy.spin()


if __name__ == '__main__':
    main()