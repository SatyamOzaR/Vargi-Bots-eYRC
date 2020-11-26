;; Auto-generated. Do not edit!


(when (boundp 'gazebo_conveyor::ConveyorBeltState)
  (if (not (find-package "GAZEBO_CONVEYOR"))
    (make-package "GAZEBO_CONVEYOR"))
  (shadow 'ConveyorBeltState (find-package "GAZEBO_CONVEYOR")))
(unless (find-package "GAZEBO_CONVEYOR::CONVEYORBELTSTATE")
  (make-package "GAZEBO_CONVEYOR::CONVEYORBELTSTATE"))

(in-package "ROS")
;;//! \htmlinclude ConveyorBeltState.msg.html


(defclass gazebo_conveyor::ConveyorBeltState
  :super ros::object
  :slots (_power _enabled ))

(defmethod gazebo_conveyor::ConveyorBeltState
  (:init
   (&key
    ((:power __power) 0.0)
    ((:enabled __enabled) nil)
    )
   (send-super :init)
   (setq _power (float __power))
   (setq _enabled __enabled)
   self)
  (:power
   (&optional __power)
   (if __power (setq _power __power)) _power)
  (:enabled
   (&optional __enabled)
   (if __enabled (setq _enabled __enabled)) _enabled)
  (:serialization-length
   ()
   (+
    ;; float64 _power
    8
    ;; bool _enabled
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _power
       (sys::poke _power (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; bool _enabled
       (if _enabled (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _power
     (setq _power (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; bool _enabled
     (setq _enabled (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get gazebo_conveyor::ConveyorBeltState :md5sum-) "c0b232b8dd148cb7c71d4df1ea72012c")
(setf (get gazebo_conveyor::ConveyorBeltState :datatype-) "gazebo_conveyor/ConveyorBeltState")
(setf (get gazebo_conveyor::ConveyorBeltState :definition-)
      "# Conveyor belt state message
float64 power  # power of the belt (percentage, in +Y direction of belt frame)
bool enabled  # true if the power of the belt can be modified; false if the belt is stopped

")



(provide :gazebo_conveyor/ConveyorBeltState "c0b232b8dd148cb7c71d4df1ea72012c")


