# -*- coding=utf-8 -*-

from __future__ import print_function, division

import unittest
from data.vec3 import Vec3
from data.quat import Quat
from data.imu import Imu
from data.myo import Myo
from data.device_data import Packet
import time

class TestDeviceData(unittest.TestCase):
    def test_pack(self):
        acc = Vec3(1, 2, 3)
        gyr = Vec3(4, 5, 6)
        quat = Quat(1, 0, 0, 0)
        imu = Imu(acc, gyr, quat)
        myo = Myo(1,2,3,4,5,6,7,8)
        t = time.time()

        packet = Packet(t, imu, myo)
        unpacked_packet = Packet.unpack(packet.pack())

        self.assertEqual(packet.time, unpacked_packet.time)
        self.assertEqual(packet.imu, unpacked_packet.imu)
