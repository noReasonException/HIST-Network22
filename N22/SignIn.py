"The TrafficController Client "
"Version 0.0.1 "

import socket
import sys

username = sys.argv[1]
password = sys.argv[2]
#command  = sys.argv[3]
#parameters = (sys.argv[4:])

#Init

Connection = socket.socket()
Connection.connect(('localhost',1090))
while(True):
    continue
