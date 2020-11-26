;; Auto-generated. Do not edit!


(when (boundp 'gazebo_conveyor::ConveyorBeltControl)
  (if (not (find-package "GAZEBO_CONVEYOR"))
    (make-package "GAZEBO_CONVEYOR"))
  (shadow 'ConveyorBeltControl (find-package "GAZEBO_CONVEYOR")))
(unless (find-package "GAZEBO_CONVEYOR::CONVEYORBELTCONTROL")
  (make-package "GAZEBO_CONVEYOR::CONVEYORBELTCONTROL"))
(unless (find-package "GAZEBO_CONVEYOR::CONVEYORBELTCONTROLREQUEST")
  (make-package "GAZEBO_CONVEYOR::CONVEYORBELTCONTROLREQUEST"))
(unless (find-package "GAZEBO_CONVEYOR::CONVEYORBELTCONTROLRESPONSE")
  (make-package "GAZEBO_CONVEYOR::CONVEYORBELTCONTROLRESPONSE"))

(in-package "ROS")





(defclass gazebo_conveyor::ConveyorBeltControlRequest
  :super ros::object
  :slots (_power ))

(defmethod gazebo_conveyor::ConveyorBeltControlRequest
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

(defclass gazebo_conveyor::ConveyorBeltControlResponse
  :super ros::object
  :slots (_success ))

(defmethod gazebo_conveyor::ConveyorBeltControlResponse
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

(defclass gazebo_conveyor::ConveyorBeltControl
  :super ros::object
  :slots ())

(setf (get gazebo_conveyor::ConveyorBeltControl :md5sum-) "8b0e8e2d213d4fc4d0fcb5152aec2d9d")
(setf (get gazebo_conveyor::ConveyorBeltControl :datatype-) "gazebo_conveyor/ConveyorBeltControl")
(setf (get gazebo_conveyor::ConveyorBeltControl :request) gazebo_conveyor::ConveyorBeltControlRequest)
(setf (get gazebo_conveyor::ConveyorBeltControl :response) gazebo_conveyor::ConveyorBeltControlResponse)

(defmethod gazebo_conveyor::ConveyorBeltControlRequest
  (:response () (instance gazebo_conveyor::ConveyorBeltControlResponse :init)))

(setf (get gazebo_conveyor::ConveyorBeltControlRequest :md5sum-) "8b0e8e2d213d4fc4d0fcb5152aec2d9d")
(setf (get gazebo_conveyor::ConveyorBeltControlRequest :datatype-) "gazebo_conveyor/ConveyorBeltControlRequest")
(setf (get gazebo_conveyor::ConveyorBeltControlRequest :definition-)
      "# Conveyor belt control

# desired conveyor belt power
float64 power

---
bool success

")

(setf (get gazebo_conveyor::ConveyorBeltControlResponse :md5sum-) "8b0e8e2d213d4fc4d0fcb5152aec2d9d")
(setf (get gazebo_conveyor::ConveyorBeltControlResponse :datatype-) "gazebo_conveyor/ConveyorBeltControlResponse")
(setf (get gazebo_conveyor::ConveyorBeltControlResponse :definition-)
      "# Conveyor belt control

# desired conveyor belt power
float64 power

---
bool success

")



(provide :gazebo_conveyor/ConveyorBeltControl "8b0e8e2d213d4fc4d0fcb5152aec2d9d")


