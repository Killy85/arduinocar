#!/usr/bin/python3

import time
from random import randint
from bluepy.btle import Scanner, DefaultDelegate, Peripheral

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)


    def HandleDiscovery(self,dev,new_dev,new_dat):
        if new_dev:
            pass
        if new_dat:
            pass
        
scanner = Scanner().withDelegate(ScanDelegate())

time_diff = 0
first_time = 1
try:
    devices = scanner.scan(0.35)
    for ii in devices:
        if ii.addr == '34:03:de:34:94:69':
            periph = Peripheral(ii.addr)
            continue

    chars = periph.getCharacteristics()

    peripheral = chars[6]

    peripheral.write(('POW '+str(randint(0,255))).encode('ascii'))
    time.sleep(2)

    peripheral.write(('ROT '+str(randint(0,255))).encode('ascii'))

    time.sleep(2)

    peripheral.write(('POW 0').encode('ascii'))
    time.sleep(2)

    peripheral.write(('ROT 0').encode('ascii'))

    time.sleep(2)

    peripheral.write(('POW '+str(randint(0,255))).encode('ascii'))
    time.sleep(2)

    peripheral.write(('ROT '+str(randint(0,255))).encode('ascii'))

    time.sleep(2)
except Exception as e:
    print(e)

