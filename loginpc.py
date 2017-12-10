# encoding UTF-8
import telnetlib, sys
from time import sleep
import threading

def telnetdo(HOST=None, USER=None, PASS=None, COMMAND=None): #define a function

    tn = telnetlib.Telnet() #
    try:
        tn.open(HOST)

    except:
        print "Cannot open host"
        return

    tn.write('\r\n')
    tn.read_until("login:")
    tn.write(USER+'\r\n')
    print tn.read_until("password:")
    tn.write(PASS +'\r\n')
    print tn.read_until(">")
    tn.write(COMMAND + '\r\n')

    tmp = tn.read_all()
    tn.close()
    return tmp.decode('GBK')

if __name__ == '__main__':
    t1=threading.Thread(target=telnetdo,args=('b901-040-t','xuanyuan\\b901-040','Root@123','start.bat'))
    t1.setDaemon(True)
    t1.start()
    print '*****************'
    #do something test
    sleep(90)