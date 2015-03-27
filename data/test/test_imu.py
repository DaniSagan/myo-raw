# -*- coding=utf-8 -*-

from __future__ import print_function, division

import unittest
from data.imu import Imu
from data.vec3 import Vec3
from data.quat import Quat

class TestImu(unittest.TestCase):
    def test_tuple(self):
        acc = Vec3(1, 2, 3)
        gyr = Vec3(4, 5, 6)
        quat = Quat(1, 0, 0, 0)
        imu = Imu(acc, gyr, quat)
        t = imu.tuple()

        self.assertEqual(t[0], acc.x)
        self.assertEqual(t[1], acc.y)
        self.assertEqual(t[2], acc.z)
        self.assertEqual(t[3], gyr.x)
        self.assertEqual(t[4], gyr.y)
        self.assertEqual(t[5], gyr.z)
        self.assertEqual(t[6], quat.w)
        self.assertEqual(t[7], quat.x)
        self.assertEqual(t[8], quat.y)
        self.assertEqual(t[9], quat.z)

    def test_from_tuple(self):
        acc = Vec3(1, 2, 3)
        gyr = Vec3(4, 5, 6)
        quat = Quat(1, 0, 0, 0)
        tp = acc.tuple() + gyr.tuple() + quat.tuple()
        imu = Imu.from_tuple(tp)

        self.assertEqual(acc.x, imu.acc.x)
        self.assertEqual(acc.y, imu.acc.y)
        self.assertEqual(acc.z, imu.acc.z)
        self.assertEqual(gyr.x, imu.gyr.x)
        self.assertEqual(gyr.y, imu.gyr.y)
        self.assertEqual(gyr.z, imu.gyr.z)
        self.assertEqual(quat.w, imu.quat.w)
        self.assertEqual(quat.x, imu.quat.x)
        self.assertEqual(quat.y, imu.quat.y)
        self.assertEqual(quat.z, imu.quat.z)
