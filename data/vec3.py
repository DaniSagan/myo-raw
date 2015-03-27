# -*- coding=utf-8 -*-

from __future__ import division, print_function
from data.array import Array
import operator

class Vec3(Array):
    def __init__(self, x, y, z):
        Array.__init__(self)
        self.x = x
        self.y = y
        self.z = z

    def tuple(self):
        return (self.x, self.y, self.z)

    @staticmethod
    def dot(self, other):
        return reduce(operator.add, Vec3.map(self, other, operator.mul).tuple())

    @staticmethod
    def cross(v1, v2):
        return Vec3(
            v1.y*v2.z-v1.z*v2.y,
            v1.z*v2.y-v1.y*v2.z,
            v1.x*v2.y-v1.y*v2.x
        )
