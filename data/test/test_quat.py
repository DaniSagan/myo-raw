# -*- coding=utf-8 -*-

from __future__ import print_function, division

import unittest
from data.quat import Quat

class TestQuat(unittest.TestCase):
    def test_add(self):
        q1 = Quat(1,2,3,4)
        q2 = Quat(4,5,6,7)
        q_sum = q1 + q2
        self.assertEqual(q1.w+q2.w, q_sum.w)
        self.assertEqual(q1.x+q2.x, q_sum.x)
        self.assertEqual(q1.y+q2.y, q_sum.y)
        self.assertEqual(q1.z+q2.z, q_sum.z)

    def test_sub(self):
        q1 = Quat(1,2,3,4)
        q2 = Quat(4,5,6,7)
        q_diff = q1 - q2
        self.assertEqual(q1.w-q2.w, q_diff.w)
        self.assertEqual(q1.x-q2.x, q_diff.x)
        self.assertEqual(q1.y-q2.y, q_diff.y)
        self.assertEqual(q1.z-q2.z, q_diff.z)

    def test_mul(self):
        q1 = Quat(1,2,3,4)
        q_mul = q1 * 2
        self.assertEqual(q1.w*2, q_mul.w)
        self.assertEqual(q1.x*2, q_mul.x)
        self.assertEqual(q1.y*2, q_mul.y)
        self.assertEqual(q1.z*2, q_mul.z)
