使用 python 可以很方便调用命令行，实现对不同的开发板写入不同的代码  
准备工作：
1. 读出端口号  
2. 遍历端口号，写入不同的 ID  
3. 测试 ID 是否正确写入   

自动化编程：
1. 读出 ID 
2. 遍历 ID，写入对应的程序
   
clearinfo.py 可以擦除所有的内存信息，包括 INFO 和 MAIN  
readinfo.py 将 INFO 信息读出到 txt 文件中  
writeinfo.py 遍历端口号，将 ID 写入 INFO 地址中  
[ccs生成.txt文件](http://bbs.elecfans.com/jishu_1729823_1_1.html)
