import os
import os.path
import threading
import datetime
import sys

def download_file(url, num_thread = 5):
    
    r = requests.head(url)
    try:
        file_name = url.split('/')[-1]
        file_size = int(r.headers['content-length'])   # Content-Length获得文件主体的大小，当http服务器使用Connection:keep-alive时，不支持Content-Length
    except:
        print("检查URL，或不支持对线程下载")
        return
 
    #  创建一个和要下载文件一样大小的文件
    fp = open(file_name, "wb")
    fp.truncate(file_size)
    fp.close()
 
    # 启动多线程写文件
    part = file_size // num_thread  # 如果不能整除，最后一块应该多几个字节
    for i in range(num_thread):
        start = part * i
        if i == num_thread - 1:   # 最后一块
            end = file_size
        else:
            end = start + part
 
        t = threading.Thread(target=Handler, kwargs={'start': start, 'end': end, 'url': url, 'filename': file_name})
        t.setDaemon(True)
        t.start()
 
    # 等待所有线程下载完成
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()
    print('%s 下载完成' % file_name)
if __name__ == '__main__':
    rootdir = "D:\\写真\\takeda-rena"                               # 指明被遍历的文件夹
    pathSet=set()
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:                        #输出文件信息
            #print ("parent is:" + parent)
            #print ("filename is:" + filename)
            #print ("the full name of the file is:" + os.path.join(parent,filename)) #输出文件路径信息
            pathSet.add(os.path.join(parent,filename))
    #print(pathSet)
    for path in pathSet:
        print ('--------'+path+'--------')
        print(os.path.split(path)[0])
        basePath=os.path.split(path)[0]
        f = open(path, 'r')
        for line in f.readlines():
            print(line.strip())
            print(basePath+'\\'+line.split('/')[-1])
            filePath=basePath+'\\'+line.split('/')[-1]

        f.close()
