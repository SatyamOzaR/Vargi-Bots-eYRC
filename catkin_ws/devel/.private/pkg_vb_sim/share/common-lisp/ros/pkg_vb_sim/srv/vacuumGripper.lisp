; Auto-generated. Do not edit!


(cl:in-package pkg_vb_sim-srv)


;//! \htmlinclude vacuumGripper-request.msg.html

(cl:defclass <vacuumGripper-request> (roslisp-msg-protocol:ros-message)
  ((activate_vacuum_gripper
    :reader activate_vacuum_gripper
    :initarg :activate_vacuum_gripper
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass vacuumGripper-request (<vacuumGripper-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <vacuumGripper-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'vacuumGripper-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pkg_vb_sim-srv:<vacuumGripper-request> is deprecated: use pkg_vb_sim-srv:vacuumGripper-request instead.")))

(cl:ensure-generic-function 'activate_vacuum_gripper-val :lambda-list '(m))
(cl:defmethod activate_vacuum_gripper-val ((m <vacuumGripper-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg_vb_sim-srv:activate_vacuum_gripper-val is deprecated.  Use pkg_vb_sim-srv:activate_vacuum_gripper instead.")
  (activate_vacuum_gripper m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <vacuumGripper-request>) ostream)
  "Serializes a message object of type '<vacuumGripper-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'activate_vacuum_gripper) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <vacuumGripper-request>) istream)
  "Deserializes a message object of type '<vacuumGripper-request>"
    (cl:setf (cl:slot-value msg 'activate_vacuum_gripper) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<vacuumGripper-request>)))
  "Returns string type for a service object of type '<vacuumGripper-request>"
  "pkg_vb_sim/vacuumGripperRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'vacuumGripper-request)))
  "Returns string type for a service object of type 'vacuumGripper-request"
  "pkg_vb_sim/vacuumGripperRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<vacuumGripper-request>)))
  "Returns md5sum for a message object of type '<vacuumGripper-request>"
  "22dce99b1d1e31fc9ba6b2faee126298")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'vacuumGripper-request)))
  "Returns md5sum for a message object of type 'vacuumGripper-request"
  "22dce99b1d1e31fc9ba6b2faee126298")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<vacuumGripper-request>)))
  "Returns full string definition for message of type '<vacuumGripper-request>"
  (cl:format cl:nil "bool activate_vacuum_gripper~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'vacuumGripper-request)))
  "Returns full string definition for message of type 'vacuumGripper-request"
  (cl:format cl:nil "bool activate_vacuum_gripper~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <vacuumGripper-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <vacuumGripper-request>))
  "Converts a ROS message object to a list"
  (cl:list 'vacuumGripper-request
    (cl:cons ':activate_vacuum_gripper (activate_vacuum_gripper msg))
))
;//! \htmlinclude vacuumGripper-response.msg.html

(cl:defclass <vacuumGripper-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass vacuumGripper-response (<vacuumGripper-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <vacuumGripper-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'vacuumGripper-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pkg_vb_sim-srv:<vacuumGripper-response> is deprecated: use pkg_vb_sim-srv:vacuumGripper-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <vacuumGripper-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg_vb_sim-srv:result-val is deprecated.  Use pkg_vb_sim-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <vacuumGripper-response>) ostream)
  "Serializes a message object of type '<vacuumGripper-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <vacuumGripper-response>) istream)
  "Deserializes a message object of type '<vacuumGripper-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<vacuumGripper-response>)))
  "Returns string type for a service object of type '<vacuumGripper-response>"
  "pkg_vb_sim/vacuumGripperResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'vacuumGripper-response)))
  "Returns string type for a service object of type 'vacuumGripper-response"
  "pkg_vb_sim/vacuumGripperResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<vacuumGripper-response>)))
  "Returns md5sum for a message object of type '<vacuumGripper-response>"
  "22dce99b1d1e31fc9ba6b2faee126298")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'vacuumGripper-response)))
  "Returns md5sum for a message object of type 'vacuumGripper-response"
  "22dce99b1d1e31fc9ba6b2faee126298")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<vacuumGripper-response>)))
  "Returns full string definition for message of type '<vacuumGripper-response>"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'vacuumGripper-response)))
  "Returns full string definition for message of type 'vacuumGripper-response"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <vacuumGripper-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <vacuumGripper-response>))
  "Converts a ROS message object to a list"
  (cl:list 'vacuumGripper-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'vacuumGripper)))
  'vacuumGripper-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'vacuumGripper)))
  'vacuumGripper-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'vacuumGripper)))
  "Returns string type for a service object of type '<vacuumGripper>"
  "pkg_vb_sim/vacuumGripper")