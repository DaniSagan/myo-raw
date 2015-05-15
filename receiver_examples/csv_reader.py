#! /usr/bin/python
# -*- coding=utf8 -*-

import matplotlib.pyplot as plt
import sys


def main():
    filename = sys.argv[1]
    times = []
    accx = []
    accy = []
    accz = []
    gyrx = []
    gyry = []
    gyrz = []
    with open(filename, 'r') as fobj:
        for k, line in enumerate(fobj.readlines()):
            if k != 0:
                tokens = line.split()
                times.append(float(tokens[0]))
                accx.append(int(tokens[1]))
                accy.append(int(tokens[2]))
                accz.append(int(tokens[3]))
                gyrx.append(int(tokens[4]))
                gyry.append(int(tokens[5]))
                gyrz.append(int(tokens[6]))

    plt.figure('Acc')
    plt.plot(accx, label='accx')
    plt.plot(accy, label='accy')
    plt.plot(accz, label='accz')
    plt.grid()
    plt.legend()
    plt.show(block=False)

    plt.figure('Gyr')
    plt.plot(gyrx, label='gyrx')
    plt.plot(gyry, label='gyry')
    plt.plot(gyrz, label='gyrz')
    plt.grid()
    plt.legend()
    plt.show(block=False)

    raw_input('Pulse cualquier tecla para finalizar')


if __name__ == '__main__':
    main()
