;; Auto-generated. Do not edit!


(when (boundp 'iahrs_driver::euler_angle_init)
  (if (not (find-package "IAHRS_DRIVER"))
    (make-package "IAHRS_DRIVER"))
  (shadow 'euler_angle_init (find-package "IAHRS_DRIVER")))
(unless (find-package "IAHRS_DRIVER::EULER_ANGLE_INIT")
  (make-package "IAHRS_DRIVER::EULER_ANGLE_INIT"))
(unless (find-package "IAHRS_DRIVER::EULER_ANGLE_INITREQUEST")
  (make-package "IAHRS_DRIVER::EULER_ANGLE_INITREQUEST"))
(unless (find-package "IAHRS_DRIVER::EULER_ANGLE_INITRESPONSE")
  (make-package "IAHRS_DRIVER::EULER_ANGLE_INITRESPONSE"))

(in-package "ROS")





(defclass iahrs_driver::euler_angle_initRequest
  :super ros::object
  :slots ())

(defmethod iahrs_driver::euler_angle_initRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass iahrs_driver::euler_angle_initResponse
  :super ros::object
  :slots (_command_Result ))

(defmethod iahrs_driver::euler_angle_initResponse
  (:init
   (&key
    ((:command_Result __command_Result) nil)
    )
   (send-super :init)
   (setq _command_Result __command_Result)
   self)
  (:command_Result
   (&optional (__command_Result :null))
   (if (not (eq __command_Result :null)) (setq _command_Result __command_Result)) _command_Result)
  (:serialization-length
   ()
   (+
    ;; bool _command_Result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _command_Result
       (if _command_Result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _command_Result
     (setq _command_Result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass iahrs_driver::euler_angle_init
  :super ros::object
  :slots ())

(setf (get iahrs_driver::euler_angle_init :md5sum-) "6b370111df6d9d8116fbdd43bd394a52")
(setf (get iahrs_driver::euler_angle_init :datatype-) "iahrs_driver/euler_angle_init")
(setf (get iahrs_driver::euler_angle_init :request) iahrs_driver::euler_angle_initRequest)
(setf (get iahrs_driver::euler_angle_init :response) iahrs_driver::euler_angle_initResponse)

(defmethod iahrs_driver::euler_angle_initRequest
  (:response () (instance iahrs_driver::euler_angle_initResponse :init)))

(setf (get iahrs_driver::euler_angle_initRequest :md5sum-) "6b370111df6d9d8116fbdd43bd394a52")
(setf (get iahrs_driver::euler_angle_initRequest :datatype-) "iahrs_driver/euler_angle_initRequest")
(setf (get iahrs_driver::euler_angle_initRequest :definition-)
      "#This message is used to send command to IAHRS(IMU)
#Euler_angle_init command

---
bool command_Result

")

(setf (get iahrs_driver::euler_angle_initResponse :md5sum-) "6b370111df6d9d8116fbdd43bd394a52")
(setf (get iahrs_driver::euler_angle_initResponse :datatype-) "iahrs_driver/euler_angle_initResponse")
(setf (get iahrs_driver::euler_angle_initResponse :definition-)
      "#This message is used to send command to IAHRS(IMU)
#Euler_angle_init command

---
bool command_Result

")



(provide :iahrs_driver/euler_angle_init "6b370111df6d9d8116fbdd43bd394a52")


