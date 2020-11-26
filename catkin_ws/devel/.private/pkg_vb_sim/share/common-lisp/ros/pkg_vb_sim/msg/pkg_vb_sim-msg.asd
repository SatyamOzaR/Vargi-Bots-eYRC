
(cl:in-package :asdf)

(defsystem "pkg_vb_sim-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "ConveyorBeltState" :depends-on ("_package_ConveyorBeltState"))
    (:file "_package_ConveyorBeltState" :depends-on ("_package"))
    (:file "LogicalCameraImage" :depends-on ("_package_LogicalCameraImage"))
    (:file "_package_LogicalCameraImage" :depends-on ("_package"))
    (:file "Model" :depends-on ("_package_Model"))
    (:file "_package_Model" :depends-on ("_package"))
  ))