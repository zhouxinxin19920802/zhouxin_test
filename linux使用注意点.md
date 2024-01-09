# **切记，切记！！！**

1.**系统可以正常用，正常工作时，千万不要手贱去更新显卡驱动，网卡驱动等，否则就可能不会用**



2.2023年12月17日10:23:00，故障经历

  更新显卡驱动后，无法连接wifi

  根据csdn的解决办法: 更新驱动后，系统自动升级内核，但是相关的依赖又没有完整安装。进入ubuntu advance后选择低版本进入。

执行

```shell
uname -a 查看内核版本

dpkg --get-slections | grep linux
```

比较不同版本的，安装新版本对应的包

3. ubuntu显卡安装教程
```
 a. 禁用系统默认显卡驱动
    sudo gedit /etc/modprobe.d/blacklist.conf
    文件末尾加入
    blacklist nouveau
    options nouveau modeset=0
    更新
    sudo update-initramfs -u
    电脑重启，输入下列指令进行确认，若无输出，则禁用成功：
    lsmod | grep nouveau

 b. 进入纯命令行模式
    ctrl+alt+F1

 c. 卸载所有显卡nvida
    sudo apt-get --purge remove nvidia*
    sudo apt autoremove
 d. 关闭所有gpu教程
    sudo systemctl isolate multi-user.target
 e. 在nvidia官网下载启动
    chmod u+x NVIDIA-Linux-x86_64-535.146.02.run
    ./chmod u+x NVIDIA-Linux-x86_64-535.146.02.run
  ```
    1.The distribution-provided pre-install script failed! Are you sure you want to continue? 

    “Yes”

    2.Would you like to register the kernel module souces with DKMS? This will allow DKMS to automatically build a new module, if you install a different kernel later?

    “No”

    3.Nvidia’s 32-bit compatibility libraries?

    “No”

    4.Would you like to run the nvidia-xconfigutility to automatically update your x configuration so that the NVIDIA x driver will be used when you restart x? Any pre-  existing x confile will be backed up. 

    “Yes”
  ```
 f. 挂载NVIDIA驱动
    modprobe nvidia
 g. 测试,回到图形界面
    sudo nvidia-smi
    sudo reboot now 
```
