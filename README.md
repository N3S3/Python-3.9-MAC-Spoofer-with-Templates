# Python-3.9-MAC-Spoofer-with-Templates version 0.9.1A for Linux


 _______  _______  _______         _______  _______  _______  _______  _______   
(       )(  ___  )(  ____ \       (  ____ \(  ____ )(  ___  )(  ___  )(  ____ \
| () () || (   ) || (    \/       | (    \/| (    )|| (   ) || (   ) || (    \/
| || || || (___) || |       _____ | (_____ | (____)|| |   | || |   | || (__    
| |(_)| ||  ___  || |      (_____)(_____  )|  _____)| |   | || |   | ||  __)   
| |   | || (   ) || |                   ) || (      | |   | || |   | || (         
| )   ( || )   ( || (____/\       /\____) || )      | (___) || (___) || )      
|/     \||/     \|(_______/       \_______)|/       (_______)(_______)|/  


This program is only for educational and research purposes and I am not responsible for any damage.

Why to change the Media Access Control (MAC) address?

The MAC address is a unique identifier. Changing the assigned MAC address may allow the user to bypass access control lists on servers or routers, either hiding a computer on a network or allowing it to impersonate another network device. It is stored in Networkprotocolls (for example NAT) because of that it can be used to track Your Internetactivity and your Geolocalisation via public networks. MAC spoofing is done for legitimate and illicit purposes alike.


Installation:


Commands marked with * [] *, like * [COMMAND] * --> type: COMMAND into the console.

1. * [sudo apt update && sudo apt full-upgrade] *

2. You need to have root or superuser priveleges.--> * [sudo su] *

3. Requirements: Python => 3.9.0
                 Rfkill lists, enabling and disabling wireless devices. For killing any daemon processes. --> * [pip3 install] * or * [apt install] * + * [rfkill] *
                 optional: * [pip3 install] * or * [apt install] * + * [mac2vendors] * --> for later features like implementing a vendor lookup in the script

4. * [git clone https://github.com/nese1110/Python-3.9-MAC-Spoofer-with-Templates.git] *

5. * [cd ~/Downloads/] * --> * [python3 mac.py]. Do * [python3 mac.py] * + * [-i] * or * [--interface] * followed by [eth0] or [wlan0] or [tun0] ,[etc]) and * [-m] * or * [--mac]        
   followed by the 12 digits seperaded into equal 6 bytes by colon --> (XX:XX:XX:XX:XX:XX / X=0-9 or A-F / hexadecimal seperated by colons), when You used to the program.
   * [python3 mac.py] will guid through the interface and mac options. Here You can choose 3 id bytes from a list of all Vendors XX:XX:XX. You have to add the other 3         
   random bytes. You can also choose a complete random MAC as long it is UNICAST(11:22:33:44:55:66 wont work!)!!! 
  
  The original hardcoded MAC address is EVERY TIME RESTORED when a shut down, a restart or a switch user is executed. If You have trouble with Your internet connection because of the   
  program, just log out and log in or better try first a * [sudo ifconfig (submit your interface here) up] *. This should solve the problem.
  
  Ressources: 
 https://zsecurity.com ; https://devops.datenkollektiv.de/banner.txt/index.html ; https://docs.python.org/3/library/ ; http://manpages.ubuntu.com/manpages/bionic/man8/rfkill.8.html ;     
 https://www.programcreek.com/python/?CodeExample=print+banner ; https://stackoverflow.com/questions/ ; https://en.wikipedia.org/wiki/ ; 
 
