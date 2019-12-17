'''
@Author: your name
@Date: 2019-12-10 21:46:43
@LastEditTime: 2019-12-17 21:27:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \msp430\function.py
'''
import os
import numpy as np
import re


# 找出ID对应的端口
def id2port(id, first=None):
    if first is True:
        os.system('python readinfo.py')

    with open('./output/port_com.txt', 'r') as f:
        tempporttable = f.readlines()[1:]
    porttable = []
    for fileline in tempporttable:
        porttable.append(list(map(int, re.findall(r'\d+', str(fileline)))))
    porttable = np.array(porttable).reshape(-1, 2)
    for i in range(porttable.shape[0]):
        if porttable[i][1] == id:
            return porttable[i][0]
    return -1


# 找出端口对应的ID
def port2id(port, first=None):
    if first is True:
        os.system('python readinfo.py')

    with open('./output/port_com.txt', 'r') as f:
        tempporttable = f.readlines()[1:]
    porttable = []
    for fileline in tempporttable:
        porttable.append(list(map(int, re.findall(r'\d+', str(fileline)))))
    porttable = np.array(porttable).reshape(-1, 2)
    for i in range(porttable.shape[0]):
        if porttable[i][0] == port:
            return porttable[i][1]
    return -1


def deletenode(port):
    with open('./output/port_com.txt', 'r') as f:
        tempporttable = f.readlines()
    porttable = []
    for fileline in tempporttable:
        portid = list(map(int, re.findall(r'\d+', str(fileline))))
        if len(portid) and portid[0] == port:
            continue
        else:
            porttable.append(fileline)

    with open('./output/port_com.txt', 'w') as f:
        f.writelines(porttable)

    return


# 根据端口号和ID生成写入指令并返回，ID主要用来查表或者计算，ID和file其实只需要提供一个
def write(port, id, file):
    print('id is {}'.format(id))
    if id % 2:
        command = 'MSP430Flasher.exe -n MSP430FR5969 -i COM' + str(
            port) + ' -w ' + file + ' -e ERASE_MAIN'
    else:
        command = 'MSP430Flasher.exe -n MSP430FR5969 -i COM' + str(
            port) + ' -w ' + file + ' -e ERASE_MAIN'
    # os.system(command)
    print(command)
    return command


# 根据端口和ID生成亮灯指令并返回
def blink(port, id):
    print('com is {}, id is {}'.format(port, id))
    if id % 2:
        command = 'MSP430Flasher.exe -n MSP430FR5969 -i COM' + str(
            port) + ' -w blinkLED1.txt -e ERASE_MAIN'
    else:
        command = 'MSP430Flasher.exe -n MSP430FR5969 -i COM' + str(
            port) + ' -w blinkLED2.txt -e ERASE_MAIN'
    # os.system(command)
    print(command)
    return command


# 得到端口和ID对应表
def gettable(first=False):
    if first is True:
        os.system('readinfo.py')
    with open('./output/port_com.txt', 'r') as f:
        tempporttable = f.readlines()[1:]
    porttable = []
    for fileline in tempporttable:
        porttable.append(list(map(int, re.findall(r'\d+', str(fileline)))))
    porttable = np.array(porttable).reshape(-1, 2)
    print('porttable is {}'.format(porttable))
    return porttable


# 给某个端口写入指定的ID
def writeid(port_num, IDnum):
    # suppose lancupad num < 100
    if (IDnum < 10):
        IDinfo = '0' + str(IDnum) + ' 00 00 00\n'
    else:
        IDinfo = str(IDnum) + ' 00 00 00\n'

    with open('writeID.txt', 'r') as f1:
        # we can use f1.readlines(2) to read line 2
        flist = f1.readlines()
        flist[1] = IDinfo

    newfile = 'input/writeCOM' + port_num + '.txt'
    print(newfile)
    with open(newfile, 'w') as f2:
        f2.writelines(flist)

    # write msp430
    os.system('MSP430Flasher.exe -n MSP430FR5969 -i COM' + port_num + ' -w ' +
              newfile)
    print('MSP430Flasher.exe -n MSP430FR5969 -i COM' + port_num + ' -w ' +
          newfile)

    return