I2C
===============

I2C是设备之间的两线通信协议。在物理层它只需要两个信号线：SCL 和 SDA，分别是时钟和数据线。
I2C 对象关联到总线，它可以在创建时初始化，也可以稍后初始化。


示例::

    from mpython import *

    # construct an I2C bus
    i2c = I2C(scl=Pin(Pin.P19), sda=Pin(Pin.P20), freq=100000)

    i2c.readfrom(0x3a, 4)   # read 4 bytes from slave device with address 0x3a
    i2c.writeto(0x3a, '12') # write '12' to slave device with address 0x3a

    buf = bytearray(10)     # create a buffer with 10 bytes
    i2c.writeto(0x3a, buf)  # write the given buffer to the slave


有关I2C更详细的使用方法请查阅 :ref:`machine.I2C<machine.I2C>` 。


sht20温湿度模块的示例::


    from mpython import *

    i2c = I2C(scl=Pin(Pin.P19), sda=Pin(Pin.P20),freq=100000)      
                                                                                            
    def temperature():
        i2c.writeto(0x40,b'\xf3',False)
        sleep_ms(70)
        t=i2c.readfrom(0x40, 2)
        return -46.86+175.72*(t[0]*256+t[1])/65535

    def humidity():
        i2c.writeto(0x40,b'\xf5',False)
        sleep_ms(25)
        t=i2c.readfrom(0x40, 2)
        return -6+125*(t[0]*256+t[1])/65535

