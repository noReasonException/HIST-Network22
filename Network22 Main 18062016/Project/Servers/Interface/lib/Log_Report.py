import MySQLdb 
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class log_report_object():
	host="192.168.1.8"
	database ="logs"
	username="tester"
	password="12312312345"
	country=""
	domain = ""

	def __init__(self,country,domain):
		global main_communication_object,main_cursor_object
		self.country = country
		self.domain = domain
		main_communication_object = MySQLdb.connect(self.host,self.username,self.password,self.database)
		main_cursor_object = main_communication_object.cursor()

	def redirect_report(self,from_ip,from_ipv6,from_port,to_ip,to_ipv6,to_port,Interface_server_ip,Interface_server_ipv6,Interface_server_port,DomainNameRequested):
		main_cursor_object.execute('insert into '+str(self.country)+' values("'+str(from_ip)+'","'+str(from_ipv6)+'",'+str(from_port)+',"'+str(to_ip)+'","'+str(from_ipv6)+'",'+str(from_port)+',"'+str(Interface_server_ip)+'","'+str(Interface_server_ipv6)+'",'+str(Interface_server_port)+',"'+str(self.domain)+'");')
		main_communication_object.commit()


	def no_volunteers_alert(self,temp_redirect_host):
		main_cursor_object.execute("insert into no_vol_alert values ('"+self.domain+"','"+temp_redirect_host+"');")
		main_communication_object.commit()
