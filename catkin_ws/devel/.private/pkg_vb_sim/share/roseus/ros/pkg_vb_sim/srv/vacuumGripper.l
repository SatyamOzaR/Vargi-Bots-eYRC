;; Auto-generated. Do not edit!


(when (boundp 'pkg_vb_sim::vacuumGripper)
  (if (not (find-package "PKG_VB_SIM"))
    (make-package "PKG_VB_SIM"))
  (shadow 'vacuumGripper (find-package "PKG_VB_SIM")))
(unless (find-package "PKG_VB_SIM::VACUUMGRIPPER")
  (make-package "PKG_VB_SIM::VACUUMGRIPPER"))
(unless (find-package "PKG_VB_SIM::VACUUMGRIPPERREQUEST")
  (make-package "PKG_VB_SIM::VACUUMGRIPPERREQUEST"))
(unless (find-package "PKG_VB_SIM::VACUUMGRIPPERRESPONSE")
  (make-package "PKG_VB_SIM::VACUUMGRIPPERRESPONSE"))

(in-package "ROS")





(defclass pkg_vb_sim::vacuumGripperRequest
  :super ros::object
  :slots (_activate_vacuum_gripper ))

(defmethod pkg_vb_sim::vacuumGripperRequest
  (:init
   (&key
    ((:activate_vacuum_gripper __activate_vacuum_gripper) nil)
    )
   (send-super :init)
   (setq _activate_vacuum_gripper __activate_vacuum_gripper)
   self)
  (:activate_vacuum_gripper
   (&optional __activate_vacuum_gripper)
   (if __activate_vacuum_gripper (setq _activate_vacuum_gripper __activate_vacuum_gripper)) _activate_vacuum_gripper)
  (:serialization-length
   ()
   (+
    ;; bool _activate_vacuum_gripper
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _activate_vacuum_gripper
       (if _activate_vacuum_gripper (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _activate_vacuum_gripper
     (setq _activate_vacuum_gripper (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass pkg_vb_sim::vacuumGripperResponse
  :super ros::object
  :slots (_result ))

(defmethod pkg_vb_sim::vacuumGripperResponse
  (:init
   (&key
    ((:result __result) nil)
    )
   (send-super :init)
   (setq _result __result)
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass pkg_vb_sim::vacuumGripper
  :super ros::object
  :slots ())

(setf (get pkg_vb_sim::vacuumGripper :md5sum-) "22dce99b1d1e31fc9ba6b2faee126298")
(setf (get pkg_vb_sim::vacuumGripper :datatype-) "pkg_vb_sim/vacuumGripper")
(setf (get pkg_vb_sim::vacuumGripper :request) pkg_vb_sim::vacuumGripperRequest)
(setf (get pkg_vb_sim::vacuumGripper :response) pkg_vb_sim::vacuumGripperResponse)

(defmethod pkg_vb_sim::vacuumGripperRequest
  (:response () (instance pkg_vb_sim::vacuumGripperResponse :init)))

(setf (get pkg_vb_sim::vacuumGripperRequest :md5sum-) "22dce99b1d1e31fc9ba6b2faee126298")
(setf (get pkg_vb_sim::vacuumGripperRequest :datatype-) "pkg_vb_sim/vacuumGripperRequest")
(setf (get pkg_vb_sim::vacuumGripperRequest :definition-)
      "bool activate_vacuum_gripper
---
bool result
")

(setf (get pkg_vb_sim::vacuumGripperResponse :md5sum-) "22dce99b1d1e31fc9ba6b2faee126298")
(setf (get pkg_vb_sim::vacuumGripperResponse :datatype-) "pkg_vb_sim/vacuumGripperResponse")
(setf (get pkg_vb_sim::vacuumGripperResponse :definition-)
      "bool activate_vacuum_gripper
---
bool result
")



(provide :pkg_vb_sim/vacuumGripper "22dce99b1d1e31fc9ba6b2faee126298")


