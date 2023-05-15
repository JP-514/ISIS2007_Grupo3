import pywhatkit
import time
import geocoder

import datetime
snd_list = {}# "juan___":present day
def send_msg(sospechoso):
    t = time.localtime()
    hora = time.strftime("%H", t)
    minutos = time.strftime("%M", t)


    g = geocoder.ip('me')
    print (hora)
    print(minutos)
    print(g.latlng)
    msg = "Se ha detectado un "+sospechoso+" en latitud:  "+str(g.latlng[0])+ " en longitud: "+ str (g.latlng[1])

                            #telephone num
    pywhatkit.sendwhatmsg("+573053658375",msg,int(hora),int(minutos)+2, 3,True,2)
    snd_list[sospechoso]= datetime.datetime.now()
    




def name_in_send_list():

    return snd_list
def ret_lst_send(sospechoso):
    return snd_list[sospechoso]