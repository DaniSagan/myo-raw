# -*- coding=utf-8 -*-

from __future__ import division, print_function

import sys
sys.path.append('..')
from network.subscriber import Subscriber
from data.device_data import Packet


if __name__ == '__main__':
    host = 'localhost'
    port = 5000
    s = Subscriber(host, port)

    def print_data(data):
        print(Packet.unpack(data))

    s.add_callback(print_data)
    s.run()
