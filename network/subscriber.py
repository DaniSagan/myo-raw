# -*- coding=utf-8 -*-

from __future__ import division, print_function

import socket
import select
import sys
sys.path.append('..')
from data.device_data import Packet


class Subscriber(object):
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        print('Connected to publisher')
        self.callbacks = []

    def run(self):
        self.running = True
        while self.running:
            socket_list = [self.sock]
            to_read, to_write, in_error = select.select(socket_list, [], [])
            for sock in to_read:
                if sock == self.sock:
                    data = sock.recv(1024)
                    if data:
                        print('Data received')
                        self.execute_callbacks(data)
                        #print(Packet.unpack(data))

    def execute_callbacks(self, data):
        for c in self.callbacks:
            c(data)

    def add_callback(self, callback):
        self.callbacks.append(callback)


if __name__ == '__main__':
    host = 'localhost'
    port = 5000
    #Subscriber(host, port).run()
    s = Subscriber(host, port)

    def print_data(data):
        print(Packet.unpack(data))

    s.add_callback(print_data)
    s.run()
