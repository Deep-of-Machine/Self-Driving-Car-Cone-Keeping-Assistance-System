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
  :slots (_lidar_mid_X _lidar_mid_y _lidar_mid_z _lidar_con_name _lidar_con_color ))

(defmethod lidar_pkg::lavacon
  (:init
   (&key
    ((:lidar_mid_X __lidar_mid_X) 0.0)
    ((:lidar_mid_y __lidar_mid_y) 0.0)
    ((:lidar_mid_z __lidar_mid_z) 0.0)
    ((:lidar_con_name __lidar_con_name) "")
    ((:lidar_con_color __lidar_con_color) "")
    )
   (send-super :init)
   (setq _lidar_mid_X (float __lidar_mid_X))
   (setq _lidar_mid_y (float __lidar_mid_y))
   (setq _lidar_mid_z (float __lidar_mid_z))
   (setq _lidar_con_name (string __lidar_con_name))
   (setq _lidar_con_color (string __lidar_con_color))
   self)
  (:lidar_mid_X
   (&optional __lidar_mid_X)
   (if __lidar_mid_X (setq _lidar_mid_X __lidar_mid_X)) _lidar_mid_X)
  (:lidar_mid_y
   (&optional __lidar_mid_y)
   (if __lidar_mid_y (setq _lidar_mid_y __lidar_mid_y)) _lidar_mid_y)
  (:lidar_mid_z
   (&optional __lidar_mid_z)
   (if __lidar_mid_z (setq _lidar_mid_z __lidar_mid_z)) _lidar_mid_z)
  (:lidar_con_name
   (&optional __lidar_con_name)
   (if __lidar_con_name (setq _lidar_con_name __lidar_con_name)) _lidar_con_name)
  (:lidar_con_color
   (&optional __lidar_con_color)
   (if __lidar_con_color (setq _lidar_con_color __lidar_con_color)) _lidar_con_color)
  (:serialization-length
   ()
   (+
    ;; float64 _lidar_mid_X
    8
    ;; float64 _lidar_mid_y
    8
    ;; float64 _lidar_mid_z
    8
    ;; string _lidar_con_name
    4 (length _lidar_con_name)
    ;; string _lidar_con_color
    4 (length _lidar_con_color)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _lidar_mid_X
       (sys::poke _lidar_mid_X (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _lidar_mid_y
       (sys::poke _lidar_mid_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _lidar_mid_z
       (sys::poke _lidar_mid_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; string _lidar_con_name
       (write-long (length _lidar_con_name) s) (princ _lidar_con_name s)
     ;; string _lidar_con_color
       (write-long (length _lidar_con_color) s) (princ _lidar_con_color s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _lidar_mid_X
     (setq _lidar_mid_X (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _lidar_mid_y
     (setq _lidar_mid_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _lidar_mid_z
     (setq _lidar_mid_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; string _lidar_con_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _lidar_con_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _lidar_con_color
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _lidar_con_color (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get lidar_pkg::lavacon :md5sum-) "8869dac3714f40275d5d1c09afbfd6f5")
(setf (get lidar_pkg::lavacon :datatype-) "lidar_pkg/lavacon")
(setf (get lidar_pkg::lavacon :definition-)
      "float64 lidar_mid_X
float64 lidar_mid_y
float64 lidar_mid_z
string lidar_con_name
string lidar_con_color

")



(provide :lidar_pkg/lavacon "8869dac3714f40275d5d1c09afbfd6f5")


