#-*- coding: utf-8 -*- 
#Κωδικοποίηση utf-8

from lib.DefineVolunteer import * #εισαγωγη custom Βιβλιοθήκης δήλωσης εθελοντη στο cluster
from lib.Log_Report import *    #εισαγωγή custom βιβλιοθήκης για δηλώση των Logs στις βάσεις δεδομένων
from lib.Settings import *  #εισαγωγή custom βιβλιθήκης για παραλαβή των ρυθμίσεων του καθε εξυπηρετητη TrafficProtocol.
import socket #Socket
import time
import thread #υποστηριξή πολυνυμάτικου προγραμματισμού 
import sys

"""
Traffic Controller Protocol version0.1

"""
#Κάθε φορά που μια σύνδεση εισέρχεται στα sock streams δημιουργείται μια instance του 
#πρωτοκόλλου με σκοπο την διαχειριση του σε ξεχωριστό νήμα του επεξεργαστη 
#οταν η συνδεση τερματιστει , τότε η istance κανει del τον εαυτο της(del self)
class Traffic_Controller_Protocol_Activate(): #Κλάση του πρωτοκόλλου 
	#Απαραίτητα attritudes 
	user_username=""
	user_password=""
	user_email=""
	user_ip=""
	user_port=""
	isOnline=""
	req=""
	def sign_in(self,username,password,email):
		pass
	def log_in(self,username,password):
		pass
	def get_list(self,**args):
		pass
	def Join(self,username,password,domainname):
		
		ReturnedConnectionObject.send(username+password+domainname+" : Attemt to join in the network 22  ")
		DatabaseInterfaceObject = DefineVolunteer()

	def __init__(self,ReturnedConnectionObject,logs=[]): #consructor της κλάσης 
		try:#δοκιμασε τον κάτωθι κώδικα 
			ReturnedConnectionObject.send("HELLO "+str(logs[0])+":"+str(logs[1]))#Εναρξή σύνδεσης 
			ReturnedConnectionObject.send("connection estabilished") #Δήλωση εγκαθίδρυσης της σύνδεσης
			print("Connection estabilished") #DEBUG CODE
		except: #Σε περίπτωση λάθους 
			print("Error on connection initilisation")#Debug code
			ReturnedConnectionObject.close()#Κλείσιμο σύνδεσης 
			del self #Διαγραφή αντικειμένου σύνδεσης
		print ReturnedConnectionObject.recv(10000)
		Responce = ReturnedConnectionObject.recv(10000)#Αναμονή απάντησης απο τον client
		#Responce = "NULL"
		is_User_Defined=False #Σημαία οτι ο χρήστης δεν έχει δηλώσει τα στοιχεία του 

		#while (Responce.split()[0] != "EXIT"): #Όσο δεν επιθυμεί ο client τον τερματισμό της σύνδεσης 
		while(1):
			print (Responce)#Εκτύπωση  απάντησης 
			try:#Δοκιμή κώδικά 
				if (Responce.split()[0] =="DEFINE" and is_User_Defined==False): #Σε περίπτωση χρήσης της εντολής Define
					user_username = Responce.split()[1] #Το πρώτο κενό είναι το Username
					user_password = Responce.split()[2] #Το δεύτερο είναι το Password
					user_email    = Responce.split()[3] #Το τρίτο είναι το email
					user_ip       = logs[0]
					user_port     = Responce.split()[4] #Το τέταρτο είναι η port 
					isOnline 	  = 1 #Προφανώς και οταν θέλει να συνδεθεί ειναι Isonline
					req           = 0 #Μηδενισμός των request 
					ReturnedConnectionObject.send("1.0 -> OK ") #Απάντηση (ολα κομπλε! :P )
					is_User_Defined=True#Ο χρήστης εχεί καθοριστεί 
					print ("1.0 -> OK ") #log ολα κομπλε!
					Responce = ReturnedConnectionObject.recv(10000) #Αναμονή απάντησης 
					continue #restart τον κεντρικό βρόνχο
				if(not(is_User_Defined)): #Σε περίπτωση που ο χρήστης δεν έχει δηλώσει τα στοιχεία του ακόμη 
					print("run DEFINE first") #LOG Που πας ρε καραμήτρο ?
					print ("2.1->REPEAT")     #ΕΠΑΝΕΛΑΒΕ 
					ReturnedConnectionObject.send("ERR ->RUN DEFINE FIRST \n 2.1->REPEAT") #αποστολή απάντησης λάθους 
					Responce = ReturnedConnectionObject.recv(10000) #Αναμονή επανάληψης 
					continue#restart τον κεντρικό βρόνχο

				if (Responce.split()[0] == "SIGN_IN"):#Σε περιπτώση της εντολής SignIn
					self.sign_in()#Ε συνδέσου και εσυ! 
				elif (Responce.split()[0] == "LOG_IN"):#Σε περιπτώση Log_in
					self.log_in() # θες και εξηγηση τρ?
				elif (Responce.split()[0] == "GET_LIST"):#Σε περιπτωση ζητησης της λιστας των 
														#διαθεσιμων domain με τις τιμες
					self.get_list()#καλεσε την get_list()
				elif (Responce.split()[0] == "JOIN"):
					self.Join()
				else:#Σε περιπτώση μη χρησιμοποιησης καποιας εντολης 
					#προφανως και αποσκοπείται καποιου είδους επίθεση FIX DAT SHIT
					ReturnedConnectionObject.send("2.2 -> BLOCKED IP \n nice try ;)  ")
					print("2.1 -> REPEAT")
				ReturnedConnectionObject.recv(10000)
				Responce = ReturnedConnectionObject.recv(10000)
			except IndexError:
				ReturnedConnectionObject.send("2.1 -> REPEAT ")
				print("2.1 -> REPEAT")
				ReturnedConnectionObject.recv(10000)
				Responce = ReturnedConnectionObject.recv(10000)
				continue
		else:#In case of EXIT
			ReturnedConnectionObject.send("Bye!")# Τερματισμος σύνδεσης 
			ReturnedConnectionObject.close()
			print("Connection Terminated by host")
			del self


	



def main():
	try:
		sys.stdout.write(' Creating a socket object ........')
		time.sleep(1)
		connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#ορισμος του socket 
		sys.stdout.write('ok\n')
	except:
		print("Error creating a socket object ")
		exit()
	try:
		sys.stdout.write("Attemting to bind........")
		time.sleep(1)
		connection.bind(("localhost",1090)) #bind την συ8κεκριμενη port
		sys.stdout.write('.ok\n')
	except:
		print("Error in bind proccess")
		exit()


	connection.listen(10) #μεγιστος αριθμός εισερχόμενων συνδεσεων = 10 
	print("Maximum Amount of connections = 10")
	while True:
		print("Standby..")
		ReturnedConnectionObject,logs=connection.accept() #αναμενουμε για accept
		print "Incoming Connection ->" + str(logs[0]) +":"+str(logs[1])#debug
		thread.start_new_thread(Traffic_Controller_Protocol_Activate,(ReturnedConnectionObject,logs))
		#NewClient = Traffic_Controller_Protocol_Activate(ReturnedConnectionObject,logs)
main()
