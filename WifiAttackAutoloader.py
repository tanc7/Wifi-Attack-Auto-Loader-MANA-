#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
from termcolor import colored
import sys
import time
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

os.system('cat /root/WifiAttackAutoloaderProject/autoloaderBanner.txt')
print colored('Autoloader, written by Chang Tan Lister\nIntended to reduce the difficulty of initial setup of Kali Wireless Attack Tools\nSpecial thanks  goes to the developers of Mana-Toolkit, Fern Wifi Cracker, and the Aircrack Suite','red','on_white')
os.system('cat /root/WifiAttackAutoloaderProject/DISCLAIMER')

def step_1_check():
    step_One = str(raw_input("Insert your external Wi-Fi Card, then type CONTINUE: "))
    if step_One == "CONTINUE":
        step_2_check()
    else:
        print colored('Please type CONTINUE in all caps','red','on_white')
        step_1_check()
def step_2_check():
    step_Two = str(raw_input("Using your INTERNAL PCI Wi-Fi Card, connect to your internet uplink source using Wicd, then type CONTINUE: "))
    if step_Two == "CONTINUE":
        print colored('Restarting network interfaces to bring all Wi-Fi cards up','red','on_white')
        os.system('/root/WifiAttackAutoloaderProject/bring_Interfaces_Down.sh')
        os.system('/root/WifiAttackAutoloaderProject/bring_Interfaces_Up.sh')
        print colored('Starting Mana','red','on_white')
        #os.system('/usr/share/mana-toolkit/run-mana/start-nat-full.sh')
        os.system("gnome-terminal -e 'bash -c \"/usr/share/mana-toolkit/run-mana/start-nat-full.sh; exec bash\"'")
        mana_toolkit()

    else:
        print colored('Please type CONTINUE in all caps','red','on_white')
        step_2_check()

def mana_toolkit():
    opt_List = [
        '\n\t#INSTALL. Install Mana-Toolkit Prerequisites',
        '#HELP. Learn how Mana-Tookit works and what to configure in #1 and #2',
        '#1. Configure start-nat-full, change which hostapd file to use, etc.',
        '#2. Configure the Mana-Tookit Settings (hostapd file), Change BSSID Name, MAC Address, etc',
        '#3. Start the Mana Man-In-The-Middle Attack',
        '#4. Open FireLamb to check on Intercepted Cookies and Creds (while MANA is running)',
        '#5. Start TCPDump while the attack is running to start capturing packets',
        '#999. Restart All Network Interfaces (If there is something wrong with wifi card detection in Mana)',
        '#0. Return to the Main Menu'
    ]
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))
        #Sample open new terminal window code from other projects
        #os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/IDS_flood.py; exec bash\"'")

    if opt_Choice == "INSTALL":
        os.system('clear')
        os.system("gnome-terminal -e 'bash -c \"python /root/WifiAttackAutoloaderProject/Mana_Installer.py; exec bash\"'")
        mana_toolkit()
    elif opt_Choice == "1":
        os.system("gnome-terminal -e 'bash -c \"nano /usr/share/mana-toolkit/run-mana/start-nat-full.sh; exec bash\"'")
        mana_toolkit()
    elif opt_Choice == "2":
        os.system("gnome-terminal -e 'bash -c \"nano /etc/mana-toolkit/hostapd-mana.conf\"'")
        mana_toolkit()
    elif opt_Choice == "3":
        step_1_check()
    elif opt_Choice == "4":
        os.system("gnome-terminal -e 'bash -c \"/usr/share/mana-toolkit/run-mana/firelamb-view.sh; exec bash\"'")
    elif opt_Choice == "5":
        timestr = time.strftime("%Y%m%d-%H%M%S")
        basic_Filename = "/root/WifiAttackAutoloaderProject/logs/TCPDump_"
        modified_Filename = basic_Filename + timestr + '.pcap'
        tcp_Dump_String = "gnome-terminal -e 'bash -c \"sudo tcpdump -i wlan1 -w {0}; exec bash\"'".format(
            modified_Filename
        )
        os.system(tcp_Dump_String)
    elif opt_Choice == "999":
        os.system('/root/WifiAttackAutoloaderProject/bring_Interfaces_Down.sh')
        os.system('/root/WifiAttackAutoloaderProject/bring_Interfaces_Up.sh')
        mana_toolkit()
    elif opt_Choice == "HELP":
        os.system('cat /root/WifiAttackAutoloaderProject/HowToConfigureMana.txt')
        mana_toolkit()
    elif opt_Choice == "0":
        main()
    else:
        print colored('You have entered a invalid option','red','on_white')
        mana_toolkit()


def fern_wifi_cracker():
    opt_List = [
        '\n\t#INSTALL. Install Fern-Wifi-cracker Prequisites',
        '#1. Start Fern-Wifi-Cracker',
        '#0. Return to the Main Menu'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "INSTALL":
        print colored('Updating APT Repositories','red','on_white')
        os.system('sudo apt-get update')
        print colored('Installing Fern-Wifi-Cracker','red','on_white')
        os.system('sudo apt-get install fern-wifi-cracker')
        fern_wifi_cracker()
    elif opt_Choice == "1":
        print colored('Bringing interfaces down and up to make sure it all works','red','on_white')
        os.system('/root/WifiAttackAutoloaderProject/bring_Interfaces_Down.sh')
        os.system('/root/WifiAttackAutoloaderProject/bring_Interfaces_Up.sh')
        os.system('airmon-ng wlan1 start')
        os.system('airodump-ng wlan1mon')
        print colored('Starting Fern Wifi Cracker','red','on_white')
        os.system("gnome-terminal -e 'bash -c \"fern-wifi-cracker; exec bash\"'")
        main()
def aircrack_suite():
    os.system("gnome-terminal -e 'bash -c \"python /root/WifiAttackAutoloaderProject/CrackHead.py; exec bash\"'")
    main()

def main():
    print colored('MAIN MENU','red','on_white')
    opt_List = [
        '\n\t#1. Run Mana-Toolkit "Evil Twin" MitM Attacks',
        '#2. Run the Fern-Wifi-Cracker Suite',
        '#3. Run the Aircrack Suite'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        os.system('clear')
        mana_toolkit()
    elif opt_Choice == "2":
        os.system('clear')
        fern_wifi_cracker()
    elif opt_Choice == "3":
        os.system('clear')
        aircrack_suite()
    else:
        print colored('You have entered a invalid option','red','on_white')
        main()

main()
