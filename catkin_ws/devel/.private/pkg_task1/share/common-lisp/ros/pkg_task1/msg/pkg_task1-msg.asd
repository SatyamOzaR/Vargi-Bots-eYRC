
(cl:in-package :asdf)

(defsystem "pkg_task1-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "msgTurtleAction" :depends-on ("_package_msgTurtleAction"))
    (:file "_package_msgTurtleAction" :depends-on ("_package"))
    (:file "msgTurtleActionFeedback" :depends-on ("_package_msgTurtleActionFeedback"))
    (:file "_package_msgTurtleActionFeedback" :depends-on ("_package"))
    (:file "msgTurtleActionGoal" :depends-on ("_package_msgTurtleActionGoal"))
    (:file "_package_msgTurtleActionGoal" :depends-on ("_package"))
    (:file "msgTurtleActionResult" :depends-on ("_package_msgTurtleActionResult"))
    (:file "_package_msgTurtleActionResult" :depends-on ("_package"))
    (:file "msgTurtleFeedback" :depends-on ("_package_msgTurtleFeedback"))
    (:file "_package_msgTurtleFeedback" :depends-on ("_package"))
    (:file "msgTurtleGoal" :depends-on ("_package_msgTurtleGoal"))
    (:file "_package_msgTurtleGoal" :depends-on ("_package"))
    (:file "msgTurtleResult" :depends-on ("_package_msgTurtleResult"))
    (:file "_package_msgTurtleResult" :depends-on ("_package"))
  ))