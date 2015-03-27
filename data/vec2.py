# -*- coding=utf-8 -*-

from __future__ import division, print_function
from data.array import Array
import operator

class Vec3(Array):
    def __init__(self, x, y):
        Array.__init__(self)
        self.x = x
        self.y = y

    def tuple(self):
        return (self.x, self.y)

    @staticmethod
    def dot(self, other):
        return reduce(operator.add, Vec2.map(self, other, operator.mul).tuple())
