# File: server.py

import socket
import time

#TCP_IP = '130.212.6.214'
TCP_IP = '192.168.1.110'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

print "before socket"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "about to bind"
s.bind((TCP_IP, TCP_PORT))
print "listening"
s.listen(100)

print "about to accept"
conn, addr = s.accept()
#print 'Connection address:', addr
while 1:
    try:
	print "waiting for data"
        data = conn.recv(BUFFER_SIZE)
#        if not data: break
        print "received data:", data
#        s.send(data)  # echo
        time.sleep(0.3)
    except BaseException:
        time.sleep(0.3)
	print "waiting"
        #pass
conn.close()
