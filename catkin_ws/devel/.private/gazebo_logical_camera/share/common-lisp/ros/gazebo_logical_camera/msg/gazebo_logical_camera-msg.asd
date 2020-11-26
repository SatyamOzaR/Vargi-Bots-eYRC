
(cl:in-package :asdf)

(defsystem "gazebo_logical_camera-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "LogicalCameraImage" :depends-on ("_package_LogicalCameraImage"))
    (:file "_package_LogicalCameraImage" :depends-on ("_package"))
    (:file "Model" :depends-on ("_package_Model"))
    (:file "_package_Model" :depends-on ("_package"))
  ))