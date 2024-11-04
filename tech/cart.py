
import time
import serial
import pymysql
import sys
import glob
from datetime import datetime
import pyttsx3
engine=pyttsx3.init()
def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
ports=serial_ports()
print(ports)
if len(ports)>0:
    portname=ports[0]
else:
    print("No Devices Connected")



def savedata(sql):
    db = pymysql.connect(host='localhost',user="root",password="root",port=3306,database="autocart" )
    c = db.cursor()
    c.execute(sql)
    
    db.commit()
    
    c.close()
    
    db.close()
    
def getdata(sql):
    db = pymysql.connect(host='localhost',user="root",password="root",port=3306,database="autocart" )
    c = db.cursor()
    c.execute(sql)
    dat=c.fetchall()
    db.commit()
    c.close()
    db.close()
    return dat

def coutproduct(pid,tp):
    sql="select * from product where product_id='"+ str(pid) +"'"
    dat1=getdata(sql)
    if len(dat1)>0:
        row=dat1[0]
        amt=row[4]
        pname=row[2]
    now=datetime.now()
    dt=now.strftime("%Y-%m-%d")
    tm=now.strftime("%H:%M")
    sql="select * from cart where product_id='"+ str(pid) +"'"
    dat=getdata(sql)
    if len(dat)>0:
        if tp=='+':
            sql="update cart set quantity=quantity+1 where product_id='"+ str(pid) +"'"
            lab=pname+" added to cart"
            
            engine.say(lab)
            engine.runAndWait()
            print(lab)
        elif tp=='-':
            sql="update cart set quantity=quantity-1 where product_id='"+ str(pid) +"'"
            lab=pname+" Removed from cart"
            print(lab)
            engine.say(lab)
            engine.runAndWait()
        savedata(sql)
    else:
        if tp=='+':
            if len(dat1)>0:
                row=dat1[0]
                amt=row[2]
                sql="INSERT INTO `cart` (`product_id`, `quantity`, `date`, `time`) VALUES ('"+ str(pid) +"', '1', '"+ dt +"', '"+ tm +"')"
                savedata(sql)
                lab=pname+" added to cart"
                engine.say(lab)
                engine.runAndWait()
                print(lab)




ser = serial.Serial()

ser.port = portname

ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
#ser.timeout = None          #block read
ser.timeout = 1            #non-block read
#ser.timeout = 2              #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write

try:
    if ser.isOpen():
        ser.close()
except:
    print("error")
try: 
    ser.open()
except Exception:
    print ("error open serial port: " + str(e))
    exit()
    
if ser.isOpen():
    try:
        ser.flushInput() #flush input buffer, discarding all its contents
        ser.flushOutput()#flush output buffer, aborting current output 
        numOfLines = 0
        outp=""
        ap=1
        cnt=0
        ins=0
        while True:
            
            try:
                rsp=ser.readline().decode('utf-8').rstrip()
                if rsp != '':
                    print(rsp)
                    if '+' in rsp:
                        print(rsp)
                        print('added to cart')
                        if '99 6B 73 98' in rsp:
                            pid='8'
                        elif '1A B8 77 3C' in rsp:
                            pid='5'
                        coutproduct(pid,'+')
                    elif '-' in rsp:
                        print(rsp)
                        print('removed from cart')
                        if '99 6B 73 98' in rsp:
                            pid='8'
                        elif '1A B8 77 3C' in rsp:
                            pid='5'
                        coutproduct(pid,'-')
            except Exception as ex:
                print(ex)
                pass
            
            
        ser.close()
    except Exception:
        print ("error communicating...: " + str(e1))
else:
    print ("cannot open serial port ")

