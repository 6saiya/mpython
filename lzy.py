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

    # strinfo = re.compile('?')       # bug
    # s = strinfo.sub('%3F',s)

    # strinfo = re.compile('\\')      # bug 
    # s = strinfo.sub('%5C',s)

    # strinfo = re.compile('+')     # bug
    # s = strinfo.sub('%2B',s)

    # strinfo = re.compile('(') # bug
    # s = strinfo.sub('%28',s)

    # strinfo = re.compile(')') # bug  
    # s = strinfo.sub('%29',s)
    

    print(s)
    print('Finish os & re test')
    import network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("Timerry", "2018Bunny")
    # sta_if.connect(ssid, password)
    if sta_if.isconnected() :
        print('====== Connect Success ====== ')
        import urequests
        s = 'http://192.168.1.120:3000/getfs?id=fsdbhgrwh5&title=test&msg='+s
        response = urequests.get(s)
        if(response.text == 'test') :
            print('====== Upload Success ====== ')
    return



# test 
# import lzy
# connect("Timerry", "2018Bunny")

# test.py        
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

