import os
import os.path
rootdir = "D:\\写真\\yoshioka-riho"                               # 指明被遍历的文件夹
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
    f = open(path, 'r')
    for line in f.readlines():
        print(line.strip())
    f.close()