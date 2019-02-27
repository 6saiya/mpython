def connect(ssid,password):
    import os
    import re

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
   
    # print(s)
    import network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    uuid = sta_if.uuid()
    # sta_if.connect(ssid, password)
    sta_if.connect("Timerry", "2018Bunny")
    sta_if.isconnected()
    import urequests
    url = 'http://192.168.1.120:3000/getfs?id='+uuid+'&title=test&msg='+s
    url = 'http://192.168.1.120:3000/getfs?id=liuzhenya6&title=test&msg=def%20my_abs(x)%3A%0A%20%20%20%20if%20x%20%3E%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20x%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20-x'
    print(url)
    response = urequests.get(url)
    print(response.text)

    pass