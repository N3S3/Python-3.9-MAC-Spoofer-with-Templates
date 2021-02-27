#!/usr/bin/env python
# My first script. Inspired by Zaid Sabih - Ethical Hacker, Computer Scientist and CEO of zSecurity - .
# MAC.py version 0.9

import subprocess
import optparse
import shlex

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest = "interface", help = " Interface to change its MAC (e.g. eth0, wlan0, tun0, etc.) ")
parser.add_option("-m", "--mac", dest = "mac_address", help = """ The new virtual MAC address in 6 hexadecimal bytes seperated by colons;
                                                                  e.g. XX:XX:XX:XX:XX:XX, (X=0-9 or A-F) --> 3C:7C:3F:A3:B2:C1 (ASUS device); 
                                                                  total random MACs are working too as long as they are UNICAST (e.g. 97:11:B7:A3:41:95);
                                                                  EVERY TIME when You do a shut down, a restart or a switch user the original hardcoded 
                                                                  MAC address should be RESTORED.""")

(options, arguments) = parser.parse_args()

interface   = options.interface
mac_address = options.mac_address
print()

print(""" This script is only for educational purpose and I am not responsible for any kind of damage.

[+] Please choose your interface. For help do a Ctrl+C and type " python3 mac.py --help " """)

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

mac_address = input('Type the 6 bytes of Your new virtual MAC seperated by colons --> ')

print()

print(" [+] Changing MAC address for " + interface + " to " + mac_address)


cmd1=shlex.split('sudo ' + 'rfkill ' + 'unblock ' + 'all')
cmd2=shlex.split('sudo ' + 'ip ' + 'link ' + 'set ' + 'dev ' + interface + ' addr ' + mac_address)
cmd3=shlex.quote(interface)

subprocess.run('ifconfig ' + cmd3 + ' down', shell=True)
subprocess.run(cmd1, shell=True)
subprocess.run(cmd2, shell=True)
subprocess.run('ifconfig ' + cmd3 + ' up', shell=True)

print()

print(subprocess.run('ip ' + 'link'))

# For troubleshooting try following commands:
# subprocess.run('sudo' + 'ifconfig' + cmd3 + 'promisc') -insert between line 76 and 77
# subprocess.run('sudo' + 'ifconfig' + cmd3 + 'hw' + 'ether' + shlex.quote(mac_address)) -as line 78
# subprocess.run('sudo' + 'service' + 'networking' + 'restart') - as line 79
