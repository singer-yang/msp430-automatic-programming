'''
@Author: your name
@Date: 2019-11-29 15:08:36
@LastEditTime: 2019-12-10 21:51:59
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

with open('./output/port_com.txt', 'w') as f1:
    f1.write('port id\n')

ports = list(serial.tools.list_ports.comports())
useful_ports = []
for p in ports:
    # print(p)
    p = str(p)
    match = re.search('MSP Debug Interface', p)
    if match:
        # get port number
        port_num = re.findall(r'\d+', p)[0]
        useful_ports.append(port_num)

        # output ID info
        filename = 'output/info_COM' + port_num + '.txt'
        os.system('MSP430Flasher.exe -n MSP430FR5969 -i COM' + port_num +
                  ' -r [' + filename + ',INFO] -e NO_ERASE -q')
        # print('MSP430Flasher.exe -n MSP430FR5969 -i COM' + port_num + ' -r [' +
        #       filename + ',INFO]')

        # get ID info
        with open(filename, 'r') as f:
            IDinfo = f.readlines()[1]
            if (IDinfo[0] == 'F'):
                IDnum = 0
            else:
                IDnum = int(IDinfo[1]) + 10 * int(IDinfo[0]) + 100 * int(
                    IDinfo[4]) + 1000 * int(IDinfo[3])

        with open('./output/port_com.txt', 'a') as ff:
            ff.write(str(port_num) + ' ' + str(IDnum) + '\n')

print(useful_ports)