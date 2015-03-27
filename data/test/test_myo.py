# -*- coding=utf-8 -*-

from __future__ import print_function, division

import unittest
from data.myo import Myo

class TestMyo(unittest.TestCase):
    def test_init(self):
        myo = Myo(1,2,3,4,5,6,7,8)
