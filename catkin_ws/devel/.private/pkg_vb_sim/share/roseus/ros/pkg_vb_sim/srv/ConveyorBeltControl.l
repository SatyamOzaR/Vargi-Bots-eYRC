;; Auto-generated. Do not edit!


(when (boundp 'pkg_vb_sim::ConveyorBeltControl)
  (if (not (find-package "PKG_VB_SIM"))
    (make-package "PKG_VB_SIM"))
  (shadow 'ConveyorBeltControl (find-package "PKG_VB_SIM")))
(unless (find-package "PKG_VB_SIM::CONVEYORBELTCONTROL")
  (make-package "PKG_VB_SIM::CONVEYORBELTCONTROL"))
(unless (find-package "PKG_VB_SIM::CONVEYORBELTCONTROLREQUEST")
  (make-package "PKG_VB_SIM::CONVEYORBELTCONTROLREQUEST"))
(unless (find-package "PKG_VB_SIM::CONVEYORBELTCONTROLRESPONSE")
  (make-package "PKG_VB_SIM::CONVEYORBELTCONTROLRESPONSE"))

(in-package "ROS")





(defclass pkg_vb_sim::ConveyorBeltControlRequest
  :super ros::object
  :slots (_power ))

(defmethod pkg_vb_sim::ConveyorBeltControlRequest
  (:init
   (&key
    ((:power __power) 0.0)
    )
   (send-super :init)
   (setq _power (float __power))
   self)
  (:power
   (&optional __power)
   (if __power (setq _power __power)) _power)
  (:serialization-length
   ()
   (+
    ;; float64 _power
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _power
       (sys::poke _power (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _power
     (setq _power (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass pkg_vb_sim::ConveyorBeltControlResponse
  :super ros::object
  :slots (_success ))

(defmethod pkg_vb_sim::ConveyorBeltControlResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass pkg_vb_sim::ConveyorBeltControl
  :super ros::object
  :slots ())

(setf (get pkg_vb_sim::ConveyorBeltControl :md5sum-) "8b0e8e2d213d4fc4d0fcb5152aec2d9d")
(setf (get pkg_vb_sim::ConveyorBeltControl :datatype-) "pkg_vb_sim/ConveyorBeltControl")
(setf (get pkg_vb_sim::ConveyorBeltControl :request) pkg_vb_sim::ConveyorBeltControlRequest)
(setf (get pkg_vb_sim::ConveyorBeltControl :response) pkg_vb_sim::ConveyorBeltControlResponse)

(defmethod pkg_vb_sim::ConveyorBeltControlRequest
  (:response () (instance pkg_vb_sim::ConveyorBeltControlResponse :init)))

(setf (get pkg_vb_sim::ConveyorBeltControlRequest :md5sum-) "8b0e8e2d213d4fc4d0fcb5152aec2d9d")
(setf (get pkg_vb_sim::ConveyorBeltControlRequest :datatype-) "pkg_vb_sim/ConveyorBeltControlRequest")
(setf (get pkg_vb_sim::ConveyorBeltControlRequest :definition-)
      "# Conveyor belt control

# desired conveyor belt power
float64 power

---
bool success

")

(setf (get pkg_vb_sim::ConveyorBeltControlResponse :md5sum-) "8b0e8e2d213d4fc4d0fcb5152aec2d9d")
(setf (get pkg_vb_sim::ConveyorBeltControlResponse :datatype-) "pkg_vb_sim/ConveyorBeltControlResponse")
(setf (get pkg_vb_sim::ConveyorBeltControlResponse :definition-)
      "# Conveyor belt control

# desired conveyor belt power
float64 power

---
bool success

")



(provide :pkg_vb_sim/ConveyorBeltControl "8b0e8e2d213d4fc4d0fcb5152aec2d9d")


