# -*- coding: utf-8 -*-

import MySQLdb
import time
import sys
#import ipdb 

#ipdb.set_trace()
class Updater():  #δηλώση κλάσης

	host = None #δηλωση στον constructor της Ip της βάσης δεδομένων
	user = "updater_script" #χρήστης 
	password = "12312312345" #Κωδικός 
	database = None #Ονομα βάσης
	domain = None #Ονομα table 
	def __init__(self,host,database,domain):
		self.host = host
		self.database = database
		self.domain = domain
		print "[LOG]>> Updater_bot() is loading.."
		connect = MySQLdb.connect(self.host , self.user , self.password, self.database) #Σύνδεση με βάση 
		cursor = connect.cursor() #Επιστροφη αντικειμένου τυπου cursor
		#print "[ERR]>> Updater Cant Connect with Interface Database: "+host+" On user "+user	
		print "[LOG]>> Updater_bot() starting.."
		while True :
			cursor.execute("select MAX(TempPressureLevel) from "+database+"."+domain+";") #εκτέλεση του query
			max_TempPressureLevel = int(cursor.fetchone()[0]) #επιστροφη τιμής με την χρήση της fetchone()
			if (max_TempPressureLevel <= 0) :#Σε περίπτωση που η max ειναι 0 
				print "[LOG]"+str(time.strftime("%H:%M:%S on %d/%m/%Y"))+">> Updater_bot() is update TempPressureLevels to default values on InterfaceServer"
				cursor.execute("update "+database+"."+domain+" set TempPressureLevel=PressureLevel;") #εκτέλεση του query
				connect.commit()#commit () για επιβεβαιωση αλλαγων 
			cursor.close()
			connect.close()
			connect = MySQLdb.connect(self.host,self.user,self.password)
			cursor = connect.cursor()
Updater_Bot_Instance = Updater(sys.argv[1],sys.argv[2],sys.argv[3])
