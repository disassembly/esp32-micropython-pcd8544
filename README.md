# esp32-micropython-pcd8544
A modified repository of https://github.com/mcauser/micropython-pcd8544
Add font.py to display ascii characters,originated from http://www.cnblogs.com/xiaowuyi/p/6347336.html
Add chinese.py to display several chinese characters created with zimo221.exe.
Add chinese1.py to display inversed chinese characters also created with zimo221.exe.
Simple test with changing pcd8544_test.py to main.py and uploading it to esp32 with uPyLoader.
Connections of esp32 and pcd8544 (nokia 5110):
VCC <--> 3.3 V
GND <--> GND
CLK <--> D14
DIN <--> D12
DC  <--> D33 
CE  <--> D32
RST <--> D25
