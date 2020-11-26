#!/usr/bin/env python

#importing the library required, topics and mathematical functions
import rospy        #the main library for ROS functions in python
from geometry_msgs.msg import Twist     #the (node_turtle_revolve) node will publish velocities to this Twist
from turtlesim.msg import Pose      #the (node_turtle_revolve) node will subscribe to position of tutle at different instances from Pose
from math import pow, sqrt      #importing the math functions required to vary velocities

class turtle_revolve():

    def __init__(self):
    #defining the node, publisher and subcriber in this section
        rospy.init_node('node_turtle_revolve')
        self.vel_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size = 10)
        self.pos_sub = rospy.Subscriber('/turtle1/pose', Pose, self.pos_callback)
        self.pose = Pose()
        self.rate = rospy.Rate(10)


    #defining the pos_callback function to update pose values
    def pos_callback(self, msg):
        self.pose = msg
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
        self.pose.theta = round(self.pose.theta, 4)
        #print(self.pose.x, self.pose.y, self.pose.theta)


    #calculating distance from updated_pose to goal_pose 
    def distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance


    #main loop function
    def main(self):
        goal_pose = Pose()
        goal_pose.x = 5.5344  #spawn_pose.x - distance_tolerance = goal_pose.x
        goal_pose.y = 5.5344  #spawn_pose.y - distance_tolerance = goal_pose.y
        distance_tolerance = 0.01


        vel_msg = Twist()

        while sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2)) >= distance_tolerance:

            #linear velocity component
            vel_msg.linear.x =  0.9325 * sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
            vel_msg.linear.y =  0
            vel_msg.linear.z =  0

            t1=float(rospy.Time.now().to_sec())
            rospy.loginfo('moving in a circle... Time:')
            print t1
            #angular velocity component
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = vel_msg.linear.x #equating to linear_velocity to get circle of radius 1 (unit)
                                                            # [radius=(linear_velocity/angular_velocity)]

            #Publishing our vel_msg
            self.vel_pub.publish(vel_msg)
            self.rate.sleep()

        #terminating after the goal reached
        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        self.vel_pub.publish(vel_msg)
        rospy.loginfo('goal reached. Final Time:')
        print t1
        rospy.spin() #terminate executing script on ctrl+c



if __name__ == '__main__':
    try:
        p = turtle_revolve()
        p.main()

    except rospy.ROSInterruptException: pass
