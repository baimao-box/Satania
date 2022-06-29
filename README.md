# Satania v1.1

![fanart3](https://user-images.githubusercontent.com/52622597/176340163-16b62ac6-aa48-4fa0-b8a3-2bb31f155cf1.png)


这是一款半自动渗透测试的工具，当前版本多用于渗透测试的信息搜集，每周保持更新，最终的目标是类似于linpeas的全自动渗透测试信息搜集工具，并探测其存在哪些漏洞

## 安装

```
chmod 777 setup.py
python3 setup.py
```
## 使用

直接运行satania即可

![image](https://user-images.githubusercontent.com/52622597/176213179-35fbd93b-cd87-4101-8425-15cbb430c969.png)

可以直接输入next进入模块选择界面，或者输入目标ip后，工具将自动扫描目标主机开放的服务和端口

![image](https://user-images.githubusercontent.com/52622597/176213350-07936fbd-ca0a-4a72-8393-4f784a6cd18b.png)


扫描完成后会提供信息收集模块选项

![image](https://user-images.githubusercontent.com/52622597/176213468-7f77df5e-a77a-4230-9219-8dc358a41ea5.png)

模块的功能如下：

```
1.nmap枚举
2.nmap常规漏洞探测
3.内网存活主机探测
4.网站根目录枚举
5.网站子域名枚举
6.网站中间件漏洞探测
7.smb枚举
8.匿名登录smb
9.nfs枚举
10.本地挂载nfs
11.更改目标ip地址
12.Searchsploit
13.退出
```
在工具的使用期间，还是可以执行正常的linux命令

![4](https://user-images.githubusercontent.com/52622597/175947512-342c2a03-e54c-4d9d-99c4-b8b3c453053e.png)
