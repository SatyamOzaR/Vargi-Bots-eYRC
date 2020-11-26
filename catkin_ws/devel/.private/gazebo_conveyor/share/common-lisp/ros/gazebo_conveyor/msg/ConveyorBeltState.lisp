; Auto-generated. Do not edit!


(cl:in-package gazebo_conveyor-msg)


;//! \htmlinclude ConveyorBeltState.msg.html

(cl:defclass <ConveyorBeltState> (roslisp-msg-protocol:ros-message)
  ((power
    :reader power
    :initarg :power
    :type cl:float
    :initform 0.0)
   (enabled
    :reader enabled
    :initarg :enabled
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ConveyorBeltState (<ConveyorBeltState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ConveyorBeltState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ConveyorBeltState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gazebo_conveyor-msg:<ConveyorBeltState> is deprecated: use gazebo_conveyor-msg:ConveyorBeltState instead.")))

(cl:ensure-generic-function 'power-val :lambda-list '(m))
(cl:defmethod power-val ((m <ConveyorBeltState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gazebo_conveyor-msg:power-val is deprecated.  Use gazebo_conveyor-msg:power instead.")
  (power m))

(cl:ensure-generic-function 'enabled-val :lambda-list '(m))
(cl:defmethod enabled-val ((m <ConveyorBeltState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gazebo_conveyor-msg:enabled-val is deprecated.  Use gazebo_conveyor-msg:enabled instead.")
  (enabled m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ConveyorBeltState>) ostream)
  "Serializes a message object of type '<ConveyorBeltState>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'power))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'enabled) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ConveyorBeltState>) istream)
  "Deserializes a message object of type '<ConveyorBeltState>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'power) (roslisp-utils:decode-double-float-bits bits)))
    (cl:setf (cl:slot-value msg 'enabled) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ConveyorBeltState>)))
  "Returns string type for a message object of type '<ConveyorBeltState>"
  "gazebo_conveyor/ConveyorBeltState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ConveyorBeltState)))
  "Returns string type for a message object of type 'ConveyorBeltState"
  "gazebo_conveyor/ConveyorBeltState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ConveyorBeltState>)))
  "Returns md5sum for a message object of type '<ConveyorBeltState>"
  "c0b232b8dd148cb7c71d4df1ea72012c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ConveyorBeltState)))
  "Returns md5sum for a message object of type 'ConveyorBeltState"
  "c0b232b8dd148cb7c71d4df1ea72012c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ConveyorBeltState>)))
  "Returns full string definition for message of type '<ConveyorBeltState>"
  (cl:format cl:nil "# Conveyor belt state message~%float64 power  # power of the belt (percentage, in +Y direction of belt frame)~%bool enabled  # true if the power of the belt can be modified; false if the belt is stopped~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ConveyorBeltState)))
  "Returns full string definition for message of type 'ConveyorBeltState"
  (cl:format cl:nil "# Conveyor belt state message~%float64 power  # power of the belt (percentage, in +Y direction of belt frame)~%bool enabled  # true if the power of the belt can be modified; false if the belt is stopped~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ConveyorBeltState>))
  (cl:+ 0
     8
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ConveyorBeltState>))
  "Converts a ROS message object to a list"
  (cl:list 'ConveyorBeltState
    (cl:cons ':power (power msg))
    (cl:cons ':enabled (enabled msg))
))
