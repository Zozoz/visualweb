#!/usr/bin/env python
# encoding: utf-8


import subprocess


def run_algorithm(algorithm, minSup, minConf, datafile):
    datapath = 'media/' + datafile
    pypath = 'algorithm/'
    command = []
    command.append('time')
    command.append('python')
    command.append(pypath + algorithm.lower() + '.py')
    command.append('-s')
    command.append(minSup)
    command.append('-c')
    command.append(minConf)
    command.append('-f')
    command.append(datapath)
    subprocess.call(command)


if __name__ == '__main__':
    run_algorithm('apriori', '0.91', '0.8', 'tmp.data')
