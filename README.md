# Wifi-Attack-Auto-Loader-MANA-
Easily walks you through the Mana Evil AP Attack (While eliminating common mistakes). Other features (Aircrack suite) have not yet been implemented

# Recommended Usage
Only to be used with a DISPOSABLE copy of Kali Linux. As it turns out, messing with network-manager and/or wicd could permanently break your network settings as of March 1st. 

Gnome Network-Manager won't let you run MANA because of a software conflict
And Wicd won't let you restore your Ethernet settings after remnoving network-manager >.>

I tried this ALOT. Came to the conclusion that the best way is to use this on a minimalist Kali Install that is specifically meant to perform Evil AP Attacks. In other words, a Kali install that only has the Wireless Attack Tools installed.

Recommended Disposable Kali Installs:
1. Kali VM Image
2. Kali Live Persistent USB

# Installation, Prerequisites
Requires Python 2.7.13, Python-Pip, and Termcolor Python Module, If you do not have this, run the dependencyInstall.sh script
Terminal Commands:
"cd to the directory with unzipped files"
"sudo chmod 777 dependencyInstall.sh"
"./dependencyInstall.sh"

# Installation, Main Program
Terminal Commands:
"cd to unzipped directory"
"sudo chmod 777 autoInstaller.sh"
"./autoInstaller.sh"
At this point you can run it with a terminal command

# Running Wifi Autoloader
Terminal Command:
"WifiAttackAutoloader.py" # You can just [TAB] complete it in terminal

# First Time Setup
Install the prerequisites for Mana toolkit, including Wicd, and also for the installer to remove and purge network-manager
From the Main Menu
Press #1 [Enter]
Type "INSTALL" [Enter]
Follow the directions

# First Time Usage
Follow the prompt closely.
Do NOT do anything unless the program tells you do (like when to insert your external network card). 
