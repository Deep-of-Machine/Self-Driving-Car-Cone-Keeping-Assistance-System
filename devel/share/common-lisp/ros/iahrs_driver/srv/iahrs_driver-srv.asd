
(cl:in-package :asdf)

(defsystem "iahrs_driver-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "all_data_reset" :depends-on ("_package_all_data_reset"))
    (:file "_package_all_data_reset" :depends-on ("_package"))
    (:file "euler_angle_init" :depends-on ("_package_euler_angle_init"))
    (:file "_package_euler_angle_init" :depends-on ("_package"))
    (:file "euler_angle_reset" :depends-on ("_package_euler_angle_reset"))
    (:file "_package_euler_angle_reset" :depends-on ("_package"))
    (:file "pose_velocity_reset" :depends-on ("_package_pose_velocity_reset"))
    (:file "_package_pose_velocity_reset" :depends-on ("_package"))
    (:file "reboot_sensor" :depends-on ("_package_reboot_sensor"))
    (:file "_package_reboot_sensor" :depends-on ("_package"))
  ))