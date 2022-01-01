import MySQLdb #Βιβλιοθήκη για διασύνδεση με MySQL βάση δεδομένων 
import random
# -*- coding: utf-8 -*-
class SettingsLoadUp():
    sqlhost="192.168.1.9"                 #Δηλώση της τοποθεσίας του MySQL Server
    database_username="tester"          #Όνομα χρήστη 
    database_password="12312312345"     #Κώδικός Πρόσβασης 
    DATABASE="settings"                 #Βασή δεδομένων 
    #Πρωσωρίνα υπάρχει συγκεντρωτική βάση δεδομένων , αργότερα θα υπάρχει βάση δεδομένων 
    #με ρυθμίσεις ανα χώρα
    global DomainName                  #δηλώση του DomainName ως global μεταβλητη
    DomainName=""                       #Κενό αρχίκα 
    def __init__(self,Domain):                 #Constructor της SettingsLoadUp  
        global MainObject,MainCursor    #Δηλώση του αντικειμένου MainObject και MainCursor ως global 
        #το MainObject ειναι το αντικείμενο που επίστρέφεται απο την συνδεση μεταξύ του Interface Server και του DatabaseServer 
        #Και μέσω αυτού χειριζόμαστε την μεταξύ τους επικοινωνία
        #Το MainCursor είναι το αντικείμενο που χειριζόμαστε την βάση δεδομένων 
        self.DomainName = Domain
        MainObject = MySQLdb.connect(self.sqlhost,self.database_username,self.database_password,self.DATABASE) #Συνδεσή με βάση δεδομένων 
        MainCursor=MainObject.cursor() #Επιστροφή του MainCursor
    def check(self):
        #ελενχεται αν υπάρχουν ρυθμίσεις για το Domain αυτο 
        #Αν οχι , τοτε εμφανίζεται μυνημα και δημιουργούνται οι default ρυθμισεις 


        MainCursor.execute("select Server_Status from greece where DomainName='"+self.DomainName+"';")#Καλείται το row των ρυθμίσεων του συγκεκριμένου Domain
        resp=MainCursor.fetchone()#Αποθηκεύουμε την απάντηση
        if(resp==None):
            print("Προσοχή : Δεν βρέθηκαν ρυθμίσεις για το "+self.DomainName)#debug messages
            print("Δημιουργία προεπιλεγμένων ρυθμίσεων για το"+self.DomainName)#debug messages
            MainCursor.execute("INSERT INTO greece values ('"+self.DomainName+"',0,"+str(random.randint(1,65550))+",4096,10,0,0,'localhost');")
            MainObject.commit()
            """
                Προεπιλεγμένες ρυθμίσεις 
                    1)DomainName                         = $DomainName
                    2)Server_Status                      = 0
                    3)Server_Port                        = random port (1-65550)
                    4)Server_BufferSize                         = 4096
                    5)MaximumAmountOfIncomingConnections = 10
                    6)shutdown                           = not
                    7)Restart                            = Not
                    8)OnServerName                       = 'Localhost'
            """

        else :
            print("Οι ρυθμίσεις βρέθηκαν επιτυχώς")#The settings is found! <3

    def __del__(self): #o Decostructor της κλάσης 
        MainObject.close()#Κλείσιμο όλων των συνδέσεων 
    def Server_Status(self): 
        MainCursor.execute("select Server_Status from greece where DomainName='"+self.DomainName+"';")
        return MainCursor.fetchone()[0]
    def Server_Port(self):
        MainCursor.execute("select Server_Port from greece where DomainName='"+self.DomainName+"';")
        return MainCursor.fetchone()[0]
    def Server_BufferSize(self):
        MainCursor.execute("select Server_BufferSize from greece where DomainName='"+self.DomainName+"';")
        return MainCursor.fetchone()[0]
    def Server_MaximumAmountOfIncomingConnections(self):
        MainCursor.execute("select MaximumAmountOfIncomingConnections from greece where DomainName='"+self.DomainName+"';")
        return MainCursor.fetchone()[0]
    def Server_Shutdown(self):
        MainCursor.execute("select Shutdown from greece where DomainName='"+self.DomainName+"';")
        return MainCursor.fetchone()[0]
    def Server_Restart(self):
        MainCursor.execute("select Restart from greece where DomainName='"+self.DomainName+"';")
        return MainCursor.fetchone()[0]
    def Server_OnServerName(self):
        MainCursor.execute("select OnServerName from greece where DomainName='"+self.DomainName+"';")
        return MainCursor.fetchone()[0]


        
        


