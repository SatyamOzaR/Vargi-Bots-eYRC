; Auto-generated. Do not edit!


(cl:in-package pkg_vb_sim-srv)


;//! \htmlinclude ConveyorBeltControl-request.msg.html

(cl:defclass <ConveyorBeltControl-request> (roslisp-msg-protocol:ros-message)
  ((power
    :reader power
    :initarg :power
    :type cl:float
    :initform 0.0))
)

(cl:defclass ConveyorBeltControl-request (<ConveyorBeltControl-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ConveyorBeltControl-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ConveyorBeltControl-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pkg_vb_sim-srv:<ConveyorBeltControl-request> is deprecated: use pkg_vb_sim-srv:ConveyorBeltControl-request instead.")))

(cl:ensure-generic-function 'power-val :lambda-list '(m))
(cl:defmethod power-val ((m <ConveyorBeltControl-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg_vb_sim-srv:power-val is deprecated.  Use pkg_vb_sim-srv:power instead.")
  (power m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ConveyorBeltControl-request>) ostream)
  "Serializes a message object of type '<ConveyorBeltControl-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'power))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ConveyorBeltControl-request>) istream)
  "Deserializes a message object of type '<ConveyorBeltControl-request>"
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
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ConveyorBeltControl-request>)))
  "Returns string type for a service object of type '<ConveyorBeltControl-request>"
  "pkg_vb_sim/ConveyorBeltControlRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ConveyorBeltControl-request)))
  "Returns string type for a service object of type 'ConveyorBeltControl-request"
  "pkg_vb_sim/ConveyorBeltControlRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ConveyorBeltControl-request>)))
  "Returns md5sum for a message object of type '<ConveyorBeltControl-request>"
  "8b0e8e2d213d4fc4d0fcb5152aec2d9d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ConveyorBeltControl-request)))
  "Returns md5sum for a message object of type 'ConveyorBeltControl-request"
  "8b0e8e2d213d4fc4d0fcb5152aec2d9d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ConveyorBeltControl-request>)))
  "Returns full string definition for message of type '<ConveyorBeltControl-request>"
  (cl:format cl:nil "# Conveyor belt control~%~%# desired conveyor belt power~%float64 power~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ConveyorBeltControl-request)))
  "Returns full string definition for message of type 'ConveyorBeltControl-request"
  (cl:format cl:nil "# Conveyor belt control~%~%# desired conveyor belt power~%float64 power~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ConveyorBeltControl-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ConveyorBeltControl-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ConveyorBeltControl-request
    (cl:cons ':power (power msg))
))
;//! \htmlinclude ConveyorBeltControl-response.msg.html

(cl:defclass <ConveyorBeltControl-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ConveyorBeltControl-response (<ConveyorBeltControl-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ConveyorBeltControl-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ConveyorBeltControl-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pkg_vb_sim-srv:<ConveyorBeltControl-response> is deprecated: use pkg_vb_sim-srv:ConveyorBeltControl-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <ConveyorBeltControl-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg_vb_sim-srv:success-val is deprecated.  Use pkg_vb_sim-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ConveyorBeltControl-response>) ostream)
  "Serializes a message object of type '<ConveyorBeltControl-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ConveyorBeltControl-response>) istream)
  "Deserializes a message object of type '<ConveyorBeltControl-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ConveyorBeltControl-response>)))
  "Returns string type for a service object of type '<ConveyorBeltControl-response>"
  "pkg_vb_sim/ConveyorBeltControlResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ConveyorBeltControl-response)))
  "Returns string type for a service object of type 'ConveyorBeltControl-response"
  "pkg_vb_sim/ConveyorBeltControlResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ConveyorBeltControl-response>)))
  "Returns md5sum for a message object of type '<ConveyorBeltControl-response>"
  "8b0e8e2d213d4fc4d0fcb5152aec2d9d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ConveyorBeltControl-response)))
  "Returns md5sum for a message object of type 'ConveyorBeltControl-response"
  "8b0e8e2d213d4fc4d0fcb5152aec2d9d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ConveyorBeltControl-response>)))
  "Returns full string definition for message of type '<ConveyorBeltControl-response>"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ConveyorBeltControl-response)))
  "Returns full string definition for message of type 'ConveyorBeltControl-response"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ConveyorBeltControl-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ConveyorBeltControl-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ConveyorBeltControl-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ConveyorBeltControl)))
  'ConveyorBeltControl-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ConveyorBeltControl)))
  'ConveyorBeltControl-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ConveyorBeltControl)))
  "Returns string type for a service object of type '<ConveyorBeltControl>"
  "pkg_vb_sim/ConveyorBeltControl")