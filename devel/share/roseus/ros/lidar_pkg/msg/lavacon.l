;; Auto-generated. Do not edit!


(when (boundp 'lidar_pkg::lavacon)
  (if (not (find-package "LIDAR_PKG"))
    (make-package "LIDAR_PKG"))
  (shadow 'lavacon (find-package "LIDAR_PKG")))
(unless (find-package "LIDAR_PKG::LAVACON")
  (make-package "LIDAR_PKG::LAVACON"))

(in-package "ROS")
;;//! \htmlinclude lavacon.msg.html


(defclass lidar_pkg::lavacon
  :super ros::object
  :slots (_con_mid_X _con_mid_y _con_mid_z _con_name _con_color ))

(defmethod lidar_pkg::lavacon
  (:init
   (&key
    ((:con_mid_X __con_mid_X) 0.0)
    ((:con_mid_y __con_mid_y) 0.0)
    ((:con_mid_z __con_mid_z) 0.0)
    ((:con_name __con_name) "")
    ((:con_color __con_color) "")
    )
   (send-super :init)
   (setq _con_mid_X (float __con_mid_X))
   (setq _con_mid_y (float __con_mid_y))
   (setq _con_mid_z (float __con_mid_z))
   (setq _con_name (string __con_name))
   (setq _con_color (string __con_color))
   self)
  (:con_mid_X
   (&optional __con_mid_X)
   (if __con_mid_X (setq _con_mid_X __con_mid_X)) _con_mid_X)
  (:con_mid_y
   (&optional __con_mid_y)
   (if __con_mid_y (setq _con_mid_y __con_mid_y)) _con_mid_y)
  (:con_mid_z
   (&optional __con_mid_z)
   (if __con_mid_z (setq _con_mid_z __con_mid_z)) _con_mid_z)
  (:con_name
   (&optional __con_name)
   (if __con_name (setq _con_name __con_name)) _con_name)
  (:con_color
   (&optional __con_color)
   (if __con_color (setq _con_color __con_color)) _con_color)
  (:serialization-length
   ()
   (+
    ;; float64 _con_mid_X
    8
    ;; float64 _con_mid_y
    8
    ;; float64 _con_mid_z
    8
    ;; string _con_name
    4 (length _con_name)
    ;; string _con_color
    4 (length _con_color)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _con_mid_X
       (sys::poke _con_mid_X (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _con_mid_y
       (sys::poke _con_mid_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _con_mid_z
       (sys::poke _con_mid_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; string _con_name
       (write-long (length _con_name) s) (princ _con_name s)
     ;; string _con_color
       (write-long (length _con_color) s) (princ _con_color s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _con_mid_X
     (setq _con_mid_X (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _con_mid_y
     (setq _con_mid_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _con_mid_z
     (setq _con_mid_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; string _con_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _con_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _con_color
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _con_color (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get lidar_pkg::lavacon :md5sum-) "d7d5d863398db1715dabc8c59e13dbfe")
(setf (get lidar_pkg::lavacon :datatype-) "lidar_pkg/lavacon")
(setf (get lidar_pkg::lavacon :definition-)
      "float64 con_mid_X
float64 con_mid_y
float64 con_mid_z
string con_name
string con_color

")



(provide :lidar_pkg/lavacon "d7d5d863398db1715dabc8c59e13dbfe")


