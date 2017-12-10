#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time,datetime
import ddc,setting
from tkinter import *
import tkMessageBox,win32api,fileinput

# global f
def is_valid_date(str):
  '''判断是否是一个有效的日期字符串'''
  try:
    time.strptime(str, "%H:%M:%S")
    return True
  except:
    print '请输入正确的时间格式'

def insert_point():
    #获取输入框框中的值
    var = e1.get()
    #清除text中的内容
    t.delete('0.0', END)
    #转换字符串
    f = var.decode('utf-8')
    cure_date=time.strftime('%Y-%m-%d', time.localtime())
    #获取当前日
    # cure_date.append(time.strftime('%Y-%m-%d', time.localtime()))
    # cure_date.append(f)
    d = cure_date+'  ' +f
    #计算6个相差一秒的时间值格式为'%Y-%m-%d %H:%M:%S'
    d1 = datetime.datetime.strptime(d,'%Y-%m-%d %H:%M:%S')
    # d1 = datetime.timedelta(seconds=1)+d1
    d2 = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.timedelta(seconds=1)+d1
    d3 = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
    d3 = datetime.timedelta(seconds=2)+d1
    d4 = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
    d4 = datetime.timedelta(seconds=3)+d1
    d5 = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
    d5 = datetime.timedelta(seconds=4)+d1
    d6= datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
    d6 = datetime.timedelta(seconds=5)+d1
    #还原格式'%Y-%m-%d %H:%M:%S'为‘%H:%M:%S‘



    with open('C:\\Users\\baiban\\PycharmProjects\\DDC\\DDC\\setting.py','a') as w:
        w.write("\nVM_restart_time = ['%s','%s','%s','%s','%s','%s']" %(d1,d2,d3,d4,d5,d6))
    if is_valid_date(f) == True:
        tkMessageBox.showinfo("重启时间", "设置成功！！")

        t.insert('insert', var)
        # cure_time = time.strftime('%H:%M:%S', time.localtime())
        # restart_no = 0
        # if cure_time == f:
        #     for num in range(len(vm)):
        #         print vm[num], vm_account[num]
        #         ddc.call_remote_bat(vm[num], vm_account[num], setting.VM_pwd)
        #         restart_no += restart_no
        #         # ddc.waittime(60)
        # else:
        #     # ddc.waittime(5)
        #
        #     # print('\033[1;31;40m')
        #     print  unicode('当前时间为：%s 还未到重启时间 %s 请等待 ' %(cure_time,setting.VM_restart_time), 'utf-8')
        #     ddc.waittime(60)
        #     t.insert('insert', '当前时间为：%s 还未到重启时间 %s 请等待 ' %(cure_time,setting.VM_restart_time))
        win32api.ShellExecute(0,'open','C:\\Users\\baiban\\PycharmProjects\\DDC\DDC\\ddc.py','','',1)
    else:

        t.insert('insert', u'请输入正确的时间格式 例如：23:12:12')



root = Tk()
root.title("DDC重启时间设置")
root.geometry('300x123')
l = Label(root,text='时间：')
l.pack()
e1 =Entry(root,show=None,background = 'red')
e1.pack()

b1 = Button(root, text='确定', width=10, height=1, command=insert_point)

b1.pack()
# 通过command属性来指定Button的回调函数
# Button(root, text='Hello问问 Button', command=helloButton).pack()
t =Text(root,height=10)
t.pack()

root.mainloop()
