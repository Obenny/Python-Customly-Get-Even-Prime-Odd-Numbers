#!/usr/bin/python

# Copyright (c) Isaac Obenson "(eT. A. M)".
# See LICENSE for details.


import os #for operating system dependent functionality


#uninstalling playsound to play .mp3 notifications.
print("\n\nUninstalling playsound:\n\n")
os.system("pip uninstall playsound")

#updating system
print("\n\nUpdating system:\n\n")
os.system("sudo apt-get update")

#uninstallation complete
print("\n\nUninstallations completed!\n\n")
