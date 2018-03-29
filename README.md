# esp32-micropython-pcd8544
=============================
A modified repository of https://github.com/mcauser/micropython-pcd8544
<br>
Add font.py to display ascii characters,originated from http://www.cnblogs.com/xiaowuyi/p/6347336.html
<br>
Add chinese.py to display several chinese characters created with zimo221.exe.
<br>
Add chinese1.py to display inversed chinese characters also created with zimo221.exe.
<br>
Simple test with changing pcd8544_test.py to main.py and uploading it to esp32 with uPyLoader.
<br>
Connections of esp32 and pcd8544 (nokia 5110):
<br>
VCC <--> 3.3 V
<br>
GND <--> GND
<br>
CLK <--> D14
<br>
DIN <--> D12
<br>
DC  <--> D33 
<br>
CE  <--> D32
<br>
RST <--> D25
<br>
