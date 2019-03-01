def connect(ssid,password,web):
    import os
    import re
    import network
    import urequests
    import time

    f = open('test.py', 'r')
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

    print('Finish os & re')
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    time.sleep(1)
    uuid = sta_if.uuid()
    sta_if.connect(ssid, password)
    time.sleep(3)
    if sta_if.isconnected() :
        print('====== Connect Success ====== ')

        url = web+'/getfs?id='+uuid+'&title=test&msg='+s
        
        response = urequests.get(url)
        if(response.text == 'test') :
            print('====== Upload Success ====== ')
        else :
            print('====== Upload Error ====== ')
    else :
        print('====== Connect Error ====== ')
    pass

# test 
# import lzy
# connect(‘Timerry‘, ‘2018Bunny‘)