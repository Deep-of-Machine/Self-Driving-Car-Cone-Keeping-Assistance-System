; Auto-generated. Do not edit!


(cl:in-package lidar_pkg-msg)


;//! \htmlinclude lidar_lavacon.msg.html

(cl:defclass <lidar_lavacon> (roslisp-msg-protocol:ros-message)
  ((lidar_mid_X
    :reader lidar_mid_X
    :initarg :lidar_mid_X
    :type cl:float
    :initform 0.0)
   (lidar_mid_y
    :reader lidar_mid_y
    :initarg :lidar_mid_y
    :type cl:float
    :initform 0.0)
   (lidar_mid_z
    :reader lidar_mid_z
    :initarg :lidar_mid_z
    :type cl:float
    :initform 0.0)
   (lidar_con_name
    :reader lidar_con_name
    :initarg :lidar_con_name
    :type cl:string
    :initform "")
   (lidar_con_color
    :reader lidar_con_color
    :initarg :lidar_con_color
    :type cl:string
    :initform ""))
)

(cl:defclass lidar_lavacon (<lidar_lavacon>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <lidar_lavacon>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'lidar_lavacon)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lidar_pkg-msg:<lidar_lavacon> is deprecated: use lidar_pkg-msg:lidar_lavacon instead.")))

(cl:ensure-generic-function 'lidar_mid_X-val :lambda-list '(m))
(cl:defmethod lidar_mid_X-val ((m <lidar_lavacon>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar_pkg-msg:lidar_mid_X-val is deprecated.  Use lidar_pkg-msg:lidar_mid_X instead.")
  (lidar_mid_X m))

(cl:ensure-generic-function 'lidar_mid_y-val :lambda-list '(m))
(cl:defmethod lidar_mid_y-val ((m <lidar_lavacon>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar_pkg-msg:lidar_mid_y-val is deprecated.  Use lidar_pkg-msg:lidar_mid_y instead.")
  (lidar_mid_y m))

(cl:ensure-generic-function 'lidar_mid_z-val :lambda-list '(m))
(cl:defmethod lidar_mid_z-val ((m <lidar_lavacon>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar_pkg-msg:lidar_mid_z-val is deprecated.  Use lidar_pkg-msg:lidar_mid_z instead.")
  (lidar_mid_z m))

(cl:ensure-generic-function 'lidar_con_name-val :lambda-list '(m))
(cl:defmethod lidar_con_name-val ((m <lidar_lavacon>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar_pkg-msg:lidar_con_name-val is deprecated.  Use lidar_pkg-msg:lidar_con_name instead.")
  (lidar_con_name m))

(cl:ensure-generic-function 'lidar_con_color-val :lambda-list '(m))
(cl:defmethod lidar_con_color-val ((m <lidar_lavacon>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar_pkg-msg:lidar_con_color-val is deprecated.  Use lidar_pkg-msg:lidar_con_color instead.")
  (lidar_con_color m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <lidar_lavacon>) ostream)
  "Serializes a message object of type '<lidar_lavacon>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'lidar_mid_X))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'lidar_mid_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'lidar_mid_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'lidar_con_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'lidar_con_name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'lidar_con_color))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'lidar_con_color))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <lidar_lavacon>) istream)
  "Deserializes a message object of type '<lidar_lavacon>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'lidar_mid_X) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'lidar_mid_y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'lidar_mid_z) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'lidar_con_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'lidar_con_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'lidar_con_color) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'lidar_con_color) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<lidar_lavacon>)))
  "Returns string type for a message object of type '<lidar_lavacon>"
  "lidar_pkg/lidar_lavacon")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'lidar_lavacon)))
  "Returns string type for a message object of type 'lidar_lavacon"
  "lidar_pkg/lidar_lavacon")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<lidar_lavacon>)))
  "Returns md5sum for a message object of type '<lidar_lavacon>"
  "8869dac3714f40275d5d1c09afbfd6f5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'lidar_lavacon)))
  "Returns md5sum for a message object of type 'lidar_lavacon"
  "8869dac3714f40275d5d1c09afbfd6f5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<lidar_lavacon>)))
  "Returns full string definition for message of type '<lidar_lavacon>"
  (cl:format cl:nil "float64 lidar_mid_X~%float64 lidar_mid_y~%float64 lidar_mid_z~%string lidar_con_name~%string lidar_con_color~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'lidar_lavacon)))
  "Returns full string definition for message of type 'lidar_lavacon"
  (cl:format cl:nil "float64 lidar_mid_X~%float64 lidar_mid_y~%float64 lidar_mid_z~%string lidar_con_name~%string lidar_con_color~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <lidar_lavacon>))
  (cl:+ 0
     8
     8
     8
     4 (cl:length (cl:slot-value msg 'lidar_con_name))
     4 (cl:length (cl:slot-value msg 'lidar_con_color))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <lidar_lavacon>))
  "Converts a ROS message object to a list"
  (cl:list 'lidar_lavacon
    (cl:cons ':lidar_mid_X (lidar_mid_X msg))
    (cl:cons ':lidar_mid_y (lidar_mid_y msg))
    (cl:cons ':lidar_mid_z (lidar_mid_z msg))
    (cl:cons ':lidar_con_name (lidar_con_name msg))
    (cl:cons ':lidar_con_color (lidar_con_color msg))
))
