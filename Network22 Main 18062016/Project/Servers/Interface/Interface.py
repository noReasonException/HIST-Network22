from lib.Redirects import * #Εισαγωγή custom βιβλιοθηκων για επιστροφή της ip που θα γίνει το 302
from lib.Settings import *  #Εισαγωγή της βιβλιοθήκης ενημέρωσης των ρυθμίσεων απο το SettingsSystem
from lib.Log_Report import * #Εισαγωγή της βιβλιοθήκης Αναφοράς των logs
import thread #Πολυνυματική υποστηρίξη 
import random # Βιβλιοθήκη τυχαίων Αριθμων 
import socket #Εισαγωγή της socket
import ipdb 
import time #Βιβλιοθήκη για χρονισμό των ρυθμίσεων 
import sys #w8
import os
#ipdb.set_trace()
#Κωδικοποίηση utf-8
#-*- coding: utf-8 -*-  

Domain_Name="hey" 	#Εξυπηρετούμενο DomainName
Settings_Dictionary={} 	#Δηλωση της κενής λίστας των προσωρινών ρυθμίσεων 

print ("Start Updater bot() for server ",Domain_Name)
os.system('start Scripts/Updater.py 192.168.1.1 greece hey')


"""
Συνάρτηση Settings_Updater()
Χρησιμοποιεί την βιβλιοθήκη lib.Settings 

1)Αδειάζει την λίστα πρωσωρινών ρυθμίσεων 
2)Γεμίζει ξανά την λίστα με τις τελευταίες ρυθμίσεις (Απο την SettingsDatabase)
3)Διαγράφει απο την μνήμη την πρωσωρινή συνδεση με την βάση δεδομένων 
"""
def Settings_Updater():
    global Settings_Dictionary #Επεκτείνει την εμβέλεια της λίστας πρωσωρινών ρυθμίσεων 
    Settings_Dictionary={} #Καθαρίζει την λίστα πρωσωρινών ρυθμίσεων 
    MainSettingsObject=SettingsLoadUp(Domain_Name) #Δημιουργεί ενα object της κλασής SettingsLoadUp()
    MainSettingsObject.check()
    #Fill the Settings Turple properly! <3
    Settings_Dictionary["Server_Status"]=MainSettingsObject.Server_Status()
    Settings_Dictionary["Server_Port"]=MainSettingsObject.Server_Port()
    Settings_Dictionary["Server_BufferSize"]=MainSettingsObject.Server_BufferSize()
    Settings_Dictionary["Server_MaximumAmountOfIncomingConnections"]=MainSettingsObject.Server_MaximumAmountOfIncomingConnections()
    Settings_Dictionary["Server_Shutdown"]=MainSettingsObject.Server_Shutdown()
    Settings_Dictionary["Server_Restart"]=MainSettingsObject.Server_Restart()
    Settings_Dictionary["Server_OnServerName"]=MainSettingsObject.Server_OnServerName()
    del MainSettingsObject#Deletes the object
    print("New Config Loaded !")
    for i,j in Settings_Dictionary.iteritems(): #DEBUG CODE
        print i,j#print all elements of Settings_Dictionary

Settings_Updater()#Call for the first time the Settings_Updater





#answer_to_client 
""" 
Η συνάρτηση αυτή αναλαμβάνει εξολοκλήρου τον κάθε client για να τον ανακαυθύνει κατάλληλα 
"""
def answer_to_client(IncomingConnectionInfo,IncomingConnectionObject): #Δήλωση της συνάρτησης 
    global Domain_Name #επέκταση της εμβέλειας του domain 
    database_object=redirection(Domain_Name) #Create the basic redirects object
    #redirect_form = the HTTP version 1.1 responce to redirect the client
    #with the NULL in the place of redirect address....
    redirect_form="""
HTTP/1.1 302 Found
Location: NULL
"""
    redirect_destination=str(("http://"+str(database_object.return_ip()))) #δημιουργία της διεύθυνσης προορισμου (#fix it για να εχει και Port)
    redirect_form=redirect_form.replace("NULL",redirect_destination)  #Αντικατάσταση στο αρχική απάντηση
    try:#Try this code
        request=IncomingConnectionObject.recv(Settings_Dictionary["Server_BufferSize"])#λήψη του αρχικού αιτήματος απο τον buffer
        IncomingConnectionObject.sendall(redirect_form)#αποστολή της αίτητης ανακατεύθυνσης 
        #Καταγραφή της ανακατεύθυνσης 
        log_object=log_report_object("greece",str(Domain_Name)) 
        #FIXXXX -> log_object.redirect_report(IncomingConnectionInfo[0],IncomingConnectionInfo[1],redirect_destination,"80(static)","127.0.0.1(static),",Settings_Dictionary["Server_Port"],Domain_Name)
        print IncomingConnectionInfo[0] , IncomingConnectionInfo[1],"->OK"# Debug message
    except :#In Case of any error
        #raise ResponceError #Raise the Responce Error
        print("[ERR]>>Responce Error on client"+IncomingConnectionInfo[0]+":"+IncomingConnectionInfo[1])
    IncomingConnectionObject.close()#Close the specific incoming connection
    del database_object



def pause():
    print("Server "+Domain_Name+" PAUSED ")
    while(not int(Settings_Dictionary['Server_Status'])):
        time.sleep(50)
        Settings_Updater()
    else:
        return





def socket_starter():#Δηλώση συνάρτησης εκκίνησης του server
    global connection#επέκταση της εμβέλειας του socket.socket() αντικειμενου 

    connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    """
    ================================socket.socket docstring :)
    1)socket.AF_INET = uses ip version 4
    2)socket.SOCK_STREAM = uses TCP oriented connection
    =================================================
    2.1)We can use SOCK_DGRAM parameter when we want
    to use the UDP protocol

    """

    try:#Try this code
    #Settings_Dictionary["Server_OnServerName"]
        connection.bind(('localhost',int(Settings_Dictionary["Server_Port"]))) #Bind the specific port and servername

    except:
        print("[ERR]>>Error in bind process #Try to change the binded port ;) ]")#Debug Message

    #δηλώση των μέγιστων εισερχόμενων συνδέσεων 
    connection.listen(Settings_Dictionary["Server_MaximumAmountOfIncomingConnections"]) #Maximum amount of waitin connections = 10
    #αποθήκευση της τωρινής ημερομηνίας
    current_time=time.localtime(time.time())#Get First time the current time!

    while(True):
        #αποθηκεύση της τωρινης πρωσωρινης ώρας
        if (time.localtime(time.time()) != current_time): #αν έχει περάσει τουλαχιστον ενα λεπτο 
            current_time=time.localtime(time.time())#τοτε η επισημη ώρα αλλαζει 
            pause() #ελενέται αν ο server ειναι σε pausemode 
            Settings_Updater() # και η ρυθμίσεις γίνονται update 


        #Αναμονή για εισερχόμενη σύνδεση 
        responce_connection,connection_info=connection.accept()#wait for incoming connections
        """
            responce connection is the connection object that the client estabilished
            connection info is a turple with logs
                connection_info [0] -> the incoming ip address <3
                connection_info [1]-> the incoming tcp port <3
        """
        #Σε περίπτωση εισερχόμενης σύνδεσης , τότε η answer_to_client αναλαμβάνει να απαντήσει 
        answer_to_client(connection_info,responce_connection)#call the answer_to_client func
        """
        Answer to client func handles all incoming clients <3 ;)
        """
#Εκκίνηση του server
socket_starter()#the power button <3 :P
