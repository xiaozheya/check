#-*- coding:utf-8 -*-
from tkinter import *
from tkinter.filedialog import askdirectory
import md5
import re

def selectPath():
    path_ = askdirectory()
    path.set(path_)
    global res
    res = path_
def begin():
    md5.find(res)

root = Tk()
path = StringVar()

Label(root,text = "目标路径:").grid(row = 0, column = 0)
Entry(root, textvariable = path).grid(row = 0, column = 1)
Button(root, text = "路径选择", command = selectPath).grid(row = 0, column = 2)
Button(root, text = "search", command = begin).grid(row = 1, column = 1)
root.mainloop()
