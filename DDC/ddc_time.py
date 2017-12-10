#-*-encoding:utf-8 -*-
from  Tkinter import *
import ddc,setting
import sys
reload(sys)
sys.setdefaultencoding('utf8')
root = Tk()
root.title('设置DDC重启时间')
root.geometry('300x123')
l = Label(root,text='时间：')
l.pack()
e1 =Entry(root,show=None,background = 'red')
e1.pack()

def insert_point():
    str1 = u'DDC重启时间为'

    var =e1.get()
    f = var.decode('utf-8')
    # VM_restart_time.join(f)
    # print type(f)
    # print type(var)


    t.insert('insert',var)
def test1():
    var = e1.get()
    f = var.decode('utf-8')
    print f
b1 = Button(root, text='确定', width=15, height=2,command=insert_point)
b1.pack()
# b2 = Button(root, text='执行', command=ddc.admin)
# b2.pack()
t =Text(root,height=2)
t.pack()
# print setting.VM_restart_time
root.mainloop()
