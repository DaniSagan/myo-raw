# -*- coding=utf-8 -*-

from __future__ import division, print_function
from data.array import Array

class Quat(Array):
    def __init__(self, w, x, y, z):
        Array.__init__(self)
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def tuple(self):
        return (self.w, self.x, self.y, self.z)
