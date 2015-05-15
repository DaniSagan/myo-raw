#! /usr/bin/python
# -*- coding=utf-8 -*-

from __future__ import print_function, division

import collections
import sys
import pygame

sys.path.append('..')
from network.subscriber import Subscriber
from data.device_data import Packet


def main():

    n = 100

    accx = collections.deque([0]*n, n)
    accy = collections.deque([0]*n, n)
    accz = collections.deque([0]*n, n)
    acc_scale = 2048.

    gyrx = collections.deque([0]*n, n)
    gyry = collections.deque([0]*n, n)
    gyrz = collections.deque([0]*n, n)
    gyr_scale = 16.

    def plot_data(unpacked_data):
        data = Packet.unpack(unpacked_data)
        accx.appendleft(data.imu.acc.x / acc_scale)
        accy.appendleft(data.imu.acc.y / acc_scale)
        accz.appendleft(data.imu.acc.z / acc_scale)
        gyrx.appendleft(data.imu.gyr.x / gyr_scale)
        gyry.appendleft(data.imu.gyr.y / gyr_scale)
        gyrz.appendleft(data.imu.gyr.z / gyr_scale)


    SIZE = WIDTH, HEIGHT = 1024, 640
    screen = pygame.display.set_mode(SIZE)


    host = 'localhost'
    port = 5000
    s = Subscriber(host, port, buffer_size=80)
    s.add_callback(plot_data)
    s.run()


if __name__ == '__main__':
    main()
