#!/usr/bin/env python

import rospy
import cv2
import sys
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from pyzbar.pyzbar import decode


import numpy as np

class Camera1:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/eyrc/vb/camera_1/image_raw", Image,self.callback)

  # Ref: GeekforGeeks.com, https://www.geeksforgeeks.org/detect-the-rgb-color-from-a-webcam-using-python-opencv/
  def get_dominant_colour(self, arg_img):
    # setting values for base colors 
    b = arg_img[:, :, :1] 
    g = arg_img[:, :, 1:2] 
    r = arg_img[:, :, 2:] 
  
    # computing the mean 
    b_mean = np.mean(b) 
    g_mean = np.mean(g) 
    r_mean = np.mean(r)

    d = decode(arg_img)
    print(d)

    # displaying the most prominent color 
    if (g_mean > r_mean and g_mean > b_mean): 
        return 'green' 
    else: 
        return 'something else'
  
  
  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      rospy.logerr(e)

    (rows,cols,channels) = cv_image.shape
    
    image = cv_image

    # Resize a 720x1280 image to 360x640 to fit it on the screen
    resized_image = cv2.resize(image, (720/2, 1280/2)) 

    cv2.imshow("/eyrc/vb/camera_1/image_raw", resized_image)

    rospy.loginfo(self.get_dominant_colour(image))

    cv2.waitKey(3)


def main(args):
  
  rospy.init_node('node_eg2_colour_detection', anonymous=True)

  ic = Camera1()
  
  try:
    rospy.spin()
  except KeyboardInterrupt:
    rospy.loginfo("Shutting down")
  
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
