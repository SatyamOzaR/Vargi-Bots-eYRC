;; Auto-generated. Do not edit!


(when (boundp 'pkg_vb_sim::conveyorBeltPowerMsg)
  (if (not (find-package "PKG_VB_SIM"))
    (make-package "PKG_VB_SIM"))
  (shadow 'conveyorBeltPowerMsg (find-package "PKG_VB_SIM")))
(unless (find-package "PKG_VB_SIM::CONVEYORBELTPOWERMSG")
  (make-package "PKG_VB_SIM::CONVEYORBELTPOWERMSG"))
(unless (find-package "PKG_VB_SIM::CONVEYORBELTPOWERMSGREQUEST")
  (make-package "PKG_VB_SIM::CONVEYORBELTPOWERMSGREQUEST"))
(unless (find-package "PKG_VB_SIM::CONVEYORBELTPOWERMSGRESPONSE")
  (make-package "PKG_VB_SIM::CONVEYORBELTPOWERMSGRESPONSE"))

(in-package "ROS")





(defclass pkg_vb_sim::conveyorBeltPowerMsgRequest
  :super ros::object
  :slots (_power ))

(defmethod pkg_vb_sim::conveyorBeltPowerMsgRequest
  (:init
   (&key
    ((:power __power) 0)
    )
   (send-super :init)
   (setq _power (round __power))
   self)
  (:power
   (&optional __power)
   (if __power (setq _power __power)) _power)
  (:serialization-length
   ()
   (+
    ;; int8 _power
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _power
       (write-byte _power s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _power
     (setq _power (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _power 127) (setq _power (- _power 256)))
   ;;
   self)
  )

(defclass pkg_vb_sim::conveyorBeltPowerMsgResponse
  :super ros::object
  :slots (_result ))

(defmethod pkg_vb_sim::conveyorBeltPowerMsgResponse
  (:init
   (&key
    ((:result __result) nil)
    )
   (send-super :init)
   (setq _result __result)
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass pkg_vb_sim::conveyorBeltPowerMsg
  :super ros::object
  :slots ())

(setf (get pkg_vb_sim::conveyorBeltPowerMsg :md5sum-) "734278aaf6d621cbe98c5cbee4553347")
(setf (get pkg_vb_sim::conveyorBeltPowerMsg :datatype-) "pkg_vb_sim/conveyorBeltPowerMsg")
(setf (get pkg_vb_sim::conveyorBeltPowerMsg :request) pkg_vb_sim::conveyorBeltPowerMsgRequest)
(setf (get pkg_vb_sim::conveyorBeltPowerMsg :response) pkg_vb_sim::conveyorBeltPowerMsgResponse)

(defmethod pkg_vb_sim::conveyorBeltPowerMsgRequest
  (:response () (instance pkg_vb_sim::conveyorBeltPowerMsgResponse :init)))

(setf (get pkg_vb_sim::conveyorBeltPowerMsgRequest :md5sum-) "734278aaf6d621cbe98c5cbee4553347")
(setf (get pkg_vb_sim::conveyorBeltPowerMsgRequest :datatype-) "pkg_vb_sim/conveyorBeltPowerMsgRequest")
(setf (get pkg_vb_sim::conveyorBeltPowerMsgRequest :definition-)
      "int8 power
---
bool result
")

(setf (get pkg_vb_sim::conveyorBeltPowerMsgResponse :md5sum-) "734278aaf6d621cbe98c5cbee4553347")
(setf (get pkg_vb_sim::conveyorBeltPowerMsgResponse :datatype-) "pkg_vb_sim/conveyorBeltPowerMsgResponse")
(setf (get pkg_vb_sim::conveyorBeltPowerMsgResponse :definition-)
      "int8 power
---
bool result
")



(provide :pkg_vb_sim/conveyorBeltPowerMsg "734278aaf6d621cbe98c5cbee4553347")


