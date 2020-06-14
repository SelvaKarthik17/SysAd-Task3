
#This is a generic client side script. Run multiple instances of it after the server code starts running. 

import socket
import _thread

flag = 1

name = input("enter your name:")
c=socket.socket()

c.connect(('localhost',9999))

def send():
 
    msg = input("enter:")
    while True:

        c.send(msg.encode())

        msg = input("enter:")

def receive():
   
    while True:
         print(c.recv(1024).decode('utf-8'))


c.send(name.encode())

while True:
    if flag == 1:
        _thread.start_new_thread(send,())
        _thread.start_new_thread(receive,())
        flag = 0

