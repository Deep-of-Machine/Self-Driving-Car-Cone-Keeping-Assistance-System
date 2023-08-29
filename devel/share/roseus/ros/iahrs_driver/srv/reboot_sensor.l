;; Auto-generated. Do not edit!


(when (boundp 'iahrs_driver::reboot_sensor)
  (if (not (find-package "IAHRS_DRIVER"))
    (make-package "IAHRS_DRIVER"))
  (shadow 'reboot_sensor (find-package "IAHRS_DRIVER")))
(unless (find-package "IAHRS_DRIVER::REBOOT_SENSOR")
  (make-package "IAHRS_DRIVER::REBOOT_SENSOR"))
(unless (find-package "IAHRS_DRIVER::REBOOT_SENSORREQUEST")
  (make-package "IAHRS_DRIVER::REBOOT_SENSORREQUEST"))
(unless (find-package "IAHRS_DRIVER::REBOOT_SENSORRESPONSE")
  (make-package "IAHRS_DRIVER::REBOOT_SENSORRESPONSE"))

(in-package "ROS")





(defclass iahrs_driver::reboot_sensorRequest
  :super ros::object
  :slots ())

(defmethod iahrs_driver::reboot_sensorRequest
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

(defclass iahrs_driver::reboot_sensorResponse
  :super ros::object
  :slots (_command_Result ))

(defmethod iahrs_driver::reboot_sensorResponse
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

(defclass iahrs_driver::reboot_sensor
  :super ros::object
  :slots ())

(setf (get iahrs_driver::reboot_sensor :md5sum-) "6b370111df6d9d8116fbdd43bd394a52")
(setf (get iahrs_driver::reboot_sensor :datatype-) "iahrs_driver/reboot_sensor")
(setf (get iahrs_driver::reboot_sensor :request) iahrs_driver::reboot_sensorRequest)
(setf (get iahrs_driver::reboot_sensor :response) iahrs_driver::reboot_sensorResponse)

(defmethod iahrs_driver::reboot_sensorRequest
  (:response () (instance iahrs_driver::reboot_sensorResponse :init)))

(setf (get iahrs_driver::reboot_sensorRequest :md5sum-) "6b370111df6d9d8116fbdd43bd394a52")
(setf (get iahrs_driver::reboot_sensorRequest :datatype-) "iahrs_driver/reboot_sensorRequest")
(setf (get iahrs_driver::reboot_sensorRequest :definition-)
      "#This message is used to send command to IAHRS(IMU)
#Reboot Sensor command

---
bool command_Result

")

(setf (get iahrs_driver::reboot_sensorResponse :md5sum-) "6b370111df6d9d8116fbdd43bd394a52")
(setf (get iahrs_driver::reboot_sensorResponse :datatype-) "iahrs_driver/reboot_sensorResponse")
(setf (get iahrs_driver::reboot_sensorResponse :definition-)
      "#This message is used to send command to IAHRS(IMU)
#Reboot Sensor command

---
bool command_Result

")



(provide :iahrs_driver/reboot_sensor "6b370111df6d9d8116fbdd43bd394a52")


