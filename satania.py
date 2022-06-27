#!/bin/python3

import time
import sys
import os
import readline
#import tab

start = 0
frequency = 0
num1 = "1"
num2 = "2"
num3 = "3"
num4 = "4"
num5 = "5"
num6 = "6"
num7 = "7"
num8 = "8"
num9 = "9"
num10 = "10"

os.system("service apache2 start")
print("-----------------------------------------------------")
print(" ____        _              _       ")
print("/ ___|  __ _| |_ __ _ _ __ (_) __ _ ")
print("\___ \ / _` | __/ _` | '_ \| |/ _` |")
print(" ___) | (_| | || (_| | | | | | (_| |")
print("|____/ \__,_|\__\__,_|_| |_|_|\__,_|    v1.0")
print("")
print("-----------------------------------------------------")
time.sleep(0.6)

try:
	rhost = input("\033[1;31;40mTarget ip >\033[0m ")
	nmapscan = "nmap -sS -sV -T4 -p- -oN scan.txt " + rhost
	os.system(nmapscan)
except:
	print("\nPlease enter the IP address")

while start == frequency:
	print("")
	#print("-----------------------------------------------------")
	print("\033[1;31;40mTarget IP: \033[0m" + rhost)
	print("")
	print("########## Website Enumeration ##########")
	print("1.Website Directory Enumeration")
	print("2.Website Subdomain Name Enumeration")
	print("3.Website Framework Enumeration")
	print("")
	print("########## SMB Enumeration ##########")
	print("4.SMB Shared File Probe")
	print("5.SMB Anonymous Login")
	print("")
	print("########## NFS Enumeration ##########")
	print("6.NFS Scan")
	print("7.NFS File Mount")
	print("")
	print("########## Other ##########")
	print("8.Change Target IP")
	print("9.Searchsploit")
	print("10.Exit")
	print("")
	
	number = input("\033[1;31;40mpleas Enter the option >\033[0m ")
	
	if number in (num1,num2,num3,num4,num5,num6,num7,num8,num9,num10):
		if(number == num1):
			os.system("ffuf -w /usr/share/seclists/Discovery/Web-Content/raft-small-directories.txt -t 100 -mc 200,302,301 -u http://{}/FUZZ".format(rhost))
		
		elif(number == num2):
			os.system("wfuzz -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt --sc 200 -u http://{}/ -c -H 'Host:FUZZ.url' --hw 26".format(rhost))
		
		elif(number == num3):
			os.system("nuclei -u http://{}".format(rhost))
		
		elif(number == num8):
			print("")
			rhost = input("\033[1;31;40mTarget IP >\033[0m ")
		
		elif(number == num9):
			start2 = 0
			frequency2 = 0
			stri = "back"
			while start2 == frequency2:
				try:
					print("")
					searchsploit = input("\033[1;31;40mSearchsploit > \033[0m")
					if(stri != searchsploit):
						os.system("searchsploit " + searchsploit)
					else:
						start2 = start2 + 1
				except:
					print("\nPlease enter `back` to return")
					
		elif(number == num4):
			os.system("nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse {}".format(rhost))
			os.system("smbclient -L //{}/".format(rhost))
			
		elif(number == num5):
			os.system("smbclient //{}/anonymous".format(rhost))
			
		elif(number == num6):
			os.system("nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount {}".format(rhost))
            
		elif(number == num7):
			start3 = 0
			frequency3 = 0
			strx = "back"
			while start3 == frequency3:
				try:
					print("")
					mount1 = input("\033[1;31;40mPlease enter the destination folder to mount > \033[0m")
					if(mount1 == strx):
						start3 = start3 + 1
					else:
						mount1 = mount1
						if(mount1 == mount1):
							print("")
							mount2 = input("\033[1;31;40mMounted local directory > \033[0m")
							if(mount2 == strx):
								start3 = start3 + 1
							else:
								mount2 = mount2
								if(mount2 == mount2):
									os.system("mount {}".format(rhost) + ":/{} ".format(mount1) + "/{}".format(mount2))
				except:
					print("\nPlease enter `back` to return")
		
		elif(number == num10):
			print("")
			print("Bye")
			start = start + 1 
			
	else:
		os.system(number)

