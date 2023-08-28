;; Auto-generated. Do not edit!


(when (boundp 'lidar_pkg::yolo_lavacon)
  (if (not (find-package "LIDAR_PKG"))
    (make-package "LIDAR_PKG"))
  (shadow 'yolo_lavacon (find-package "LIDAR_PKG")))
(unless (find-package "LIDAR_PKG::YOLO_LAVACON")
  (make-package "LIDAR_PKG::YOLO_LAVACON"))

(in-package "ROS")
;;//! \htmlinclude yolo_lavacon.msg.html


(defclass lidar_pkg::yolo_lavacon
  :super ros::object
  :slots (_yolo_mid_X _yolo_mid_y _yolo_con_name _yolo_con_color ))

(defmethod lidar_pkg::yolo_lavacon
  (:init
   (&key
    ((:yolo_mid_X __yolo_mid_X) 0.0)
    ((:yolo_mid_y __yolo_mid_y) 0.0)
    ((:yolo_con_name __yolo_con_name) "")
    ((:yolo_con_color __yolo_con_color) "")
    )
   (send-super :init)
   (setq _yolo_mid_X (float __yolo_mid_X))
   (setq _yolo_mid_y (float __yolo_mid_y))
   (setq _yolo_con_name (string __yolo_con_name))
   (setq _yolo_con_color (string __yolo_con_color))
   self)
  (:yolo_mid_X
   (&optional __yolo_mid_X)
   (if __yolo_mid_X (setq _yolo_mid_X __yolo_mid_X)) _yolo_mid_X)
  (:yolo_mid_y
   (&optional __yolo_mid_y)
   (if __yolo_mid_y (setq _yolo_mid_y __yolo_mid_y)) _yolo_mid_y)
  (:yolo_con_name
   (&optional __yolo_con_name)
   (if __yolo_con_name (setq _yolo_con_name __yolo_con_name)) _yolo_con_name)
  (:yolo_con_color
   (&optional __yolo_con_color)
   (if __yolo_con_color (setq _yolo_con_color __yolo_con_color)) _yolo_con_color)
  (:serialization-length
   ()
   (+
    ;; float64 _yolo_mid_X
    8
    ;; float64 _yolo_mid_y
    8
    ;; string _yolo_con_name
    4 (length _yolo_con_name)
    ;; string _yolo_con_color
    4 (length _yolo_con_color)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _yolo_mid_X
       (sys::poke _yolo_mid_X (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yolo_mid_y
       (sys::poke _yolo_mid_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; string _yolo_con_name
       (write-long (length _yolo_con_name) s) (princ _yolo_con_name s)
     ;; string _yolo_con_color
       (write-long (length _yolo_con_color) s) (princ _yolo_con_color s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _yolo_mid_X
     (setq _yolo_mid_X (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yolo_mid_y
     (setq _yolo_mid_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; string _yolo_con_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _yolo_con_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _yolo_con_color
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _yolo_con_color (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get lidar_pkg::yolo_lavacon :md5sum-) "da269e966072bed82c14a04982ff80e5")
(setf (get lidar_pkg::yolo_lavacon :datatype-) "lidar_pkg/yolo_lavacon")
(setf (get lidar_pkg::yolo_lavacon :definition-)
      "float64 yolo_mid_X
float64 yolo_mid_y
string yolo_con_name
string yolo_con_color

")



(provide :lidar_pkg/yolo_lavacon "da269e966072bed82c14a04982ff80e5")


