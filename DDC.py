#!/bin/env python
#-*-coding: utf-8 -*-
#function:周期性的控制DDC中的虚拟机重启
#Author:Timberland
# -*- coding: utf-8 -*-
import wmi,json
import time,setting
logfile = 'logs_%s.txt' % time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())

#远程执行bat文件
def call_remote_bat(ipaddress,username,password):
    try:
        #用wmi连接到远程win7系统
        conn = wmi.WMI(computer=ipaddress, user=username, password=password)
        filename=r"c:\app\start.bat"   #win7C盘的重启系统脚本
        cmd_callbat=r"cmd /c call %s"%filename
        conn.Win32_Process.Create(CommandLine=cmd_callbat)  #执行bat文件
        print "执行成功!"
        return True
    except Exception,e:
        log = open(logfile, 'a')
        log.write(('%s, call  Failed!\r\n') % ipaddress)
        log.close()
        return False
    return False
'''
5分钟时间暂停
'''
def waittime(s):
    time.sleep(s)
    return True

if __name__=='__main__':

    vm = []
    vm_account = []
    for vmlist in setting.xygroup.keys():

        vm.append(vmlist+setting.VM_join)

    for vmlist in setting.xygroup.keys():
        vm_account.append(setting.VM_domain+vmlist)

    # call_remote_bat('b901-040-t', 'xuanyuan\\b901-040', 'Root@123')
    while True:
        cure_time = time.strftime('%H:%M:%S', time.localtime())
        restart_no = 0
        if cure_time == '23:50:50':
            for num in range(len(vm)):
                print vm[num], vm_account[num]
                call_remote_bat(vm[num],vm_account[num],setting.VM_pwd)
                restart_no +=restart_no
                waittime(60)
            # call_remote_bat(setting., 'xuanyuan\\zhangyuanzhang', '1qaz@WSX')
        print unicode('共重启%d虚拟机' %(restart_no),'utf-8')
    # call_remote_bat('b901-040-t', 'xuanyuan\\zhangyuanzhang', '1qaz@WSX')
    # print  time.strftime('%H:%M:%S',time.localtime())
