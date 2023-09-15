; Auto-generated. Do not edit!


(cl:in-package lidar_pkg-msg)


;//! \htmlinclude lavacon.msg.html

(cl:defclass <lavacon> (roslisp-msg-protocol:ros-message)
  ((con_mid_X
    :reader con_mid_X
    :initarg :con_mid_X
    :type cl:float
    :initform 0.0)
   (con_mid_y
    :reader con_mid_y
    :initarg :con_mid_y
    :type cl:float
    :initform 0.0)
   (con_mid_z
    :reader con_mid_z
    :initarg :con_mid_z
    :type cl:float
    :initform 0.0)
   (con_name
    :reader con_name
    :initarg :con_name
    :type cl:string
    :initform "")
   (con_color
    :reader con_color
    :initarg :con_color
    :type cl:string
    :initform ""))
)

(cl:defclass lavacon (<lavacon>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <lavacon>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'lavacon)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lidar_pkg-msg:<lavacon> is deprecated: use lidar_pkg-msg:lavacon instead.")))

(cl:ensure-generic-function 'con_mid_X-val :lambda-list '(m))
(cl:defmethod con_mid_X-val ((m <lavacon>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar_pkg-msg:con_mid_X-val is deprecated.  Use lidar_pkg-msg:con_mid_X instead.")
  (con_mid_X m))

(cl:ensure-generic-function 'con_mid_y-val :lambda-list '(m))
(cl:defmethod con_mid_y-val ((m <lavacon>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar_pkg-msg:con_mid_y-val is deprecated.  Use lidar_pkg-msg:con_mid_y instead.")
  (con_mid_y m))

(cl:ensure-generic-function 'con_mid_z-val :lambda-list '(m))
(cl:defmethod con_mid_z-val ((m <lavacon>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar_pkg-msg:con_mid_z-val is deprecated.  Use lidar_pkg-msg:con_mid_z instead.")
  (con_mid_z m))

(cl:ensure-generic-function 'con_name-val :lambda-list '(m))
(cl:defmethod con_name-val ((m <lavacon>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar_pkg-msg:con_name-val is deprecated.  Use lidar_pkg-msg:con_name instead.")
  (con_name m))

(cl:ensure-generic-function 'con_color-val :lambda-list '(m))
(cl:defmethod con_color-val ((m <lavacon>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar_pkg-msg:con_color-val is deprecated.  Use lidar_pkg-msg:con_color instead.")
  (con_color m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <lavacon>) ostream)
  "Serializes a message object of type '<lavacon>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'con_mid_X))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'con_mid_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'con_mid_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'con_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'con_name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'con_color))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'con_color))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <lavacon>) istream)
  "Deserializes a message object of type '<lavacon>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'con_mid_X) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'con_mid_y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'con_mid_z) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'con_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'con_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'con_color) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'con_color) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<lavacon>)))
  "Returns string type for a message object of type '<lavacon>"
  "lidar_pkg/lavacon")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'lavacon)))
  "Returns string type for a message object of type 'lavacon"
  "lidar_pkg/lavacon")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<lavacon>)))
  "Returns md5sum for a message object of type '<lavacon>"
  "d7d5d863398db1715dabc8c59e13dbfe")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'lavacon)))
  "Returns md5sum for a message object of type 'lavacon"
  "d7d5d863398db1715dabc8c59e13dbfe")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<lavacon>)))
  "Returns full string definition for message of type '<lavacon>"
  (cl:format cl:nil "float64 con_mid_X~%float64 con_mid_y~%float64 con_mid_z~%string con_name~%string con_color~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'lavacon)))
  "Returns full string definition for message of type 'lavacon"
  (cl:format cl:nil "float64 con_mid_X~%float64 con_mid_y~%float64 con_mid_z~%string con_name~%string con_color~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <lavacon>))
  (cl:+ 0
     8
     8
     8
     4 (cl:length (cl:slot-value msg 'con_name))
     4 (cl:length (cl:slot-value msg 'con_color))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <lavacon>))
  "Converts a ROS message object to a list"
  (cl:list 'lavacon
    (cl:cons ':con_mid_X (con_mid_X msg))
    (cl:cons ':con_mid_y (con_mid_y msg))
    (cl:cons ':con_mid_z (con_mid_z msg))
    (cl:cons ':con_name (con_name msg))
    (cl:cons ':con_color (con_color msg))
))
