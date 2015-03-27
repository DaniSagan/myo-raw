# -*- coding=utf-8 -*-

class MyographData(Array):
    def __init__(self, *data):
        Array.__init__(self)
        self.data = data

    def tuple(self):
        return self.data
