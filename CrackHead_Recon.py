#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
from termcolor import colored
import sys
# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

capture_Interface = str(raw_input("Enter the capture INTERFACE that was revealed to you in AIRMON: "))
# capture_Interface = CrackHead.airodump_String #For some reason this isnt working, it was supposed to import airodump_String from the first module
cmd_String = "airodump-ng %s" % capture_Interface
print colored(cmd_String,'red','on_white')
os.system(cmd_String)# we should open this in a new box to avoid disrupting the process
