import pywhatkit
import time
import threading

def send_msg(sospechoso,locacion):
    t = time.localtime()
    hora = time.strftime("%H", t)
    minutos = time.strftime("%M", t)
    print (hora)
    print(minutos)
    msg = "Se ha detectado un "+sospechoso+" en "+locacion


                            #telephone num
    pywhatkit.sendwhatmsg("+1000000000",msg,int(hora),int(minutos)+4)

