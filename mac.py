#!/usr/bin/env python

import subprocess
import optparse
import shlex
import urllib.parse
import urllib.request
import fileinput
import time
import os
import sys
from termcolor import colored, cprint
import pydoc
from subprocess import Popen, PIPE


# from mac2vendors import get_mac_vendor
# [['00:00:00', '00:00:00', 'Officially Xerox, but 0:0:0:0:0:0 is more common']]

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface",help=" Interface to change its MAC (e.g. eth0, wlan0, tun0, etc.) ")
parser.add_option("-m", "--mac", dest="new_address", help=""" The new virtual MAC address in 6 hexadecimal bytes seperated by colons;
                                                                  e.g. XX:XX:XX:XX:XX:XX, (X=0-9 or A-F) --> 3C:7C:3F:A3:B2:C1 (ASUS device);
                                                                  total random MAC addresses are working too as long as they are UNICAST (e.g. 97:11:B7:A3:41:95);
                                                                  EVERY TIME when You do a shut down, a restart or a switch user the original hardcoded
                                                                  MAC address is being RESTORED.--> If You have trouble with Your internet connection
                                                                  because of the script, just log out and log in or do a ifconfig [interface] up.
                                                                  Everything should be working as usual again. """)
# parser.add_option("-v", "--vendor", dest="vendor_list, help="Vendor lookup")

(options, arguments) = parser.parse_args()

interface = options.interface
new_address = options.new_address
# vendor_list = options.vendor_list
# vendor_list = get_mac_vendor(mac_address = input("please enter the 1st 6 digits of the MAC address [colon seperated] --> ")
# print(vendor_list)

print()

cprint("!!! This script is only for educational and research purposes. I am not responsible for any kind of damage !!!", 'red', 'on_white', attrs = ['blink', 'bold'])

print()
print()

stopp = shlex.shlex(input("Please press Enter to confirm the aspects above and to continue."))


print()

cprint ("""
 _______  _______  _______         _______  _______  _______  _______  _______   
(       )(  ___  )(  ____ l       (  ____ l(  ____ )(  ___  )(  ___  )(  ____ l
| () () || (   ) || (    l/       | (    l/| (    )|| (   ) || (   ) || (    l/
| || || || (___) || |       _____ | (_____ | (____)|| |   | || |   | || (__    
| |(_)| ||  ___  || |      (_____)(_____  )|  _____)| |   | || |   | ||  __)   
| |   | || (   ) || |                   ) || (      | |   | || |   | || (         
| )   ( || )   ( || (____/l       /l____) || )      | (___) || (___) || )      
|/     l||/     l|(_______/       l_______)|/       (_______)(_______)|/""", 'red', 'on_grey', ['bold'])
print()
cprint("Version 0.9.1", 'red', 'on_grey')
print()
cprint("written by Sebastian Nestler aka _N3S3_", 'red', 'on_grey', ['bold'])
print()
time.sleep(3)
# https://devops.datenkollektiv.de/banner.txt/index.html
# https://www.programcreek.com/python/?CodeExample=print+banner

print()

# print("Please make sure that the file - oui.txt - is in the same the path like the file - mac.py - .")

print()

# vendor_list = open("oui.txt", "rt")
# print(vendor_list, sep = "\n")

print()

print(""" [+] Please choose your interface. For help do a Ctrl+c and type " python3 mac.py --help " """)

interface = input("interface --> ")

print()
# data = urllib.parse.urlencode()
# data = data.encode('ascii')
url  = "http://standards-oui.ieee.org/oui/oui.txt"
req  = urllib.request.urlopen(url)
print(""" [+] Loading the large updated MAC address database from the Institute of Electrical and Electronics Engineers (IEEE). 
              No fear, its just a huge .txt!""")
time.sleep(4)
string=req.read().decode()

pydoc.pager(string)
print()
print()

print("""
The 3 identifier bytes of some famous random companies in hexadecimal.
54:77:8A        Hewlett Packard Enterprise
24:71:52        DELL Inc.
3C:7C:3F        ASUSTek COMPUTER Inc.
FC:44:9F        ZTE Corporation
CC:D2:81        Apple Inc.
F0:1D:2D        Cisco Systems Inc.
4C:02:02        Xiaomi Communications Co. LTD
9C:B2:E8        HUAWEI TECHNOLOGIES Co. LTD
A4:E3:1B        Nokia 
F4:D9:FB        Samsung Electronics Co. LTD
70:BC:10        Microsoft Corporation
[+] Please scroll up and choose the 3 identifier bytes - 1st 6 digits XX:XX:XX - from a company above and 
    add another 3 bytes - 2nd 6 digits XX:XX:XX - with random values in hexadecimal [X=0-9 or A-F]. All seperated by colons. 
    You have to substitute the dash (-) with a colon (:) of the hex bytes from the IEEE list. Enter the MAC like this: 70:BC:10:A3:B2:C1. """)

print()
print()

new_address = input(
    'Type the 6 bytes (12 digits) of Your new virtual MAC address seperated by colons --> ')

print()

print(f" [+] Changing MAC address for {interface} to {new_address}")

sp = Popen(cmd , shell=True, stdin=PIPE)
out, err = sp.communicate(_user_pass+'\n')   


cmd1 = shlex.split("rfkill unblock all")
cmd2 = shlex.split(f"ifconfig {interface} hw ether {new_address}")
cmd3 = shlex.quote(interface)
cmd4 = shlex.split("ip link")
cmd5 = shlex.quote(new_address)


subprocess.run(f"ifconfig {cmd3} down", shell = True)  # line 1
subprocess.run(cmd1, shell = True)                          # line 2
subprocess.run(cmd2, shell = True)                          # line 3
subprocess.run(f"ifconfig {cmd3} up", shell = True)    # line 4

print()

subprocess.check_output(cmd4)
print(subprocess.check_output(cmd4))


# For troubleshooting try following commands with and without sudo:                                   --UNICAST Test MAC: A3:56:94:B1:F8:00 for copy and paste
# subprocess.run('sudo ' + 'ifconfig ' + cmd3 + ' promisc', shell=True)                               --insert between # line 1 and # line 2 !!!Attention the device will capture all packets in the network!!!
# subprocess.run('sudo ' + 'ip ' + 'link ' + 'set ' + 'dev 'cmd3 + ' address ' + cmd5, shell=True)    --replace # line 3
# subprocess.run('sudo ' + 'service ' + 'networking ' + 'restart', shell=True)                        --replace # line 4
