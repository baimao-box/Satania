# Satania v1.2

![fanart3](https://user-images.githubusercontent.com/52622597/176340163-16b62ac6-aa48-4fa0-b8a3-2bb31f155cf1.png)


这是一款半自动渗透测试的工具，当前版本多用于渗透测试的信息搜集，每周保持更新，最终的目标是类似于linpeas的全自动渗透测试信息搜集工具，并探测其存在哪些漏洞

## 安装

```
chmod 777 setup.py
./setup.py
```
## 使用

直接运行satania即可

![image](https://user-images.githubusercontent.com/52622597/177001004-f5121c63-89bd-41a9-9cf8-994a9de974ac.png)


可以直接输入next进入模块选择界面，或者输入目标ip后，工具将自动扫描目标主机开放的服务和端口

之后会提供信息收集模块选项

![image](https://user-images.githubusercontent.com/52622597/177001336-8e905fe8-41c3-49b3-b16b-a2b3405e48ef.png)

## nmap枚举
```
1.nmap枚举
2.nmap常规漏洞扫描
3.nmap内网存活主机探测
```

## 网站枚举
```
4.网站根目录文件扫描
5.网站子域名枚举
6.网站框架枚举
7.wpscan枚举
```

## smb枚举
```
8.smb共享目录枚举
9.匿名登录
10.smb指定文件夹登录
11.smb指定用户名登录
```

## MFS枚举
```
12.nfs扫描
13.nfs本地挂载
```

## shellcode
```
14.msfvenom生成shellcode
15.连接上传的shellcode
```

## 其他
```
16.更改目标ip
17.searchsploit
18.重新获取本机IP
19.退出
```

在执行命令期间，还是可以正常运行linux命令

![image](https://user-images.githubusercontent.com/52622597/177001668-b60fecb1-6a37-4942-9f8a-db8d57862082.png)

详细介绍文章地址：
```
https://blog.csdn.net/qq_45894840/article/details/125578975?spm=1001.2014.3001.5502
```
