创建ID有两种方法：
1. 直接读出 msp430 制造过程中的晶圆位置（这是唯一的）作为标识，通过建立一个对应表，将 ID 和 wafer number 对应起来
2. 将 ID 写入 msp430 的一段内存空间中，msp430 的 info 内存一直是空的，同时和 main 相互隔离，是一个很好的选择

run **WaferInfo.c** to read wafer info(including wafer num, x position, y position), which can be a unique ID for a MSP430FR5969 launchpad.  

run **ModifyInfoD.c** to store your data in memory space InfoD(address 0x1800, length 0x0080). You can store your data(also your own unique ID) here.  
