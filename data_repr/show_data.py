#! /usr/bin/python
# -*- coding=utf-8 -*-

from __future__ import division, print_function
import sys
import csv
import matplotlib.pyplot as plt
import numpy


def read_csv(filename):
    data = {}
    with open(filename, 'r') as fobj:
        reader = csv.reader(fobj, delimiter='\t')
        for k, row in enumerate(reader):
            if k == 0:
                keywords = row
                for keyword in keywords:
                    data[keyword] = []
            else:
                for n, item in enumerate(row):
                    data[keywords[n]].append(float(item))
    return data


def main(argv):
    filename = argv[0]
    data = read_csv(filename)

    plt.figure('gyr')
    plt.plot(data['time'], data['gyrx'], color='red', label='gyrx')
    plt.plot(data['time'], data['gyry'], color='green', label='gyry')
    plt.plot(data['time'], data['gyrz'], color='blue', label='gyrz')
    plt.grid()
    plt.legend()
    plt.show(block=False)

    plt.figure('acc')
    plt.plot(data['time'], data['accx'], color='red', label='accx')
    plt.plot(data['time'], data['accy'], color='green', label='accy')
    plt.plot(data['time'], data['accz'], color='blue', label='accz')
    plt.grid()
    plt.legend()
    plt.show(block=False)

    print('stddev(gyrx):', numpy.std(data['gyrx']))
    print('stddev(gyry):', numpy.std(data['gyry']))
    print('stddev(gyrz):', numpy.std(data['gyrz']))

    print('stddev(accx):', numpy.std(data['accx']))
    print('stddev(accy):', numpy.std(data['accy']))
    print('stddev(accz):', numpy.std(data['accz']))

    raw_input('Press any key to finish')


if __name__ == '__main__':
    main(sys.argv[1:])
