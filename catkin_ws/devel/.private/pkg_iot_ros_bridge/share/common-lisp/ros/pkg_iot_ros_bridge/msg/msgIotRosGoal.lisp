; Auto-generated. Do not edit!


(cl:in-package pkg_iot_ros_bridge-msg)


;//! \htmlinclude msgIotRosGoal.msg.html

(cl:defclass <msgIotRosGoal> (roslisp-msg-protocol:ros-message)
  ((protocol
    :reader protocol
    :initarg :protocol
    :type cl:string
    :initform "")
   (mode
    :reader mode
    :initarg :mode
    :type cl:string
    :initform "")
   (topic
    :reader topic
    :initarg :topic
    :type cl:string
    :initform "")
   (message
    :reader message
    :initarg :message
    :type cl:string
    :initform ""))
)

(cl:defclass msgIotRosGoal (<msgIotRosGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <msgIotRosGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'msgIotRosGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pkg_iot_ros_bridge-msg:<msgIotRosGoal> is deprecated: use pkg_iot_ros_bridge-msg:msgIotRosGoal instead.")))

(cl:ensure-generic-function 'protocol-val :lambda-list '(m))
(cl:defmethod protocol-val ((m <msgIotRosGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg_iot_ros_bridge-msg:protocol-val is deprecated.  Use pkg_iot_ros_bridge-msg:protocol instead.")
  (protocol m))

(cl:ensure-generic-function 'mode-val :lambda-list '(m))
(cl:defmethod mode-val ((m <msgIotRosGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg_iot_ros_bridge-msg:mode-val is deprecated.  Use pkg_iot_ros_bridge-msg:mode instead.")
  (mode m))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <msgIotRosGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg_iot_ros_bridge-msg:topic-val is deprecated.  Use pkg_iot_ros_bridge-msg:topic instead.")
  (topic m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <msgIotRosGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg_iot_ros_bridge-msg:message-val is deprecated.  Use pkg_iot_ros_bridge-msg:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <msgIotRosGoal>) ostream)
  "Serializes a message object of type '<msgIotRosGoal>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'protocol))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'protocol))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'mode))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'mode))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'topic))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'topic))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <msgIotRosGoal>) istream)
  "Deserializes a message object of type '<msgIotRosGoal>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'protocol) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'protocol) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'mode) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'mode) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'topic) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'topic) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<msgIotRosGoal>)))
  "Returns string type for a message object of type '<msgIotRosGoal>"
  "pkg_iot_ros_bridge/msgIotRosGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'msgIotRosGoal)))
  "Returns string type for a message object of type 'msgIotRosGoal"
  "pkg_iot_ros_bridge/msgIotRosGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<msgIotRosGoal>)))
  "Returns md5sum for a message object of type '<msgIotRosGoal>"
  "e9cbc8cd1a46fb612c6675b9cee83b82")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'msgIotRosGoal)))
  "Returns md5sum for a message object of type 'msgIotRosGoal"
  "e9cbc8cd1a46fb612c6675b9cee83b82")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<msgIotRosGoal>)))
  "Returns full string definition for message of type '<msgIotRosGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# goal~%string protocol~%string mode~%string topic~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'msgIotRosGoal)))
  "Returns full string definition for message of type 'msgIotRosGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# goal~%string protocol~%string mode~%string topic~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <msgIotRosGoal>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'protocol))
     4 (cl:length (cl:slot-value msg 'mode))
     4 (cl:length (cl:slot-value msg 'topic))
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <msgIotRosGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'msgIotRosGoal
    (cl:cons ':protocol (protocol msg))
    (cl:cons ':mode (mode msg))
    (cl:cons ':topic (topic msg))
    (cl:cons ':message (message msg))
))
