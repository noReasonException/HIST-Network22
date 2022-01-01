from lib import DefineVolunteer
from lib import Log_Report
from lib import Settings

import socket
import thread
import time
import sys
import os

class IncomingConnectionHandler():
	username = ""
	password = ""
	command  = ""
	parameters = list()
	IncomingConnectionObject = None
	logs = list()
	def __init__(self,IncomingConnectionObject,logs):
		print ('>>[INFO]Connection Estabilished with volunteer -> ',logs[0],":",logs[1])
		IncomingConnectionObject.send('C_E OK') #CONNECTION ESTABILISHED OKAY!
		self.IncomingConnectionObject = IncomingConnectionObject
		self.logs = logs
		self.Handle(IncomingConnectionObject,logs)
	def __del__(self):
		self.IncomingConnectionObject.close()
	def exec_command():
		return 'C_E[ERR] 100'
	def Handle(self,IncomingConnectionObject,logs):
		time.sleep(1)
		print(">>[WAIT]Wait to receive logs..")
		self.IncomingConnectionObject.send('D_U') #Define Username
		time.sleep(2)
		self.username = self.IncomingConnectionObject.recv(4096)
		print ">>[INFO]Username ", self.username
		self.IncomingConnectionObject.send('D_P')#Define Password
		time.sleep(2)
		self.password = self.IncomingConnectionObject.recv(4096)
		print ">>[INFO]Password " , self.password
		self.IncomingConnectionObject.send("D_O") #DEFINE OPERATION
		time.sleep(2)
		self.command = self.IncomingConnectionObject.recv(4096)
		print ">>[INFO]command ",self.command
		self.IncomingConnectionObject.send("D_A")#DEFINE ARGUMENTS
		time.sleep(2)
		argument = self.IncomingConnectionObject.recv(4096)
		counter = 0 
		while (argument != 'END') :
			counter+=1
			self.parameters.append(argument)
			print (">>[INFO] Argument No:"+str(counter)+" -> "+argument)
			time.sleep(2)
			argument = self.IncomingConnectionObject.recv(4096)
		else:
			self.IncomingConnectionObject.send(self.exec_command())
			del self



Incoming_Ip = str(sys.argv[1])
Binded_Port = int(sys.argv[2])
print ('>>[START The Traffic Controller Protocol (Server version 0.2 (Rebuild))]')
print ('>>[LOG]Creating Socket Socket Object ')
ServerConnectionObject = socket.socket()
print (">>[LOG]OK \n>>[LOG]Trying to bind ")
ServerConnectionObject.bind((Incoming_Ip,Binded_Port))
print (">>[LOG]Listen on IPv4 = "+Incoming_Ip+":"+str(Binded_Port)+" [OK]\n>>[LOG]Define MaximumAmountOfIncomingConnections ;) ")
ServerConnectionObject.listen(10)
print (">>[LOG]10 ")

while True:
	print (">>[LOG]StandBy Mode Activated")
	conn,addr=ServerConnectionObject.accept()
	print (">>[INFO]Incoming Connection")
	IncomingConnectionHandler(conn,addr)


