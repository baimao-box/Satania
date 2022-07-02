#!/bin/python3

import os
import time

def mkdir():
	a = os.path.exists("/home/satania")
	if(a != True):
		os.system("mkdir /home/satania")

print("installing...")
print("Please wait a few minutes...")


try:
	os.system("chmod 777 install.sh")
	os.system("./install.sh")
	s = 1
except:
	s = 0
	
if(s == 1):
	mkdir()
	os.system("sudo mv satania.py /home/satania/satania.py")
	a = os.path.exists("/usr/bin/satania")
	if(a == True):
		os.system("sudo rm -rf /usr/bin/satania")
		os.system("sudo ln -s /home/satania/satania.py /usr/bin/satania")
	else:
		os.system("sudo ln -s /home/satania/satania.py /usr/bin/satania")
		time.sleep(0.8)
		print("\033[1;31;40mInstallation succeeded\033[0m")
		a = input("Whether to install searchsploit"+"(Y/N): " )
		if(a == "Y" or a == "y"):
			os.system("sudo git clone https://github.com/offensive-security/exploitdb.git /opt/exploitdb")
			os.system("sudo ln -sf /opt/exploitdb/searchsploit /usr/local/bin/searchsploit")
			print("\033[1;31;40mInstallation succeeded\033[0m")
		
	
	
	
	
