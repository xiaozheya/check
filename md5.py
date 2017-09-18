#!/usr/bin/python
#-*- coding:utf-8 -*-
import xlwt
import hashlib
import os
def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = file(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

def find(path):
    print "in"
    f1 = xlwt.Workbook()
    table = f1.add_sheet('info', cell_overwrite_ok=True)
    d_path = path.decode('utf8')
    count=0
    for fpathe, dirs, fs in os.walk(d_path):
        for f in fs:
            temp= f.split('.')
            if len(temp)>1:
                if temp[1]=='mp4' or temp[1]=='MOV'or temp[1]=='rmvb'or temp[1]=='flv'or temp[1]=='avi'or temp[1]=='mov'or temp[1]=='wmv'or temp[1]=='mpg':
                    str=os.path.join(fpathe, f)
                    table.write(count, 0, str)
                    table.write(count, 1, GetFileMd5(str))
                    count+=1
                    #print str
                    #print GetFileMd5(str)
        f1.save('file.xls')


if __name__ == "__main__":
    path = raw_input("please input the path：")
    find(path)