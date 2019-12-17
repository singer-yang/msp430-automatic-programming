'''
@Author: your name
@Date: 2019-12-10 16:42:49
@LastEditTime: 2019-12-11 17:13:47
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \msp430\blinkLED_v1.py
'''
import os
from multiprocessing import Pool

from function import testblink, gettable, blink
from testpool import func

if __name__ == "__main__":
    porttable = gettable()
    command = [blink(port, id) for port, id in porttable]
    # print(command)

    pool = Pool(processes=3)
    pool.map(os.system, command)

    # for portnum, idnum in porttable:
    #     t = pool.apply_async(testblink, (portnum, idnum))
    
    pool.close()
    pool.join()
    print('all done')
