#!/bin/python3

import time
import sys
import os
import readline

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
num11 = "11"
num12 = "12"
num13 = "13"
num14 = "14"

print("-----------------------------------------------------")
print(" ____        _              _       ")
print("/ ___|  __ _| |_ __ _ _ __ (_) __ _ ")
print("\___ \ / _` | __/ _` | '_ \| |/ _` |")
print(" ___) | (_| | || (_| | | | | | (_| |")
print("|____/ \__,_|\__\__,_|_| |_|_|\__,_|    v1.1")
print("")
print("-----------------------------------------------------")
time.sleep(0.6)
start4 = 0
frequency4 = 0
back = "back"
n = "next"

while start4 == frequency4:
	try:
		print("Please enter the IP address or `next`\n")
		rhost = input("\033[1;31;40mTarget ip >\033[0m ")

	except:
		
		print("\nBye")
		print("")

	if(rhost != n):
		nmapscan = "nmap -sS -sV -T4 -p- -oN scan.txt " + rhost
		os.system(nmapscan)
		start4 = start4 + 1
		
	else:
		rhost = ""
		start4 = start4 + 1

while start == frequency:
	print("")
	#print("-----------------------------------------------------")
	print("\033[1;31;40mTarget IP: \033[0m" + rhost)
	print("")
	print("########## Nmap Enumeration ##########")
	print("1.Nmap Scan")
	print("2.Nmap Vulnerability Scan")
	print("3.Nmap Intranet Scanning")
	print("")
	print("########## Website Enumeration ##########")
	print("4.Website Directory Enumeration")
	print("5.Website Subdomain Name Enumeration")
	print("6.Website Framework Enumeration")
	print("")
	print("########## SMB Enumeration ##########")
	print("7.SMB Shared File Probe")
	print("8.SMB Anonymous Login")
	print("")
	print("########## NFS Enumeration ##########")
	print("9.NFS Scan")
	print("10.NFS File Mount")
	print("")
	print("########## Other ##########")
	print("11.Change Target IP")
	print("12.Searchsploit")
	print("13.Exit")
	print("")
	
	number = input("\033[1;31;40mPleas Enter the option >\033[0m ")
	
	if number in (num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14):
		if(number == num1):
			os.system("nmap -sS -sV -T4 -p- -oN scan.txt " + rhost)
			
		elif(number == num2):
			os.system("nmap --script=vuln " + rhost)
		
		elif(number == num3):
			start5 = 0
			frequency5 = 0
			while start5 == frequency5:
				try:
					print("")
					print("#######################################")
					print("1.192.168.0.1/24")
					print("2.192.168.1.0/24")
					print("3.172.16.0.1/16")
					print("4.Custom range")
					print("#######################################")
					print("")
					ra = input("\033[1;31;40mPleas Enter the option >\033[0m ")
					if ra in (num1,num2,num3,num4):
						if(ra == num1):
							os.system("nmap -sP 192.168.0.1/24")
						elif(ra == num2):
							os.system("nmap -sP 192.168.1.0/24")
						elif(ra == num3):
							os.system("nmap -sP 172.16.0.1/16")
						elif(ra == num4):
							start6 = 0
							frequency6 = 0
							while start6 == frequency6:
								try:	
									ra = input("\033[1;31;40mPlease enter the scanning range >\033[0m ")
									if(ra != back):
										os.system("nmap -sP" + ra)
									else:
										start6 = start6 + 1
								except:
									print("\nPlease enter `back` to return")
						elif(ra == back):
							start5 = start5 + 1
					elif(ra == back):
						start5 = start5 + 1
					else:
						os.system(ra)
				except:
					print("\nPlease enter `back` to return")
				
		elif(number == num4):
			os.system("ffuf -w /usr/share/seclists/Discovery/Web-Content/raft-small-directories.txt -t 100 -mc 200,302,301 -u http://{}/FUZZ".format(rhost))
		
		elif(number == num5):
			os.system("wfuzz -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt --sc 200 -u http://{}/ -c -H 'Host:FUZZ.url' --hw 26".format(rhost))
		
		elif(number == num6):
			os.system("nuclei -u http://{}".format(rhost))
		
		elif(number == num11):
			print("")
			rhost = input("\033[1;31;40mTarget IP >\033[0m ")
		
		elif(number == num12):
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
					
		elif(number == num7):
			os.system("nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse {}".format(rhost))
			os.system("smbclient -L //{}/".format(rhost))
			
		elif(number == num8):
			os.system("smbclient //{}/anonymous".format(rhost))
			
		elif(number == num9):
			os.system("nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount {}".format(rhost))
            
		elif(number == num10):
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
		
		elif(number == num13):
			print("")
			print("Bye")
			start = start + 1 
			
	else:
		os.system(number)

