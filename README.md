这是Espressif ESP32微控制器的MicroPython实验端口。它使用ESP-IDF框架，MicroPython作为FreeRTOS下的任务运行。

支持的功能包括：

通过UART0进行REPL（Python提示）。
用于MicroPython任务的16k堆栈和96k Python堆。
MicroPython的许多功能都已启用：unicode，任意精度整数，单精度浮点数，复数，冻结字节码以及许多内部模块。
使用闪存的内部文件系统（目前大小为2M）。
机器模块具有GPIO，UART，SPI，软件I2C，ADC，DAC，PWM，触摸板，WDT和定时器。
具有WLAN（WiFi）支持的网络模块。
这个ESP32端口的开发部分由Microbric Pty Ltd.赞助。

设置工具链和ESP-IDF
构建固件需要两个主要组件：

Xtensa交叉编译器，它针对ESP32中的CPU（这与ESP8266使用的编译器不同）
Espressif IDF（物联网开发框架，又称SDK）
ESP-IDF变化很快，MicroPython只支持某个版本。可以通过在make没有配置的情况 下运行来找到此版本的git哈希ESPIDF。然后，您可以使用以下命令仅获取给定的esp-idf：

$ git clone https://github.com/espressif/esp-idf.git
$ git checkout <Current supported ESP-IDF commit hash>
$ git submodule update --init --recursive
可以使用以下指南安装二进制工具链（binutils，gcc等）：

Linux安装
MacOS安装
Windows安装
如果您使用的是Windows计算机，则 Windows子系统Linux 是安装ESP32工具链和构建项目的最有效方法。如果您使用WSL，请遵循 ESP-IDF 的 Linux准则而不是Windows 准则。

上面的Espressif ESP-IDF指令只为Python 2安装pyserial，所以如果你运行的是Python 3或非系统Python，你还需要安装pyserial（或esptool），以便Makefile可以刷新电路板并设置参数：

$ pip install pyserial
一旦设置好所有内容，您应该拥有一个功能正常的工具链，前缀为xtensa-esp32-elf-（或者如果您配置不同的话，则为其他）以及ESP-IDF存储库的副本。您需要更新PATH 环境变量以包含ESP32工具链。例如，您可以在（至少）Linux上发出以下命令：

$ export PATH=$PATH:$HOME/esp/crosstool-NG/builds/xtensa-esp32-elf/bin
你可以把这个命令放在你的.profile或.bash_login。

然后，您需要将ESPIDFenvironment / makefile变量设置为指向ESP-IDF存储库的根目录。您可以在PATH中设置变量，或在调用make时在命令行中设置变量，或者在您自己的自定义中设置变量makefile。建议使用最后一个选项，因为它允许您轻松配置构建的其他变量。在这种情况下，在esp32目录中创建一个新文件makefile，并将以下行添加到该文件：

ESPIDF = <path to root of esp-idf repository>
#PORT = /dev/ttyUSB0
#FLASH_MODE = qio
#FLASH_SIZE = 4MB
#CROSS_COMPILE = xtensa-esp32-elf-
#SDKCONFIG = boards/sdkconfig.spiram

include Makefile
请务必输入IDF存储库本地副本的正确路径（并使用$(HOME)而不是代字号来引用您的主目录）。如果您的文件系统不区分大小写，那么您需要使用GNUmakefile 而不是makefile。如果Xtensa交叉编译器不在您的路径中，您可以使用该 CROSS_COMPILE变量来设置其位置。其他感兴趣的选项是PORTesp32模块的串口，FLASH_MODE （可能需要dio用于某些模块）和FLASH_SIZE。有关详细信息，请参阅Makefile。

默认的ESP IDF配置设置在文件中提供 boards/sdkconfig，此文件由make变量在构建中指定SDKCONFIG。要使用在自SDKCONFIG 定义makefile（或GNUmakefile）中设置的自定义配置，或在命令行上设置此变量：

$ make SDKCONFIG = sdkconfig.myboard
该文件boards/sdkconfig.spiram是为具有外部SPIRAM的ESP32模块提供的。

构建固件
必须构建MicroPython交叉编译器以将一些内置脚本预编译为字节码。这可以通过（从此存储库的根目录）完成：

$ make -C mpy-cross
ESP32端口依赖于Berkeley DB，这是一个外部依赖（git子模块）。你需要让git使用命令初始化该模块：

$ git submodule init lib / berkeley-db-1.xx 
$ git submodule update
然后为ESP32运行构建MicroPython：

$ cd ports / esp32 
$ make
这将在build/子目录中生成二进制固件映像（其中三个：bootloader.bin，partitions.bin和application.bin）。

要刷新固件，必须将ESP32模块置于引导加载程序模式并连接到PC上的串行端口。有关如何执行此操作，请参阅特定ESP32模块的文档。串口和闪存设置在中设置Makefile，可以在本地覆盖makefile; 请参阅上文了解更多详情。

您还需要具有访问/ dev / ttyUSB0设备的用户权限。在Linux上，您可以通过将用户添加到dialout组中，然后重新启动或注销并重新启动来启用此功能。

$ sudo adduser <用户名>拨出
如果您是第一次将MicroPython安装到模块中，或者在安装任何其他固件之后，应首先完全擦除闪存：

$ make erase
要将MicroPython固件刷新到ESP32，请使用：

$ make deploy
这将使用esptool.py脚本（由ESP-IDF提供）来下载二进制图像。

获取Python提示
您可以通过串行端口通过UART0获得提示，UART0与用于编程固件的UART相同。REPL的波特率为115200，您可以使用如下命令：

$ picocom -b 115200 / dev / ttyUSB0
配置WiFi并使用主板
在模块和面向用户的API方面，ESP32端口被设计为（几乎）等同于ESP8266。存在一些小的差异，特别是ESP32在启动时不会自动连接到最后一个接入点。但在大多数情况下，ESP8266的文档和教程应该适用于ESP32（至少对于实现的组件而言）。

有关快速参考，请参见http://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html，以及http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro。 html 的教程。

以下功能可用于连接到WiFi接入点（您可以传入自己的SSID和密码，也可以更改默认设置，以便快速拨打电话wlan_connect()，它可以正常工作）：

DEF  wlan_connect（SSID = ' MYSSID '，口令= '为mypass '）：
     进口网络
    WLAN = network.WLAN（网络。STA_IF）
     如果 不 wlan.active（）或 不 wlan.isconnected（）：
        wlan.active（真）
         打印（'连接到：'，ssid）
        wlan.connect（ssid，密码）而不是 wlan.isconnected（）：
             传递
         
    print（' network config：'，wlan.ifconfig（））
请注意，某些主板要求您在使用WiFi之前配置WiFi天线。在像LoPy和WiPy 2.0这样的Pycom板上，您需要执行以下代码来选择内部天线（最好将此行放在boot.py文件中）：

进口机
天线= machine.Pin（16，machine.Pin。OUT，值= 0）
故障排除
编程后连续重新启动：确保FLASH_MODE对于您的电路板是正确的（例如ESP-WROOM-32应该是DIO）。然后执行make clean，重建，重新部署。
##mac の 坑
### download
1.git clone --recursive https://github.com/espressif/esp-idf.git
2.https://dl.espressif.com/dl/xtensa-esp32-elf-osx-1.22.0-75-gbaf03c2-5.2.0.tar.gz
3.git clone https://github.com/micropython/micropython.git
4.picocom
5.esptool.py

### PATH
vi ~/.profile
export PATH=$PATH:~/esp/xtensa-esp32-elf/bin
source ~/.profile

### Makefile
PORT ?= /dev/cu.SLAB_USBtoUART
ESPIDF = /Users/lishinian/esp/esp-idf
PYTHON2 ?= python

### GNUmakefile
ESPIDF = <path to root of esp-idf repository>
PORT = /dev/cu.SLAB_USBtoUART
`#FLASH_MODE = qio`
`#FLASH_SIZE = 4MB`
`#CROSS_COMPILE = xtensa-esp32-elf-`
`#CONFIG_SPIRAM_SUPPORT = 1`

include Makefile

### compile
make
make -f GNUmakefile

### clear
make clean
make erase

### upload
make deploy

### serialport 
picocom -b 115200 /dev/cu.SLAB_USBtoUART


# ide
micropython IDE

electron + yarn + serialPort + monacoEditor + blockly + micropython

esp32烧写固件
// 擦除
sudo esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART erase_flash
// 烧写
sudo esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART write_flash -z 0x1000 ~/Desktop/work/esp32-20180511-v1.9.4.bin
// 连接
picocom -b 115200 /dev/cu.SLAB_USBtoUART

import os
os.listdir(os.getcwd())
f = open('boot.py', 'r')
f = open('lzy.py', 'r')
r = bytes(f.read(), 'ascii')
print(r)
f.close()


os.remove()

http://www.52pi.net/archives/636

import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan()
sta_if.connect("Timerry", "2018Bunny")
sta_if.isconnected()

import urequests

response = urequests.get('http://192.168.1.120:3000/getfs?id=fsdbhgrwh5&title=main&msg=def%20calc_sum(*args)%3A%0A%20%20%20%20ax%20%3D%200%0A%20%20%20%20for%20n%20in%20args%3A%0A%20%20%20%20%20%20%20%20ax%20%3D%20ax%20%2B%20n%0A%20%20%20%20return%20ax%0A%20%20%20%20%0Adef%20lazy_sum(*args)%3A%0A%20%20%20%20def%20sum()%3A%0A%20%20%20%20%20%20%20%20ax%20%3D%200%0A%20%20%20%20%20%20%20%20for%20n%20in%20args%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ax%20%3D%20ax%20%2B%20n%0A%20%20%20%20%20%20%20%20return%20ax%0A%20%20%20%20return%20sum%0A%20%20%20%20')

print(response)