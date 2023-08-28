; Auto-generated. Do not edit!


(cl:in-package iahrs_driver-srv)


;//! \htmlinclude euler_angle_init-request.msg.html

(cl:defclass <euler_angle_init-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass euler_angle_init-request (<euler_angle_init-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <euler_angle_init-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'euler_angle_init-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iahrs_driver-srv:<euler_angle_init-request> is deprecated: use iahrs_driver-srv:euler_angle_init-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <euler_angle_init-request>) ostream)
  "Serializes a message object of type '<euler_angle_init-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <euler_angle_init-request>) istream)
  "Deserializes a message object of type '<euler_angle_init-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<euler_angle_init-request>)))
  "Returns string type for a service object of type '<euler_angle_init-request>"
  "iahrs_driver/euler_angle_initRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'euler_angle_init-request)))
  "Returns string type for a service object of type 'euler_angle_init-request"
  "iahrs_driver/euler_angle_initRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<euler_angle_init-request>)))
  "Returns md5sum for a message object of type '<euler_angle_init-request>"
  "6b370111df6d9d8116fbdd43bd394a52")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'euler_angle_init-request)))
  "Returns md5sum for a message object of type 'euler_angle_init-request"
  "6b370111df6d9d8116fbdd43bd394a52")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<euler_angle_init-request>)))
  "Returns full string definition for message of type '<euler_angle_init-request>"
  (cl:format cl:nil "#This message is used to send command to IAHRS(IMU)~%#Euler_angle_init command~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'euler_angle_init-request)))
  "Returns full string definition for message of type 'euler_angle_init-request"
  (cl:format cl:nil "#This message is used to send command to IAHRS(IMU)~%#Euler_angle_init command~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <euler_angle_init-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <euler_angle_init-request>))
  "Converts a ROS message object to a list"
  (cl:list 'euler_angle_init-request
))
;//! \htmlinclude euler_angle_init-response.msg.html

(cl:defclass <euler_angle_init-response> (roslisp-msg-protocol:ros-message)
  ((command_Result
    :reader command_Result
    :initarg :command_Result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass euler_angle_init-response (<euler_angle_init-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <euler_angle_init-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'euler_angle_init-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iahrs_driver-srv:<euler_angle_init-response> is deprecated: use iahrs_driver-srv:euler_angle_init-response instead.")))

(cl:ensure-generic-function 'command_Result-val :lambda-list '(m))
(cl:defmethod command_Result-val ((m <euler_angle_init-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iahrs_driver-srv:command_Result-val is deprecated.  Use iahrs_driver-srv:command_Result instead.")
  (command_Result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <euler_angle_init-response>) ostream)
  "Serializes a message object of type '<euler_angle_init-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'command_Result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <euler_angle_init-response>) istream)
  "Deserializes a message object of type '<euler_angle_init-response>"
    (cl:setf (cl:slot-value msg 'command_Result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<euler_angle_init-response>)))
  "Returns string type for a service object of type '<euler_angle_init-response>"
  "iahrs_driver/euler_angle_initResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'euler_angle_init-response)))
  "Returns string type for a service object of type 'euler_angle_init-response"
  "iahrs_driver/euler_angle_initResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<euler_angle_init-response>)))
  "Returns md5sum for a message object of type '<euler_angle_init-response>"
  "6b370111df6d9d8116fbdd43bd394a52")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'euler_angle_init-response)))
  "Returns md5sum for a message object of type 'euler_angle_init-response"
  "6b370111df6d9d8116fbdd43bd394a52")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<euler_angle_init-response>)))
  "Returns full string definition for message of type '<euler_angle_init-response>"
  (cl:format cl:nil "bool command_Result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'euler_angle_init-response)))
  "Returns full string definition for message of type 'euler_angle_init-response"
  (cl:format cl:nil "bool command_Result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <euler_angle_init-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <euler_angle_init-response>))
  "Converts a ROS message object to a list"
  (cl:list 'euler_angle_init-response
    (cl:cons ':command_Result (command_Result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'euler_angle_init)))
  'euler_angle_init-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'euler_angle_init)))
  'euler_angle_init-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'euler_angle_init)))
  "Returns string type for a service object of type '<euler_angle_init>"
  "iahrs_driver/euler_angle_init")