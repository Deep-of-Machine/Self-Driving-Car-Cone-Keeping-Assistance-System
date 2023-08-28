#!/usr/bin/python3

import rospy
from datetime import datetime
from rtcm_msgs.msg import Message

from base64 import b64encode
from threading import Thread
import requests

class ntripconnect(Thread):
    def __init__(self, ntc):
        super(ntripconnect, self).__init__()
        self.ntc = ntc
        self.stop = False

    def run(self):
        headers = {
            'Ntrip-Version': 'Ntrip/2.0',
            'User-Agent': 'NTRIP ntrip_ros',
            'Authorization': 'Basic ' + b64encode((self.ntc.ntrip_user + ':' + str(self.ntc.ntrip_pass)).encode()).decode()
        }
        url = "http://" + self.ntc.ntrip_server + '/' + self.ntc.ntrip_stream
        
        try:
            print('s')
            response = requests.get(url, headers=headers, stream=True)
            response.raise_for_status()

            buf = b""
            rmsg = Message()
            for data in response.iter_content(chunk_size=1):
                if data[0] == 211:
                    buf += data
                    data = response.iter_content(chunk_size=2)
                    buf += data
                    cnt = data[0] * 256 + data[1]
                    data = response.iter_content(chunk_size=2)
                    buf += data
                    typ = (data[0] * 256 + data[1]) // 16
                    print(str(datetime.now()), cnt, typ)
                    cnt = cnt + 1
                    for x in range(cnt):
                        data = response.iter_content(chunk_size=1)
                        buf += data
                    rmsg.message = buf
                    rmsg.header.seq += 1
                    rmsg.header.stamp = rospy.get_rostime()
                    self.ntc.pub.publish(rmsg)
                    buf = b""
                else:
                    print(data)
        except requests.RequestException as e:
            rospy.logerr("Error during request: %s", str(e))

class ntripclient:
    def __init__(self):
        rospy.init_node('ntripclient', anonymous=True)

        self.rtcm_topic = rospy.get_param('~rtcm_topic', 'rtcm')
        self.nmea_topic = rospy.get_param('~nmea_topic', 'nmea')

        self.ntrip_server = rospy.get_param('~ntrip_server')
        self.ntrip_user = rospy.get_param('~ntrip_user')
        self.ntrip_pass = rospy.get_param('~ntrip_pass')
        self.ntrip_stream = rospy.get_param('~ntrip_stream')
        self.nmea_gga = rospy.get_param('~nmea_gga')

        self.pub = rospy.Publisher(self.rtcm_topic, Message, queue_size=10)

        self.connection = None
        self.connection = ntripconnect(self)
        self.connection.start()

    def run(self):
        rospy.spin()
        if self.connection is not None:
            self.connection.stop = True

if __name__ == '__main__':
    c = ntripclient()
    c.run()

