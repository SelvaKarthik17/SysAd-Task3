
import  socket
import _thread

i=0 #general user id

#by default,the 'message' thread will start only after all 154 users have connected.Change the value of i inside while loop at the end of the code(at line 154) ,if the number of users connected will be different.

#class id - chiefcommander:0 ArmyChief:1 NavyMarshall:2 AirForceChief:3 Army:4 Navy:5 Airforce:6
Army = [];
Navy = [];
Airforce = [];
Chiefcommander = None
Armychief = None
Navymarshall = None
Airforcechief = None
ps = []; #stores the class/hierarchy of user.

cx = [];
addrx = [];


msg0 = ""


def newclient(cc,addr):
    global i,Chiefcommander,Armychief,Navymarshall,Airforcechief
    cx.append(cc)
    addrx.append(addr)

    pos = cc.recv(1024).decode('utf-8')

    if pos.lower() == "chiefcommander":
        ps.append(0)
        Chiefcommander = cc

    elif pos.lower() == "armychief" :
        ps.append(1)
        Armychief = cc

    elif pos.lower() == "navymarshall":
        ps.append(2)
        Navymarshall = cc

    elif pos.lower() == "airforcechief":
        ps.append(3)
        Airforcechief = cc

    elif ((pos.find("army") == 0) and (pos.find("armychief") == -1)):
        ps.append(4)
        Army.append(cc)

    elif pos.find("navy") == 0 and pos.find("navymarshall") == -1 :
        ps.append(5)
        Navy.append(cc)

    elif pos.find("airforce") == 0 and pos.find("airforcechief") == -1 :
        ps.append(6)
        Airforce.append(cc)

    i +=1

def message():
        global msg0

        while True:

            for x in range(len(cx)):
                     msg0 = cx[x].recv(1024).decode('utf-8')

                     if ps[x] == 0:
                        if Armychief != None:
                            Armychief.send(bytes(msg0,'utf-8'))
                        if Navymarshall != None:
                            Navymarshall.send(bytes(msg0,'utf-8'))
                        if Airforcechief != None:
                            Airforcechief.send(bytes(msg0,'utf-8'))


                     elif ps[x] == 1:
                       if Chiefcommander != None:
                            Chiefcommander.send(bytes(msg0, 'utf-8'))
                       if Airforcechief != None:
                            Airforcechief.send(bytes(msg0, 'utf-8'))
                       if Navymarshall != None:
                            Navymarshall.send(bytes(msg0, 'utf-8'))

                       for y in range(len(Army)):
                           Army[y].send(bytes(msg0,'utf-8'))


                     elif ps[x] == 2:
                       if Chiefcommander != None:
                            Chiefcommander.send(bytes(msg0, 'utf-8'))
                       if Airforcechief != None:
                            Airforcechief.send(bytes(msg0, 'utf-8'))
                       if Armychief != None:
                            Armychief.send(bytes(msg0, 'utf-8')) 
                      
                       for y in range(len(Navy)):
                           Navy[y].send(bytes(msg0,'utf-8'))


                     elif ps[x] == 3:
                       if Chiefcommander != None:
                            Chiefcommander.send(bytes(msg0, 'utf-8'))
                       if Navymarshall != None:
                            Navymarshall.send(bytes(msg0, 'utf-8'))
                       if Armychief !=None:
                            Armychief.send(bytes(msg0, 'utf-8'))  
                       
                       for y in range(len(Airforce)):
                           Airforce.send(bytes(msg0,'utf-8'))


                     elif ps[x] == 4:
                       if Armychief != None:
                           Armychief.send(bytes(msg0, 'utf-8'))
                       for y in range(len(Army)):
                           if Army[y] != cx[x]:
                              Army[y].send(bytes(msg0,'utf-8'))


                     elif ps[x] == 5:
                       for y in range(len(Navy)):
                           if Navy[y] != cx[x]:
                              Navy[y].send(bytes(msg0,'utf-8'))
                       if Navymarshall != None:
                           Navymarshall.send(bytes(msg0, 'utf-8'))
   

                     elif ps[x] == 6:
                       for y in range(len(Airforce)):
                           if Airforce[y] != cx[x]:
                              Airforce[y].send(bytes(msg0,'utf-8'))
                       if Airforcechief != None:
                           Airforcechief.send(bytes(msg0, 'utf-8'))
  
                     

s=socket.socket()
print("socket created")

s.bind(('localhost',9999))

s.listen(3)
print("waiting")


while True:
    c,addr = s.accept()
    _thread.start_new_thread(newclient,(c,addr,))

    if i==153:
        _thread.start_new_thread(message,())
        # Here, i represents the total numbers of users that will be connected to the server before initating the message function thread,change the value of i to (user - 1) when required.

c.close()
