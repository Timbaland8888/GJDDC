#!/bin/env python
# -*- coding: utf-8 -*-
#function:周期性的控制DDC中的虚拟机重启
#Author:Timberland

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import wmi
import time,setting
logfile = 'logs_%s.txt' % time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())

#远程控制win7登入
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
时间暂停
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
        cure_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        restart_no = 0
        if cure_time in setting.VM_restart_time:
            for num in range(len(vm)):
                print unicode(vm[num],'utf-8').encode('gbk'), unicode(vm_account[num],'utf-8').encode('gbk')
                call_remote_bat(vm[num],vm_account[num],setting.VM_pwd)
                restart_no +=restart_no
                waittime(180)
            # call_remote_bat(setting., 'xuanyuan\\zhangyuanzhang', '1qaz@WSX')
        else:
            waittime(6)

            # print('\033[1;31;40m')
            print  unicode('\n当前时间为：%s 还未到重启时间 %s 请等待 ' %(cure_time,setting.VM_restart_time), 'utf-8').encode('gbk')

            # print('\033[0m')
        print unicode('共重启%d虚拟机' %(restart_no), 'utf-8').encode('gbk')

        # waittime(1000)
        # call_remote_bat('b901-040-t', 'xuanyuan\\zhangyuanzhang', '1qaz@WSX')
    # print  time.strftime('%H:%M:%S',time.localtime())
