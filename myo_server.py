# -*- coding=utf-8 -*-

from __future__ import print_function, division

from myo_raw import MyoRaw
import binascii
import socket
import struct
import sys
from data.vec3 import Vec3
from data.quat import Quat
from data.imu import Imu
from data.myo import Myo
from data.device_data import Packet
import time

try:
    import pygame
    HAVE_PYGAME = True
except ImportError:
    HAVE_PYGAME = False

class App:
    def __init__(self, ip, port):
        self.running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.device = MyoRaw(None)
        self.frame = 0

        def proc_emg(emg, moving):
            self.myo = Myo(*emg)
        self.device.add_emg_handler(proc_emg)

        def proc_imu(quat, acc, gyro):
            self.imu = Imu(Vec3(*acc), Vec3(*gyro), Quat(*quat))
        self.device.add_imu_handler(proc_imu)

        self.device.connect()

        pygame.init()
        self.init_time = time.time()

    def run(self):
        while self.running:
            self.update()
            if HAVE_PYGAME:
                self.render()
                self.handle_input()

    def update(self):
        self.myo = None
        self.imu = None
        while self.myo == None or self.imu == None:
            self.device.run(1)
        packet = Packet(self.get_time(), self.imu, self.myo)
        print('frame:', self.frame)
        print(packet)
        print('-'*64)
        self.frame += 1

    def render(self):
        pass

    def handle_input(self):
        for ev in pygame.event.get():
            if ev.type == QUIT:
                self.on_quit()

    def cleanup(self):
        self.device.disconnect()

    def on_quit(self):
        self.running = False

    def get_time(self):
        return time.time() - self.init_time


def main(*args):
    try:
        port = int(args[0])
        print('Using port %d.' % port)
    except IndexError:
        port = 5000
        print("Port not specified. Using port %d." % port)

    app = App('localhost', port)
    try:
        app.run()
    except KeyboardInterrupt:
        pass
    finally:
        app.cleanup()


if __name__ == '__main__':
    main(*sys.argv[1:])
