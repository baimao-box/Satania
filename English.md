# Satania v1.2


![在这里插入图片描述](https://img-blog.csdnimg.cn/18ab2eae3e0e4bfc86417229e147b914.png)

This is a semi-automatic penetration testing tool. The current version is mostly used for penetration testing information collection and is updated every week. The ultimate goal is to be a fully automatic penetration testing information collection tool similar to linpeas, and to detect its vulnerabilities.


# Major update
```
BUG fix
smb specifies the account to log in to the folder
Interface optimization, program optimization
Generate shellcode and connect
Added WPScan tool
```
# Install
git：
```
git clone https://github.com/baimao-box/satania.git
```
After downloading the tool, enter the directory where the tool exists to install
```
chmod 777 setup.py
python3 setup.py
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/cbc5ca0af70849148ae26e0f0b1b6ee1.png)
You need to wait a few minutes, during which you need to manually select something, the default is OK


After the installation is complete, you will be prompted whether to install the searchsploit tool. This tool is very large, so ask here, if the network is good, you can install it
![在这里插入图片描述](https://img-blog.csdnimg.cn/b69dcf649bca4ef29ad784eae002f013.png)

Then directly enter satania to run the tool

![在这里插入图片描述](https://img-blog.csdnimg.cn/c8c501407b4a4a59b1b725c7bf8bd3db.png)
# Tool module introduction
![在这里插入图片描述](https://img-blog.csdnimg.cn/045bb8d8ff8047c1bb55ecf3b96ed6a5.png)
## nmap enumeration
```
1. nmap enumeration
2. Nmap routine vulnerability scanning
3. nmap intranet live host detection
```

## Site enumeration
```
4. Website root directory file scan
5. Website subdomain enumeration
6. Website frame enumeration
7. wpscan enumeration
  1. WPScan Vulnerability Scan
  2. WPScan username enumeration
  3. WPScan account blasting
```

## smb enumeration
```
8. smb shared directory enumeration
9. Anonymous login
10. smb specified folder login
11. smb specify the user name to log in
```

## MFS enumeration
```
12. nfs scan
13. nfs local mount
```

## shellcode
```
14. msfvenom generates shellcode
	1. aspx shellcode
  2. php shellcode
  3. exe shellcode
  4. netcat monitoring
  5. Change the local ip and port of the settings
15. Connect the uploaded shellcode
```

## other
```
16. Change the target ip
17. searchsploit
18. Re-acquire the local IP
19. Exit
```

During the execution of the command, the linux command can still be run normally

![在这里插入图片描述](https://img-blog.csdnimg.cn/a8fcf0ca92044ba6be2fc4b7a6115a17.png)
# Some demos of this update
```
Updates are as follows:
BUG fix
smb specifies the account to log in to the folder
Interface optimization, program optimization
Generate shellcode and connect
Added WPScan tool
```

Use the wpscan enumeration module to perform default vulnerability scans
![在这里插入图片描述](https://img-blog.csdnimg.cn/1b214ced6f67454bb0d45d0236fce992.png)
Here you will be asked to enter the api token

![在这里插入图片描述](https://img-blog.csdnimg.cn/1e724249717f43d3a1f4e4bc43d2e6a0.png)

When we usually use wpscan, we need to enter the api token for each scan. Using this tool, you can store your api token, and then you don't need to enter it for calls.

Various scans can then be performed

We enter the msfvenom module

![在这里插入图片描述](https://img-blog.csdnimg.cn/a0993ce73652446084d1d2ed5e763890.png)

The tool will prompt you to enter the local ip and listening port for subsequent shellcode generation, now we generate a shellcode

![在这里插入图片描述](https://img-blog.csdnimg.cn/b0cb3bac013543feb78efa311ceb543d.png)

The tool will enter the file name, the address where it is stored, and the payload used

This update puts the executed linux command below

![在这里插入图片描述](https://img-blog.csdnimg.cn/f3cf08cd5dd34734b51c0d129c769707.png)
Keep updating every week

