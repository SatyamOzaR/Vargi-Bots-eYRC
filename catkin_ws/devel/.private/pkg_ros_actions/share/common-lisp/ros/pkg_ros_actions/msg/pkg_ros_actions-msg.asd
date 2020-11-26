
(cl:in-package :asdf)

(defsystem "pkg_ros_actions-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "myActionMsgAction" :depends-on ("_package_myActionMsgAction"))
    (:file "_package_myActionMsgAction" :depends-on ("_package"))
    (:file "myActionMsgActionFeedback" :depends-on ("_package_myActionMsgActionFeedback"))
    (:file "_package_myActionMsgActionFeedback" :depends-on ("_package"))
    (:file "myActionMsgActionGoal" :depends-on ("_package_myActionMsgActionGoal"))
    (:file "_package_myActionMsgActionGoal" :depends-on ("_package"))
    (:file "myActionMsgActionResult" :depends-on ("_package_myActionMsgActionResult"))
    (:file "_package_myActionMsgActionResult" :depends-on ("_package"))
    (:file "myActionMsgFeedback" :depends-on ("_package_myActionMsgFeedback"))
    (:file "_package_myActionMsgFeedback" :depends-on ("_package"))
    (:file "myActionMsgGoal" :depends-on ("_package_myActionMsgGoal"))
    (:file "_package_myActionMsgGoal" :depends-on ("_package"))
    (:file "myActionMsgResult" :depends-on ("_package_myActionMsgResult"))
    (:file "_package_myActionMsgResult" :depends-on ("_package"))
  ))