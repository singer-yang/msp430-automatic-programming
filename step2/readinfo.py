'''
@Author: your name
@Date: 2019-11-29 15:08:36
@LastEditTime: 2019-11-29 15:18:26
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \msp430\readinfo.py
'''
import os
import serial.tools.list_ports
import re
import logging

path = os.getcwd()
print("current path is " + path)

ports = list(serial.tools.list_ports.comports())
useful_ports = []
for p in ports:
    # print(p)
    p = str(p)
    match = re.search('MSP Debug Interface', p)
    if match:
        port_num = re.findall(r'\d+', p)[0]
        useful_ports.append(port_num)
        filename = 'output/info_COM' + port_num +'.txt'
        # clear msp430
        os.system('MSP430Flasher.exe -n MSP430FR5969 -i COM' + port_num + ' -r [' + filename + ',INFO]')
        print('MSP430Flasher.exe -n MSP430FR5969 -i COM' + port_num + ' -r [' + filename + ',INFO]')

print('debug ports are', useful_ports)
