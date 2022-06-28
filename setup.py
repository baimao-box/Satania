#!/bin/python3

import os
import time

print("installing...")
print("Please wait a few minutes...")
time.sleep(0.8)

try:
	os.system("sudo apt-get install python3-pip")
	os.system("sudo pip3 install readline")
	os.system("sudo apt install nmap")
	os.system("sudo apt install ffuf")
	os.system("sudo apt install wfuzz")
	os.system("sudo apt install nuclei")
	os.system("sudo apt install seclists")
	os.system("sudo apt install smbclient")
	os.system("sudo apt install mount")
	s = 1
except:
	s = 0
	
if(s == 1):
	start = 0
	frequency = 0
	while start == frequency:
		os.system("sudo mv satania.py /home/satania.py")
		os.system("sudo ln -s /home/satania.py /usr/bin/satania")
		time.sleep(0.8)
		print("\033[1;31;40mInstallation succeeded\033[0m")
		a = input("Whether to install searchsploit"+"(Y/N): " )
		if(a == "y"):
			os.system("sudo git clone https://github.com/offensive-security/exploitdb.git /opt/exploitdb")
			os.system("sudo ln -sf /opt/exploitdb/searchsploit /usr/local/bin/searchsploit")
			print("\033[1;31;40mInstallation succeeded\033[0m")
		else:
			start = start + 1
	
	