# power by lzy
from machine import Pin, I2C, ADC, PWM
import ssd1306
i2c = I2C(scl = Pin(22), sda = Pin(23), freq = 100000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def push(ssid,password):
    import os
    import re
    import network
    import urequests
    import time
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    time.sleep(1)
    uuid = sta_if.uuid()
    sta_if.connect(ssid, password)
    time.sleep(1)
    
    libfiles = ['main.py','boot.py','libs.py','ssd1306.py']
    if sta_if.isconnected() :
        print('====== Connect Success ====== ')
        l = os.listdir(os.getcwd())
        for fn in l:
            if fn in libfiles:
                continue
            else:
                f = open(fn, 'r')
                r = f.read()
                f.close()

                strinfo = re.compile('%')    
                s = strinfo.sub('%25',r)
                strinfo = re.compile(' ')
                s = strinfo.sub('%20',s)
                strinfo = re.compile('"')      
                s = strinfo.sub('%22',s)
                strinfo = re.compile('#')   
                s = strinfo.sub('%23',s)
                strinfo = re.compile('&')    
                s = strinfo.sub('%26',s)
                strinfo = re.compile('|')       
                s = strinfo.sub('%7C',s)
                strinfo = re.compile(',')       
                s = strinfo.sub('%2C',s)
                strinfo = re.compile('/')       
                s = strinfo.sub('%2F',s)
                strinfo = re.compile(':')       
                s = strinfo.sub('%3A',s)
                strinfo = re.compile(';')       
                s = strinfo.sub('%3B',s)
                strinfo = re.compile('<')      
                s = strinfo.sub('%3C',s)
                strinfo = re.compile('=')      
                s = strinfo.sub('%3D',s)
                strinfo = re.compile('>')      
                s = strinfo.sub('%3E',s)
                strinfo = re.compile('@')
                s = strinfo.sub('%40',s)
                strinfo = re.compile('\n')
                s = strinfo.sub('%0A',s)
                strinfo = re.compile('\+')     
                s = strinfo.sub('%2B',s)
                strinfo = re.compile('\(') 
                s = strinfo.sub('%28',s)
                strinfo = re.compile('\)')  
                s = strinfo.sub('%29',s)
                strinfo = re.compile('\?')       
                s = strinfo.sub('%3F',s)
                # strinfo = re.compile('\\')      # bug 
                # s = strinfo.sub('%5C',s)
                url = 'https://umpwqw-3000-lwdnuw.dev.ide.live/getfs?id='+uuid+'&title='+fn+'&msg='+s
                response = urequests.get(url)
                time.sleep(1)
                if(response.text == 'test') :
                    oled.clear()
                    oled.text(fn+' Upload ',10,10)
                    oled.show()
                    print('====== '+fn+' Upload ====== ')
                else :
                    print('====== '+fn+' Upload Error ====== ')
                    oled.clear()
                    oled.text(fn+' Upload Error',0,10)
                    oled.show()
    else :
        print('====== Connect Error ====== ')
        oled.clear()
        oled.text('Connect Error',10,10)
        oled.show()
    pass

def pull(ssid,password,filename):
    import os
    import re
    import network
    import urequests
    import time
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    time.sleep(1)
    uuid = sta_if.uuid()
    sta_if.connect(ssid, password)
    time.sleep(1)
    
    if sta_if.isconnected() :
        print('====== Connect Success ====== ')
        url = 'https://umpwqw-3000-apjyis.dev.ide.live/pullfs?id='+uuid+'&title='+filename
        response = urequests.get(url)
        l = os.listdir(os.getcwd())
        f = open(filename, 'w')
        f.write(response.text)
        f.close()
    else :
        print('====== Connect Error ====== ')
        oled.clear()
        oled.text('Connect Error',10,10)
        oled.show()
    pass

# test 
# import libs
# push(‘Timerry‘, ‘2018Bunny‘)