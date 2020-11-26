; Auto-generated. Do not edit!


(cl:in-package pkg_iot_ros_bridge-msg)


;//! \htmlinclude msgMqttSub.msg.html

(cl:defclass <msgMqttSub> (roslisp-msg-protocol:ros-message)
  ((timestamp
    :reader timestamp
    :initarg :timestamp
    :type cl:real
    :initform 0)
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

(cl:defclass msgMqttSub (<msgMqttSub>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <msgMqttSub>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'msgMqttSub)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pkg_iot_ros_bridge-msg:<msgMqttSub> is deprecated: use pkg_iot_ros_bridge-msg:msgMqttSub instead.")))

(cl:ensure-generic-function 'timestamp-val :lambda-list '(m))
(cl:defmethod timestamp-val ((m <msgMqttSub>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg_iot_ros_bridge-msg:timestamp-val is deprecated.  Use pkg_iot_ros_bridge-msg:timestamp instead.")
  (timestamp m))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <msgMqttSub>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg_iot_ros_bridge-msg:topic-val is deprecated.  Use pkg_iot_ros_bridge-msg:topic instead.")
  (topic m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <msgMqttSub>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pkg_iot_ros_bridge-msg:message-val is deprecated.  Use pkg_iot_ros_bridge-msg:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <msgMqttSub>) ostream)
  "Serializes a message object of type '<msgMqttSub>"
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'timestamp)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'timestamp) (cl:floor (cl:slot-value msg 'timestamp)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <msgMqttSub>) istream)
  "Deserializes a message object of type '<msgMqttSub>"
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'timestamp) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<msgMqttSub>)))
  "Returns string type for a message object of type '<msgMqttSub>"
  "pkg_iot_ros_bridge/msgMqttSub")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'msgMqttSub)))
  "Returns string type for a message object of type 'msgMqttSub"
  "pkg_iot_ros_bridge/msgMqttSub")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<msgMqttSub>)))
  "Returns md5sum for a message object of type '<msgMqttSub>"
  "76824121accacb087a76246dc01cbb0b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'msgMqttSub)))
  "Returns md5sum for a message object of type 'msgMqttSub"
  "76824121accacb087a76246dc01cbb0b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<msgMqttSub>)))
  "Returns full string definition for message of type '<msgMqttSub>"
  (cl:format cl:nil "time timestamp~%string topic~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'msgMqttSub)))
  "Returns full string definition for message of type 'msgMqttSub"
  (cl:format cl:nil "time timestamp~%string topic~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <msgMqttSub>))
  (cl:+ 0
     8
     4 (cl:length (cl:slot-value msg 'topic))
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <msgMqttSub>))
  "Converts a ROS message object to a list"
  (cl:list 'msgMqttSub
    (cl:cons ':timestamp (timestamp msg))
    (cl:cons ':topic (topic msg))
    (cl:cons ':message (message msg))
))
