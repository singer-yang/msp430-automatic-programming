'''
@Author: your name
@Date: 2019-11-19 14:43:08
@LastEditTime: 2019-12-10 15:43:59
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \msp430\writeinfo.py
'''
import os
import serial.tools.list_ports
import re
import logging
from function import writeid

path = os.getcwd()
print("current path is " + path)

# logger = logging.getLogger('testLogger')

## test command line programming and success
# os.system("mkdir testdir")

## read ports info
# ports = list(serial.tools.list_ports.comports())
# useful_ports=[]
# for p in ports:
#     print(p)
#     p=str(p)
#     match = re.search('MSP Debug Interface',p)
#     if match :
#         port_num=re.findall(r'\d+', p)[0]
#         useful_ports.append(port_num)

# print('debug ports are', useful_ports)

## generate corresponding command line code
ports = list(serial.tools.list_ports.comports())
useful_ports = []
IDnum = 1
for p in ports:
    # print(p)
    p = str(p)
    match = re.search('MSP Debug Interface', p)
    if match:
        port_num = re.findall(r'\d+', p)[0]
        useful_ports.append(port_num)

        writeid(port_num,IDnum)
        # # suppose lancupad num < 100
        # if (IDnum < 10):
        #     IDinfo = '0' + str(IDnum) + ' 00 00 00\n'
        # else:
        #     IDinfo = str(IDnum) + ' 00 00 00\n'

        # # a stupid method
        # with open('writeID.txt', 'r') as f1:
        #     # we can use f1.readlines(2) to read line 2
        #     flist = f1.readlines()
        #     flist[1] = IDinfo

        # newfile = 'input/writeCOM' + port_num + '.txt'
        # print(newfile)
        # with open(newfile, 'w') as f2:
        #     f2.writelines(flist)

        # # write msp430
        # os.system('MSP430Flasher.exe -n MSP430FR5969 -i COM' + port_num +
        #           ' -w ' + newfile)
        # print('MSP430Flasher.exe -n MSP430FR5969 -i COM' + port_num + ' -w ' +
        #       newfile)
        IDnum = IDnum + 1

print('debug ports are', useful_ports)

# i = 1
# command = "MSP430Flasher.exe -n MSP430FR5969 -i COM" + str(
#     i) + "-r [output" + str(i) + ".txt, INFO]"
# print(command)
