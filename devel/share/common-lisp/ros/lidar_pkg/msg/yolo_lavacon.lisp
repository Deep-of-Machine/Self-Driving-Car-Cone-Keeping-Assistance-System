; Auto-generated. Do not edit!


(cl:in-package lidar_pkg-msg)


;//! \htmlinclude yolo_lavacon.msg.html

(cl:defclass <yolo_lavacon> (roslisp-msg-protocol:ros-message)
  ((yolo_mid_X
    :reader yolo_mid_X
    :initarg :yolo_mid_X
    :type cl:float
    :initform 0.0)
   (yolo_mid_y
    :reader yolo_mid_y
    :initarg :yolo_mid_y
    :type cl:float
    :initform 0.0)
   (yolo_con_name
    :reader yolo_con_name
    :initarg :yolo_con_name
    :type cl:string
    :initform "")
   (yolo_con_color
    :reader yolo_con_color
    :initarg :yolo_con_color
    :type cl:string
    :initform ""))
)

(cl:defclass yolo_lavacon (<yolo_lavacon>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <yolo_lavacon>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'yolo_lavacon)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lidar_pkg-msg:<yolo_lavacon> is deprecated: use lidar_pkg-msg:yolo_lavacon instead.")))

(cl:ensure-generic-function 'yolo_mid_X-val :lambda-list '(m))
(cl:defmethod yolo_mid_X-val ((m <yolo_lavacon>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar_pkg-msg:yolo_mid_X-val is deprecated.  Use lidar_pkg-msg:yolo_mid_X instead.")
  (yolo_mid_X m))

(cl:ensure-generic-function 'yolo_mid_y-val :lambda-list '(m))
(cl:defmethod yolo_mid_y-val ((m <yolo_lavacon>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar_pkg-msg:yolo_mid_y-val is deprecated.  Use lidar_pkg-msg:yolo_mid_y instead.")
  (yolo_mid_y m))

(cl:ensure-generic-function 'yolo_con_name-val :lambda-list '(m))
(cl:defmethod yolo_con_name-val ((m <yolo_lavacon>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar_pkg-msg:yolo_con_name-val is deprecated.  Use lidar_pkg-msg:yolo_con_name instead.")
  (yolo_con_name m))

(cl:ensure-generic-function 'yolo_con_color-val :lambda-list '(m))
(cl:defmethod yolo_con_color-val ((m <yolo_lavacon>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar_pkg-msg:yolo_con_color-val is deprecated.  Use lidar_pkg-msg:yolo_con_color instead.")
  (yolo_con_color m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <yolo_lavacon>) ostream)
  "Serializes a message object of type '<yolo_lavacon>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'yolo_mid_X))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'yolo_mid_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'yolo_con_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'yolo_con_name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'yolo_con_color))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'yolo_con_color))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <yolo_lavacon>) istream)
  "Deserializes a message object of type '<yolo_lavacon>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'yolo_mid_X) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'yolo_mid_y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'yolo_con_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'yolo_con_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'yolo_con_color) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'yolo_con_color) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<yolo_lavacon>)))
  "Returns string type for a message object of type '<yolo_lavacon>"
  "lidar_pkg/yolo_lavacon")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'yolo_lavacon)))
  "Returns string type for a message object of type 'yolo_lavacon"
  "lidar_pkg/yolo_lavacon")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<yolo_lavacon>)))
  "Returns md5sum for a message object of type '<yolo_lavacon>"
  "da269e966072bed82c14a04982ff80e5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'yolo_lavacon)))
  "Returns md5sum for a message object of type 'yolo_lavacon"
  "da269e966072bed82c14a04982ff80e5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<yolo_lavacon>)))
  "Returns full string definition for message of type '<yolo_lavacon>"
  (cl:format cl:nil "float64 yolo_mid_X~%float64 yolo_mid_y~%string yolo_con_name~%string yolo_con_color~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'yolo_lavacon)))
  "Returns full string definition for message of type 'yolo_lavacon"
  (cl:format cl:nil "float64 yolo_mid_X~%float64 yolo_mid_y~%string yolo_con_name~%string yolo_con_color~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <yolo_lavacon>))
  (cl:+ 0
     8
     8
     4 (cl:length (cl:slot-value msg 'yolo_con_name))
     4 (cl:length (cl:slot-value msg 'yolo_con_color))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <yolo_lavacon>))
  "Converts a ROS message object to a list"
  (cl:list 'yolo_lavacon
    (cl:cons ':yolo_mid_X (yolo_mid_X msg))
    (cl:cons ':yolo_mid_y (yolo_mid_y msg))
    (cl:cons ':yolo_con_name (yolo_con_name msg))
    (cl:cons ':yolo_con_color (yolo_con_color msg))
))
