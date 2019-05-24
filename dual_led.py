#!/usr/bin/python3

import time
from random import randint
from bluepy.btle import Scanner, DefaultDelegate, Peripheral

from tkinter import *


peripheral = None


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)


    def HandleDiscovery(self,dev,new_dev,new_dat):
        if new_dev:
            pass
        if new_dat:
            pass


def update_motor_rot(val):
    peripheral.write(('ROT '+val).encode('ascii'))


def update_motor_pow(val):
    peripheral.write(('POW '+ val).encode('ascii'))

scanner = Scanner().withDelegate(ScanDelegate())

time_diff = 0
first_time = 1
try:
    import ipdb; ipdb.set_trace()
    devices = scanner.scan(0.35)
    for ii in devices:
        if ii.addr == '34:03:de:34:94:69':
            periph = Peripheral(ii.addr)
            continue

    chars = periph.getCharacteristics()

    peripheral = chars[6]

    master = Tk()
    w1 = Scale(master, from_=255, to=0, tickinterval=2, command=update_motor_rot)
    w1.set(0)
    w1.pack()
    w2 = Scale(master, from_=255, to=0,tickinterval=2, command=update_motor_pow)
    w2.set(0)
    w2.pack()

    time.sleep(2)
except Exception as e:
    print(e)

mainloop()