# -*- coding=utf-8 -*-

from __future__ import division, print_function

from data.vec3 import Vec3
from data.quat import Quat

class Imu(object):
    def __init__(self, acc, gyr, quat):
        self.acc = acc
        self.gyr = gyr
        self.quat = quat

    def tuple(self):
        return tuple([item
            for v in[self.acc, self.gyr, self.quat]
            for item in v.tuple()])

    @staticmethod
    def from_tuple(tp):
        acc = Vec3(*tp[:3])
        gyr = Vec3(*tp[3:6])
        quat = Quat(*tp[6:])
        return Imu(acc, gyr, quat)

    def __str__(self):
        return 'acc: %s\ngyr: %s\nquat: %s' % (str(self.acc), str(self.gyr), str(self.quat))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if other == None:
            return False
        if self.__class__ != other.__class__:
            raise ValueError('Both objects must be of type %s' % self.__class__.__name__)
        return self.tuple() == other.tuple()
