import pcd8544
from machine import Pin, SPI

spi=SPI(baudrate=100000, polarity=1, phase=0, sck=Pin(14),mosi=Pin(12),miso=Pin(0)) #miso is not used
#spi.init(baudrate=8000000, polarity=0, phase=0)
cs = Pin(32)
dc = Pin(33)
rst = Pin(25)
lcd = pcd8544.PCD8544(spi, cs, dc, rst)
lcd.clear()
lcd.print("HELLO,world.")
lcd.clear()
lcd.lcd_write_chinese('2018m03m29',0,0)
lcd.lcd_write_chinese('x',15,10)
lcd.lcd_write_chinese('y',35,10)
lcd.clear()
lcd.lcd_write_chinese1('2018m03m29',75,20)
lcd.lcd_write_chinese1('x',57,10)
lcd.lcd_write_chinese1('y',35,10)
