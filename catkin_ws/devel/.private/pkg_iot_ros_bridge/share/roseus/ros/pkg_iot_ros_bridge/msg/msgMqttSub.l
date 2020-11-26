;; Auto-generated. Do not edit!


(when (boundp 'pkg_iot_ros_bridge::msgMqttSub)
  (if (not (find-package "PKG_IOT_ROS_BRIDGE"))
    (make-package "PKG_IOT_ROS_BRIDGE"))
  (shadow 'msgMqttSub (find-package "PKG_IOT_ROS_BRIDGE")))
(unless (find-package "PKG_IOT_ROS_BRIDGE::MSGMQTTSUB")
  (make-package "PKG_IOT_ROS_BRIDGE::MSGMQTTSUB"))

(in-package "ROS")
;;//! \htmlinclude msgMqttSub.msg.html


(defclass pkg_iot_ros_bridge::msgMqttSub
  :super ros::object
  :slots (_timestamp _topic _message ))

(defmethod pkg_iot_ros_bridge::msgMqttSub
  (:init
   (&key
    ((:timestamp __timestamp) (instance ros::time :init))
    ((:topic __topic) "")
    ((:message __message) "")
    )
   (send-super :init)
   (setq _timestamp __timestamp)
   (setq _topic (string __topic))
   (setq _message (string __message))
   self)
  (:timestamp
   (&optional __timestamp)
   (if __timestamp (setq _timestamp __timestamp)) _timestamp)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:serialization-length
   ()
   (+
    ;; time _timestamp
    8
    ;; string _topic
    4 (length _topic)
    ;; string _message
    4 (length _message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; time _timestamp
       (write-long (send _timestamp :sec) s) (write-long (send _timestamp :nsec) s)
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; time _timestamp
     (send _timestamp :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _timestamp :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get pkg_iot_ros_bridge::msgMqttSub :md5sum-) "76824121accacb087a76246dc01cbb0b")
(setf (get pkg_iot_ros_bridge::msgMqttSub :datatype-) "pkg_iot_ros_bridge/msgMqttSub")
(setf (get pkg_iot_ros_bridge::msgMqttSub :definition-)
      "time timestamp
string topic
string message

")



(provide :pkg_iot_ros_bridge/msgMqttSub "76824121accacb087a76246dc01cbb0b")


