; Auto-generated. Do not edit!


(cl:in-package pkg_vb_sim-srv)


;//! \htmlinclude conveyorBeltPowerMsg-request.msg.html

(cl:defclass <conveyorBeltPowerMsg-request> (roslisp-msg-protocol:ros-message)
  ((power
    :reader power
    :initarg :power
    :type cl:fixnum
    :initform 0))
)

(cl:defclass conveyorBeltPowerMsg-request (<conveyorBeltPowerMsg-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <conveyorBeltPowerMsg-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'conveyorBeltPowerMsg-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pkg_vb_sim-srv:<conveyorBeltPowerMsg-request> is deprecated: use pkg_vb_sim-srv:conveyorBeltPowerMsg-request instead.")))

(cl:ensure-generic-function 'power-val :lambda-list '(m))
(cl:defmethod power-val ((m <conveyorBeltPowerMsg-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg_vb_sim-srv:power-val is deprecated.  Use pkg_vb_sim-srv:power instead.")
  (power m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <conveyorBeltPowerMsg-request>) ostream)
  "Serializes a message object of type '<conveyorBeltPowerMsg-request>"
  (cl:let* ((signed (cl:slot-value msg 'power)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <conveyorBeltPowerMsg-request>) istream)
  "Deserializes a message object of type '<conveyorBeltPowerMsg-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'power) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<conveyorBeltPowerMsg-request>)))
  "Returns string type for a service object of type '<conveyorBeltPowerMsg-request>"
  "pkg_vb_sim/conveyorBeltPowerMsgRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'conveyorBeltPowerMsg-request)))
  "Returns string type for a service object of type 'conveyorBeltPowerMsg-request"
  "pkg_vb_sim/conveyorBeltPowerMsgRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<conveyorBeltPowerMsg-request>)))
  "Returns md5sum for a message object of type '<conveyorBeltPowerMsg-request>"
  "734278aaf6d621cbe98c5cbee4553347")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'conveyorBeltPowerMsg-request)))
  "Returns md5sum for a message object of type 'conveyorBeltPowerMsg-request"
  "734278aaf6d621cbe98c5cbee4553347")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<conveyorBeltPowerMsg-request>)))
  "Returns full string definition for message of type '<conveyorBeltPowerMsg-request>"
  (cl:format cl:nil "int8 power~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'conveyorBeltPowerMsg-request)))
  "Returns full string definition for message of type 'conveyorBeltPowerMsg-request"
  (cl:format cl:nil "int8 power~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <conveyorBeltPowerMsg-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <conveyorBeltPowerMsg-request>))
  "Converts a ROS message object to a list"
  (cl:list 'conveyorBeltPowerMsg-request
    (cl:cons ':power (power msg))
))
;//! \htmlinclude conveyorBeltPowerMsg-response.msg.html

(cl:defclass <conveyorBeltPowerMsg-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass conveyorBeltPowerMsg-response (<conveyorBeltPowerMsg-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <conveyorBeltPowerMsg-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'conveyorBeltPowerMsg-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pkg_vb_sim-srv:<conveyorBeltPowerMsg-response> is deprecated: use pkg_vb_sim-srv:conveyorBeltPowerMsg-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <conveyorBeltPowerMsg-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg_vb_sim-srv:result-val is deprecated.  Use pkg_vb_sim-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <conveyorBeltPowerMsg-response>) ostream)
  "Serializes a message object of type '<conveyorBeltPowerMsg-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <conveyorBeltPowerMsg-response>) istream)
  "Deserializes a message object of type '<conveyorBeltPowerMsg-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<conveyorBeltPowerMsg-response>)))
  "Returns string type for a service object of type '<conveyorBeltPowerMsg-response>"
  "pkg_vb_sim/conveyorBeltPowerMsgResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'conveyorBeltPowerMsg-response)))
  "Returns string type for a service object of type 'conveyorBeltPowerMsg-response"
  "pkg_vb_sim/conveyorBeltPowerMsgResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<conveyorBeltPowerMsg-response>)))
  "Returns md5sum for a message object of type '<conveyorBeltPowerMsg-response>"
  "734278aaf6d621cbe98c5cbee4553347")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'conveyorBeltPowerMsg-response)))
  "Returns md5sum for a message object of type 'conveyorBeltPowerMsg-response"
  "734278aaf6d621cbe98c5cbee4553347")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<conveyorBeltPowerMsg-response>)))
  "Returns full string definition for message of type '<conveyorBeltPowerMsg-response>"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'conveyorBeltPowerMsg-response)))
  "Returns full string definition for message of type 'conveyorBeltPowerMsg-response"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <conveyorBeltPowerMsg-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <conveyorBeltPowerMsg-response>))
  "Converts a ROS message object to a list"
  (cl:list 'conveyorBeltPowerMsg-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'conveyorBeltPowerMsg)))
  'conveyorBeltPowerMsg-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'conveyorBeltPowerMsg)))
  'conveyorBeltPowerMsg-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'conveyorBeltPowerMsg)))
  "Returns string type for a service object of type '<conveyorBeltPowerMsg>"
  "pkg_vb_sim/conveyorBeltPowerMsg")