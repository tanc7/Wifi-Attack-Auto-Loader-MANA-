# coding=UTF-8

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

        #os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/IDS_flood.py; exec bash\"'")
print colored('Mana-Toolkit Installer','red','on_white')

def mana_installer():

    tool_List = [
        'mana-toolkit',
        'wicd'
    ]
    print colored('Beginning toolkit installation','red','on_white')
    cmd_str = "sudo apt-get install %s" % ' '.join(map(str(tool_List)))
    print colored(cmd_str,'red','on_white')
    os.system('apt-get update')
    os.system(cmd_str)
    print colored('Installation finished, please proceed to configuring Wicd, option #2 on Main Menu','red','on_white')
    main()

def configure_wicd():
    print colored('Please do not lose your internet connection during this process!','red','on_white')
    print colored('Downloading a backup copy of Gnome Network Manager in case something goes wrong','red','on_white')
    cmd_str = "apt-get install --download-only network-manager"
    os.system(cmd_str)
    print colored('Updating APT Repositories','red','on_white')
    os.system('sudo apt-get update')
    print colored('Installing Wicd Network Manager','red','on_white')
    os.system('sudo apt-get install wicd')
    print colored('Removing GNOME network-manager, to allow Wicd and DNSMasq to run unimpeded','red','on_white')
    os.system('sudo apt-get --purge autoremove network-manager')
    print colored('Configuration finished, all network management is now taken over by Wicd, please restart your machine','red','on_white')
    main()
def restore_network_manager():
    os.system('sudo apt-get install network-manager')
    os.system('sudo apt-get install plasma-nm')
    os.system('sudo apt-get --purge autoremove wicd')
    print colored('Restoration Completed, restart your machine','red','on_white')
    main()
def main():
    opt_List = [
        '\n\t#1. Install the required components to run Mana',
        '#2. Remove Gnome-Network-Manager, configure Wicd as default, and retain a copy of Network-Manager in case of a screwup',
        '#RESTORE. Restore Gnome-Network_Manager, get rid of Wicd'
    ]
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        os.system('clear')
        mana_installer()
    elif opt_Choice == "2":
        os.system('clear')
        configure_wicd()
    elif opt_Choice == "RESTORE":
        os.system('clear')
    else:
        print colored('You have entered a invalid option','red','on_white')
    main()
main()
