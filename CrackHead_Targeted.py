#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
from termcolor import colored
import sys
# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

class airodump_Parameters_Targeted(object):

    def __init__(self, capture_Interface, capture_Channel, capture_BSSID, capture_Writefile):
        self.capture_Interface = capture_Interface
        self.capture_Channel = capture_Channel
        self.capture_BSSID = capture_BSSID
        self.capture_Writefile = capture_Writefile

    @classmethod
    def from_input(cls):
        return cls(
            str(raw_input("Enter the capture INTERFACE that was revealed to you in AIRMON: ")),
            str(raw_input("Enter the CHANNEL of the device you want to TARGET: ")),
            str(raw_input("Enter the BSSID/Broadcast MAC Address of your TARGET: ")),
            str(raw_input("Enter the full PATH and NAME of your pcap writefile: "))
        )

user_input = airodump_Parameters_Targeted.from_input()
print colored('Beginning targeted capture','red','on_white')
cmd_String = "airodump-ng --bssid {0} -c {1} --write {2} {3}".format(
    user_input.capture_BSSID,
    user_input.capture_Channel,
    user_input.capture_Writefile,
    user_input.capture_Interface
)
print colored(cmd_String,'red','on_white')

os.system(cmd_String)
