
(cl:in-package :asdf)

(defsystem "gazebo_conveyor-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ConveyorBeltControl" :depends-on ("_package_ConveyorBeltControl"))
    (:file "_package_ConveyorBeltControl" :depends-on ("_package"))
  ))