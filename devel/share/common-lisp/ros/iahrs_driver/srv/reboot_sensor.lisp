; Auto-generated. Do not edit!


(cl:in-package iahrs_driver-srv)


;//! \htmlinclude reboot_sensor-request.msg.html

(cl:defclass <reboot_sensor-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass reboot_sensor-request (<reboot_sensor-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <reboot_sensor-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'reboot_sensor-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iahrs_driver-srv:<reboot_sensor-request> is deprecated: use iahrs_driver-srv:reboot_sensor-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <reboot_sensor-request>) ostream)
  "Serializes a message object of type '<reboot_sensor-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <reboot_sensor-request>) istream)
  "Deserializes a message object of type '<reboot_sensor-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<reboot_sensor-request>)))
  "Returns string type for a service object of type '<reboot_sensor-request>"
  "iahrs_driver/reboot_sensorRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'reboot_sensor-request)))
  "Returns string type for a service object of type 'reboot_sensor-request"
  "iahrs_driver/reboot_sensorRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<reboot_sensor-request>)))
  "Returns md5sum for a message object of type '<reboot_sensor-request>"
  "6b370111df6d9d8116fbdd43bd394a52")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'reboot_sensor-request)))
  "Returns md5sum for a message object of type 'reboot_sensor-request"
  "6b370111df6d9d8116fbdd43bd394a52")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<reboot_sensor-request>)))
  "Returns full string definition for message of type '<reboot_sensor-request>"
  (cl:format cl:nil "#This message is used to send command to IAHRS(IMU)~%#Reboot Sensor command~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'reboot_sensor-request)))
  "Returns full string definition for message of type 'reboot_sensor-request"
  (cl:format cl:nil "#This message is used to send command to IAHRS(IMU)~%#Reboot Sensor command~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <reboot_sensor-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <reboot_sensor-request>))
  "Converts a ROS message object to a list"
  (cl:list 'reboot_sensor-request
))
;//! \htmlinclude reboot_sensor-response.msg.html

(cl:defclass <reboot_sensor-response> (roslisp-msg-protocol:ros-message)
  ((command_Result
    :reader command_Result
    :initarg :command_Result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass reboot_sensor-response (<reboot_sensor-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <reboot_sensor-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'reboot_sensor-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iahrs_driver-srv:<reboot_sensor-response> is deprecated: use iahrs_driver-srv:reboot_sensor-response instead.")))

(cl:ensure-generic-function 'command_Result-val :lambda-list '(m))
(cl:defmethod command_Result-val ((m <reboot_sensor-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iahrs_driver-srv:command_Result-val is deprecated.  Use iahrs_driver-srv:command_Result instead.")
  (command_Result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <reboot_sensor-response>) ostream)
  "Serializes a message object of type '<reboot_sensor-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'command_Result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <reboot_sensor-response>) istream)
  "Deserializes a message object of type '<reboot_sensor-response>"
    (cl:setf (cl:slot-value msg 'command_Result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<reboot_sensor-response>)))
  "Returns string type for a service object of type '<reboot_sensor-response>"
  "iahrs_driver/reboot_sensorResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'reboot_sensor-response)))
  "Returns string type for a service object of type 'reboot_sensor-response"
  "iahrs_driver/reboot_sensorResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<reboot_sensor-response>)))
  "Returns md5sum for a message object of type '<reboot_sensor-response>"
  "6b370111df6d9d8116fbdd43bd394a52")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'reboot_sensor-response)))
  "Returns md5sum for a message object of type 'reboot_sensor-response"
  "6b370111df6d9d8116fbdd43bd394a52")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<reboot_sensor-response>)))
  "Returns full string definition for message of type '<reboot_sensor-response>"
  (cl:format cl:nil "bool command_Result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'reboot_sensor-response)))
  "Returns full string definition for message of type 'reboot_sensor-response"
  (cl:format cl:nil "bool command_Result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <reboot_sensor-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <reboot_sensor-response>))
  "Converts a ROS message object to a list"
  (cl:list 'reboot_sensor-response
    (cl:cons ':command_Result (command_Result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'reboot_sensor)))
  'reboot_sensor-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'reboot_sensor)))
  'reboot_sensor-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'reboot_sensor)))
  "Returns string type for a service object of type '<reboot_sensor>"
  "iahrs_driver/reboot_sensor")