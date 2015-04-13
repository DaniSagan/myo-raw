# -*- coding=utf-8 -*-

from __future__ import division, print_function

import socket
import select
import time


class Publisher(object):
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port))
        self.sock.listen(10)
        self.socket_list = [self.sock]
        print('Publisher started on port', port)

    def run(self):
        self.running = True
        count = 0
        while self.running:
            to_read, to_write, in_error = select.select(self.socket_list, [], [], 0)
            for sock in to_read:
                if sock == self.sock:
                    sockfd, addr = self.sock.accept()
                    self.socket_list.append(sockfd)
            print('broadcasting...')
            self.broadcast('hello ' + str(count))
            count += 1
            time.sleep(1/50)
        self.sock.close()

    def publish(self, data):
        to_read, to_write, in_error = select.select(self.socket_list, [], [], 0)
        for sock in to_read:
            if sock == self.sock:
                sockfd, addr = self.sock.accept()
                self.socket_list.append(sockfd)
        print('broadcasting data...')
        self.broadcast(data)

    def broadcast(self, message):
        for s in self.socket_list:
            if s != self.sock:
                try:
                    s.send(message)
                except:
                    s.close()
                    if s in self.socket_list:
                        self.socket_list.remove(s)
