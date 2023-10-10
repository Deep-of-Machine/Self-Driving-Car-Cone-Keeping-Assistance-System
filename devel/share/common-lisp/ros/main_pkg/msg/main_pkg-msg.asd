
(cl:in-package :asdf)

(defsystem "main_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "lavacon" :depends-on ("_package_lavacon"))
    (:file "_package_lavacon" :depends-on ("_package"))
    (:file "lidar_lavacon" :depends-on ("_package_lidar_lavacon"))
    (:file "_package_lidar_lavacon" :depends-on ("_package"))
    (:file "yolo_lavacon" :depends-on ("_package_yolo_lavacon"))
    (:file "_package_yolo_lavacon" :depends-on ("_package"))
  ))