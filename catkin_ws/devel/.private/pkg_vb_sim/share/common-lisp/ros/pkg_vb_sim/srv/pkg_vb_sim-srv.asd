
(cl:in-package :asdf)

(defsystem "pkg_vb_sim-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ConveyorBeltControl" :depends-on ("_package_ConveyorBeltControl"))
    (:file "_package_ConveyorBeltControl" :depends-on ("_package"))
    (:file "conveyorBeltPowerMsg" :depends-on ("_package_conveyorBeltPowerMsg"))
    (:file "_package_conveyorBeltPowerMsg" :depends-on ("_package"))
    (:file "vacuumGripper" :depends-on ("_package_vacuumGripper"))
    (:file "_package_vacuumGripper" :depends-on ("_package"))
  ))