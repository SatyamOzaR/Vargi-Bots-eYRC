;; Auto-generated. Do not edit!


(when (boundp 'pkg_vb_sim::LogicalCameraImage)
  (if (not (find-package "PKG_VB_SIM"))
    (make-package "PKG_VB_SIM"))
  (shadow 'LogicalCameraImage (find-package "PKG_VB_SIM")))
(unless (find-package "PKG_VB_SIM::LOGICALCAMERAIMAGE")
  (make-package "PKG_VB_SIM::LOGICALCAMERAIMAGE"))

(in-package "ROS")
;;//! \htmlinclude LogicalCameraImage.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass pkg_vb_sim::LogicalCameraImage
  :super ros::object
  :slots (_models _pose ))

(defmethod pkg_vb_sim::LogicalCameraImage
  (:init
   (&key
    ((:models __models) (let (r) (dotimes (i 0) (push (instance pkg_vb_sim::Model :init) r)) r))
    ((:pose __pose) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _models __models)
   (setq _pose __pose)
   self)
  (:models
   (&rest __models)
   (if (keywordp (car __models))
       (send* _models __models)
     (progn
       (if __models (setq _models (car __models)))
       _models)))
  (:pose
   (&rest __pose)
   (if (keywordp (car __pose))
       (send* _pose __pose)
     (progn
       (if __pose (setq _pose (car __pose)))
       _pose)))
  (:serialization-length
   ()
   (+
    ;; pkg_vb_sim/Model[] _models
    (apply #'+ (send-all _models :serialization-length)) 4
    ;; geometry_msgs/Pose _pose
    (send _pose :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; pkg_vb_sim/Model[] _models
     (write-long (length _models) s)
     (dolist (elem _models)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Pose _pose
       (send _pose :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; pkg_vb_sim/Model[] _models
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _models (let (r) (dotimes (i n) (push (instance pkg_vb_sim::Model :init) r)) r))
     (dolist (elem- _models)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Pose _pose
     (send _pose :deserialize buf ptr-) (incf ptr- (send _pose :serialization-length))
   ;;
   self)
  )

(setf (get pkg_vb_sim::LogicalCameraImage :md5sum-) "8d82d9667c3484c611dd31e2f750668a")
(setf (get pkg_vb_sim::LogicalCameraImage :datatype-) "pkg_vb_sim/LogicalCameraImage")
(setf (get pkg_vb_sim::LogicalCameraImage :definition-)
      "# Logical camera image message
Model[] models                  # models detected (poses in the frame of the camera)
geometry_msgs/Pose pose         # camera pose

================================================================================
MSG: pkg_vb_sim/Model
string type                     # model type
geometry_msgs/Pose pose         # model pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :pkg_vb_sim/LogicalCameraImage "8d82d9667c3484c611dd31e2f750668a")


