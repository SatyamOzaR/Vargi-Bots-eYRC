
(cl:in-package :asdf)

(defsystem "gazebo_conveyor-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ConveyorBeltState" :depends-on ("_package_ConveyorBeltState"))
    (:file "_package_ConveyorBeltState" :depends-on ("_package"))
  ))