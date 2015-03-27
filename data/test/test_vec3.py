# -*- coding=utf-8 -*-
from __future__ import print_function, division

import unittest
from data.vec3 import Vec3

class TestVec3(unittest.TestCase):
    def test_add(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(4,5,6)
        v_sum = v1 + v2
        self.assertEqual(v1.x+v2.x, v_sum.x)
        self.assertEqual(v1.y+v2.y, v_sum.y)
        self.assertEqual(v1.z+v2.z, v_sum.z)

    def test_sub(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(4,5,6)
        v_diff = v1 - v2
        self.assertEqual(v1.x-v2.x, v_diff.x)
        self.assertEqual(v1.y-v2.y, v_diff.y)
        self.assertEqual(v1.z-v2.z, v_diff.z)

    def test_mul(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(4,5,6)
        v_mul = v1 * 2
        self.assertEqual(v1.x*2, v_mul.x)
        self.assertEqual(v1.y*2, v_mul.y)
        self.assertEqual(v1.z*2, v_mul.z)
