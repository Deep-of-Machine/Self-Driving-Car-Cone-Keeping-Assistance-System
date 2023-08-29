;; Auto-generated. Do not edit!


(when (boundp 'iahrs_driver::all_data_reset)
  (if (not (find-package "IAHRS_DRIVER"))
    (make-package "IAHRS_DRIVER"))
  (shadow 'all_data_reset (find-package "IAHRS_DRIVER")))
(unless (find-package "IAHRS_DRIVER::ALL_DATA_RESET")
  (make-package "IAHRS_DRIVER::ALL_DATA_RESET"))
(unless (find-package "IAHRS_DRIVER::ALL_DATA_RESETREQUEST")
  (make-package "IAHRS_DRIVER::ALL_DATA_RESETREQUEST"))
(unless (find-package "IAHRS_DRIVER::ALL_DATA_RESETRESPONSE")
  (make-package "IAHRS_DRIVER::ALL_DATA_RESETRESPONSE"))

(in-package "ROS")





(defclass iahrs_driver::all_data_resetRequest
  :super ros::object
  :slots ())

(defmethod iahrs_driver::all_data_resetRequest
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

(defclass iahrs_driver::all_data_resetResponse
  :super ros::object
  :slots (_command_Result ))

(defmethod iahrs_driver::all_data_resetResponse
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

(defclass iahrs_driver::all_data_reset
  :super ros::object
  :slots ())

(setf (get iahrs_driver::all_data_reset :md5sum-) "6b370111df6d9d8116fbdd43bd394a52")
(setf (get iahrs_driver::all_data_reset :datatype-) "iahrs_driver/all_data_reset")
(setf (get iahrs_driver::all_data_reset :request) iahrs_driver::all_data_resetRequest)
(setf (get iahrs_driver::all_data_reset :response) iahrs_driver::all_data_resetResponse)

(defmethod iahrs_driver::all_data_resetRequest
  (:response () (instance iahrs_driver::all_data_resetResponse :init)))

(setf (get iahrs_driver::all_data_resetRequest :md5sum-) "6b370111df6d9d8116fbdd43bd394a52")
(setf (get iahrs_driver::all_data_resetRequest :datatype-) "iahrs_driver/all_data_resetRequest")
(setf (get iahrs_driver::all_data_resetRequest :definition-)
      "#This message is used to send command to IAHRS(IMU)
#All Data Reset command

---
bool command_Result

")

(setf (get iahrs_driver::all_data_resetResponse :md5sum-) "6b370111df6d9d8116fbdd43bd394a52")
(setf (get iahrs_driver::all_data_resetResponse :datatype-) "iahrs_driver/all_data_resetResponse")
(setf (get iahrs_driver::all_data_resetResponse :definition-)
      "#This message is used to send command to IAHRS(IMU)
#All Data Reset command

---
bool command_Result

")



(provide :iahrs_driver/all_data_reset "6b370111df6d9d8116fbdd43bd394a52")


