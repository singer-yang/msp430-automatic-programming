# msp430-automatic-programming
## code of my dual degree graduation project  
My goal is to achieve automatic programming of MSP430 network, writing relevant program into each launchpad simultaneously. The steps are following:  
1. create a unique ID to identify each msp430
2. write different programs into msp430s by their ID
3. use multithreading to write programs into msp430s simultaneously  

代码文件说明：  
writeinfo.py可以实现遍历端口，对每个MSP430写入ID，产生的txt文件在input/下；  
readinfo.py可以实现遍历端口，读取每个MSP430的ID并整合成一个表，产生的txt文件在output/下；  
function.py保存了用到的函数文件，通过form function import xx调用这些函数；  
multiprocess.py实现了多进程烧写MSP430，但是还没经过充分的检验。  
