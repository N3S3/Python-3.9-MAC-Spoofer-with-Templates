#!/usr/bin/env python
# My first script. Inspired by Zaid Sabih - Ethical Hacker, Computer Scientist and CEO of zSecurity - .
# mac.py version 0.9 for Linux

import subprocess
import optparse
import shlex
# from mac2vendors import get_mac_vendor

# [['00:00:00', '00:00:00', 'Officially Xerox, but 0:0:0:0:0:0 is more common']]

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest = "interface", help = " Interface to change its MAC (e.g. eth0, wlan0, tun0, etc.) ")
parser.add_option("-m", "--mac", dest = "new_address", help = """ The new virtual MAC address in 6 hexadecimal bytes seperated by colons;
                                                                  e.g. XX:XX:XX:XX:XX:XX, (X=0-9 or A-F) --> 3C:7C:3F:A3:B2:C1 (ASUS device); 
                                                                  total random MACs are working too as long as they are UNICAST (e.g. 97:11:B7:A3:41:95);
                                                                  EVERY TIME when You do a shut down, a restart or a switch user the original hardcoded 
                                                                  MAC address should be RESTORED.""")
# parser.add_option("-v", "--vendor", dest = "vendor_list", help = "prints a vendor list")

(options, arguments) = parser.parse_args()

interface   = options.interface
new_address = options.new_address
# vendor_list = options.vendor_list
# vendor_list = get_mac_vendor(mac_address = "00:00:00")
# print(vendor_list)

print()

print(""" This script is only for educational purpose and I am not responsible for any kind of damage.""")

print()

print()

print(""" [+] Please choose your interface. For help do a Ctrl+C and type " python3 MAC.py --help " """)

interface = input("interface --> ")

print("""

The 3 identifier bytes of some random companies in hexadecimal.


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


[+] Choose the 3 identifier bytes from a example company above and add 3 bytes with random values in hexadecimal. All seperated by colons.
     
[+] Looking for a special company? Search on the updated database of the IEEE: http://standards-oui.ieee.org/oui/oui.txt .""")

print()
print()

new_address = input('Type the 6 bytes of Your new virtual MAC seperated by colons --> ')

print()

print(" [+] Changing MAC address for " + interface + " to " + new_address)


cmd1=shlex.split('rfkill ' + 'unblock ' + 'all')
cmd2=shlex.split('ip ' + 'link ' + 'set ' + 'dev ' + interface + ' addr ' + new_address)
cmd3=shlex.quote(interface)
cmd4=shlex.split('ip' + ' link')
cmd5=shlex.quote(new_address)


subprocess.run('ifconfig ' + cmd3 + ' down', shell=True)
subprocess.run(cmd1, shell=True)
subprocess.run(cmd2, shell=True)
subprocess.run('ifconfig ' + cmd3 + ' up', shell=True)

print()

subprocess.check_output(cmd4)
print(subprocess.check_output(cmd4))


# For troubleshooting try following commands:
# subprocess.run('sudo ' + 'ifconfig ' + cmd3 + ' promisc', shell=True)                 --insert between line 91 and 92
# subprocess.run('sudo ' + 'ifconfig ' + cmd3 + ' hw ' + 'ether ' + cmd5, shell=True)   --replace line 93
# subprocess.run('sudo ' + 'service ' + 'networking ' + 'restart', shell=True)          --replace line 94
