# -*- coding: utf-8 -*-
from Log_Report import * 

import MySQLdb
#!/usr/bin/env python



class redirection():
    sqlhost="192.168.1.6" #τοποθεσια βασης δεδομενων 
    database_username="tester"#Username
    database_password="12312312345"#Password
    database_name="greece"#ΑναφερομενηΧωρα
    domain = ""
    connect = None
    cursor_object = None
    def __init__(self,domain):
        self.domain = domain
        #connect to mysql localhost server 
        self.connect = MySQLdb.connect(self.sqlhost,self.database_username,self.database_password,self.database_name)
        #create the cursor object
        self.cursor_object = self.connect.cursor()
        
        try:
            self.cursor_object.execute("select * from "+self.domain+";") #ελενχος αν υπάρχει table με εθελοντες για συγκεκριμενο domain
        except :
            print("ERR02: The domain "+domain+"has no volunteers!!!!  ") #Αν δεν υπάρχει .... 

            #Δημιουργια κενου πίνακα και μυνημα λαθους
            print("solution step 02.1 -> creating an volunteers table for"+domain+"! must manually add volunteers btw!")
            #΄Χρησιμοποιηση βασής ελλαδας
            self.cursor_object.execute("use greece;")
            #δημιουργία πίνακα 
            self.cursor_object.execute("create table "+self.domain+" (username varchar(20),ip varchar(16),ipv6 varchar(40),port integer,Tempreq integer,PressureLevel integer,TempPressureLevel integer,IsOnline bool);")
            self.connect.commit()
            #Ανακατεύθυνση στον MAIN_BACKUP_HOST
            print("Temponary Solution 02 -> Redirect client to Main Backup Host")
            self.cursor_object.execute("insert into "+self.domain+" values ('MAIN_BACKUP_HOST','www.facebook.com','NULL',0,0,0,0,1);")
            self.connect.commit()
            #Αναφορα σφαλματος στην βαση δεδομενων καταγραφων (logs database)
            log_report=log_report_object("greece",self.domain)
            log_report.no_volunteers_alert('MAIN_BACKUP_HOST')

    def __del__(self):
        self.cursor_object.close()
    def return_ip(self): #define την return_ip συναρτηση , η οποια επιστρεφει την Ip που πρεπει να γινει redirect 
        #execute the proper sql query!
        #select the ip of the row with minimum requests in "domain" table where IsOnline=1
        self.cursor_object.execute("select MAX(TempPressureLevel),ip from "+self.domain+" where IsOnline=1 GROUP BY ip;")
        #get the fuckin data!
        data = self.cursor_object.fetchone()
        #requests+1 ! 
        self.cursor_object.execute("UPDATE "+self.domain+" SET Temprec=Temprec+1 , TempPressureLevel=TempPressureLevel-1 where ip='"+data[1]+"';")
        self.connect.commit()
        #self.connect.close()
        #return only the destination!!!
        return data[1]




