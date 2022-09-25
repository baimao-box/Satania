# Satania v1.2
### [English](https://github.com/baimao-box/satania/blob/main/English.md)

![在这里插入图片描述](https://img-blog.csdnimg.cn/18ab2eae3e0e4bfc86417229e147b914.png)


这是一款半自动渗透测试的工具，当前版本多用于渗透测试的信息搜集，每周保持更新，最终的目标是类似于linpeas的全自动渗透测试信息搜集工具，并探测其存在哪些漏洞

# 主要更新
```
BUG修复
smb指定账号于文件夹登录
界面优化，程序优化
生成shellcode并连接
加入了WPScan工具
```
# 安装
git库：
```
git clone https://github.com/baimao-box/satania.git
```
下载完工具后，进入工具存在的目录安装
```
chmod 777 setup.py
python3 setup.py
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/cbc5ca0af70849148ae26e0f0b1b6ee1.png)
需要等待几分钟，期间需要手动选择一些东西，默认即可

安装完成后，会提示是否安装searchsploit工具，这个工具很大，所以在这里询问，网络好的话可以安装

![在这里插入图片描述](https://img-blog.csdnimg.cn/b69dcf649bca4ef29ad784eae002f013.png)

之后直接输入satania即可运行工具

![在这里插入图片描述](https://img-blog.csdnimg.cn/c8c501407b4a4a59b1b725c7bf8bd3db.png)
# 工具模块介绍
![在这里插入图片描述](https://img-blog.csdnimg.cn/045bb8d8ff8047c1bb55ecf3b96ed6a5.png)
## nmap枚举
```
1. nmap枚举
2. nmap常规漏洞扫描
3. nmap内网存活主机探测
```

## 网站枚举
```
4. 网站根目录文件扫描
5. 网站子域名枚举
6. 网站框架枚举
7. wpscan枚举
	1. WPScan漏洞扫描
	2. WPScan用户名枚举
	3. WPScan账号爆破
```

## smb枚举
```
8. smb共享目录枚举
9. 匿名登录
10. smb指定文件夹登录
11. smb指定用户名登录
```

## MFS枚举
```
12. nfs扫描
13. nfs本地挂载
```

## shellcode
```
14. msfvenom生成shellcode
	1. aspx的shellcode
	2. php的shellcode
	3. exe的shellcode
	4. netcat监听
	5. 更改设置的本地ip和端口
15. 连接上传的shellcode
```

## 其他
```
16. 更改目标ip
17. searchsploit
18. 重新获取本机IP
19. 退出
```

在执行命令期间，还是可以正常运行linux命令

![在这里插入图片描述](https://img-blog.csdnimg.cn/a8fcf0ca92044ba6be2fc4b7a6115a17.png)
# 本次更新的一些演示
```
更新如下：
BUG修复
smb指定账号于文件夹登录
界面优化，程序优化
生成shellcode并连接
加入了WPScan工具
```
使用wpscan枚举模块，执行默认漏洞扫描

![在这里插入图片描述](https://img-blog.csdnimg.cn/1b214ced6f67454bb0d45d0236fce992.png)
这里会叫你输入api token

![在这里插入图片描述](https://img-blog.csdnimg.cn/1e724249717f43d3a1f4e4bc43d2e6a0.png)

我们平常在使用wpscan时，每次扫描都需要输入api token，使用这个工具，可以将你的api token存储下来，之后调用就不需要输入

之后就能执行各种扫描

我们进入msfvenom模块

![在这里插入图片描述](https://img-blog.csdnimg.cn/a0993ce73652446084d1d2ed5e763890.png)

工具会提示你输入本地ip和监听端口，用于之后的shellcode生成，现在我们生成一个shellcode

![在这里插入图片描述](https://img-blog.csdnimg.cn/b0cb3bac013543feb78efa311ceb543d.png)

工具会输入文件名，存放的地址，以及使用的payload

本次更新将执行的linux命令放在了下方

![在这里插入图片描述](https://img-blog.csdnimg.cn/f3cf08cd5dd34734b51c0d129c769707.png)

每周保持更新中
