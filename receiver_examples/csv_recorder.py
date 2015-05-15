# -*- coding=utf-8 -*-

from __future__ import division, print_function

import sys
import csv
sys.path.append('..')
from network.subscriber import Subscriber
from data.device_data import Packet
import sys


if __name__ == '__main__':
    host = 'localhost'
    port = 5000
    s = Subscriber(host, port)
    try:
        output_file = sys.argv[1]
    except:
        output_file = 'output.csv'

    with open(output_file, 'w') as fobj:
        writer = csv.writer(fobj, delimiter='\t')
        headers = ['time', 'accx', 'accy', 'accz', 'gyrx', 'gyry', 'gyrz',
                   'quatw', 'quatx', 'quaty', 'quatz']
        writer.writerow(headers)

        def write_data(unpacked_data):
            data = Packet.unpack(unpacked_data)
            str_data = ['{:0.3f}'.format(data.time),
                        str(data.imu.acc.x), str(data.imu.acc.y), str(data.imu.acc.z),
                        str(data.imu.gyr.x), str(data.imu.gyr.y), str(data.imu.gyr.z),
                        str(data.imu.quat.w), str(data.imu.quat.x), str(data.imu.quat.y), str(data.imu.quat.z)]
            writer.writerow(str_data)

        s.add_callback(write_data)
        s.run()
