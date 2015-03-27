# -*- coding=utf-8 -*-

from data.array import Array

class Myo(Array):
    def __init__(self, *data):
        Array.__init__(self)
        self.data = data

    def tuple(self):
        return self.data
