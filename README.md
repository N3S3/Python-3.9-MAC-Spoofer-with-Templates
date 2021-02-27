# Python-3.9-MAC-Spoofer-with-Templates version 0.9 for linux

This program is only for educational purpose and I am not responsible for any damage.

Why to change the Media Access Control (MAC) address?

The MAC address is a unique identifier. Changing the assigned MAC address may allow the user to bypass access control lists on servers or routers, either hiding a computer on a network or allowing it to impersonate another network device. It is stored in Networkprotocolls (for example NAT) and can be used to track Your Internetactivity and your Geolocalisation via public networks. MAC spoofing is done for legitimate and illicit purposes alike.


Installation:

1. sudo apt update && sudo apt -y full-upgrade

2. You need to have root or superuser priveleges.

3. Requirements: Python => 3.9.0
                 Rfkill lists, enabling and disabling wireless devices. For killing any daemon processes. --> pip3 install or apt install rfkill
                 optional: pip3 install or apt install mac2vendors --> for later features like implementing the big MAC-list (oui.txt) from the IEEE in the script

4. git clone https://github.com/nese1110/Python-3.9-MAC-Spoofer-with-Templates.git 

5.cd ~/Downloads/ --> python3 mac.py -i or --interface (eth0, wlan0, tun0 ,etc) -m or --mac (XX:XX:XX:XX:XX:XX / X=0-9 or A-F / hexadecimal seperated by colons)
  or just python3 mac.py and You will be guided through the interface and mac section. Here You can choose 3 id bytes from a list of famous Vendors XX:XX:XX. You have to add the other 3         
  random bytes. You also can choose a complete random MAC as long it is UNICAST(11:22:33:44:55:66 wont work!)!!! 
  
  The original hardcoded MAC is EVERY TIME RESTORED when shut down, restart or switch user is executed.
  
  Ressources: 
 https://zsecurity.com ; https://docs.python.org/3/library/ ; http://manpages.ubuntu.com/manpages/bionic/man8/rfkill.8.html ; https://en.wikipedia.org/wiki/MAC_spoofing
 
