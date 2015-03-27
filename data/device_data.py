# -*- coding=utf-8 -*-

from __future__ import division, print_function

from data.vec3 import Vec3
from data.quat import Quat
from data.myo import Myo
from data.imu import Imu
import struct

class Packet(object):
    PACKER = struct.Struct('d 18i')

    def __init__(self, time, imu, myo):
        self.time = time
        self.imu = imu
        self.myo = myo

    def tuple(self):
        return (self.time,) + tuple([item
            for v in [self.imu, self.myo]
            for item in v.tuple()])

    def pack(self):
        return Packet.PACKER.pack(*self.tuple())

    @staticmethod
    def unpack(packet):
        unpacked_data = Packet.PACKER.unpack(packet)
        t = unpacked_data[0]
        imu = Imu.from_tuple(tuple(unpacked_data[1:11]))
        myo = Myo(*tuple(unpacked_data[11:]))
        return Packet(t, imu, myo)

    def __str__(self):
        fmt = 'time: %f\nimu:\n\tacc: %s\n\tgyr: %s\n\tquat: %s\nmyo: %s'
        items = (self.time, self.imu.acc, self.imu.gyr, self.imu.quat, self.myo)
        return fmt % items

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if other == None:
            return False
        if self.__class__ != other.__class__:
            raise ValueError('Both objects must be of type %s' % self.__class__.__name__)
        return self.tuple() == other.tuple()
